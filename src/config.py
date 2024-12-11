# dataset from: https://www.kaggle.com/datasets/nelgiriyewithana/emotions/data

class Paths:
    TRAIN_DATA_100p = "dataset/train_data_100p.csv"
    TRAIN_DATA_10p = "dataset/train_data_10p.csv"
    TRAIN_DATA_5p = "dataset/train_data_5p.csv"
    TRAIN_DATA_1p = "dataset/train_data_1p.csv"
    
    TEST_DATA = "dataset/test_data.csv"

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

class BERTsmallConfig:
    MODEL_NAME = "prajjwal1/bert-small"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 64

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class BERTlargeConfig:
    MODEL_NAME = "google-bert/bert-large-uncased"
    NUM_LABELS = 6
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 32

    LEARNING_RATE = 2e-5
    WEIGHT_DECAY = 0.01

    PATIENCE = 3

class PredictionConfig:
    MAX_LENGTH = 512

    BATCH_SIZE = 512
