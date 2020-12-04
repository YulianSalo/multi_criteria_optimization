''' 
Q1 = 2x1 + x2 -> max
Q2 = -2x1 - x2 -> min
Q3 = x1 + 2x2 -> max 

x1 + 3x2 -x3 = 6
2x1 - 2x2 + x4 = 4
-x1 + 4x2 + x5 = 3
-----
x1 + 2x2 = 5
-2x1 - x2 = 3
'''

import numpy as np
from scipy.optimize import linprog

np.set_printoptions(suppress=True)

#File content to array conversion
def fileConvert(fileName):
    with open(fileName) as file:
        array2d = [[float(digit) for digit in line.split()] for line in file]

    dataArray = np.array(array2d)
    return dataArray


def fileConvert1d(fileName):
    dataArray = np.loadtxt(fileName)

    return dataArray

def main():

    newline = "\n--------------------------------------------------------------------\n"
    new_section = "\n#################################################################################################\n"

    #left side default eq
    A_default = fileConvert("leftside_default_eq.txt")
    #right side default eq
    B_default = fileConvert("rightside_default_eq.txt")

    #left side eq
    A = fileConvert("leftside_eq.txt")
    #right side eq
    B = fileConvert("rightside_eq.txt")

    #target function
    C_1 = fileConvert("func_eq1.txt")
    C_2 = fileConvert("func_eq2.txt")
    C_3 = fileConvert("func_eq3.txt")
    
    bnd0 = [(None, 0),
        (None, 0),
        (None, 0),
        (None, 0),
        (None, 0)
        ] 

    bnd1 = [(0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None)]

    # res_1 = linprog(-C_1, A, B, bounds=bnd1, method="simplex")
    # print(res_1)

    print(new_section)
    print(newline)
    print("Main component method\n")
    res_main_comp= linprog(C_2, A, B, bounds=bnd1, method="simplex")
    print(res_main_comp)


    #Lexicographical method    
    
    print(new_section)
    print(newline)
    print("Lexicographical method\n")
    #1st iter
    
    print("Criterion #2 is selected\n")
    print("1st iteration\n")

    res_lex_1 = linprog(C_2, A_default, B_default, bounds=bnd1, method="simplex")
    print(res_lex_1)

    print(newline)
    #1st iter
    print("2nd iteration\n")


    A_L = np.append(A_default, -C_2, axis=0)
    B_L = np.append(B_default, res_lex_1.fun)

    res_lex_2 = linprog(C_3, -A_L, -B_L, bounds=bnd1, method="simplex")
    print(res_lex_2)
    
    #2nd iter
    
    print(newline)
    print("3rd iteration\n")
    
    A_L = np.append(A_L, C_3, axis=0)
    B_L = np.append(B_L, res_lex_1.fun)
    
    res_lex_3 = linprog(C_1, -A_L, -B_L, bounds=bnd1, method="simplex")
    print(res_lex_3)


    ##############################################################################################
    #concession method
    
    print(new_section)
    print(newline)
    print("Consecutive concession method\n")
   
    #1st iter
    print(newline)
    print("1st iteration\n")

    coeff_1 = 0.3
    
    A_C = np.append(A, -C_2, axis=0)
    B_C = np.append(B, res_lex_1.fun*coeff_1)

    res_conc1 = linprog(C_3, -A_C, -B_C, bounds=bnd1, method="simplex")
    print(res_conc1)

    #2nd iter
    print(newline)
    print("2nd iteration\n")

    coeff_2 = 0.35
    
    A_C = np.append(A_C, C_3, axis=0)
    B_C = np.append(B_C, res_conc1.fun*coeff_2)

    res_conc2 = linprog(C_1, -A_C, -B_C, bounds=bnd1, method="simplex")
    print(res_conc2)


    #center of mass method

    print(new_section)
    print(newline)
    print("Center of mass method\n")
    
    #1st eq
    print(newline)
    print(print("1st default eq\n"))
    res_center_mass_1 = linprog(C_1, -A_default, -B_default, bounds=bnd1, method="simplex")
    print(res_center_mass_1)

    #2nd eq
    print(newline)
    print(print("2nd default eq\n"))
    res_center_mass_2 = linprog(-C_2, A_default, B_default, bounds=bnd1, method="simplex")
    print(res_center_mass_2)
    
    #3rd eq
    print(newline) 
    print(print("3rd default eq\n"))   
    res_center_mass_3 = linprog(C_3, -A_default, -B_default, bounds=bnd1, method="simplex")
    print(res_center_mass_3)

    #sum of all fucntion values
    func_sum = res_center_mass_1.fun + res_center_mass_2.fun + res_center_mass_3.fun

    #function default values array
    old_func_mass_arr = [float(res_center_mass_1.fun), float(res_center_mass_2.fun), float(res_center_mass_3.fun)]
    
    #center mass function values array
    mass_v_arr = [0.0] * 3
    
    for i in range(len(old_func_mass_arr)):
        if old_func_mass_arr[i] == 0:
            mass_v_arr[i] = 0.0
        else:
            mass_v_arr[i] = float(func_sum/old_func_mass_arr[i])

    #new arrays for x and function values initialization
    mass_arr_x = [x  for x in range(5)]
    mass_func1, mass_func2, mass_func3 = 0.0, 0.0, 0.0

    #center mass x value calculation
    for i in range(len(mass_arr_x)):
        mass_arr_x[i] = (res_center_mass_1.x[i] * mass_v_arr[0]) + (res_center_mass_2.x[i] * mass_v_arr[1]) + (res_center_mass_3.x[i] * mass_v_arr[2])
        mass_arr_x[i] = mass_arr_x[i]/(mass_v_arr[0] + mass_v_arr[1] + mass_v_arr[2])


    # center mass function values calculation
    #  
    for i in range(len(C_1)):
        for j in range(len(C_1[0])):
            mass_func1 += C_1[i][j] * mass_arr_x[j]

    for i in range(len(C_2)):
        for j in range(len(C_2[0])):
            mass_func1 += C_2[i][j] * mass_arr_x[j]

    for i in range(len(C_3)):
        for j in range(len(C_3[0])):
            mass_func1 += C_3[i][j] * mass_arr_x[j]

    print(newline)
    print("X values, center of mass method: ", mass_arr_x)
    print("Function values, center of mass method: ", mass_func1, mass_func2, mass_func3)

    ############################################################################################################################################
    #ideal point method
    print(new_section)
    print(newline)
    print("Ideal point method\n")

    #ideal point x  values array initialization
    ideal_arr_x = [x  for x in range(5)]

    #ideal point x values calculation
    for i in range(len(ideal_arr_x)):
        ideal_arr_x[i] = res_center_mass_1.x[i] + res_center_mass_2.x[i] + res_center_mass_3.x[i]
        ideal_arr_x[i] = ideal_arr_x[i]/3
    
    #ideal point function values array initialization
    ideal_func1, ideal_func2, ideal_func3 = 0.0, 0.0, 0.0

    #ideal point function values calculation
    #
    for i in range(len(C_1)):
        for j in range(len(C_1[0])):
            ideal_func1 += C_1[i][j] * ideal_arr_x[j]

    for i in range(len(C_2)):
        for j in range(len(C_2[0])):
            ideal_func1 += C_2[i][j] * ideal_arr_x[j]

    for i in range(len(C_3)):
        for j in range(len(C_3[0])):
            ideal_func1 += C_3[i][j] * ideal_arr_x[j] 

    print(newline)
    print("X values, idael point method: ", mass_arr_x)
    print("Function values, ideal point method: ", ideal_func1, ideal_func2, ideal_func3)
    
if __name__ == "__main__":
    main()