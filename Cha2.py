# Cha 2.2 Variables 变量
message = "Hello Python World!"
print(message)

# Cha 2.3 String 字符串
# 2.2.1 使用方法修改字符串大小写
name = "ada loveles"
print(name.title())
print(name.upper())
print(name.lower())

# 2.3.2 合并字符串
first_name = "ada"
last_name = "lovelaces"
full_name = first_name + " " + last_name
message1 = "Hello, " + full_name.title() + "!"
print(message1)

# 2.3.3 制表符/换行符
print("Languages:\n\tPython\n\tJava\n\tC++")

# 2.3.4 删除空白
favorite_language = ' Python '
f1 = favorite_language.rstrip()
print(f1)
f2 = favorite_language.lstrip()
print(f2)
f3 = favorite_language.strip()
print(f3)

# Cha 2.4 Number
# 2.4.1 int
a = 3**3
print(a)

# 2.4.2 flot
b = 0.05 * 2
print (b)

# 2.4.3 str()
age = 23
message2 = "Happy " + str(age) + "rd Birthday!"
print(message2)
import this
