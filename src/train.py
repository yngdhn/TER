import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import AutoTokenizer

from config import Paths, SingleTransferRoBERTaConfig, DoubleTransferBERTConfig
from utils import EmotionDataset, load_and_preprocess_data, split_data
from models import SingleTransferRoBERTa, DoubleTransferBERT

def train(model, texts, labels, model_config, model_path, device):
    train_texts, val_texts, train_labels, val_labels = split_data(texts=texts, labels=labels)

    tokenizer = AutoTokenizer.from_pretrained(model_config.MODEL_NAME)
    train_dataset = EmotionDataset(train_texts, train_labels, tokenizer, model_config.MAX_LENGTH)
    val_dataset = EmotionDataset(val_texts, val_labels, tokenizer, model_config.MAX_LENGTH)

    train_loader = DataLoader(train_dataset, batch_size=model_config.BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=model_config.BATCH_SIZE, shuffle=True)

    model = model.to(device)

    OPTIMIZER = torch.optim.SGD(model.parameters(), lr=model_config.LEARNING_RATE, momentum=model_config.MOMENTUM)
    SCHEDULER = torch.optim.lr_scheduler.StepLR(OPTIMIZER, step_size=model_config.STEP_SIZE, gamma=model_config.GAMMA)

    def loss_fn(predictions, targets):
        return nn.CrossEntropyLoss()(input=predictions, target=targets)
    
    # checkpoint
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

    # train
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

            # forward pass
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = loss_fn(outputs, labels)
            
            # back propagation
            OPTIMIZER.zero_grad()
            loss.backward()
            OPTIMIZER.step()

            train_loss += loss.item()
            
        SCHEDULER.step()

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
        
        avg_val_loss = val_loss / len(val_loader)
        accuracy = (correct / total) * 100

        logs['train_loss'] = train_loss / len(train_loader)
        logs['val_loss'] = avg_val_loss
        logs['accuracy'] = accuracy

        print(f"Epoch {epoch+1}/{model_config.EPOCHS}, "
              f"Train Loss: {logs['train_loss']:.4f}, "
              f"Validation Loss: {logs['val_loss']:.4f}, "
              f"Accuracy: {accuracy:.2f}%")
                
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
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

def train_single_transfer_RoBERTa(device):
    model = SingleTransferRoBERTa
    model_config = SingleTransferRoBERTaConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA, model_config.EMOTIONS)
    model_path = Paths.SINGLE_ROBERTA

    print("=== train single transfer RoBERTa ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer RoBERTa training completed ===")

def train_double_transfer_BERT(device):
    model = DoubleTransferBERT
    model_config = DoubleTransferBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA, model_config.EMOTIONS)
    model_path = Paths.DOUBLE_BERT

    print("=== train double transfer BERT ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== double transfer BERT training completed ===")

def main():
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print("device:", device)

    train_single_transfer_RoBERTa(device)
    train_double_transfer_BERT(device)

if __name__ == "__main__":
    main()
