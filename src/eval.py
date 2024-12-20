import os
import torch
from torch.utils.data import DataLoader
import pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from config import (
    Paths,
    LabelMap,
    SingleTransferRoBERTaConfig,
    SingleTransferBERTConfig,
    SingleTransferMLBERTConfig,
    DoubleTransferMLBERTConfig,
    BERTsmallConfig,
    BERTlargeConfig,
    PredictionConfig,
)
from utils import EmotionDataset, load_and_preprocess_data
from models import (
    SingleTransferRoBERTa,
    SingleTransferBERT,
    SingleTransferMLBERT,
    DoubleTransferMLBERT,
    BERTsmall,
    BERTlarge,
)

def predict(model, tokenizer, device):
    texts, labels = load_and_preprocess_data(Paths.TEST_DATA, LabelMap.EMOTIONS)
    eval_dataset = EmotionDataset(texts, labels, tokenizer, PredictionConfig.MAX_LENGTH)
    eval_loader = DataLoader(eval_dataset, batch_size=PredictionConfig.BATCH_SIZE)

    predictions = []
    with torch.no_grad():
        for batch in tqdm(eval_loader, desc="Prediction"):
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
        
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            probs = torch.softmax(outputs, dim=1)
            preds = torch.argmax(probs, dim=1)
            predicted_emotions = [list(LabelMap.EMOTIONS.keys())[list(LabelMap.EMOTIONS.values()).index(pred.item())] for pred in preds]
            predictions.extend(predicted_emotions)
    return predictions

def evaluation(models, device):
    os.makedirs("predictions", exist_ok=True)

    for model_class, model_config in models.items():
        for train_data_idx in range(4):
            model_name = model_class.__name__
            data_size = ["100p", "10p", "5p", "1p"][train_data_idx]
            eval_model_path = f"models/{model_name}_{data_size}.pt"
            result_file_path = f"predictions/{model_name}_{data_size}_prediction.csv"
            
            if os.path.exists(result_file_path):
                print(f"{result_file_path} already exists")
            elif not os.path.exists(eval_model_path):
                continue
            else:
                model = model_class()
                tokenizer = AutoTokenizer.from_pretrained(model_config.MODEL_NAME)

                checkpoint = torch.load(eval_model_path, map_location=device)
                model.load_state_dict(checkpoint["model_state_dict"])
                print(f"Loaded model: {model_name}")

                model.to(device)
                model.eval()

                predictions = predict(model, tokenizer, device)

                test_data = pd.read_csv(Paths.TEST_DATA)
                test_data["Prediction"] = predictions
                test_data.to_csv(result_file_path, index=False)
                print(f"Predictions saved to {result_file_path}")

def calculate_scores(folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    file_names.sort()

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        
        df = pd.read_csv(file_path)
        
        y_true = df['Label']
        y_pred = df['Prediction']
        
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='macro', zero_division=0)
        recall = recall_score(y_true, y_pred, average='macro', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
        
        print(f"{file_name} scores:")
        print(f"Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}\n")

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
        DoubleTransferMLBERT: DoubleTransferMLBERTConfig,
        BERTsmall: BERTsmallConfig,
        BERTlarge: BERTlargeConfig,
    }

    evaluation(models, device)
    calculate_scores("predictions")

if __name__ == "__main__":
    main()
