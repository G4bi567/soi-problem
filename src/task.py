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
    liste_infos= input().strip().split()
    def f(n,r):
        if r == 1:
            return [n]
        else:
            return [f(n,r-1)]
    print(f(int(liste_infos[0]),int(liste_infos[1])))

if __name__ == '__main__':
    main()