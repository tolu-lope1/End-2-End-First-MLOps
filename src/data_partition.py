from config import *
def data_partiton(dataframe):
    train_data = dataframe[0:int(split_size*(len(dataframe)))]
    test_data = dataframe[int(split_size*(len(dataframe)))::]
    train_data.to_csv(f"{train_path}")
    test_data.to_csv(f"{test_path}")
    print("Partiton Complete")