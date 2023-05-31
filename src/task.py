'''
This file contains a bug to illustrate the debugger in the gitpod environment.
'''
import math
# Load tests from the `test1.in` file in the `tests` folder
try:
    from pysoi import *
    load_test('test1')
except:
    pass
    

def main():
    '''
    This is where the task is solved
    '''
    n= int(input())
    a=1
    while factorial(a)>n:
        a+=1 
    a-=1
    print(a)
    for _ in range(a,1,-1):
        m= n//factorial(a)
        n= n-m*factorial(a)
        print(m,end="")

    


if __name__ == '__main__':
    main()