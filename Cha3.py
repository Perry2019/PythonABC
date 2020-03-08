# Cha 3.1 Basic list
# 3.1.1 访问列表元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].upper())

# 3.1.2 列表中的索引从0开始
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].upper())
print(bicycles[-1].title())

# 3.1.3 使用列表中的值
bicycles = ['trek','cannondale','redline','specialized']
message = "My favorite bicycle is a " + bicycles[-2].title() + "."
print(message)

# Cha 3.2 Modify list
# 3.2.1 修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[2] = 'ducati'
print(motorcycles)

# 3.2.2 列表中添加元素
# 列表末尾添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
# 列表中插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(1, 'dajiang')
print(motorcycles)

# 3.2.2 列表中删除元素
# 删除任意已知位置的元素且该元素不再可用
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[2]
print(motorcycles)
# 删除列表末尾的元素且该元素可用
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
# 删除列表任意位置的元素且该元素可用
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(2)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# 根据值删除列表中的元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
too_expensive = 'yamaha'
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

# Cha 3.3 Organized list
# 3.3.1 sort对列表按字母顺序排序
cars = ['bmw','audi','toyota','bench']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 3.3.2 sort functin对列表按字母顺序临时排序
cars = ['bmw','audi','toyota','bench']
print('Here is the original list:')
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

# 3.3.3 反转打印列表
cars = ['bmw','audi','toyota','bench']
print(cars)
cars.reverse()
print(cars)

# 3.3.4 确定列表长度
cars = ['bmw','audi','toyota','bench']
print(len(cars))