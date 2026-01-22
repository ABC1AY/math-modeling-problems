import pulp

# 1. 初始化模型：求最大化 (LpMaximize)
model = pulp.LpProblem("科研经费优化方案", pulp.LpMaximize)

# 2. 准备数据
devices = ["高性能服务器", "三维打印机", "精密示波器", "无人机平台", "实验机器人"]
prices = [4.5, 2.3, 3.8, 1.5, 3.0]  # 单位：万元
values = [9.2, 6.8, 8.5, 5.0, 7.2]  # 科研价值评分

# 3. 定义变量：0-1变量 (Binary)
# x[i] = 1 代表购买，0 代表不买
x = [pulp.LpVariable(f"x_{i}", cat='Binary') for i in range(len(devices))]

# 4. 目标函数：总科研价值最大化
model += pulp.lpSum([values[i] * x[i] for i in range(len(devices))]), "总价值"

# 5. 约束条件：总预算不超过 10 万元
model += pulp.lpSum([prices[i] * x[i] for i in range(len(devices))]) <= 10.0, "预算限制"

# 6. 求解
model.solve()

# 7. 打印结果
print(f"--- 求解状态: {pulp.LpStatus[model.status]} ---")
print("建议购买名单：")
total_cost = 0
for i in range(len(devices)):
    if pulp.value(x[i]) == 1:
        print(f"✅ {devices[i]}: {prices[i]}万 (价值 {values[i]})")
        total_cost += prices[i]

print("-" * 30)
print(f"总科研价值评分: {pulp.value(model.objective):.2f}")
print(f"总经费支出: {total_cost:.2f} 万元")
print(f"剩余经费: {10.0 - total_cost:.2f} 万元")
