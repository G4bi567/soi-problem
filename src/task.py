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
    def tete(n):
        text1="0 ="
        text2="0"
        if n==0:
            return text1+text2
        elif n==1:
            return text2.replace("0","(0 + 0)")
        else:
            return tete(n-1).replace("0","(0 + 0)")
    tete(2)

if __name__ == '__main__':
    main()