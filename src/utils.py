import torch
import pandas as pd
from sklearn.model_selection import train_test_split

class EmotionDataset(torch.utils.data.Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(label, dtype=torch.long),
        }

# 데이터 로드 및 전처리
def load_and_preprocess_data(file_path, label_map):
    data = pd.read_csv(file_path)
    texts = data["Text"].tolist()
    labels = [label_map[label] for label in data["Label"].tolist()]
    return texts, labels

# 데이터 분리
def split_data(texts, labels, test_size=0.1, random_state=42):
    return train_test_split(texts, labels, test_size=test_size, random_state=random_state)
