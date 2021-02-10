import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split
import numpy as np

def split_sets_random (df: pd.DataFrame, 
                       target_col: str,
                       test_size: float=0.2,
                       to_numpy: bool=False,
                       random_state: int=42) -> Tuple[pd.DataFrame]:
    """
    
    """
    y = df[target_col]
    X = df.drop(columns=target_col)
    
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=test_size,
                                                        random_state=random_state)
    
    if to_numpy:
        X_train = X_train.to_numpy()
        X_test = X_test.to_numpy()
        y_train = y_train.to_numpy()
        y_test = y_test.to_numpy()
        
    return X_train, X_test, y_train, y_test

def save_sets(X_train, X_test, y_train, y_test, path) -> None:
    """
    
    """
    np.save(path / 'X_train', X_train)
    np.save(path / 'X_test', X_test)
    np.save(path / 'y_train', y_train)
    np.save(path / 'y_test', y_test)