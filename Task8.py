#Task 8
#In python it is possible to create function without returning value,these functions are called void
#For example
def greetings(who):
    print ('Hello', who + '!')
    print ('Nice to meet you')
greetings('John')#Basically here is the example of a void example, where function doesn't return anything but none

#Let's create returning value function to see the difference
def fahrenheit(T_in_celsius):
    "returns the temperature in degrees fahrenheit "
    return (T_in_celsius * 9 / 5) + 32

for t in (20, 30, 40, 50):
    print(t, ": ", fahrenheit(t))