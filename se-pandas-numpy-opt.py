import time
import numpy as np
import pandas as pd

MY_COLUMN_VALS = ["a" ,"e" , "h", "n", "o", "r", "s", "t", "u", "w"]
MY_COLUMN_WORDS = ['north', 'west', 'south', 'east','earth']


def mpermutations(n):
    '''NumPy solution that builds the permutations of size m 
    by modifying the permutations of size m-1. 
    Credit to Superb Rain https://stackoverflow.com/questions/64291076/generating-all-permutations-efficiently'''
    a = np.zeros((np.math.factorial(n), n), np.uint8)
    f = 1
    for m in range(2, n+1):
        b = a[:f, n-m+1:]      # the block of permutations of range(m-1)
        for i in range(1, m):
            a[i*f:(i+1)*f, n-m] = i
            a[i*f:(i+1)*f, n-m+1:] = b + (b >= i)
        b += 1
        f *= m
    
    return a

def create_dataframes():
    '''Create DataFrames using the Pandas library'''
    my_np_array = mpermutations(10)
    
    char_val_df = pd.DataFrame(data = my_np_array, columns=MY_COLUMN_VALS)
    char_val_df.drop(char_val_df[(char_val_df.n > char_val_df.e) | (char_val_df.s > char_val_df.e)].index, inplace=True)
    
    for char in MY_COLUMN_VALS:
         char_val_df[char]= char_val_df[char].astype(str)

    word_val_df = pd.DataFrame(data = char_val_df)

    # Concatenate specific column values (Strings only)
    word_val_df['north'] = char_val_df['n'] + char_val_df['o'] + char_val_df['r'] + char_val_df['t'] + char_val_df['h']
    word_val_df['west'] = char_val_df['w'] + char_val_df['e'] + char_val_df['s'] + char_val_df['t']
    word_val_df['south'] = char_val_df['s'] + char_val_df['o'] + char_val_df['u'] + char_val_df['t'] + char_val_df['h']
    word_val_df['east'] = char_val_df['e'] + char_val_df['a']+ char_val_df['s'] + char_val_df['t']
    word_val_df['earth'] = char_val_df['e'] + char_val_df['a'] + char_val_df['r'] + char_val_df['t'] + char_val_df['h']

    for word in MY_COLUMN_WORDS:
        word_val_df[word] = word_val_df[word].astype(int)
    
    return word_val_df

def equation_test(word_val_df):
    '''Use numpy to sum values and test if equation holds true'''
    word_val_df['earth_test'] = (word_val_df['north'].to_numpy() \
        + word_val_df['west'].to_numpy() + word_val_df['south'].to_numpy() \
        + word_val_df['east'].to_numpy()).tolist()

    word_val_df.drop(word_val_df[~(word_val_df.earth == word_val_df.earth_test)].index, inplace=True)
    
    df_solution_output = f"Solutions DataFrame: \n{word_val_df}"
    df_datashape = f"\nData Shape: \n{word_val_df.shape}\n"
    
    max_val = word_val_df['earth'].max()
    df_max_val = f"Max Value: {max_val}"

    print(df_solution_output,df_datashape,df_max_val)

#-- Driver Code --#
word_val_df = create_dataframes()
equation_solve = equation_test(word_val_df)
