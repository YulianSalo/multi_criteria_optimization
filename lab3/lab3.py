import pandas as pd
import matplotlib.pyplot as plt

def main():

    new_section = "########################################################################################"

    #CSV file reading
    given_df = pd.read_csv("data.csv")
    
    #Starting dataframe indexing from 1
    given_df.index +=1

    #Coefficient definition
    coeff = [0.3, 0.5, 0.2]

    #Column names for plotting dataframe
    plot_df_columns = ["Price UAH thousand * 100", "Reliability hours * 10", "Productivity units/hour"]
    
    #New empty dataframe for plotting the given data
    given_plot_df = pd.DataFrame(columns = plot_df_columns)
    
    #starting dataframe indexing from 1
    given_plot_df.index +=1

    #Plotting data normalization
    given_plot_df["Price UAH thousand * 100"] = given_df["Price UAH thousand"]*100
    given_plot_df["Reliability hours * 10"] = given_df["Reliability hours"]*10
    given_plot_df["Productivity units/hour"] = given_df["Productivity units/hour"]

    #New dataframe for the coeffs use
    coeff_df = given_df
    
    #Coeffs application
    coeff_df = coeff_df.loc[:,["Price UAH thousand", "Reliability hours", "Productivity units/hour"]].mul(coeff, axis=1)

    #New plotting coeff dataframe
    coeff_plot_df = given_plot_df

    #Coeff plotting data normalization
    coeff_plot_df = coeff_plot_df.mul(coeff, axis=1)

    #Coeff dataframe sort
    coeff_df_sorted = coeff_df.sort_values(["Price UAH thousand", "Reliability hours", "Productivity units/hour"], ascending=[True, False, False])
    
    #Coeff plotting dataframe sort
    coeff_plot_df = coeff_plot_df.sort_values(["Price UAH thousand * 100", "Reliability hours * 10", "Productivity units/hour"], ascending=[True, False, False])

    #Given dataframes print&plot
    print(new_section)
    print("\nGiven data\n")
    print (given_df)

    given_plot_df.plot.bar()
    print("\n")
    plt.title("Given data")

    #Coeff dataframes print&plot
    print(new_section)
    print("\n Coefficents applied\n")
    print(coeff_df)
    print("\n Coefficents applied, data sorted. Targat functions: Price -> min; Reliablity -> max; Productivity -> max\n")
    print(coeff_df_sorted)
    coeff_plot_df.plot.bar()
    plt.title("Coefficents applied. Targat functions: Price -> min; Reliablity -> max; Productivity -> max")
    
    #Solution dataframes print&plot
    print(new_section)
    print("\nSolution: Top 4\n")
    print(coeff_df_sorted.head(4))
    
    coeff_plot_df.head(4).plot.bar()
    plt.title("Solution: Top 4")

    #Plotting all the plots
    plt.show()



#main() function call
if __name__ == "__main__":
    main()