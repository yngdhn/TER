# dataset from: https://www.kaggle.com/datasets/nelgiriyewithana/emotions/data

class Paths:
    TRAIN_DATA_100p = "dataset/train_data_100p.csv"
    TRAIN_DATA_10p = "dataset/train_data_10p.csv"
    TRAIN_DATA_1p = "dataset/train_data_1p.csv"
    
    TEST_DATA = "dataset/test_data.csv"

    SINGLE_ROBERTA_100p = "models/SingleTransferRoBERTa_100p.pt"
    SINGLE_ROBERTA_10p = "models/SingleTransferRoBERTa_10p.pt"
    SINGLE_ROBERTA_1p = "models/SingleTransferRoBERTa_1p.pt"

    SINGLE_BERT_100p = "models/SingleTransferBERT_100p.pt"
    SINGLE_BERT_10p = "models/SingleTransferBERT_10p.pt"
    SINGLE_BERT_1p = "models/SingleTransferBERT_1p.pt"

    SINGLE_MLBERT_100p = "models/SingleTransferMLBERT_100p.pt"
    SINGLE_MLBERT_10p = "models/SingleTransferMLBERT_10p.pt"
    SINGLE_MLBERT_1p = "models/SingleTransferMLBERT_1p.pt"

    DOUBLE_MLBERT_100p = "models/DoubleTransferMLBERT_100p.pt"
    DOUBLE_MLBERT_10p = "models/DoubleTransferMLBERT_10p.pt"
    DOUBLE_MLBERT_1p = "models/DoubleTransferMLBERT_1p.pt"

    DISTIL_BERT_100p = "models/DistilBERT_100p.pt"
    DISTIL_BERT_10p = "models/DistilBERT_10p.pt"
    DISTIL_BERT_1p = "models/DistilBERT_1p.pt"

    LARGE_BERT_100p = "models/LargeBERT_100p.pt"
    LARGE_BERT_10p = "models/LargeBERT_10p.pt"
    LARGE_BERT_1p = "models/LargeBERT_1p.pt"

class LabelMap:
    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

class SingleTransferRoBERTaConfig:
    MODEL_NAME = "FacebookAI/roberta-base"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class SingleTransferBERTConfig:
    MODEL_NAME = "google-bert/bert-base-uncased"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class SingleTransferMLBERTConfig:
    MODEL_NAME = "google-bert/bert-base-multilingual-uncased"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class DoubleTransferMLBERTConfig:
    MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class DistilBERTConfig:
    MODEL_NAME = "distilbert/distilbert-base-uncased"

class LargeBERTConfig:
    MODEL_NAME = "google-bert/bert-large-uncased"

class PredictionConfig:
    MAX_LENGTH = 512

    BATCH_SIZE = 512
