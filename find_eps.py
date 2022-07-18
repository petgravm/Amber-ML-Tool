import pandas as pd
import os
import re
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


#empty dataframe, which will be filled
bigdata = pd.DataFrame()
for i in range(1,11):
    dfname = 'df%i' % i
    #the cut off for the distance between each K-dist
    # take the average, if the average is less than 0.0499, indicates values are in high density
    cut_off = 0.8500
        
    dfname = pd.read_csv('Kdist.%i.dat' % i,sep=',\s', delimiter=' ', encoding="utf-8", skipinitialspace=True)
    dfname.drop(dfname.columns[dfname.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    
#append the dataframes together
    if bigdata.empty == True: 
        #bigdata = dfname.append(dfname, ignore_index=True)
        bigdata = dfname
    else:
        bigdata['%i-dist' % i] = dfname['%i-dist' % i]
        
        #print(bigdata)
    
#subrtract the succedding column from the current
count = 0
for i in range(1,9):                        # to get last column --> bigdata[:,-1:]
    succed = bigdata['%i-dist' % (i+1)]
    further = bigdata['%i-dist' % (i+2)]
    current = bigdata['%i-dist' % i]
    #take the difference between two columns to compare their average
    difference = succed - current
    difference_2 = further - succed
    if count <1 and (difference_2.mean()/difference.mean()) >= 0.8500:
        count+=1
    elif count >=1 and (difference_2.mean()/difference.mean()) >= 0.8500:
        #print('%i-dist' % i)
        mini_points = i
        break
    else:
        count = count*0
        continue
            
    # do linear regression to find an ideal fitting flat line
    # compute the standard deivation of the residuals, the instance of smaller residuals indicates the better flat region
    #state the x- and y- values:
x=bigdata[['#Point']].to_numpy().reshape((-1, 1))
y= bigdata[['%i-dist' % i]].to_numpy()
    
    #classify the linear regression model
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
    
    #uncomment to print out stats of graph
    #print(f"coefficient of determination: {r_sq}")
    #print(f"intercept: {model.intercept_}")
    #print(f"slope: {model.coef_}")
    #print("std of arr : ", np.std(y, dtype = np.float32))
    
    #epslion is the y-intercept, indicates when the values when the line is zero
esp = model.intercept_
    #plot the graph
ax = plt.gca() 
bigdata.plot(kind='line', x= '#Point', ax=ax)
    #print(mini_points)
    
    #plot the linear regression line (or line of best fit)
    #plt.plot(x, model.coef_*x + model.intercept_, color='black')
    
    #plot the y-intercept with a slope of zero 
plt.plot(x, 0*x + model.intercept_, color='black')
bigdata
    
plt.savefig('K-dist.png', bbox_inches='tight',dpi=300)

with open('Eps.txt','w+') as bc:
    bc.write('MiniPoints:%i' % (mini_points) +"\n" + 'Epsilon:%f' % (float(esp)))
    
print(mini_points, float(esp))

