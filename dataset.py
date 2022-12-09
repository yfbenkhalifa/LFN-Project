import os
from pathlib import Path
import pandas as pd
import networkx as nx
from utils import Utilities as utils

class Dataset:
    dataframes = {}
    namespaces = {}
    sources = []
    df = None
    base_path = str(Path(os.path.abspath(os.getcwd())))
            
    def addDataset(self, filePath, name=''):
        df = utils.creteDataframe(filePath)
        utils.cleanDataframe(df)
        if df is None:
            print('Error: File not found or not valid')
        else:
            if self.dataframes.get(name) is None:
                self.dataframes[name] = df
            else: 
                self.dataframes[name].append(df)
            print('Added ' + filePath + ' to dataset') 
            
    def createDataset(self, files):
        frames = []
        for file in files:
            mobility_csv = self.base_path + "/data/" + file
            mob_df = pd.read_csv(mobility_csv, sep=";")
            frames.append(mob_df)
        self.df = pd.concat(frames) 
        
    def cleanDataframe(self):
        self.df = utils.cleanDataframe(self.df)
        
    def getCountryNodes(self):
        return self.df["Receiving Country Code"].unique()
        
    def getUniversitiesNodes(self):
        return self.df["Receiving Organization"].unique()
         
    def applyPreprocessing(self):
        self.df.drop(["Mobility Duration", "Education Level", "Special Needs", "Fewer Opportunities", "GroupLeader",
                     "Sending Organisation Erasmus Code", "Receiving Organisation Erasmus Code"], axis=1, inplace=True)
        self.df = self.df[self.df["Participant Profile"] == "Learner"]
        self.df = self.df[self.df["Activity (mob)"].str.contains("Student")]
        self.df = self.df.loc[:, ["Sending Organization", "Receiving Organization", "Participants", "Sending Country Code", "Receiving Country Code"]]
        self.df["Sending Organization"] = self.df["Sending Organization"].str.upper()
        self.df["Receiving Organization"] = self.df["Receiving Organization"].str.upper()
        self.df["Sending Country Code"] = self.df["Sending Country Code"].str.upper()
        self.df["Receiving Country Code"] = self.df["Receiving Country Code"].str.upper()
    
    def applyFilter(self, column, value, maxrows=None):
        if maxrows is not None:
            self.df = self.df.head(maxrows)
        self.df = self.df[self.df[column] == value]
            
    
                
                