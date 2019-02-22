def mergesort(arr,first,last):
    if(first<last):
        mid=(first+last)/2
        mergesort(arr,first,mid)
        mergesort(arr,mid+1,last)
    merge(arr,first,mid,last)

def merge(arr,first,mid,last):
    n1=mid-first+1
    n2=last-mid
    for i in range(1,n1+1):
        arr1[i]=arr[first+i-1]
    for j in range(1,n2+1):
        arr2[j]=arr[mid+j]
    arr1[n1+1]=1000
    arr2[n2+1]=1000
    i=j=1
    for k in range(first,last+1):
        if(arr1[i]<arr2[i]):
            arr[k]=arr1[i]
            i=i+1
        else:
            arr[k]=arr2[j]
            j=j+1

list=[3,4,1,6,9,14,20,21,25,21]
l=len(list)
start=0
mergesort(list,start,l-1)
print(list)
