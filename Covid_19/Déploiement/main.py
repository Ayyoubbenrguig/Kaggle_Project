# Librairies
from joblib import load
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris



# iris = load_iris()
loaded_model = load('Forest_classifier')


# Création d'une nouvelle instance fastAPI
app = FastAPI()

# Définir un objet pour réaliser des requêts
class requets_model(BaseModel):
    Patient_age_quantile : int
    Hematocrit : float 
    Hemoglobin : float
    


# Définition du chemin du point de terminaison(API) 

@app.post("/predi") 

def predict(data : requets_model):
    new_data = [[
        data.Patient_age_quantile,
        data.Hematocrit,
        data.Hemoglobin,
    ]]

    #prediction

    class_index = loaded_model.predict(new_data)[0]

    return 



