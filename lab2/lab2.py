import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Function to find the best result. It takes a working dataframe, given dataframe, specific column and minimum or maximun criterial as function parameters
def selectTheBestFunc(df_used, df_default, points_value, search_v):
    
    #if the maximum criterial was given as func.parameter the fucntion returns an element with the maximum value in a specified column
    if search_v == "max":
        
        points_max = df_used[points_value].idxmax()
        result = df_default.iloc[points_max,:]
        return points_max, result

    #if the minimum criterial was given as func.parameter the fucntion returns an element with the minimum value in a specified column
    elif search_v == "min":

        points_min = df_used[points_value].idxmin()
        result = df_default.iloc[points_min,:]
        return points_min, result


#Function to print the best result according to solution. It takes number of the best solution element and the element itself as function parameters
def printTheBestFunc(df_points, df_value):
    
    print("\nThe best solution is number :", df_points, "\n")
    print(df_value)
    print("\n")

#Function to find column name of the dataframe. It takes series object and specific element as function parameters
def findIndexSeriesFunc(series, el):
    
    #Iterating through the loop and checking whether specific element is in the series 
    for i in series.index:

        #If the element is in the series the fucntion returns its index that stands for column name
        if series[i] == el: 

            return i
    #If the element is not in the series the fuction returns None object
    return None

#Function to plot dataframes. It takes a dataframe as function parameters
def funcPlot(df):

    #Iteration through each column in dataframe    
    for col in df.columns:
        
        #plotting each column
        df.plot(kind = 'bar', y = col)
        plt.show()

def main():
    #CSV file reading
    df = pd.read_csv("data.csv")

    #Coefficient definition
    coeff = [0.3, 0.5, 0.2]

    #Finding maximum values of each column
    maxColValue = df.max(axis=0)

    #New dataframe with divided by maximum values in each column
    divided = df.divide(maxColValue, axis=1)

    #################################################    
    #Summing final value for each row
    additive = df.divide(maxColValue, axis=1)

    #Points sum
    additive["Points sum"] = additive.sum(axis=1)

    #selectTheBestFunc fucntion call
    additive_points_max, additive_max = selectTheBestFunc(additive, df, "Points sum", "max")
    

    ################################################# 
    #Multiplication 
    multiplicative = df.divide(maxColValue, axis=1)

    #Points product
    multiplicative["Points product"] = multiplicative.prod(axis=1)

    #selectTheBestFunc fucntion call
    multi_points_max, multi_max = selectTheBestFunc(multiplicative, df, "Points product", "max")

    #################################################
    #MiniMax
     
    #product of given dataframe elements and given coeffs
    coeff_df = df.mul(coeff, axis=1)
    
    #finding minimum values in the column
    minValuesObj = coeff_df.min(axis=0)

    #selection of the max value from minimum values series
    max_minValuesObj = minValuesObj.max()

    #findIndexSeriesFunc fucntion call
    index_series = findIndexSeriesFunc(minValuesObj, max_minValuesObj)

    #selectTheBestFunc fucntion call
    minimax_points_max, minimax_max = selectTheBestFunc(coeff_df, df, index_series, "min")
   
    #############################################
    #MaxiMin

    #finding maximum values in the column
    maxValuesObj = coeff_df.max(axis=0)

    #selection of the max value from maximum values series
    min_maxValuesObj = maxValuesObj.min()

    #findIndexSeriesFunc fucntion call
    index_series = findIndexSeriesFunc(maxValuesObj, min_maxValuesObj)

    #selectTheBestFunc fucntion call
    maximin_points_min, maximin_min = selectTheBestFunc(coeff_df, df, index_series, "max")

    #Result print

    new_section = "########################################################################################"

    #Given dataframe print&plot
    print(new_section)
    print("\nGiven\n")
    print (df)
    funcPlot(df)
    print("\n")

    #Normalized dataframe print&plot
    print(new_section)
    print("\nNormalized\n")
    print (divided)
    funcPlot(divided)
    print("\n")

    #Additive method result print
    print(new_section)
    print("\nAdditive\n")
    print(additive)
    printTheBestFunc(additive_points_max, additive_max)

    #Multiplicative method result print
    print(new_section)
    print("\nMultiplicative\n")
    print(multiplicative)
    printTheBestFunc(multi_points_max, multi_max)

    #Ginen*coeffs plot
    funcPlot(coeff_df)

    #MaxiMin method result print
    print(new_section)
    print("\nMaxiMin\n")
    print(coeff_df)
    printTheBestFunc(minimax_points_max, minimax_max)
    print("\n")

    #MiniMax method result print
    print(new_section)
    print("\nMiniMax\n")
    print(coeff_df)
    print()
    printTheBestFunc(maximin_points_min, maximin_min)
    print("\n")

#main() function call
if __name__ == "__main__":
    main()