import os
import joblib
import numpy as np

class SpamClassifier:
    def __init__(self):
        # Load the trained model and vectorizer
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        model_path = os.path.join(base_path, 'trained_model', 'spam_model.pkl')
        vectorizer_path = os.path.join(base_path, 'trained_model', 'vectorizer.pkl')
        
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
    
    def predict(self, message):
        # Transform the message
        message_vector = self.vectorizer.transform([message])
        
        # Make prediction
        prediction = self.model.predict(message_vector)[0]
        probability = np.max(self.model.predict_proba(message_vector))
        
        return {
            'is_spam': bool(prediction),
            'probability': float(probability),
            'classification': 'SPAM' if prediction else 'NOT SPAM'
        }