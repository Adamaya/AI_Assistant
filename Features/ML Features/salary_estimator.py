import joblib
model=joblib.load("salary_model.pk1")

exp = input("Enter year Exp : ")
pred = model.predict([[float(exp)]] )

print( "predicted salary : ", pred[0])  


