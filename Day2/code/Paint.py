import numpy as np
import matplotlib.pyplot as plt

# 1. 设置坐标轴范围
x = np.linspace(0, 8, 400)

# 2. 定义约束条件直线
# 2x + 2y = 12  =>  y = 6 - x
y1 = 6 - x
# x + 2y = 8    =>  y = 4 - 0.5x
y2 = 4 - 0.5*x
# x = 4 (垂直线，绘图时特殊处理)

# 3. 开始绘图
plt.figure(figsize=(8, 8))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文

# 画出约束直线
plt.plot(x, y1, label=r'$2x + 2y \leq 12$ (设备I)', color='blue', linestyle='--')
plt.plot(x, y2, label=r'$x + 2y \leq 8$ (设备II)', color='green', linestyle='--')
plt.axvline(x=4, label=r'$x \leq 4$ (设备III)', color='red', linestyle='--')

# 4. 填充可行域
# 可行域是这几条线与坐标轴围成的多边形
y_min = np.minimum(y1, y2)
plt.fill_between(x, 0, y_min, where=(x <= 4), color='gray', alpha=0.3, label='可行域')

# 5. 标出关键顶点
# 经过计算，顶点为 (0,0), (4,0), (4,2), (2,3), (0,4)
points = [(0, 0), (4, 0), (4, 2), (2, 3), (0, 4)]
for p in points:
    plt.plot(p[0], p[1], 'ko') # 画黑点
    plt.text(p[0]+0.1, p[1]+0.1, f'({p[0]},{p[1]})')

# 6. 特别标注最优解 (4, 2)
plt.plot(4, 2, 'ro', markersize=10)
plt.annotate('最优解 (4, 2)\n利润: 700', xy=(4, 2), xytext=(5, 3),
             arrowprops=dict(facecolor='black', shrink=0.05))

# 7. 设置图表细节
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.xlabel('产品 A 产量')
plt.ylabel('产品 B 产量')
plt.title('生产计划线性规划图解')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()
