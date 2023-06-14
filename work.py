'''
def strcounter(s): #O(M*N)
    for syn in set(s):
        counter = 0
        for sub_sin in s:
            if syn == sub_sin:
                counter+=1
        print(syn, counter)

strcounter('hello')


def strcounter(s): #O(N**2)
    for syn in set(s):
        counter = 0
        for sub_sin in s:
            if syn == sub_sin:
                counter+=1
        print(syn, counter)

strcounter('hello')'''
def strcounter(s):#0(N)
    syns_counter ={}
    for syn in s:
        syns_counter[syn] = syns_counter.get(syn, 0)+1
    for syn, count in syns_counter.items():
        print(syn, count)
    
strcounter('aassssdddddnnnncccckkkdddbbb')