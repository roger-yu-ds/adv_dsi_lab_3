import pandas as pd
def convert_to_date(s: pd.Series):
    """
    Convert a pandas Series to date
    """
    result = pd.to_datetime(s)
    
    return result