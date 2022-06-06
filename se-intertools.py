from itertools import permutations
import time

#-- System Runtime Start --#
np_start = time.perf_counter_ns()

class Master_Dict:

    starting_words = ["north", "east", "south", "west", "earth"]
    starting_chars = ["a" ,"e" , "h", "n", "o", "r", "s", "t", "u", "w"]
    char_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self) -> None:

        self.master_comb_data =[]
        self.subset_char_vals = []
        self.master_dict = []
        self.temp_list = []
        self.final_val_list = []
        self.final_dict_comb = []

        self.create_master_comb()
    

    def create_master_comb(self):
        # Create a list with all possible combinations from the character value set (char_val)
        self.master_comb_data = [",".join(map(str, comb)) for comb in permutations(self.char_vals,10)]
        # Convert the master combination data list values to integers
        for i in range(len(self.master_comb_data)):
            new_val = list(self.master_comb_data[i].split(","))
            new_val_int = list(map(int, new_val))
            self.subset_char_vals.append(new_val_int)
        # Loop through the integers from the character value subsets and append to a master dictionary
        for i in range(len(self.subset_char_vals)):
            self.char_vals = self.subset_char_vals[i]

            for o in range(len(self.char_vals)):
                self.master_dict.append({self.starting_chars[o]:self.char_vals[o]})

            self.temp_list = []
            new_temp_list = []
            res = []
            # Iterate through the starting words and append combination's character values
            for j in range(len(self.starting_words)):
                str_list = [str(x) for x in self.starting_words[j]]
                
                for item in str_list:
                    res = next((k for k,t in enumerate(self.master_dict) if item in t), None)                   
                    my_val = self.master_dict[res]
                    new_temp_list.append(my_val[item])
                    # Combine integers in list to form number representation of the starting word
                    if len(new_temp_list) == len(str_list):
                        temp_joined_str = ''.join([str(x) for x in new_temp_list])
                        self.temp_list.append(int(temp_joined_str))
                        new_temp_list = []

            self.equation_solver() 


    def equation_solver(self):  

        val1 = self.temp_list[0]
        val2 = self.temp_list[1]
        val3 = self.temp_list[2]
        val4 = self.temp_list[3]
        val5 = self.temp_list[4]

        calc = val1 + val2 + val3 + val4

        if calc == val5:
            self.final_val_list.append(val5)
            self.final_dict_comb.append({val5 : self.master_dict})
            print(f"Master Dictionary: {self.master_dict}")
            print(f"Permutation: {self.temp_list}")

            if self.final_val_list:
                    self.max_val = max(self.final_val_list)
        
        self.master_dict =[]

        
# -- Driver Code -- #
master_dict = Master_Dict()
m_val = master_dict.max_val
solve_earth_comb = list(map(str, master_dict.final_dict_comb))
res = next((k for k,t in enumerate(master_dict.final_dict_comb) if m_val in t), None)                   
comb_earth_max = master_dict.final_dict_comb[res]

print(f"\nSolving Earth Max Value: {m_val}")
print(f"Solve_earth_comb: {comb_earth_max}")

#-- System Runtime End --#
np_end = time.perf_counter_ns()
np_time = np_end - np_start
print(f'\nRuntime: {np_time/1e+6} ms')