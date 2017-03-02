# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import qualtricsconverter_UG as QUG

PREEEG='PRE_EEG_ERAB_SURVEYCTO_FINALVERSION_WIDE.csv'
POSTEEG='POST_EEG_ERAB_SURVEYCTO_WIDE.csv'




class DataReader:
    
    def read_data(self):
        d1=pd.read_csv(PREEEG,sep=',',index_col='Subject_ID')
        d2=pd.read_csv(POSTEEG,sep=',',index_col='Subject_ID')
        
        d1 = d1.drop(d1.columns[-3:],axis=1)    
        d2 = d2.drop(d2.columns[-3:],axis=1)      
        
        
        d1 = d1.drop(d1.columns[0:10],axis=1)    
        d2 = d2.drop(d2.columns[0:10],axis=1)   
        
        
        d1=d1[pd.notnull(d1.index)]
        d1.index=d1.index.str.upper()
        
        d2=d2[pd.notnull(d2.index)]
        d2.index=d2.index.str.upper()
        
        dataf= pd.merge(d1,d2,how='inner')
        
        
        
#        
#        data.drop('UG\n\n\nParticipant ID (Filled in by experimenter)',inplace=True)
#        data.drop('1234567890',inplace=True)
#        data.drop('test',inplace=True)
#        data.drop('1234',inplace=True)
#        data.drop('tst',inplace=True)        
#        data.drop('{"ImportId":"QID455_TEXT"}',inplace=True)
#        data=data[pd.notnull(data.index)]
#        data.index=data.index.str.upper()
#        
#        data=data.drop(data.columns[0:16],axis=1)
        return data


reader=DataReader()
a=QUG.DataReader()
a.


