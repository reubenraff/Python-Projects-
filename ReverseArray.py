'''def reverseArray(A):
    if A == []:
        return(A)
    else:
        return(reverseArray(A[1:]) + A[:1])         



reverseArray([1,2,3,4])'''



def reverseArray(array):
    if array == []:
        return(array)
    else:
        return(reverseArray(array[1:]) + array[0])
reverseArray([1,2,3])
