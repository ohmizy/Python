num1 = 42 #number
num2 = 2.3 #float
boolean = True #boolean
string = 'Hello World'  #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #log and a type check
print(pizza_toppings[1])  #access value
pizza_toppings.append('Mushrooms') #adding value
print(person['name']) #log statement and access value
person['name'] = 'George' #log statement string 
person['eye_color'] = 'blue' #change value
print(fruit[2]) #log statement access value

if num1 > 45: #if condition
    print("It's greater") #log statement
else: #else
    print("It's lower") #log statement

if len(string) < 5: #if length condition
    print("It's a short word!") #log statement
elif len(string) > 15: #else if length condition
    print("It's a long word!") #log statement
else: #else
    print("Just right!") #log statement

for x in range(5): #forloop parameter
    print(x) #log statment
for x in range(2,5):#forloop parameter
    print(x) #log statement
for x in range(2,10,3): #forloop start stop increment
    print(x) #log statment
x = 0 #variable declaration
while(x < 5): #while condition
    print(x) #log statement 
    x += 1 #variable declaration

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value 

print(person) #log statment
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings:#forloop parameter
    if topping == 'Pepperoni': #if variable declaration
        continue
    print('After 1st if statement') #log statement 
    if topping == 'Olives': #if variable declaration
        break

def print_hello_ten_times():
    for num in range(10): #for loop parameter
        print('Hello') #log statement

print_hello_ten_times() #arguement

def print_hello_x_times(x):
    for num in range(x): #for loop parameter
        print('Hello') #log statement

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10):
    for num in range(x): #for loop parameter
        print('Hello') #log statement

print_hello_x_or_ten_times() #log statement
print_hello_x_or_ten_times(4) #log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)