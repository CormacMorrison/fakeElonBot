import pandas as pd

def parseCSVColumnToNumpyArray(path: str, column_name: str):
    dataFrame = pd.read_csv(path)

    tweetArray = dataFrame[column_name].to_numpy()

    return tweetArray
