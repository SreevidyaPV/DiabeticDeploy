#------------------------testing.py------------------------
import joblib


# load the model

model = joblib.load('diabetic_80.pkl')

result = model.predict([[1,2,3,4,5,6,7,8]])[0]

print(result)
