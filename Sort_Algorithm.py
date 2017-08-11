
# coding: utf-8

# # 几种常见的排序算法

# ## 1.插入排序

# In[2]:



import time
from functools import wraps
 
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    for i in range(100000): 
        
        result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer

@fn_timer
def insertedsort(l):
    for i in range(1,len(l)):
        j = i-1
        while l[i]<l[j] and j>-1:
            key = l[i]
            l[j+1] = l[j]
            i = j
            l[i] = key
            j -= 1
                
    return l
if __name__ == "__main__":
    l = [3,2,5,1,7,9,7,0,10]
    result = insertedsort(l)
    print (result)
                


# In[ ]:




# In[3]:

@fn_timer
def insertedsorted(l):
    for i in range(1,len(l)):
        for j in range(i-1,-1,-1):
            
        
            while l[i]<l[j]:
                key = l[i]
                l[j+1] = l[j]
                i = j
                l[i] = key
        
                
    return l

if __name__ == "__main__":
    l = [3,2,5,1,7,9,7,0,10]
    result = insertedsorted(l)
    print (result)
                


# In[ ]:




# ## 2.冒泡排序

# In[4]:

@fn_timer
def maopaosort(l):
    for index in range(len(l)-1):
        if l[index]>l[index+1]:
            l[index],l[index+1] = l[index+1],l[index]
    return l
if __name__ == "__main__":
    l = [3,2,5,1,7,9,7,0,10]
    result = insertedsort(l)
    print result    
    


# ## 3. 快速排序

# In[1]:

'''
def QuickSort(l,front,end):
    if front < end:
        pivot_index = Partition(l,front,end)
        QuickSort(l,front,pivot_index-1)
        QuickSort(l,pivot_index+1,end)
    return l
    
def Partition(l,front,end):
    pivot = l[end]
    i = front - 1
    for j in range(end):
        if l[j] < pivot:
            i += 1
            l[i],l[j] = l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def main():
    l = [3,2,5,1,7,9,7,0,6] 
    index = range(len(l))
    print index[0],index[-1]
    result = QuickSort(l,index[0],index[-1])
    print result

    
    
if __name__ == "__main__":
    main()
'''

def QuickSort(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        pivot = Arr[-1]
        LessThan_pivot = [element for element in Arr[:-1] if element <= pivot]
        GreatThan_pivot = [element for element in Arr[:-1] if element > pivot]
        return QuickSort(LessThan_pivot) + [pivot] + QuickSort(GreatThan_pivot)

if __name__ == "__main__":
    l = [3,2,5,1,7,9,7,0,10]
    result = QuickSort(l)
    print result

    


# ## 4.归并排序
# 

# In[33]:

def Merge(Arr,L,M,R):
    Left_Size = M - L
    Right_Size = R - M + 1
    Left_Arr = []
    Right_Arr = []
    # fill in the left sub array
    for i in range(L,M):
        Left_Arr.append(Arr[i])
    #fill in the right sub array
    for j in range(M,R+1):
        Right_Arr.append(Arr[j])
    #Merge into the original array
    i = 0
    j = 0
    k = L
    while i<Left_Size and j<Right_Size:
        if Left_Arr[i] < Right_Arr[j]:
            Arr[k] = Left_Arr[i]
            i += 1
            k += 1
        else:
            Arr[k] = Right_Arr[j]
            j += 1
            k += 1
    while i<Left_Size:
        Arr[k] = Left_Arr[i]
        i += 1
        k += 1
    while j < Right_Size:
        Arr[k] = Right_Arr[j]
        j += 1
        k += 1
def MergeSort(Arr,L,R):
    if L==R:
        return 
    else:
        
        M  = (L + R) // 2
        MergeSort(Arr,L,M)
        MergeSort(Arr,M+1,R)
        Merge(Arr,L,M+1,R)

if __name__ == "__main__":
    items = raw_input("Please input the unsorted List separated by commas: ")
    collection = [int(item) for item in items.strip().split(",")]
    print collection
    index = range(len(collection))
    L = index[0]
    R = index[-1]
    
    MergeSort(collection,L,R)
    print collection
    

            
        
    
        


# In[21]:

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python"""
    length = len(collection)
    if length > 1:
        midpoint = length//2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1
        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1
        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1
    return collection

if __name__ == "__main__":
    items = raw_input("Please input the unsorted List separated by commas: ")
    print items
    unsorted = [int(item) for item in items.split(",")]
    sorted_list = merge_sort(unsorted)
    print sorted_list
    
    


# ## 5.选择排序

# In[6]:

def selection_sort(collection):
    length = len(collection)
    if length == 1:
        pass
    else:
        for i in range(length-1):
            for j in range(i+1,length):
                
                if collection[i] > collection[j]:
                    
                    collection[i],collection[j] = collection[j],collection[i]
                    
    return collection
            
                
            


# In[7]:

collection = [2,3,2,5,1]
result = selection_sort(collection)
print result


# In[ ]:



