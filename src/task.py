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
    gns=int(input())
    ntour=int(input())
    infos=[input.split() for _ in range(ntour)]
    depl=[0]*gns
    for line in infos:
        depl[int(line[0])]+= 
        

    


if __name__ == '__main__':
    main()