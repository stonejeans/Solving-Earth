import numpy as np
import pandas as pd


def mpermutations(n):
    '''NumPy solution that builds the permutations of size m 
    by modifying the permutations of size m-1. 
    Credit to Superb Rain:
    https://stackoverflow.com/questions/64291076/generating-all-permutations-efficiently'''

    a = np.zeros((np.math.factorial(n), n), np.uint8)
    f = 1
    for m in range(2, n+1):
        b = a[:f, n-m+1:]      # the block of permutations of range(m-1)
        for i in range(1, m):
            a[i*f:(i+1)*f, n-m] = i
            a[i*f:(i+1)*f, n-m+1:] = b + (b >= i)
        b += 1
        f *= m

    #---- Remove Suspected Redundancies ----#
    a = np.delete(a, np.where(
        (~((a[:,2] == 0) | (a[:,2] == 4) | (a[:,2] == 8)) \
            | ~((a[:,7] == 1) | (a[:,7] == 5) | (a[:,7] == 6) | (a[:,7] == 8)))                                                                       
        )[0], axis=0)

    a = np.delete(a, np.where(
        ((a[:,6] > 5) | (a[:,6] == 3) \
            | (a[:,3] > 6) \
                | (a[:,1] < 3) \
                    | (a[:,9] == 5) | (a[:,9] == 9) \
                        | (a[:,8] == 5))                                                                      
        )[0], axis=0)

    a = np.delete(a, np.where(
        (a[:,3] + a[:,6] > a[:,1]) \
            | (a[:,3] + a[:,6] + 3 < a[:,1]) \
                | (a[:,3] > a[:,1]) \
                    | (a[:,6] > a[:,1])                                 
        )[0], axis=0)

    a = np.delete(a, np.where(
        (((a[:,1] == 4) & (a[:,0] >= 0)) \
            & ((a[:,1] == 4) & (a[:,0] <= 7)))                             
        )[0], axis=0)

    a = np.delete(a, np.where(
        (((a[:,1] == 8) & (a[:,0] >= 0)) \
            & ((a[:,1] == 8) & (a[:,0] <= 3)))                             
        )[0], axis=0)

    return a


def build_dataframes():
    '''Create DataFrames using the Pandas library'''

    my_np_array = mpermutations(10)

    my_column_vals = ["a" , "e", "h", "n", "o", "r", "s", "t", "u", "w"]
    char_val_df = pd.DataFrame(data = my_np_array, columns=my_column_vals)
    
    char_val_df= char_val_df.applymap(str)
    
    my_column_words = ['north', 'west', 'south', 'east','earth']
    word_val_df = pd.DataFrame(data = char_val_df, columns= my_column_words)
    
    # Concatenate specific column values
    word_val_df['north'] = char_val_df['n'] + char_val_df['o'] \
        + char_val_df['r'] + char_val_df['t'] + char_val_df['h']

    word_val_df['west'] = char_val_df['w'] \
        + char_val_df['e'] + char_val_df['s'] + char_val_df['t']

    word_val_df['south'] = char_val_df['s'] + char_val_df['o'] \
        + char_val_df['u'] + char_val_df['t'] + char_val_df['h']

    word_val_df['east'] = char_val_df['e'] + char_val_df['a'] \
        + char_val_df['s'] + char_val_df['t']

    word_val_df['earth'] = char_val_df['e'] + char_val_df['a'] \
        + char_val_df['r'] + char_val_df['t'] + char_val_df['h']

    word_final_df = word_val_df.astype(int)
    
    equation_test(word_final_df)


def equation_test(word_final_df):
    '''Sum values and test if equation holds true'''

    word_final_df.drop(word_final_df[
        ~(word_final_df.earth == word_final_df.north + word_final_df.south \
            + word_final_df.east + word_final_df.west)
        ].index, inplace=True)

    print(word_final_df, word_final_df.shape)


#-------- Driver Code With Runtime Test --------#
if __name__ == "__main__":
    build_dataframes()
