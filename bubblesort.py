def bubble_sort(input_list):
    n=len(input_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if input_list[j]>input_list[j+1]:
                temp=input_list[j]
                input_list[j]=input_list[j+1]
                input_list[j+1]=temp

list=[1,4,2,6,8,4]
print(list)
bubble_sort(list)
print(list)
