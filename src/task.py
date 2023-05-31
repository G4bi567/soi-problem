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

    for _ in range(n):
        

    values=[float(x) for x in d]
    print(values)
    maxDiff = values[1]
    data= [float(x) for x in d[2:]]
    print(data)
    i=1
    n=0
    l= [0 if abs(data[_]-data[_+1])<maxDiff else 1 for _ in range(len(data)-1)]
    if 1 in l:
        isOK=False
    else:
        isOK=True
    while isOK==False:
        i=0
        while i < len(data)-1:
            
            data[i]=(data[i-1]+data[i+1])/2
            i+=1
        l= [0 if abs(data[_]-data[_+1])<maxDiff else 1 for _ in range(len(data)-1)]
        if 1 in l:
            isOK=False
        else:
            isOK=True
        n+=1
    print(n)
        

    


if __name__ == '__main__':
    main()