# dataset from: https://www.kaggle.com/datasets/nelgiriyewithana/emotions/data

class Paths:
    TRAIN_DATA = "dataset/train_data.csv"
    TEST_DATA = "dataset/test_data.csv"

    SINGLE_ROBERTA = "models/single_transfer_RoBERTa.pt"
    DOUBLE_BERT = "models/double_transfer_BERT.pt"

class SingleTransferRoBERTaConfig:
    MODEL_NAME = "roberta-base"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

    EMOTIONS = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

class DoubleTransferBERTConfig:
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
