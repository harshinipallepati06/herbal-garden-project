import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Training data
data = {
    'cough':      [1,1,0,1,0,1,1,0,1,1],
    'fever':      [1,0,1,1,0,1,1,0,1,1],
    'breathing':  [1,0,0,1,0,1,1,0,1,1],
    'disease': [
        'bronchitis','cough','cold','asthma','cold',
        'bronchitis','bronchitis','cold','asthma','bronchitis'
    ]
}

df = pd.DataFrame(data)

X = df[['cough','fever','breathing']]
y = df['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

# 🔥 FUNCTION (IMPORTANT)
def predict_disease(cough, fever, breathing):
    prediction = model.predict([[cough, fever, breathing]])
    return prediction[0]