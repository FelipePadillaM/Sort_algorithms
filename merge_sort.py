def merge_sort(arr):

    if len(arr)<=1: #constant
        return 

    mid = len(arr)//2 # constant

    left_arr = arr[:mid] #constant
    right_arr = arr[mid:] # constant

    print(left_arr, right_arr) # constant

    merge_sort(left_arr) # lineal
    merge_sort(right_arr) # lineal

    left_index = 0 #constant
    right_index = 0 # constant
    arr_index = 0 # constant

    while left_index < len(left_arr) and right_index < len(right_arr): # lineal

        if left_arr[left_index] < right_arr[right_index]: #constant
            arr[arr_index] = left_arr[left_index] #constant
            left_index += 1
        
        else:
            arr[arr_index] = right_arr[right_index] #constant
            right_index += 1 #constant
        
        arr_index += 1 #constant
    
    if left_index < len(left_arr): #constant
        del arr[arr_index:] # constant
        arr += left_arr[left_index:] #constant

    elif right_index < len(right_arr): #constant
        del arr[arr_index:] # constant
        arr += right_arr[right_index:] #constant

    return arr # constant

print(merge_sort([8, 12, 1, 3, 5]))

#? 1: arr = [8, 12]
# 3: 5 <= 1, false
# 6: mid = 2
#* 8: left_arr = [8, 12], 9: right_arr = [1, 3, 5]

  #? 13: arr = [8, 12]
    # 3: 2 <= 1, false
    # 6: mid = 1
    #* 8: left_arr = [8], 9: right_arr = [12]
    # 20: while 0 < 1 and 0 < 1
    # 22: true
    # 23: arr = [8, 12]
    # 40: [8, 12]

  #? 14: arr = [1, 3, 5]
    # 3: 3 <= 1, false
    # 6: mid = 1
    #* 8: left_arr = [1], 9: right_arr = [3, 5]
      #? 14: arr = [3, 5]
        # 3: 2 <= 1, false
        # 6: mid = 1
        #* 8: left_arr = [3], 9: right_arr = [5]
        # 40: [3, 5]
    # 40: [1, 3, 5]
  
  # 19: arr =[8, 12, 1, 3, 5], left_arr = [8, 12], right_arr = [1, 3, 5]
  # 20: while 0 < 2 and 0 < 3
    # 22: 8 < 1, false
    # 27: arr = [1, 12, 1, 3, 5]

  # 20: while 0 < 2 and 1 < 3
    # 22: 8 < 3, false
    # 27: arr = [1, 3, 1, 3, 5]

  # 20: while 0 < 2 and 2 < 3
    # 22: 8 < 5, false
    # 27: arr = [1, 3, 5, 3, 5]

  # 20: while 0 < 2 and 3 < 3, false
  # 32: 0 < 2, true
    # 33: arr = [1, 3, 5] 
    # 34: arr = [1, 3, 5 ,8, 12]
  
  #* 40: [1, 3 ,5 ,8 ,12], answer.
    

