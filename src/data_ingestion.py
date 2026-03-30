import pandas as pd

def data_retrieval(dataset_url):
    dataframe = pd.read_csv(dataset_url)
    print("Columns: ", dataframe.columns.to_list())
    return dataframe

