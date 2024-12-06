import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import AutoTokenizer

from config import (
    Paths,
    LabelMap,
    SingleTransferRoBERTaConfig,
    SingleTransferBERTConfig,
    SingleTransferMLBERTConfig,
    DoubleTransferMLBERTConfig
)
from utils import EmotionDataset, load_and_preprocess_data, split_data
from models import (
    SingleTransferRoBERTa,
    SingleTransferBERT,
    SingleTransferMLBERT,
    DoubleTransferMLBERT
)

def train(model, model_config, train_data, model_path, device):
    texts, labels = load_and_preprocess_data(train_data, LabelMap.EMOTIONS)
    train_texts, val_texts, train_labels, val_labels = split_data(texts=texts, labels=labels)

    tokenizer = AutoTokenizer.from_pretrained(model_config.MODEL_NAME)
    train_dataset = EmotionDataset(train_texts, train_labels, tokenizer, model_config.MAX_LENGTH)
    val_dataset = EmotionDataset(val_texts, val_labels, tokenizer, model_config.MAX_LENGTH)

    train_loader = DataLoader(train_dataset, batch_size=model_config.BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=model_config.BATCH_SIZE, shuffle=True)

    model = model.to(device)

    OPTIMIZER = torch.optim.AdamW(model.parameters(), lr=model_config.LEARNING_RATE, weight_decay=model_config.WEIGHT_DECAY)
    loss_fn = nn.CrossEntropyLoss()
    
    model_path = model_path
    try:
        checkpoint = torch.load(model_path)
        model.load_state_dict(checkpoint["model_state_dict"])
        OPTIMIZER.load_state_dict(checkpoint["optimizer_state_dict"])
        start_epoch = checkpoint["epoch"]
        print(f"Resuming training from epoch {start_epoch}...")
    except FileNotFoundError:
        start_epoch = 0
        print("No checkpoint found. Starting training from scratch...")

    logs = {}
    best_val_loss = float("inf")
    patience_counter = 0
    for epoch in range(start_epoch, model_config.EPOCHS):
        model.train()
        train_loss = 0.0

        for batch in tqdm(train_loader, desc=f"Training Epoch {epoch+1}/{model_config.EPOCHS}"):
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            OPTIMIZER.zero_grad()
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = loss_fn(outputs, labels)
            loss.backward()
        
            OPTIMIZER.step()
            train_loss += loss.item()

        train_loss /= len(train_loader)
        logs['train_loss'] = train_loss

        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for batch in tqdm(val_loader, desc="Validation"):
                input_ids = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)
                labels = batch["labels"].to(device)

                outputs = model(input_ids=input_ids, attention_mask=attention_mask)
                loss = loss_fn(outputs, labels)
                val_loss += loss.item()

                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        val_loss /= len(val_loader)
        logs['val_loss'] = val_loss

        accuracy = (correct / total) * 100
        logs['accuracy'] = accuracy

        print(f"Epoch {epoch+1}/{model_config.EPOCHS}, "
              f"Train Loss: {logs['train_loss']:.4f}, "
              f"Validation Loss: {logs['val_loss']:.4f}, "
              f"Accuracy: {accuracy:.2f}%")
                
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save({"model_state_dict": model.state_dict(),
                        "optimizer_state_dict": OPTIMIZER.state_dict(),
                        "epoch": epoch+1}, model_path)
        else:
            patience_counter += 1
            if patience_counter >= model_config.PATIENCE:
                print(f'Early stopping triggered after epoch {epoch+1}')
                break

    return model

def train_model(model, model_config, train_data, model_path, description: str, device):
    print(f"=== train{description} ===")
    train(model, model_config, train_data, model_path, device)
    print(f"=== {description} training completed ===")

def main():
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print("device:", device)

    models = {
        SingleTransferRoBERTa: SingleTransferRoBERTaConfig,
        SingleTransferBERT: SingleTransferBERTConfig,
        SingleTransferMLBERT: SingleTransferMLBERTConfig,
        DoubleTransferMLBERT: DoubleTransferMLBERTConfig
    }
    train_data_list = [Paths.TRAIN_DATA_100p, Paths.TRAIN_DATA_10p, Paths.TRAIN_DATA_1p]

    for model, model_config in models.items():
        for train_data_idx, train_data in enumerate(train_data_list):
            model_name = model.__name__
            data_size = ["100p", "10p", "1p"][train_data_idx]
            description = f"{model_name} - {data_size}"
            model_path = f"models/{model_name}_{data_size}.pt"

            train_model(
                model=model(),
                model_config=model_config,
                train_data=train_data,
                model_path=model_path,
                description=description,
                device=device
            )

if __name__ == "__main__":
    main()
