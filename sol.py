import itertools
import functools

def solution(input_list:list):
    input_list.sort()

    n = len(input_list)

    for length in range(n,1,-1):
        for combination in itertools.combinations(input_list,length):
            first = combination[0]
            last = combination[-1]
            if not ( ( last - first ) % ( length -1 ) ):
                if ( sum(combination) == (( first + last )*length)/2):
                    print(combination)
                    return length
        print(length)
        

@functools.cache
def task(inputlist,res =0 ,count=0):
    if len(inputlist) < 2:
        return count

    rset = {0}

    result = inputlist[0]+inputlist[1]
    result_m = inputlist[0]+inputlist[-1]
    result_l = inputlist[-2]+inputlist[-1]

    if res:
        if res == result:
            rset.add( task(inputlist[2:],res,count+1) )

        if res == result_m:
            rset.add( task(inputlist[1:-1],res,count+1) )

        if res == result_l:
            rset.add( task(inputlist[:-2],res,count+1) )

        if not max(rset):
            return count
    else:
        rset.add( task(inputlist[2:],res,count+1) )
        rset.add( task(inputlist[1:-1],result_m,count+1) )
        rset.add( task(inputlist[:-2],result_l,count+1) )

    return max(rset)


def task2(first,last,result=0,count=0):

    if (last-first+1) < 2:
        return count

    r =  dp_array[first][last].get(result) 
    if r:
        return r

    rset = {0}

    result1 = iplist[first] + iplist[first+1]
    result_m = iplist[first]+iplist[last]
    result_l = iplist[last-1]+iplist[last]

    if result:
        if result == result1:
            rset.add( task2(first+2,last,result,count+1) )

        if result == result_m:
            rset.add( task2(first+1,last-1,result,count+1) )

        if result == result_l:
            rset.add( task2(first,last-2,result,count+1) )

        if not max(rset):
            dp_array[first][last][result] = count
            return count
    else:
        rset.add( task2(first+2,last,result1,count+1) )
        rset.add( task2(first+1,last-1,result_m,count+1) )
        rset.add( task2(first,last-2,result_l,count+1) )

    dp_array[first][last][result] = max(rset)
    return max(rset)

def solution(A):

    global iplist
    global dp_array

    iplist = tuple(A)
    n = len(A)

    dp_array =  [ [ {} for i in range(n) ] for ii in range(n) ] 


    return task2(0,n-1)
