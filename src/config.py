# dataset from: https://www.kaggle.com/datasets/nelgiriyewithana/emotions/data

class Paths:
    TRAIN_DATA_100p = "dataset/train_data_100p.csv"
    TRAIN_DATA_10p = "dataset/train_data_10p.csv"
    TRAIN_DATA_1p = "dataset/train_data_1p.csv"
    
    TEST_DATA = "dataset/test_data.csv"

    SINGLE_ROBERTA_100p = "models/single_transfer_RoBERTa_100p.pt"
    SINGLE_ROBERTA_10p = "models/single_transfer_RoBERTa_10p.pt"
    SINGLE_ROBERTA_1p = "models/single_transfer_RoBERTa_1p.pt"

    SINGLE_BERT_100p = "models/single_transfer_BERT_100p.pt"
    SINGLE_BERT_10p = "models/single_transfer_BERT_10p.pt"
    SINGLE_BERT_1p = "models/single_transfer_BERT_1p.pt"

    SINGLE_MLBERT_100p = "models/single_transfer_MLBERT_100p.pt"
    SINGLE_MLBERT_10p = "models/single_transfer_MLBERT_10p.pt"
    SINGLE_MLBERT_1p = "models/single_transfer_MLBERT_1p.pt"

    DOUBLE_MLBERT_100p = "models/double_transfer_MLBERT_100p.pt"
    DOUBLE_MLBERT_10p = "models/double_transfer_MLBERT_10p.pt"
    DOUBLE_MLBERT_1p = "models/double_transfer_MLBERT_1p.pt"

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

    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

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

    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

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

    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

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
    
    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}
