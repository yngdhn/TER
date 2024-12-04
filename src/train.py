import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import AutoTokenizer

from config import Paths, SingleTransferRoBERTaConfig, SingleTransferBERTConfig, SingleTransferMLBERTConfig, DoubleTransferMLBERTConfig
from utils import EmotionDataset, load_and_preprocess_data, split_data
from models import SingleTransferRoBERTa, SingleTransferBERT, SingleTransferMLBERT, DoubleTransferMLBERT

def train(model, texts, labels, model_config, model_path, device):
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

# single transfer RoBERTa
def train_single_transfer_RoBERTa_100p(device):
    model = SingleTransferRoBERTa()
    model_config = SingleTransferRoBERTaConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_100p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_ROBERTA_100p

    print("=== train single transfer RoBERTa - 100p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer RoBERTa - 100p training completed ===")

def train_single_transfer_RoBERTa_10p(device):
    model = SingleTransferRoBERTa()
    model_config = SingleTransferRoBERTaConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_10p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_ROBERTA_10p

    print("=== train single transfer RoBERTa - 10p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer RoBERTa - 10p training completed ===")

def train_single_transfer_RoBERTa_1p(device):
    model = SingleTransferRoBERTa()
    model_config = SingleTransferRoBERTaConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_1p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_ROBERTA_1p

    print("=== train single transfer RoBERTa - 1p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer RoBERTa - 1p training completed ===")

# single transfer BERT
def train_single_transfer_BERT_100p(device):
    model = SingleTransferBERT()
    model_config = SingleTransferBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_100p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_BERT_100p

    print("=== train single transfer BERT - 100p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer BERT - 100p training completed ===")

def train_single_transfer_BERT_10p(device):
    model = SingleTransferBERT()
    model_config = SingleTransferBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_10p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_BERT_10p

    print("=== train single transfer BERT - 10p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer BERT - 10p training completed ===")

def train_single_transfer_BERT_1p(device):
    model = SingleTransferBERT()
    model_config = SingleTransferBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_1p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_BERT_1p

    print("=== train single transfer BERT - 1p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer BERT - 1p training completed ===")

# single transfer MLBERT
def train_single_transfer_MLBERT_100p(device):
    model = SingleTransferMLBERT()
    model_config = SingleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_100p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_MLBERT_100p

    print("=== train single transfer MLBERT - 100p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer MLBERT - 100p training completed ===")

def train_single_transfer_MLBERT_10p(device):
    model = SingleTransferMLBERT()
    model_config = SingleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_10p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_MLBERT_10p

    print("=== train single transfer MLBERT - 10p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer MLBERT - 10p training completed ===")

def train_single_transfer_MLBERT_1p(device):
    model = SingleTransferMLBERT()
    model_config = SingleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_1p, model_config.EMOTIONS)
    model_path = Paths.SINGLE_MLBERT_1p

    print("=== train single transfer MLBERT - 1p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== single transfer MLBERT - 1p training completed ===")

# double transfer MLBERT
def train_double_transfer_MLBERT_100p(device):
    model = DoubleTransferMLBERT()
    model_config = DoubleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_100p, model_config.EMOTIONS)
    model_path = Paths.DOUBLE_MLBERT_100p

    print("=== train double transfer MLBERT - 100p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== double transfer MLBERT - 100p training completed ===")

def train_double_transfer_MLBERT_10p(device):
    model = DoubleTransferMLBERT()
    model_config = DoubleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_10p, model_config.EMOTIONS)
    model_path = Paths.DOUBLE_MLBERT_10p

    print("=== train double transfer MLBERT - 10p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== double transfer MLBERT - 10p training completed ===")

def train_double_transfer_MLBERT_1p(device):
    model = DoubleTransferMLBERT()
    model_config = DoubleTransferMLBERTConfig()
    texts, labels = load_and_preprocess_data(Paths.TRAIN_DATA_1p, model_config.EMOTIONS)
    model_path = Paths.DOUBLE_MLBERT_1p

    print("=== train double transfer MLBERT - 1p ===")
    train(model, texts, labels, model_config, model_path, device)
    print("=== double transfer MLBERT - 1p training completed ===")

def main():
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print("device:", device)

    # single transfer RoBERTa
    train_single_transfer_RoBERTa_100p(device)
    train_single_transfer_RoBERTa_10p(device)
    train_single_transfer_RoBERTa_1p(device)

    # single transfer BERT
    train_single_transfer_BERT_100p(device)
    train_single_transfer_BERT_10p(device)
    train_single_transfer_BERT_1p(device)

    # single transfer MLBERT
    train_single_transfer_MLBERT_100p(device)
    train_single_transfer_MLBERT_10p(device)
    train_single_transfer_MLBERT_1p(device)

    # double transfer MLBERT
    train_double_transfer_MLBERT_100p(device)
    train_double_transfer_MLBERT_10p(device)
    train_double_transfer_MLBERT_1p(device)

if __name__ == "__main__":
    main()
