# trying to make a script that calculates the limit of a function

values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.00000000001]

def f(x):
    '''
    can replace this with any function we want to put in ( the function has to be simplified, things such as 0/0 and inf/inf will not work)
    '''
    return 2*x+1




def lim(y):
    '''
    This is the part where the magic happens
    y : the function whose limit we are trying to calculate
    c : the value at which we are trying to calculate the limit
    '''
    c = int(input("Enter the point at which you want to approximate the limit of your function : "))

    left_lim(y,c)
    right_lim(y,c)



def left_lim(y, c):
    '''
    This subroutine will calculate the left limit of the function that we have.
    Since we are trying to calculate the left limit of the function at c , we will subtract c from all the values in the value
    array and then we will see where the function approaches.
    '''

    for val in values:
        print(f"The value of x is : {c - val} and the function approaches {y(c-val):.5f}")


def right_lim(y, c):
    '''
    This subroutine will calculate the right limit of the function that we have.
    Since we are trying to calculate the right limit of the function at c , we will add c to all the values in the value
    array and then we will see where the function approaches.
    '''

    for val in values:
        print(f"The value of x is : {c + val} and the function approaches {y(c+val):.5f}")
    

lim(f)

