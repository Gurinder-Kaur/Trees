def quicksort(array,st,end):
    if(st<end):
        q=partition(array,st,end)
        quicksort(array,st,q-1)
        quicksort(array,q+1,end)
def partition(array,st,end):
    x=array[end]
    i=st-1
    for j in range(st,end):
        if array[j]<=x:
            i=i+1
            array[i],array[j]=array[j],array[i]

    array[i+1],array[end]=array[end],array[i+1]

    return i+1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
start=0
end=len(test)
quicksort(test,start,end-1)
print(test)
