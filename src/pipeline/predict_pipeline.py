import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging
from src.components.data_ingestion import DataIngestion

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            #preprocessor is responsible for handling categorical featues and feature scaling
            preprocessor_path='artifacts/preprocessor.pkl'
            print("Before Loading")
            #load pickle file from utils.py
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scale=preprocessor.transform(features)
            preds=model.predict(data_scale)
            return preds
         
        except Exception as e:
            raise CustomException(e,sys)
        

#responsible in mapping all inputs we're giving in html to the backend with particular values
class CustomData:
    def __init__(self,
        gender: str,  
        race_ethnicity: str,
        parental_level_of_education,
        lunch:str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):       
        self.gender=gender
    
        self.race_ethnicity=race_ethnicity
    
        self.parental_level_of_education=parental_level_of_education
    
        self.lunch=lunch
    
        self.test_preparation_course=test_preparation_course
    
        self.reading_score= reading_score
    
        self.writing_score= writing_score
    
    #this function will return all the inputs in the form of dataframe coz we trained the model in the form of df
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict ={
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
        
#inputs from web app will get mapped with these