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
    donnees=input()
    d=donnees.strip()
    nblivres= int(d[0])
    bd= [0]*(nblivres+1)
    nbjours=int(d[2])
    d=d[4:]
    nbre=0
    for i in range(nbjours):
        nbclients=int(d[nbre])
        for n in range(nbclients):
            if bd[int(d[nbre+2+4*n])] <=0:
                print(1)
                bd[int(d[nbre+2+4*n])]=0
                bd[int(d[nbre+2+4*n])]=int(d[nbre+4+4*n])
            else:
                print(0)
        nbre += 2+4*nbclients
        bd = [x-1 for x in bd]


if __name__ == '__main__':
    main()