class Paths:
    TRAIN_DATA = "dataset/train_data.csv"
    TEST_DATA = "dataset/test_data.csv"

    SINGLE_ROBERTA = "models/single_transfer_RoBERTa.pt"
    DOUBLE_BERT = "models/double_transfer_BERT.pt"

class SingleTransferRobertaConfig:
    MODEL_NAME = "roberta-base"
    NUM_LABELS = 5
    DROPOUT = 0.1
    MAX_LENGTH = 128

    EMOTIONS = {"Neutral": 0, "Angry": 1, "Happy": 2, "Sad": 3, "Surprise": 4}

class DoubleTransferBertConfig:
    MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
    NUM_LABELS = 5
    DROPOUT = 0.1
    MAX_LENGTH = 128
    
    EMOTIONS = {"Neutral": 0, "Angry": 1, "Happy": 2, "Sad": 3, "Surprise": 4}
