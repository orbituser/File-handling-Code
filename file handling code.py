# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:02:51 2023

@author: mozea
"""
import numpy as np
import pandas as pd
import os

with open("Personal_Info.txt", "w") as PersonalInfo:
  PersonalInfo.write("This is me playing around with code")

PersonalInfo = open("Personal_Info.txt", "a")
PersonalInfo = PersonalInfo.write("\nThis is proof that the append command actually works")

PersonalInfo = open("Personal_Info.txt", "r")
PersonalInfo = PersonalInfo.read()


directory = os.getcwd()


#CHECKPOINT
filePath = "C:\\Users\mozea\Downloads\Documents\GoMyCode Git Docs\Data-Science-Tutorial-Programs\Dataset\Loan_prediction_dataset.csv"

with open(filePath) as LoanDataset:
 LoanDataset = LoanDataset.read()

NumpyDataset = np.genfromtxt(filePath, delimiter=',', skip_header = 1)
LoanAmount = NumpyDataset[:, 6]
Mean = np.mean(LoanAmount)
Median = np.median(LoanAmount)
Standard_deviation = np.std(LoanAmount)


PandasDataset = pd.read_csv(filePath)






