from src.data_ingestion import data_retrieval
from src.data_partition import data_partiton
from src.train import train
from src.test import test
from config import *

if __name__ == "__main__":
    dataframe = data_retrieval(dataset_url)
    partition_data = data_partiton(dataframe)
    train(train_path)
    test(test_path, model_path, scaler_path)
    