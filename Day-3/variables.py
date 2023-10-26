#printing the ec2 instance name by using variable
ec2_instance_name = "test-server"
print("ec2 instance name:", ec2_instance_name)


#local variables
def addition():
    a = 5   #localizing variables for addition function. local variables cant be accessed outside this function
    b = 10
    c = 15
    print("addition:", a + b+ c)
addition()

def subtraction():
    a = 5   #localizing variables for subtraction function
    b = 10
    print("subtraction:", a - b)
subtraction()


#global variables
a = 5   #declared varibles globally, so they can be accessed by any function
b = 10

def multiplication():
    print("multiplication:", a * b)
multiplication()

def division():
    print("division:", a / b)
division()