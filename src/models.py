import torch.nn as nn
from transformers import AutoModel

from config import (
    SingleTransferRoBERTaConfig,
    SingleTransferBERTConfig,
    SingleTransferMLBERTConfig,
    DoubleTransferMLBERTConfig,
    DistilBERTConfig,
    LargeBERTConfig,
)

class BaseModel(nn.Module):
    def __init__(self, model_config):
        super().__init__()
        self.model = AutoModel.from_pretrained(model_config.MODEL_NAME)
        self.dropout = nn.Dropout(model_config.DROPOUT)
        self.classifier = nn.Linear(self.model.config.hidden_size, model_config.NUM_LABELS)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls_output = outputs.last_hidden_state[:, 0, :]
        cls_output = self.dropout(cls_output)
        logits = self.classifier(cls_output)

        return logits

class SingleTransferRoBERTa(BaseModel):
    def __init__(self):
        super().__init__(model_config=SingleTransferRoBERTaConfig)

class SingleTransferBERT(BaseModel):
    def __init__(self):
        super().__init__(model_config=SingleTransferBERTConfig)

class SingleTransferMLBERT(BaseModel):
    def __init__(self):
        super().__init__(model_config=SingleTransferMLBERTConfig)

class DoubleTransferMLBERT(BaseModel):
    def __init__(self):
        super().__init__(model_config=DoubleTransferMLBERTConfig)

class DistilBERT(BaseModel):
    def __init__(self):
        super().__init__(model_config=DistilBERTConfig)

class LargeBERT(BaseModel):
    def __init__(self):
        super().__init__(model_config=LargeBERTConfig)
