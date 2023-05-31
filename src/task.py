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
    liste_disponibilité= [0]*nlivres
    for _ in range(njours):
        nclients=int(input())
        for _ in range(nclients):
            reserv= input().strip().split()
            if liste_disponibilité[int(reserv[0])]<1:
                liste_disponibilité[int(reserv[0])]=int(reserv[1])
                print(1)
            else:
                print(0)
        print(nclients)


if __name__ == '__main__':
    main()