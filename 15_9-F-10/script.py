# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:56:09 2021

@author: Luis Navarro
"""

# =============================================================================
# Script
# =============================================================================

import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import pandas as pd
import seaborn as sns


def well_plt(data):
    fig,axes = plt.subplots(1,len(data.columns), figsize=(20,20))
    for i,log in enumerate(data.columns):
        axes[i].plot(data[log],data['Depth'])
        axes[i].set_ylim(data["Depth"].min(),data["Depth"].max())
        axes[i].invert_yaxis()
        axes[i].set_title(log,fontsize=8.5)


def summarize(objs, **kwargs):
    """Create a pd.DataFrame that summarize the content of 'objs', One 
    object pr. row
    
    Parameters
    ----------
    
    objs : list()
        list of metadata objects
        
    **kwargs
        Keyword arguments 
        Use kwargs to tell summarize() which fields (attributes) of the 
        objects you want to include in the DataFrame. The parameter name 
        must match an attribute on the object in 'objs', while the value 
        of the parameters is used as a column name. Any kwargs are excepted, 
        but if the object does not have the requested attribute, 'KeyError' 
        is used as the value.
        
    Returns
    -------
    
    summary : pd.DataFrame
    """
    summary = []
    for attr, label in kwargs.items():
        column = []
        for obj in objs:
            try:
                value = getattr(obj, attr)
            except AttributeError:
                value = 'KeyError'
    
            column.append(value)
        summary.append(column)

    summary = pd.DataFrame(summary).T
    summary.columns = kwargs.values()
    return summary

def df_column_uniquify(df):
    df_columns = df.columns
    new_columns = []
    for item in df_columns:
        counter = 0
        newitem = item
        while newitem in new_columns:
            counter += 1
            newitem = "{}_{}".format(item, counter)
        new_columns.append(newitem)
    df.columns = new_columns
    return df
        
def missing_info(df):
    #Graphically 
    print("Missing data graphically:")
    plt.figure(figsize=(15,7))
    sns.heatmap(df.isnull(),cbar=False)
    plt.show()
    #Percent
    total = 0 ; percent = 0
    total = df.isna().sum().sort_values(ascending = True)
    percent = round(((df.isna().sum()/df.isna().count())*100),2).sort_values(ascending = True)
    missing_data = pd.concat([total, percent], axis = 1, keys = ["Total ","Percent"])
    print("Missing data in dataframe:\n")
    print(missing_data)


            
# :
# def ploting_func(start, stop, to_plot):
#     fig, axes = plt.subplots(1, len(to_plot), figsize=(20,10))
#     for i, plot in enumerate(to_plot):
#         segment = w_log.data[plot].to_basis(start=start, stop=stop)
#         if plot == 'SAND_FLAG':
#             segment.plot_2d(ax=axes[i])
#         else:
#             segment.plot(ax=axes[i])
#         axes[i].set_title(plot)
            
