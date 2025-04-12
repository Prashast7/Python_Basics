universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together 
# 3- mean of tuition fees

l = []
for universe in universities:
    x = universe[0]
    l.append(x)
print(l)

a = []
for universe in universities:
    x = universe[1]
    a.append(x)
print(a)
print(sum(a))

a = []
for universe in universities:
    x = universe[2]
    a.append(x)
print(a)
m = sum(a)/len(a)
print(m)


# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university


universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


univ = {}
for university in universities:
    key = university[0]
    value_1 = university[1]
    value_2 = university[2]
    univ[key] = {value_1, value_2}
print(univ)



# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"

s = input("enter a string: ")
print(s)
print(s[-1::-1])


# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.

l = input("enter numbers separated by comma: ")
raw_list = l.split(",")
num_list = []  

for item in raw_list:
    num = int(item.strip())
    num_list.append(num)
print(num_list)

largest = num_list[0]
for num in num_list[1:]:
    if num > largest:
        largest = num
print(f"largest number is {largest}")


capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}  

# pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly, 
# then repeatedly ask them for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".
# Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver". 
# Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".


state = input("Enter the state: ")
if state in capitals_dict:
    while True:
        capital = input("Enter the capital: ")
        if capital.lower() == "exit":
            print(f"correct answer: {capitals_dict[state]} goodbye")
            break
        if capital.lower() == capitals_dict[state].lower():
            print("correct answer")
            break
        else:
            print("type again")
else:
    print("state not found")   






    






