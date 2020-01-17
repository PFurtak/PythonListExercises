# Sum the numbers in a list
list_one = [5, 8, 7, 4]
list_sum = sum(list_one)
print("The sum of the list is: ", list_sum)

# Print the largest number in the  list
largest = max(list_one)
print("The largest item in the list is : ", largest)

# Print the smallest number in the list
smallest = min(list_one)
print("the smallest item in the list is: ", smallest)

# Print even numbers in a list
print("The even numbers in the list are: ")
for num in list_one:
    if num % 2 == 0:
        print(num, end=', ')
print('\n')

# Print positive numbers
print("The positive numbers in the list are: ")
for num in list_one:
    if num > -1:
        print(num, end=', ')
print('\n')

# Create new list from positive numbers
print("The positve numbers in the NEW list are: ")
list_two = []
for num in list_one:
    if num > 0:
        list_two.append(num)
print(list_two)
print('\n')

# Multiply numbers in a list by given factor, and place results into a new list. Print the new list
print("Here is the new list, with all indices multiplied by 5: ")
list_three = [i * 5 for i in list_one]
print(list_three)
print('\n')

# Multiply two lists of equal length by their corresponding indices
list_four = [3, 1, 7, 9]
vector = [list_one * list_four for list_one,
          list_four in zip(list_one, list_four)]
print(vector)
print('\n')

# Given a list, remove duplicates and print the new list
de_dup_one = [5, 5, 2, 2, 3, 3, 4, 4]
de_dup_two = set([5, 5, 2, 2, 3, 3, 4, 4])
print("Here is the list ", de_dup_one, " with duplicates removed. ")
print('\n')
print(de_dup_two)
