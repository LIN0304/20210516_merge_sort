def merge_sort(inp_arr):# merge sort
    size=len(inp_arr)
    if size>1:
        middle=size//2
        left_arr=inp_arr[:middle]
        right_arr=inp_arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        p=q=r=0
        left_size=len(left_arr)
        right_size=len(right_arr)
        while p<left_size and q<right_size:
            if left_arr[p]<right_arr[q]:
                inp_arr[r]=left_arr[p]
                p=p+1 # or p+=1
            else:
                inp_arr[r]=right_arr[q]
                q=q+1 # or q+=1
            r=r+1 # or r+=1
        while p<left_size:
            inp_arr[r]=left_arr[p]
            p=p+1 # or p+=1
            r=r+1 # or r+=1
        while q<right_size:
            inp_arr[r]=right_arr[q]
            q=q+1 # or q+=1
            r=r+1 # or r+=1
inp_arr=list(map(int, input().split()))
print("Input Array:", inp_arr)
merge_sort(inp_arr)
print("Sorted Array:", inp_arr)
