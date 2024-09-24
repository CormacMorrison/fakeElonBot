import os
import pickle
from collections import defaultdict


def save_model(model: dict, filename: str) -> None:
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model(filename: str) -> dict:
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return defaultdict(list)