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
    values =[input().strip().split() for _ in range(n)]
    values_list=[list(range(int(values[i][0]),int(values[i][1])+1)) for i in range(n)]
    print(values)
    


if __name__ == '__main__':
    main()