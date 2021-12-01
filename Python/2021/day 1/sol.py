with open('input', 'r') as fp:
    nums = [int(x) for x in fp]

x = 0
for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        x += 1
print(x)

x = 0
for i in range(len(nums) - 3):
    if sum(nums[i : i + 3]) < sum(nums[i + 1 : i + 4]):
        x += 1
print(x)
