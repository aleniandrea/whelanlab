# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 11:49:12 2017

@author: alenia
"""

class DataReader:
    
 def SSS(self,data):
        data.rename(columns={'gen.':'Gender'},inplace=True)
        data.rename(columns={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                             'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                             'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                             'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                             'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39',
                             
                             
                             'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                             'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                             'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                             'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31', 
                             'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38', 
                             'Q84': 'sss40',

                             }, inplace=True)
    
        y={}
        for i in range(1,41):
            y[i]='sss'+str(i)
        col_names=y
        
        
        columns1={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                  'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                  'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                  'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                  'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39'}
        
        
        columns2={'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                  'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                  'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                  'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31', 
                  'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38', 
                  'Q84': 'sss40'}
        
        
        
        columns1=list(columns1.viewvalues())
        columns2=list(columns2.viewvalues())

          
        for i in range(len(columns1)):
            data[columns1[i]].replace('2','0',inplace=True)
            data[columns1[i]]=data[columns1[i]].apply(pd.to_numeric)
            
        for i in range(len(columns2)):
            HashTable = {'1' : '0', '2' : '1'}
            data[columns2[i]].replace(HashTable,inplace=True)
            data[columns2[i]]=data[columns2[i]].apply(pd.to_numeric)            
    
            
        col_names=  list(col_names.values())  
        data['SSS_Total']=data[col_names].sum(axis=1)
        
        
        data['age'].replace({'1':'O18'},inplace=True)
        data.rename(columns={'age':'Age'},inplace=True)

        
        columns1=list(columns1.viewvalues())
        columns2=list(columns2.viewvalues())

          
        for i in range(len(columns1)):
            data[columns1[i]].replace('2','0',inplace=True)
            data[columns1[i]]=data[columns1[i]].apply(pd.to_numeric)
            
        for i in range(len(columns2)):
            HashTable = {'1' : '0', '2' : '1'}
            data[columns2[i]].replace(HashTable,inplace=True)
            data[columns2[i]]=data[columns2[i]].apply(pd.to_numeric)            
    
            
        col_names=  list(col_names.values())  
        data['SSS_Total']=data[col_names].sum(axis=1)
        
        col='Gender'
        data[col]=data[col].str.upper()

        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M', '3' : 'GQ'}
        
        data[col].replace(hashtable,inplace=True)
        data.drop(['ID - Topics'],inplace=True,axis=1)
        return data
        
        
        return data
    
    
    
    def define_sss_subset(self,data):
        data['SSS_boredom_susceptibility']= data['sss2']+ data['sss5'] + data['sss7']+data['sss8'] + \
                                            data['sss15']+data['sss24'] + data['sss27']+data['sss31'] + \
                                            data['sss34'] + data['sss39']
                                            
        data['SSS_disinhibition']= data['sss1']+ data['sss12'] + data['sss13']+data['sss25'] + \
                                            data['sss29']+data['sss30'] + data['sss32']+data['sss33'] + \
                                            data['sss35'] + data['sss36']
                                            
        data['SSS_experience_seeking']= data['sss4']+ data['sss6'] + data['sss9']+data['sss10'] + \
                                            data['sss14']+data['sss18'] + data['sss19']+data['sss22'] + \
                                            data['sss26'] + data['sss37']
                                            
                                            
        data['SSS_adventure_seeking']= data['sss3']+ data['sss11'] + data['sss16']+data['sss17'] + \
                                            data['sss20']+data['sss21'] + data['sss23']+data['sss28'] + \
                                            data['sss38'] + data['sss40']
        return data                                               
                                    
                                    
                                    
    def define_bis_subset(self,data):  

        data.rename(columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                             'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                             'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                             'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}, inplace=True)


                              
        bis_columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                      'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                      'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                      'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}

       
        bis_columns=list(bis_columns.viewvalues())
        
        
        
        for i in range(len(bis_columns)):
            HashTable = {'4':1,'3':2,'2':3,'1':4}
            data[bis_columns[i]].replace(HashTable,inplace=True) #SOSTITUIRE VARI VALORI
        
        
        
        a=['BIS11_5','BIS11_11','BIS11_28', 'BIS11_6','BIS11_24','BIS11_26','BIS11_2','BIS11_3','BIS11_4',\
           'BIS11_17','BIS11_19','BIS11_22','BIS11_25','BIS11_16','BIS11_21','BIS11_23','BIS11_14','BIS11_18',\
           'BIS11_27']
        bis_columns.extend(a)
        
        
        for i in range(len(bis_columns)):
            data[bis_columns[i]]=data[bis_columns[i]].apply(pd.to_numeric)







        data['BIS11_1storder_attention']=data['BIS11_5']+data['BIS11_9R']+data['BIS11_11'] + data['BIS11_20R'] +\
                                             data['BIS11_28']
                                            
                                            
        data['BIS11_1storder_cog_instab']=data['BIS11_6']+data['BIS11_24']+data['BIS11_26']
        
        
        
        
        data['BIS11_1storder_motor']=data['BIS11_2']+data['BIS11_3']+data['BIS11_4'] + \
                                          data['BIS11_17']+data['BIS11_19'] + data['BIS11_22'] + \
                                          data['BIS11_25']
                                          
                                          
                                         
        data['BIS11_1storder_perseverance']=data['BIS11_16']+data['BIS11_21']+data['BIS11_23'] + \
                                                data['BIS11_30R']

        
        data['BIS11_1storder_self_control']=data['BIS11_1R']+data['BIS11_7R']+data['BIS11_8R'] + \
                                                 data['BIS11_12R']+data['BIS11_13R'] + data['BIS11_14']
                                                 
                                                 
                                                 
                                         
        data['BIS11_1storder_cog_complex']=data['BIS11_10R']+data['BIS11_15R']+data['BIS11_18'] + \
                                                data['BIS11_27']+data['BIS11_29R']
                                                
                                                
                                                
                                                
                                         
        data['BIS11_2ndorder_attentional'] = data['BIS11_1storder_attention']+data['BIS11_1storder_cog_instab']
        
        data['BIS11_2ndorder_motor'] = data['BIS11_1storder_motor']+data['BIS11_1storder_perseverance']
        
        
        data['BIS11_2ndorder_nonplanning'] = data['BIS11_1storder_self_control']+ \
                                                data['BIS11_1storder_cog_complex']
                                                
        data['BIS11_TOTAL'] = data['BIS11_2ndorder_attentional'] + data['BIS11_2ndorder_motor'] + \
                                   data['BIS11_2ndorder_nonplanning']
                        
        return data


    def define_ftnd(self,data):
        
        data.rename(columns={'FTND_1': 'ftnd1_r', 'FTND_2': 'ftnd2_r', 'FTND_3': 'ftnd3_r',
                             'FTND_4': 'ftnd4_r','FTND_5': 'ftnd5_r', 'FTND_6': 'ftnd6_r'}, inplace=True)
            
        HashTable = {'1': 0,'2': 1,'3': 2,'4': 3}
        data['ftnd1_r'].replace(HashTable, inplace=True)
        
        
        HashTable = {'1':0,'2':1}
        data['ftnd2_r'].replace(HashTable, inplace=True)
        
        
        HashTable = {'1':1,'2': 0}
        data['ftnd3_r'].replace(HashTable, inplace=True)

        
        
        HashTable = {'1':0,'2':1,'3':2,'4':3}
        data['ftnd4_r'].replace(HashTable, inplace=True)

        
        HashTable = {'1':0,'2':1}
        data['ftnd5_r'].replace(HashTable, inplace=True)
        
        HashTable = {'1':0,'2':1,'3':1,'4':1,'5':1,'6':1}
        data['ftnd6_r'].replace(HashTable, inplace=True)
        
        data['FTND_Total'] = data['ftnd1_r'] + data['ftnd2_r'] + data['ftnd3_r'] + \
                             data['ftnd4_r'] + data['ftnd5_r'] + data['ftnd6_r']        
        return data



    def define_kirby(self,data):
        
        kirby={}
        for i in range(1,15):
            kirby['Q'+str(i+70)+'.1']='kirby'+str(i)
            
        for i in range(1,11):
            kirby['Q'+str(i+84)]='kirby'+str(14+i)   
            
            
        kirby['Q102']= 'kirby25'
        kirby['Q95']= 'kirby26'
        kirby['Q96']= 'kirby27'
                
        data.rename(columns=kirby, inplace=True)
        
        kk=list(kirby.viewvalues())
        
        for i in range(0,len(kk)):
            HashTable = {'1':'0','2':'1'}
            data[kk[i]].replace(HashTable,inplace=True)
        
        return data
    