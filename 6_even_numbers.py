nums = map(int, input().split(", "))
even_indexes = [index for index, value in enumerate(nums) if value % 2 == 0]
print(even_indexes)
