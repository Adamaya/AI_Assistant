import joblib

def sal_est(exp):

   model=joblib.load("salary_model.pk1")
   pred = model.predict([[float(exp)]] )

   return(pred[0])  


