# Exercise 13: Print multiplication table from 1 to 10

# Expected Output:
# 1  2 3 4 5 6 7 8 9 10 		
# 2  4 6 8 10 12 14 16 18 20 		
# 3  6 9 12 15 18 21 24 27 30 		
# 4  8 12 16 20 24 28 32 36 40 		
# 5  10 15 20 25 30 35 40 45 50 		
# 6  12 18 24 30 36 42 48 54 60 		
# 7  14 21 28 35 42 49 56 63 70 		
# 8  16 24 32 40 48 56 64 72 80 		
# 9  18 27 36 45 54 63 72 81 90 		
# 10 20 30 40 50 60 70 80 90 100 

#Create a for loop for the row pattern with a range starting from 1 to 10
for row_numbers in range(1, 11):
#Create another for loop for the column pattern with a range starting from 1 to 10 
    for column_numbers in range(1, 11):
#Print the result of the row pattern with a condition to multiple it with the  values of the column
        print(row_numbers * column_numbers, end = " ")
#Print the result of the column 
    print(" ")