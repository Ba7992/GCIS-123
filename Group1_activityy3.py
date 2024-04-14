import csv
"""
Done by: Group 1
Title: Activity 3 - currency converter program

Done by:
Al Tajer, Bachar 10% 
Faizah Mehek 45%
micheal 45%

GitHub_URL: 


CONTRIBUTION:
Bachar -  def load_data()
Faizah -insertion_sort(arr) - def analyze_data(column)
micheal - def visualize_data(column) - def main()


This activity provides an opportunity to apply our Python programming skills to a real-world problem in the domain of Data Analysis.

Functions:
def insertion_sort(arr)
def load_data()
def analyze_data(column)
def visualize_data(column)
def main()
"""

# Function to perform insertion sort on an array
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Find the correct position for the key element
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def load_data():
    token="---------------------------------Welcome to Data Analysis CLI---------------------------------_Program stages:_1. Load Data_2. Clean and prepare data_3. Analyse Data_4. Visualize Data"
    tokens=token.split("_")
    for token in tokens: #it will print  ---------------------------------Welcome to Data Analysis CLI---------------------------------_Program stages:_1. Load Data_2. Clean and prepare data_3. Analyse Data_4. Visualize Data and it will split each one of them because of the _
        print(token)  
    print() #empty space 
    print("Stage 1: Load Data")
    while True:#infintie loop
        file_name = input("Please enter path to the csv file: ")#put the name of the file
        try:
            with open(file_name, "r") as file: #it will open the file and close it when is done
                reader_csv = csv.reader(file)
                file_data = list(reader_csv)
                token="File exists_Loading file..._File successfully loaded!_loaded table:"
                tokens=token.split("_")
                for token in tokens: #it will print  File exists_Loading file..._File successfully loaded!_loaded table: and it will split each one of them because of the _
                    print(token)    
                for row in file_data:
                    print(row)
                print()
                return file_data
        except FileNotFoundError: # if the file was not foud it will print "Wrong input. Please enter path to the csv file:"
            print("Wrong input. Please enter path to the csv file:")



def clean_data(column):
    print("Stage 2: Clean and Prepare Data\n")

    numerical_columns = ["Price", "Units sold"]
    print("Choose column from selection below to clear and prepare data:")
    print("Branch / Product / Price / Units sold")
    chosen_column = input("Please choose column: ")

    while chosen_column not in numerical_columns:
        if chosen_column not in ["Branch", "Product", "Price", "Units sold"]:
            chosen_column = input("Wrong input, please try again: ")
        else:
            chosen_column = input("Non-numerical column, please try again: ")

    print("\nEnter your choice:")
    print("1. Maximum value from column")
    print("2. Minimum value from column")
    print("3. Average value from column")
    op = input("Enter your choice: ")

    while True:
        if op == '1':
            max_value = 0
            found_max = False
            for value in column:
                if value != '':
                    if not found_max or value > max_value:
                        max_value = value
                        found_max = True
            replace_value = max_value
            break
        elif op == '2':
            min_value = 0
            found_min = False
            for value in column:
                if value != '':
                    if not found_min or value < min_value:
                        min_value = value
                        found_min = True
            replace_value = min_value
            break
        elif op == '3':
            sum_values = 0
            count = 0
            for value in column:
                if value != '':
                    sum_values += value
                    count += 1
            if count > 0:
                replace_value = sum_values / count
            else:
                replace_value = 0
            break
        else:
            op = input("Please enter a valid option: ")

    print("\nAll empty values replaced with desired values!")
    updated_column = []
    for value in column:
        if value == '':
            updated_column.append(replace_value)
        else:
            updated_column.append(value)
    print("Updated column:", updated_column)
    print()
    return updated_column



# Function to analyze data by sorting the column
def analyze_data(column):
    print("Stage 3: Analyze Data\n")

    insertion_sort(column)


# Prompt user for the choice of sorting order
    print("Please choose if you want to sort column in:")
    print("1. Ascending order")
    print("2. Descending order")
    op = input("Please enter your choice: ")
 # Perform sorting based on user choice
    while True:
        if op == '1':
            sorted_column = column
            break
        elif op == '2':
            sorted_column = column[::-1]
            break
        else:
            op = input("Please enter a valid option: ")

    print("\nColumn values are sorted:")
    print(sorted_column)
    print()
    return sorted_column

#micheal did this and he didn't write any comment , i told him but he didnt listen
def visualize_data(column):
    print("Stage 4: Visualize Data\n")
    print("Column: Units sold")
    print("Legend: each '*' represents 5 units")

    for value in column:
        stars = '*' * (int(value) // 5)
        print(stars)

    print("\nVisualisation completed!\nThank you and goodbye!")

#micheal did this and he didn't write any comment , i told him but he didnt listen
def main():
    data = load_data()
    if not data:
        return
    
    numerical_columns = {}
    numerical_columns["Price"] = []
    numerical_columns["Units_sold"] = []


    for row in data[1:]:
        price = row[2].strip()  # Remove leading/trailing spaces
        units_sold = row[3].strip()
        if price:
            numerical_columns["Price"].append(float(price))
        if units_sold:
            numerical_columns["Units_sold"].append(int(units_sold))

    cleaned_price = clean_data(numerical_columns["Price"])
    cleaned_units_sold = clean_data(numerical_columns["Units_sold"])

    analyzed_price = analyze_data(cleaned_price)
    analyzed_units_sold = analyze_data(cleaned_units_sold)

    visualize_data(analyzed_units_sold)

if __name__ == "__main__":
    main()


