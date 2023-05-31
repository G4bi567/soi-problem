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
    lvl=[-1]*n
    for l,valeur in enumerate(values):
        for v in values:
            if int(valeur[0]) <= int(v[0]) and int(valeur[1]) >= int(v[1]):
                lvl[l]+=1
    print(lvl)
        
    


if __name__ == '__main__':
    main()