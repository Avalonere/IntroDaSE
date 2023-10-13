x = eval(input("请输入第一个数："))
y = eval(input("请输入第二个数："))
z = eval(input("请输入第三个数："))
nums = [x, y, z]
nums.sort()
print("从小到大的顺序是：")
for num in nums:
    print(num)
