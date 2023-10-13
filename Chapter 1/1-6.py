w = eval(input("请输入第一个数："))
x = eval(input("请输入第二个数："))
y = eval(input("请输入第三个数："))
z = eval(input("请输入第四个数："))
nums = [w, x, y, z]
nums.sort(reverse=True)
print("从大到小的顺序是：")
for num in nums:
    print(num)
