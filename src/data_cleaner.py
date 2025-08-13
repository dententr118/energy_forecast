import pandas as pd
import csv
import os

for file in os.listdir("./data/raw"):
    df = pd.read_csv(f"./data/raw/{file}")
    df.drop(['updatedAt','createdAt','emissionFactorType','isEstimated','estimationMethod'], axis=1, inplace=True)
    print(df)
    df.to_csv(f"./data/processed/{file}", index=False)
