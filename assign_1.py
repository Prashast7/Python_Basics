weight = int(input("Enter mass in kg: "))
height = int(input("Enter height in meters: "))
bmi = int(weight/(height*height))
print(bmi)

name = str(input("Enter your name: "))
try:
    print(name.index('a'))
except ValueError:
    print(-1)

my_word = "antidisestablishmentarianism"
print(len(my_word))

first_name = input("enter first name: ")
last_name = input("enter last name: ")
company = input("enter company: ")
email = f" {first_name[0:2]}{last_name[-3:] }@{company}.com"
print(email.lower())


s = input("enter details: ")
s = s.split(",")
print(f"First name is {s[0]} \nSecond name is {s[1]} \n{s[0]} is {s[2]} years old")


list1= [1,3,4]
list2 = [2,4,6]
print(list1+list2)

list_1=[1,2,3,4,5,6,7,8]
print(list_1[1::2])

ipl= ['CSK','MI','KKR','LSG','PBKS']
team = input("Enter team name: ")

try:
    exclude_index = ipl.index(team)
    print(ipl[:exclude_index] + ipl[exclude_index+1:])
except ValueError:
    print("Team not found in the IPL team list.")

try:
    ipl= ['CSK','MI','KKR','LSG','PBKS']
    team = input("Enter team name and index: ")
    index, element = team.split(",")
    index = int(index)
    new_team = ipl.insert(index, element)
    print(f"New team added at index {index}:{element}")
    print(ipl)
except ValueError:
    print("Team not found in the IPL team list.")
except IndexError:
    print("Index out of range. Please enter a valid index.")

ipl = ['CSK','MI','KKR','LSG','PBKS']
team = input("Enter team name: ")
print(team in ipl)


try:
    ipl = ['CSK','MI','KKR','LSG','PBKS']
    team = input("Enter index, team name: ")
    print(f"old list: {ipl} and lenght {len(ipl)}")
    index, element = team.split(",")
    index = int(index)
    new_team = ipl.insert(index,element)
    print(f"New team added at index {index}:{element}")
    print(f"New list: {ipl} and lenght {len(ipl)}")
except ValueError:
    print("team and index not found try again")
except IndexError:
    print("index oor try again")

