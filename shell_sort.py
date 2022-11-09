def shell_sort(arr):
    
    size = len(arr)#constant
    
    if size < 2:#constant
        return arr#constant
    #* Start with a big gap 
    gap = size // 2#constant
    
    while gap > 0:#lineal

        for i in range(gap, size):#lineal
            val = arr[i]#constant
            j = i#constant

            while j >= gap and arr[j - gap] > val:#lineal
                arr[j] = arr[j - gap]#constant
                j -= gap#constant
            arr[j] = val#constant
        #* reduce the gap
        gap //= 2#constant
        
    return arr

print(shell_sort([8, 12, 1, 3, 5]))

# 3: size = 5
# 5: false
# 8: gap = 2
# 10: while(2 > 0): for each loop I have written only when the array changes 
#                   because is too long for explain in comments
        # 12: range(2, 5)
          # 16: while 2 >= 2 and 8 > 1
            # 17: [8, 12, 8, 3, 5]
            # 18: j = 0
          # 19: [1, 12, 8, 3, 5]

          # 16: while 3 >= 2 and 12 > 3
            # 17: [1, 12, 8, 12, 5]
            # 18: j = 1
          # 19: [1, 3, 8, 12, 5]

          # 16: while 4 >= 2 and 8 > 5
            # 17: [1, 3, 8, 12, 8]
            # 18: j = 2
          # 19: [1, 3, 5, 12, 8]
# 21: gap = 1
# 10: while(1 > 0):
        # 12: range(1, 5)
          # 16: while 4 >= 1 and 12 > 8
            # 17: [1, 3, 8, 12, 12]
            # 18: j = 3
          # 19: [1, 3, 5, 8, 12]
# 21: gap = 0
# 10: false

#* 23: [1, 3, 5, 8, 12], answer.
          
            