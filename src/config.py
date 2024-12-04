class Paths:
    TRAIN_DATA = "dataset/train_data.csv"
    TEST_DATA = "dataset/test_data.csv"

    SINGLE_ROBERTA = "models/single_transfer_RoBERTa.pt"
    DOUBLE_BERT = "models/double_transfer_BERT.pt"

class SingleTransferRoBERTaConfig:
    MODEL_NAME = "roberta-base"
    NUM_LABELS = 5
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 16

    # optimizer
    LEARNING_RATE = 2e-5
    MOMENTUM = 0.9
    WEIGHT_DECAY = 0.01

    # scheduler
    STEP_SIZE = 10
    GAMMA = 0.1

    PATIENCE = 3

    EMOTIONS = {"Neutral": 0, "Angry": 1, "Happy": 2, "Sad": 3, "Surprise": 4}

class DoubleTransferBERTConfig:
    MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
    NUM_LABELS = 5
    DROPOUT = 0.1
    MAX_LENGTH = 512

    EPOCHS = 10
    BATCH_SIZE = 16

    # optimizer
    LEARNING_RATE = 2e-5
    MOMENTUM = 0.9
    WEIGHT_DECAY = 0.01

    # scheduler
    STEP_SIZE = 10
    GAMMA = 0.1

    PATIENCE = 3
    
    EMOTIONS = {"Neutral": 0, "Angry": 1, "Happy": 2, "Sad": 3, "Surprise": 4}
