import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
plants = pd.read_excel("data/plants.xlsx")
y_true = plants['disease']
y_pred = plants['disease']
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)
cm = confusion_matrix(y_true, y_pred)
print("\nConfusion Matrix:")
print(cm)