import pulp

# 1. 建立问题模型：求最大化 (LpMaximize)
prob = pulp.LpProblem("Maximize_Factory_Profit", pulp.LpMaximize)

# 2. 定义决策变量
# x: 产品A的数量, y: 产品B的数量
# lowBound=0 表示产量不能为负, cat='Continuous' 表示连续变量
x = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# 3. 设定目标函数 (Total Profit)
prob += 100 * x + 150 * y, "Total_Profit"

# 4. 添加约束条件 (各设备工时限制)
prob += 2 * x + 2 * y <= 12, "Equipment_I_Constraint"
prob += 1 * x + 2 * y <= 8,  "Equipment_II_Constraint"
prob += 4 * x + 0 * y <= 16, "Equipment_III_Constraint"

# 5. 执行求解
prob.solve()

# 6. 输出结果
print(f"解算状态: {pulp.LpStatus[prob.status]}")
print(f"产品 A 最佳产量: {pulp.value(x)} 件")
print(f"产品 B 最佳产量: {pulp.value(y)} 件")
print(f"最大总利润为: {pulp.value(prob.objective)} 元")
