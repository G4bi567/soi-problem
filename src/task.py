'''
This file contains a bug to illustrate the debugger in the gitpod environment.
'''

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
    n = int(input())
    longueur = 2*n-1
    
    for i in range(longueur):
        for j in range(longueur):
            reste = min(i,j,longueur-j-1,longueur-i-1)
            print(chr(ord("a")+reste), end="")
        print()


if __name__ == '__main__':
    main()