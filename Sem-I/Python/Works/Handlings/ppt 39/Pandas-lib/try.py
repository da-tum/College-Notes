import pandas as pd
'''
#series and dataframe creation
data=[10,20,30,40]
series=pd.Series(data)
print(series)

data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
series=pd.Series(data)
print(series)


df=pd.DataFrame(data)
print(df)


#vector operation 

data=[10,20,30,40]
series1=pd.Series(data)

#describe series method
data=[10,20,30,40]
series1=pd.Series(data)
print(series1.describe())

#Dataframes = tools concepts using datas - used in pandas
data={'Name':['john','anna','peter','linda'],
      'age':[28,39,18,59],
      'city':['delhi','india','lomda','lehsen']}
df=pd.DataFrame(data)
print(df)

df.to_csv('.\Handlings\ppt 39\Pandas-lib\people.csv',index=False)
print(end='\n\n\n')
df=pd.read_csv('.\Handlings\ppt 39\Pandas-lib\people.csv')
print(df)

#Dataframe Operators 
print(df.head(2))  #first 2 rows

print(df['Name'])  #specific column
print(end='\n\n\n')
df['Salary']=[50000,60000,False,80000]  #adding new column
print(df)


#Describe on Dataframe
print(df.describe())

#sorting data
df_sorted=df.sort_values(by='age',ascending=False)  #ascending order
print(df_sorted)

#dataframe filtering
df_filtered=df[df['age']>30]
print(df_filtered)

print(end='\n\n\n')
print('iloc')
#Dataframe slicing and indexing
print(df.loc['age':,'Name']) #label based slicing
print(end='\n\n\n')
print(df.iloc[2])
print(end='\n\n\n')
print(df.iloc[1:5])  #rows slicing


#Handling missign data


#Operatoes usign dataframes
data={'A':[True,False,False],'B':[False,False,True]}
df=pd.DataFrame(data)
print(df or df)
print(df and df)
'''

#Plotting with pandas
import matplotlib.pyplot as plt
  
# frequencies 
ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40] 
  
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
  
# plotting a histogram 
plt.hist(ages, bins, range, color='green',histtype='bar',rwidth=1) 
  
# x-axis label 
plt.xlabel('age') 
# frequency label 
plt.ylabel('No. of people') 
# plot title 
plt.title('My histogram') 
  
# function to show the plot 
plt.show()

