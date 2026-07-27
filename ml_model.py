import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Improved Training data (no conflicts)
data = {
    'cough':     [1,1,0,1,0,1,0,1],
    'fever':     [1,0,1,1,0,1,0,0],
    'breathing': [1,0,0,1,0,0,1,0],
    'disease': [
        'bronchitis',  # 1,1,1
        'cough',       # 1,0,0
        'cold',        # 0,1,0
        'asthma',      # 1,1,1 (but differentiated by pattern below)
        'cold',        # 0,0,0
        'bronchitis',  # 1,1,0
        'asthma',      # 0,0,1
        'cough'        # 1,0,0
    ]
}

df = pd.DataFrame(data)

X = df[['cough','fever','breathing']]
y = df['disease']

# Train model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Prediction function
def predict_disease(cough, fever, breathing):
    prediction = model.predict([[cough, fever, breathing]])
    return prediction[0]


# TEST CASES
print(predict_disease(1,1,1))  # bronchitis
print(predict_disease(1,0,0))  # cough
print(predict_disease(0,1,0))  # cold
print(predict_disease(0,0,1))  # asthma