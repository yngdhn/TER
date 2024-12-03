import torch.nn as nn
from transformers import AutoModel
from config import SingleTransferRobertaConfig, DoubleTransferBertConfig

class SingleTransferRoberta(nn.Module):
    def __init__(self):
        super().__init__()
        self.singleRoberta = AutoModel.from_pretrained(SingleTransferRobertaConfig.MODEL_NAME)
        self.dropout = nn.Dropout(SingleTransferRobertaConfig.DROPOUT)
        self.classifier = nn.Linear(self.singleRoberta.config.hidden_size, SingleTransferRobertaConfig.NUM_LABELS)
    
    def forward(self, input_ids, attention_mask, labels=None):
            outputs = self.singleRoberta(
                input_ids=input_ids.to(self.singleRoberta.device),
                attention_mask=attention_mask.to(self.singleRoberta.device)
            )
            cls_output = outputs.last_hidden_state[:, 0, :]
            cls_output = self.dropout(cls_output)
            logits = self.classifier(cls_output)

            if labels is not None:
                loss_fn = nn.CrossEntropyLoss()
                loss = loss_fn(logits, labels)
                return loss, logits

            return logits

class DoubleTransferBert(nn.Module):
    def __init__(self):
        super().__init__()
        self.doubleBert = AutoModel.from_pretrained(DoubleTransferBertConfig.MODEL_NAME)
        self.dropout = nn.Dropout(DoubleTransferBertConfig.DROPOUT)
        self.classifier = nn.Linear(self.doubleBert.config.hidden_size, DoubleTransferBertConfig.NUM_LABELS)

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
