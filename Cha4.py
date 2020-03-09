# Cha 4.1 for loop
# 4.1
magicians = ['alice','bob','david','carolina']
for magician in magicians:
    print(magician)

# 4.1.2 在for循环中执行更多的操作
magicians = ['alice','bob','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# 4.1.3 在for循环后执行操作
magicians = ['alice','bob','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone. That was a great magic show!")

# 4.3 数字列表
# 4.3.1 使用函数rangr
for value in range(1,5):   # range打印的范围需要加减1
    print(value)

# 4.3.2 使用range创建数字列表
numbers = list(range(1,6))
print(numbers)

# 10以内偶数的平方
squares = []
for value in range(1,11,2):
    square = value**2
    squares.append(square)

print(squares)

# 4.3.3 数字的统计计算
digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

# 4.4 使用列表
# 4.4.1 slicing
players = ['charles','bob','hank','alice']
print(players[-2])

# 4.4.2 遍历切片
players = ['charles','bob','hank','alice']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 4.4.3 复制列表
my_foods = ['pizza','falafel','hanboger','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend'sfavorite foods are:")
print(friend_foods)

# 4.5 Tuple
# 4.5.1 定义元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 4.5.2 遍历元组中的所有值
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,60)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)