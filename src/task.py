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
    infos=input().strip().split()
    nlivres=int(infos[0])+1
    njours=int(infos[1])+1
    infos_livres=[input().strip().split() for _ in range(njours)]
    print(infos_livres)


if __name__ == '__main__':
    main()