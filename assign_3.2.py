# # count frequency
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for item in my_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)


# #Q1. Word Count in a Sentence
sentence = "this is a test this is only a test"

# Your code here
words = sentence.split()
print(words)
count = {}
for word in words:
  word = word.strip()
  count[word] = count.get(word,0) + 1 #dictionary.get(key, default_value) SYNTAX
print(count) 


# Q2. Create Dictionary from Two Lists
# Task: Given keys and values, combine them into a dictionary.

# {key_expr: value_expr for item in iterable} - SYNTAX

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Delhi'] 

dict = {}
for key,value in zip(keys,values):
    dict[key] = value
print(dict)

dict =  {keys[i]: values[i] for i in range(len(keys))}
print(dict)



#Q3. Find the Key with the Maximum Value
data = {'Apple': 55, 'Banana': 78, 'Cherry': 43}
maximun = max(data, key = data.get)
print(maximun)



# Array Transformation Logic Questions

# Q1. Fold and Sum
# Given an array of integers, divide it into two halves, reverse the first half, and add it element-wise to the
# second half. Repeat this process until one element remains. Return that element.

# Example Input: 6
# 1 2 3 4 5 6
# Example Output: 21


# f = 1,2,3
# s = 4,5,6
# fr = 3,2,1
# 7,7,8
# 10,9,9


def fold_sum(arr):
    while len(arr) > 1:
        mid = len(arr) // 2
        first_half = arr[0:mid]
        second_half = arr[mid:]
        first_half = first_half[::-1]
        result = []
        for i in range(len(first_half)):
            result.append(first_half[i] + second_half[i])
        if len(second_half) > len(first_half):
            result.append(second_half[-1])
        arr = result
    return arr[0]

sum = fold_sum([1,2,3,4,5,6])
print(sum)





# Q2. Multiply-Reduce Array
# Given an array, repeatedly multiply each adjacent pair and form a new array. Continue until one element
# remains. Return the final element.
# Example Input:
# 4
# 2 3 4 5
# Example Output:
# 120


def multi_reduce(arr):
    while len(arr) > 1:
        res = []
        for i in range(len(arr)-1):
            res.append(arr[i] * arr[i+1])
        arr = res
    return arr[0]
x = multi_reduce([2,3,4,5])
print(x)


# Q3. Zig-Zag Transformation
# Given an array, arrange it in a zig-zag pattern (a < b > c < d > ...) and then remove the last element. Repeat
# this process until one element remains. Return that element.
# Example Input:
def zigzag(arr):
    while len(arr) > 1:
        for i in range(len(arr)-1):
            if i % 2 == 0:
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1], arr[i] 
            else:
                if arr[i] < arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1], arr[i]
        arr.pop()
    return arr  
y = zigzag([2,3,41,6,90])
print(y) 
print(zigzag([4, 1, 3, 2, 5])) 






