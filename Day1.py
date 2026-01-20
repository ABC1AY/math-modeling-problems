import random

# --- 1. 参数设置 ---
TOTAL_SEATS = 50  # 总座位数
SIM_TIME = 840  # 模拟时长（14小时 = 840分钟）
T_LIMIT = 20  # 暂离保护时间（分钟）
ARRIVAL_PROB = 0.3  # 每分钟有新同学到达的概率（λ）

# --- 2. 初始化座位状态 ---
# 每个元素记录该座位：[状态, 暂离计时器]
# 状态说明：0-空闲, 1-学习中, 2-暂离中
seats = [[0, 0] for _ in range(TOTAL_SEATS)]

occupied_minutes = 0  # 记录总的有效学习分钟数

# --- 3. 开始蒙特卡洛模拟 ---
for t in range(SIM_TIME):
    # A. 判定新同学到达
    if random.random() < ARRIVAL_PROB:
        # 寻找空位（状态为0的座位）
        for s in range(TOTAL_SEATS):
            if seats[s][0] == 0:
                seats[s][0] = 1  # 坐下学习
                break

    # B. 更新每个座位的实时情况
    for s in range(TOTAL_SEATS):
        status = seats[s][0]

        if status == 1:  # 学习中
            occupied_minutes += 1
            # 模拟随机离开（比如平均学习2小时，每分钟离开概率1/120）
            if random.random() < (1 / 120):
                # 判定是“彻底走”还是“暂时走”
                if random.random() < 0.4:  # 40%概率是暂离（厕所/接电话）
                    seats[s][0] = 2
                    seats[s][1] = 0  # 计时器清零
                else:
                    seats[s][0] = 0  # 彻底走，空出座位

        elif status == 2:  # 暂离保护中
            seats[s][1] += 1
            # 模拟回座概率（暂离通常15分钟回）
            if random.random() < (1 / 15):
                seats[s][0] = 1
            # 如果超过了 T_LIMIT 还没回来
            elif seats[s][1] > T_LIMIT:
                seats[s][0] = 0  # 座位被管理员清空

# --- 4. 计算并输出结果 ---
utilization = (occupied_minutes / (TOTAL_SEATS * SIM_TIME)) * 100
print(f"在 T_limit = {T_LIMIT} 分钟的规则下：")
print(f"50个座位的总有效利用率为: {utilization:.2f}%")