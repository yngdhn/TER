import torch.nn as nn
from transformers import AutoModel

from config import SingleTransferRoBERTaConfig, SingleTransferBERTConfig, DoubleTransferBERTConfig

class SingleTransferRoBERTa(nn.Module):
    def __init__(self):
        super().__init__()
        self.singleRoberta = AutoModel.from_pretrained(SingleTransferRoBERTaConfig.MODEL_NAME)
        self.dropout = nn.Dropout(SingleTransferRoBERTaConfig.DROPOUT)
        self.classifier = nn.Linear(self.singleRoberta.config.hidden_size, SingleTransferRoBERTaConfig.NUM_LABELS)
    
    def forward(self, input_ids, attention_mask, labels=None):
        outputs = self.singleRoberta(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls_output = outputs.last_hidden_state[:, 0, :]
        cls_output = self.dropout(cls_output)
        logits = self.classifier(cls_output)

        if labels is not None:
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(logits, labels)
            return loss, logits

        return logits

class SingleTransferBERT(nn.Module):
    def __init__(self):
        super().__init__()
        self.singleBert = AutoModel.from_pretrained(SingleTransferBERTConfig.MODEL_NAME)
        self.dropout = nn.Dropout(SingleTransferBERTConfig.DROPOUT)
        self.classifier = nn.Linear(self.singleBert.config.hidden_size, SingleTransferBERTConfig.NUM_LABELS)

    def forward(self, input_ids, attention_mask, labels=None):
        outputs = self.singleBert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls_output = outputs.last_hidden_state[:, 0, :]
        cls_output = self.dropout(cls_output)
        logits = self.classifier(cls_output)

        if labels is not None:
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(logits, labels)
            return loss, logits

        return logits

class DoubleTransferBERT(nn.Module):
    def __init__(self):
        super().__init__()
        self.doubleBert = AutoModel.from_pretrained(DoubleTransferBERTConfig.MODEL_NAME)
        self.dropout = nn.Dropout(DoubleTransferBERTConfig.DROPOUT)
        self.classifier = nn.Linear(self.doubleBert.config.hidden_size, DoubleTransferBERTConfig.NUM_LABELS)

    def forward(self, input_ids, attention_mask, labels = None):
        outputs = self.doubleBert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls_output = outputs.last_hidden_state[:, 0, :]
        cls_output = self.dropout(cls_output)
        logits = self.classifier(cls_output)

        if labels is not None:
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(logits, labels)
            return loss, logits
        
        return logits
