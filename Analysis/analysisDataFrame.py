#CHCl3
#T8n = 'Exp.,6.22,6.28,5.10' #8a 
#T8n = 'Exp.,5.64,6.27,5.03' #8b
#T8n = 'Exp.,4.88,6.28,5.05' #8c
#T8n = 'Exp.,8.15,6.43,5.06' #8d
#T8n = 'Exp.,5.91,6.89,4.96' #8e
#DMSO
#T8n = 'Exp.,8.50,6.42,7.32' #8a
#T8n = 'Exp.,8.56,6.63,7.32' #8b
#T8n = 'Exp.,8.31,6.63,7.20' #8c
#T8n = 'Exp.,8.32,6.88,7.17' #8d
T8n = 'Exp.,8.79,7.31,7.27' #8e
csvfile = '8e.csv'


T8nL = T8n.split(',')
T8nL = T8nL[1:]

#  Task 1
import pandas as pd
import math as math 



df = pd.read_csv(csvfile) 		#Creating a panel data (panda)

###########
#df1
###########
df1 = df[df['Rel.Energy'] <= 5 ]		#Below 5 kcal/mol
df1select = df1[['NH(I)','NH(II)','NH(III)']]	#Selecting only pI, pII, and pIII
df1List = list(df1select.mean())
df1Mean = pd.DataFrame([df1List], columns = ['NH(I)','NH(II)','NH(III)'], index = [10]) #Creating a DataFrame by row
df1Cont = pd.concat([df1select,df1Mean])

#Calculating RMSE
DpI = df1List[0] - float(T8nL[0])
DpII = df1List[1] - float(T8nL[1])
DpIII = df1List[2] - float(T8nL[2])
RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
dfRMSE = pd.DataFrame({'RMSE' : [RMSE]},index = [10])
#Adding RMSE to DF
df1RMSE = df1[['RMSE']]
df1RMSE = pd.concat([df1RMSE,dfRMSE])

#Additional Columns
df1Name = df1[['Name']]
dfAverage = pd.DataFrame({'Name' : ['Average']},index = [10])
df1Name = pd.concat([df1Name,dfAverage])
df1Energy = df1[['Rel.Energy']]
df1New = pd.concat([df1Name,df1Cont,df1RMSE,df1Energy], axis=1)

###########
#df2
###########
df2 = df[df['Rel.Energy'] <= 10 ]		#Below 10 kcal/mol
df2select = df2[['NH(I)','NH(II)','NH(III)']]	#Selecting only pI, pII, and pIII
df2List = list(df2select.mean())
df2Mean = pd.DataFrame([df2List], columns = ['NH(I)','NH(II)','NH(III)'], index = [10]) #Creating a DataFrame by row
df2Cont = pd.concat([df2select,df2Mean])

#Calculating RMSE
DpI = df2List[0] - float(T8nL[0])
DpII = df2List[1] - float(T8nL[1])
DpIII = df2List[2] - float(T8nL[2])
RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
dfRMSE = pd.DataFrame({'RMSE' : [RMSE]},index = [10])
#Adding RMSE to DF
df2RMSE = df2[['RMSE']]
df2RMSE = pd.concat([df2RMSE,dfRMSE])

#Additional Columns
df2Name = df2[['Name']]
dfAverage = pd.DataFrame({'Name' : ['Average']},index = [10])
df2Name = pd.concat([df2Name,dfAverage])
df2Energy = df2[['Rel.Energy']]
df2New = pd.concat([df2Name,df2Cont,df2RMSE,df2Energy], axis=1)

###########
#df3
###########
df3 = df[df['Rel.Energy'] <= 15 ]		#Below 15 kcal/mol
df3select = df3[['NH(I)','NH(II)','NH(III)']]	#Selecting only pI, pII, and pIII
df3List = list(df3select.mean())
df3Mean = pd.DataFrame([df3List], columns = ['NH(I)','NH(II)','NH(III)'], index = [10]) #Creating a DataFrame by row
df3Cont = pd.concat([df3select,df3Mean])

#Calculating RMSE
DpI = df3List[0] - float(T8nL[0])
DpII = df3List[1] - float(T8nL[1])
DpIII = df3List[2] - float(T8nL[2])
RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
dfRMSE = pd.DataFrame({'RMSE' : [RMSE]},index = [10])
#Adding RMSE to DF
df3RMSE = df3[['RMSE']]
df3RMSE = pd.concat([df3RMSE,dfRMSE])

#Additional Columns
df3Name = df3[['Name']]
dfAverage = pd.DataFrame({'Name' : ['Average']},index = [10])
df3Name = pd.concat([df3Name,dfAverage])
df3Energy = df3[['Rel.Energy']]
df3New = pd.concat([df3Name,df3Cont,df3RMSE,df3Energy], axis=1)

###########
#df4
###########
df4 = df[df['Rel.Energy'] <= 20 ]		#Below 20 kcal/mol
df4select = df4[['NH(I)','NH(II)','NH(III)']]	#Selecting only pI, pII, and pIII
df4List = list(df4select.mean())
df4Mean = pd.DataFrame([df4List], columns = ['NH(I)','NH(II)','NH(III)'], index = [10]) #Creating a DataFrame by row
df4Cont = pd.concat([df4select,df4Mean])

#Calculating RMSE
DpI = df4List[0] - float(T8nL[0])
DpII = df4List[1] - float(T8nL[1])
DpIII = df4List[2] - float(T8nL[2])
RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
dfRMSE = pd.DataFrame({'RMSE' : [RMSE]},index = [10])
#Adding RMSE to DF
df4RMSE = df4[['RMSE']]
df4RMSE = pd.concat([df4RMSE,dfRMSE])

#Additional Columns
df4Name = df4[['Name']]
dfAverage = pd.DataFrame({'Name' : ['Average']},index = [10])
df4Name = pd.concat([df4Name,dfAverage])
df4Energy = df4[['Rel.Energy']]
df4New = pd.concat([df4Name,df4Cont,df4RMSE,df4Energy], axis=1)

###########
#df5
###########
df5 = df[df['Rel.Energy'] >= 0 ]		#All
df5select = df5[['NH(I)','NH(II)','NH(III)']]	#Selecting only pI, pII, and pIII
df5List = list(df5select.mean())
df5Mean = pd.DataFrame([df5List], columns = ['NH(I)','NH(II)','NH(III)'], index = [10]) #Creating a DataFrame by row
df5Cont = pd.concat([df5select,df5Mean])

#Calculating RMSE
DpI = df5List[0] - float(T8nL[0])
DpII = df5List[1] - float(T8nL[1])
DpIII = df5List[2] - float(T8nL[2])
RMSE = math.sqrt((DpI**2 + DpII**2 + DpIII**2)/3)
dfRMSE = pd.DataFrame({'RMSE' : [RMSE]},index = [10])
#Adding RMSE to DF
df5RMSE = df5[['RMSE']]
df5RMSE = pd.concat([df5RMSE,dfRMSE])

#Additional Columns
df5Name = df5[['Name']]
dfAverage = pd.DataFrame({'Name' : ['Average']},index = [10])
df5Name = pd.concat([df5Name,dfAverage])
df5Energy = df5[['Rel.Energy']]
df5New = pd.concat([df5Name,df5Cont,df5RMSE,df5Energy], axis=1)

# Writing to a csv file
df1New.to_csv('8e-5kcal.csv')
df2New.to_csv('8e-10kcal.csv')
df3New.to_csv('8e-15kcal.csv')
df4New.to_csv('8e-20kcal.csv')
df5New.to_csv('8e-All.csv')