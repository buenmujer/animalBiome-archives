import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#calculate percentages of categorical variables
def categorical_percentages(data, categorical_data_title):
    '''
    This is a function to calculate proportions from a categorical data column
    
    data = df['count_column_title']
    categorical_data_title = df['categorical data title']
    '''
    data['count'] = 1
    data2 = data.groupby(categorical_data_title, sort=True).sum()/len(data)
    percentages = data2.reset_index()
    return percentages


#building a pie chart plotting function
def piePlot(data, labels, title, figName='figure.png', startangle=0): 
    '''
    This is a function to generate a pie chart
    
    title = str
    figName = str
    labels and data must be the same length
    labels = df['columnNameLabels']
    data = df['columnNameData']
    startangle = int (default is 0)
    '''
    
    fig = plt.figure()
    fig.set_size_inches(8,6)
    sns.set(font='serif')

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    colors = ["#a651cb","#64b546","#db5b2f","#4c7cdc","#b6b633","#6e62d3","#d99234","#5d6bab",
              "#a6a758","#e26fd0","#5ab880","#e53580","#3dbbb8","#ce3b46","#62a3da","#a2522e",
              "#b891e2","#497938","#b4398f","#846e29","#8a549e","#d89767","#d85481","#db7a76","#d687b6","#9b4863"]
    ax1.pie(data, startangle=startangle, colors=colors, labels = labels) #autopct='%1.1f%%' : add this in order to add % values to pies
    ax1.axis('equal')

    fig.suptitle(title, fontsize=15)
    fig.savefig(figName) 
    return plt.show()






