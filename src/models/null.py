class NullModel:
    def __init__(self, 
                 target_type : str='regression',
                 y,
                 pred_value: float,
                 preds):
        self.target_type = target_type
        self.y = y
        self.pred_value = pred_value
        self.preds = preds

        
    def fit(self, y):
        pass
    
    
    def get_length(self):
        pass
    
    
    def predict(self, y):
        pass
    
    
    def fit_predict(self, y):
        pass