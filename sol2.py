import random

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



def solution(A):
    return task(tuple(A))

