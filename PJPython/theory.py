#python is dynamically typed
#both single and double quotes are valid to define string 
# (//) this is a floor devision 
# Data Types - Numeric , Boolean , Dictionary , Boolean , Set , Sequence Types
# In Numeric there are - int , float , complex 
# In Sequence Types there are - string , list[] , tupple() , range
## List - Lists are mutable, meaning they can be changed.
## Tupple - Tuple is generally immutable.

# example of dictionary 
student = {
    "name": "Prince",
    "age": 20,
    "course": "CSE"
}
print(student["name"])
student["marks"] = 85 #to add new data 

#Set
numbers = {1, 2, 3, 4}

#for loop
for i in range(5):
    print(i)

#loop through list
names = ["Prince", "Rahul", "Aman"]

for name in names:
    print(name)

#While loop
i=2
while i>=1:
    print(i)
    i+=1    

#user defined datatype
# def function_name():

#example 

def greet():
    print("Hello Prince")

greet() 

# function with parameters
def add(a, b):
    print(a + b)

add(10, 20) 