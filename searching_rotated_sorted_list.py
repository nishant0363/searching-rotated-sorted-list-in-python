# test = { 'input' : { 'nums' : [5, 6, 9, 0, 2, 3, 4] }, 'query': 3 ,'output': 5 }
nums = [5, 6, 9, 0, 2, 3, 4]
query = 6
output = 1
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1 
    
    while lo <= hi:
        mid = ( hi + lo ) // 2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo1:", lo, ", hi1:", hi, ", mid1:", mid, ", mid_number1:", mid_number)
        
        if mid > 0 and mid_number < nums[mid-1]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0

print( f'NO of rotations is {count_rotations_binary(nums)}' )

if count_rotations_binary(nums) == 0:
    def testlocation( nums , query , mid):
        if nums[mid] == query:
            if mid-1 >=0 and nums[mid-1] ==query:
                return 'Left'
            else :
                return 'Found'
        elif nums[mid] > query:
            return 'Right'
        elif nums[mid] < query:
            return 'Left'
    
    def locatenums(nums , query):
        lo , hi = 0 , len(nums)-1
        while lo <= hi:

            mid = (lo + hi) // 2
            result = testlocation(nums , query , mid)
            if result == "Found":
                return mid
            elif result == "Left":
                hi = mid -1
            elif result == "Right":
                lo = mid +1
        return -1
    print(locatenums(nums,query))


else :
    if query < nums[0]:
        nums2 = nums[count_rotations_binary(nums)+1 :  ]
    else:
        nums2 = nums[0 : count_rotations_binary(nums)+1]
    print(f'New_list is {nums2}')
    def testlocation( nums2 , query , miD):
        if nums2[miD] == query:
            if miD-1 >=0 and nums2[miD-1] ==query:
                return 'Left'
            else :
                return 'Found'
        elif nums2[miD] > query:
            return 'Right'
        elif nums2[miD] < query:
            return 'Left'
    
    def locatenums2(nums2 , query):
        lo , hi = 0 , len(nums2)-1
        while lo <= hi:
            miD = (lo + hi) // 2
            result = testlocation(nums2 , query , miD)
            if result == "Found":
                return miD
            elif result == "Left":
                hi = miD -1
            elif result == "Right":
                lo = miD +1
        return -1
    print(locatenums2(nums2,query))
    
if nums2 == nums[count_rotations_binary(nums)+1 :  ] :
    print(f' position of {query} is {(locatenums2(nums2,query) + count_rotations_binary(nums) + 1)} ')

elif nums2 == nums[0 : count_rotations_binary(nums)+1]:
          print(f' position of {query} is {locatenums2(nums2,query) } ')