def addition(a, b):     #function which takes inputs from the user
    add = a + b         #not hardcoding the values in the function
    return add          


def subtraction(a,b):   #multiple functions can be called a Module, which can are re-usable
    sub = a- b
    return sub

add = addition(5, 5)
print("the addition value is:", add)

sub = subtraction(10,5)
print("the subtraction value is:", sub)