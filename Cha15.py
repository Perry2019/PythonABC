# Cha 15
# 15.2 绘制简单的折线图
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

# 15.2.1 修改标签文字和线条粗细
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()

# 15.2.5 自动计算数据
import matplotlib.pyplot as plt
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c='red', edgecolors='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()

# 15.2.8 使用颜色映射
import matplotlib.pyplot as plt
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()