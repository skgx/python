nums=[1,2,3,4,5,6,7,8,9]
alpha=['a','v','e','c']
nums.sort(reverse=True) #this changes the original list
alpha.sort(reverse=True)
print(nums)
print(alpha)
nums.sort()
sorted_num=sorted(nums) #this way we can prevent from changing the list
print(nums)

for num in nums:
    print(num)

for index,num in enumerate(nums): #this returns the index with the values
    print(index,num)

alpha_join=','.join(alpha) #returns the content of list separated by ,
print(alpha_join)

#lists are mutable and tuples are immutable