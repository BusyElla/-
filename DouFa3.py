'''
[斗法高手]
斗法比赛模拟代码
'''




import random

'''
函数-随机姓名和随机性格
'''
### 这个是用来加载字库的
def load_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

### 这个是用来生成姓名的
def generate_random_name(surnames_file, names_file):
    # 从文件加载姓氏和名字用字
    surnames = load_file_to_list(surnames_file)
    name_characters = load_file_to_list(names_file)

    # 随机选择姓氏
    surname = random.choice(surnames)

    # 随机决定名字是单字还是双字
    name_length = random.choice([1, 2])

    if name_length == 1:
        # 生成单字名
        first_name = random.choice(name_characters)
        return surname + first_name
    else:
        # 生成双字名
        first_name = random.choice(name_characters)
        second_name = random.choice(name_characters)
        return surname + first_name + second_name

### 这个是用来生成多个姓名的
def generate_multiple_names(surnames_file, names_file, count):
    names = []
    for _ in range(count):
        names.append(generate_random_name(surnames_file, names_file))
    return names

# 使用示例
surnames_file = 'xingshi.txt'  #姓氏数据库
names_file = 'xingming.txt'   #姓名数据库
count_name = 1  # 想要生成的名字数量

generated_names = generate_multiple_names(surnames_file, names_file, count_name)

# # 打印生成的名字
# for name in generated_names:
#     print(name)


def load_personality_traits(file_path):
    # 从文件中读取性格词汇
    with open(file_path, 'r', encoding='utf-8') as file:
        personality_traits = [line.strip() for line in file]
    return personality_traits


def generate_random_personality_A():
    # 加载性格词汇
    personality_A = load_personality_traits('personality_A.txt')

    # 随机选择两种不同的性格
    personality_A1, personality_A2 = random.sample(personality_A, 2)

    # 生成并返回完整性格组合
    return personality_A1 + '又' + personality_A2

def generate_random_personality_B():
    # 性格描述词语
    personality_B = ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]

    # 随机选择两种不同的性格
    personality_B1 = random.choice(personality_B)

    # 生成并返回完整性格组合
    return personality_B1

# # 调用函数生成一个随机性格组合
# print("看起来"+ generate_random_personality_A()+"的"+generate_random_personality_B())


'''
比赛基本信息
'''
competition_name = input("输入本次的比赛名称（如 剑圣争霸赛、比武大会）：")
competition_n = input("输入本次的比赛届数（数字）：")



# 参赛选手数量
n = 256

### 阵营确定

menpai_call =  input("在您的设定里，不同阵营的统称是（可填写门派、家族、国家、队伍等）：")

# 初始化空列表
menpai_options = []

# 开始循环，持续让用户输入内容
while True:
    # 提示用户输入键
    menpai = input("请输入"+menpai_call+"名称（或输入 'done' 结束输入）：")
    if menpai.lower() == 'done':
        break  # 如果用户输入 'done'，结束输入

    # 将门派名称添加到列表中
    menpai_options.append(menpai)

luck_weight=input("本场比赛中的运气成分有多少（请输入0到1之间的两位小数，数字越大，比赛中的运气成分越高，数字越低，比赛越能反映真实实力，但随机性会有所不足。建议填写0.1~0.3之间的小数。）：")
luck_weight = float(luck_weight)  # 将输入转换为浮点数

# 计算列表中的项数
number_of_menpais = len(menpai_options)


# # 输出最终的门派名称列表
# print("参加本次比赛的"+number_of_menpais + "个"+menpai_call+"有：")
# for item in menpai_options:
#     print(item)
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print(" 欢迎来到" + competition_name + "第"+ competition_n + "届的比赛现场 ")
print("来自"+str(number_of_menpais) +"个"+ menpai_call +"的256名选手将在此角逐出最终的八强")
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()




# 创建一个列表来存储所有选手的字典
players = []

# 循环创建256个参赛选手的字典
for i in range(1, n + 1):
    # 随机选择门派
    menpai = random.choice(menpai_options)
    # 随机生成力量值，并精确到两位小数
    power = round(random.uniform(60, 100), 2)
    # 设置运气值为0
    luck = 0
    player_name= generate_random_name(surnames_file, names_file)
    personality_all= "一个看起来"+ generate_random_personality_A()+"的"+generate_random_personality_B()
    gender = random.choice("女""男")

    # 创建选手的字典，并增加键位 "CurrentPower" 的值为 0
    player = {
        "MenPai": menpai,
        "Power": power,
        "Luck": luck,
        "CurrentPower": 0,
        "Player_Name": player_name,
        "Personality_All": personality_all,
        "Player_Num": i,
        "Gender": gender, # 性别
        #######

        # 第一轮
        "1__num": 0,
        "1__oppo": 0,
        "1__result": 0,
        "1__trigger": 0,

        # 第二轮
        '2__num': 0,
        '2__oppo': 0,
        '2__result': 0,
        '2__trigger': 0,
        # 第三轮
        '3__num': 0,
        '3__oppo': 0,
        '3__result': 0,
        '3__trigger': 0,
        # 第四轮
        '4__group': 0,
        '4_1_num': 0,
        '4_1_oppo': 0,
        '4_1_result': 0,
        '4_1_trigger': 0,
        '4_2_num': 0,
        '4_2_oppo': 0,
        '4_2_result': 0,
        '4_2_trigger': 0,
        '4_3_num': 0,
        '4_3_oppo': 0,
        '4_3_result': 0,
        '4_3_trigger': 0,
        '4__score': 0,
        # 第五轮
        '5__num': 0,
        '5__oppo': 0,
        '5__result': 0,
        '5__trigger': 0,
        # 第六轮
        # '6_1_num': 0,
        # '6_1_oppo': 0,
        # '6_1_result': 0,
        # '6_1_trigger': 0,
        # '6_2_num': 0,
        # '6_2_oppo': 0,
        # '6_2_result': 0,
        # '6_2_trigger': 0,
        # '6_3_num': 0,
        # '6_3_oppo': 0,
        # '6_3_result': 0,
        # '6_3_trigger': 0,
        # '6_4_num': 0,
        # '6_4_oppo': 0,
        # '6_4_result': 0,
        # '6_4_trigger': 0,
        # '6_5_num': 0,
        # '6_5_oppo': 0,
        # '6_5_result': 0,
        # '6_5_trigger': 0,
        # '6_6_num': 0,
        # '6_6_oppo': 0,
        # '6_6_result': 0,
        # '6_6_trigger': 0,
        # '6_7_num': 0,
        # '6_7_oppo': 0,
        # '6_7_result': 0,
        # '6_7_trigger': 0,
    }

    # 给选手字典起名为 "Player_i"
    player_name = f"Player_{i}"

    # 添加到列表中
    players.append((player_name, player))


# 自定义选手函数
def customize_players(players):
    player_index = 0
    while player_index < len(players):
        customize = input("是否要自定义选手？(yes/no): ").lower()
        if customize == "yes":
            name = input(f"请输入自定义选手{player_index + 1}的姓名: ")
            gender = input(f"请输入{name}的性别: ")
            power =  float(input(f"请输入{name}的实力（随机定义的选手实力值在60-100之间，但您可根据需要定义自定义选手的实力值。比如，如果您定义为101，则您的选手一定是所有选手中实力值最高的）: "))
            menpai = input(f"请输入{name}的"+ menpai_call +":" )
            # 引导用户输入两个性格词语
            personality_A1 = input(f"请输入{name}的第一个性格（2个字）: ")
            personality_A2 = input(f"请输入{name}的第二个性格（2个字）: ")

            # 引导用户输入 MBTI
            mbti = input(f"请输入{name}的 MBTI 类型: ").upper()

            # 将性格和 MBTI 组合成最终形式
            personality_all = f"一个看起来{personality_A1}又{personality_A2}的{mbti}"

            # 替换随机生成的选手
            players[player_index] = (name, {
                "Player_Name": name,
                "Power": power,
                "MenPai": menpai,
                "Personality_All": personality_all,
                "CurrentPower": 0,
                "Player_Num": player_index + 1,
                "Gender": gender  # 可以根据需要调整
            })

            print(f"已自定义选手{player_index + 1}: {name}，实力：{power}，性格：{personality_all}")
            player_index += 1  # 移动到下一个选手
        elif customize == "no":
            break
        else:
            print("请输入有效的选项 'yes' 或 'no'。")


customize_players(players)


# 创建一个字典来存储分组统计
menpai_groups = {}

# 按照MenPai分组
for name, player in players:
    menpai = player["MenPai"]
    power = player["Power"]

    if menpai not in menpai_groups:
        menpai_groups[menpai] = {"count": 0, "total_power": 0}

    menpai_groups[menpai]["count"] += 1
    menpai_groups[menpai]["total_power"] += power

# 打印分组统计结果
for menpai, stats in menpai_groups.items():
    count = stats["count"]
    average_power = stats["total_power"] / count
    print(f"{menpai}有{count}位选手参加，平均实力为{average_power:.2f}；")

# 打印所有参赛选手和其内容
print("\n以下是完整的参赛名单：")
for player_name, player in players:  # 解包为 player_name 和 player
    print(f"{player['Player_Name']}（{player['Player_Num']}-{player['Gender']}），来自{player['MenPai']}，{player['Personality_All']}，实力值为{player['Power']}")





'''
开始比赛
'''

### 前三轮：普通一对一比赛
def conduct_round(players, round_number):
    # 先给每个字典的 Luck 进行随机赋值，并计算 CurrentPower
    for player_name, player in players:
        # 使用 random.uniform() 生成带两位小数的 luck 值
        luck = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
        player["Luck"] = luck

        # 计算 CurrentPower
        player["CurrentPower"] = player["Power"] + player["Luck"]

    # 存储比赛结果的字典
    results = {}

    # 随机打乱选手列表，并进行两两分组
    random.shuffle(players)
    groups = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]

    # 对每一组进行比较
    for i, (player1, player2) in enumerate(groups):
        # 组名
        group_name = f"R{round_number}_G{i + 1}"

        # 比较两者的 CurrentPower
        if player1[1]["CurrentPower"] > player2[1]["CurrentPower"]:
            winner = player1
            loser = player2
        else:
            winner = player2
            loser = player1

        # 存储胜者和败者
        results[f"{group_name}_winner"] = winner
        results[f"{group_name}_loser"] = loser

        # 更新每个选手的“1__num”、“1__oppo”和“1__result”
        match_number = i + 1  # 比赛的场次序号

        # 更新胜者的信息
        winner[1][f"{round_number}__num"] = match_number
        winner[1][f"{round_number}__oppo"] = loser[1]["Player_Num"]
        winner[1][f"{round_number}__result"] = 1  # 胜利标记为1

        # 更新败者的信息
        loser[1][f"{round_number}__num"] = match_number
        loser[1][f"{round_number}__oppo"] = winner[1]["Player_Num"]
        loser[1][f"{round_number}__result"] = 0  # 失败标记为0

        # 输出格式化结果
        formatted_result = format_result(round_number, match_number, winner[1], loser[1])
        print(formatted_result)

    return results

#输出格式调整函数
def format_result(round_number, game_number, winner, loser):
    # 提取信息
    winner_name = winner["Player_Name"]
    winner_num = winner["Player_Num"]
    winner_gender = winner["Gender"]
    winner_menpai = winner["MenPai"]
    winner_power = winner["Power"]
    winner_luck = winner["Luck"]
    winner_current_power = winner["CurrentPower"]

    loser_name = loser["Player_Name"]
    loser_num = loser["Player_Num"]
    loser_gender = loser["Gender"]
    loser_menpai = loser["MenPai"]
    loser_power = loser["Power"]
    loser_luck = loser["Luck"]
    loser_current_power = loser["CurrentPower"]

    # 格式化输出
    result = f"【第{round_number}轮第{game_number}场比赛】\n"
    result += f"胜者：来自{winner_menpai}的{winner_name}（{winner_num}号-{winner_gender}），{winner_power}+{winner_luck}={winner_current_power}\n"
    result += f"败者：来自{loser_menpai}的{loser_name}（{loser_num}号-{loser_gender}），{loser_power}+{loser_luck}={loser_current_power}\n"
    return result

print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print("第一轮比赛")
print("以下是第一轮对决的比赛结果。在这一轮中，256名选手将两两对决，获胜者进入下一轮。")

# 调用 conduct_round 函数进行第一轮比赛
first_round_results = conduct_round(players, 1)

# # 打印比赛结束后每位选手的信息更新
# print("\n比赛结束后，每位选手的信息更新如下：")
# for player_name, player in players:
#     print(f"选手编号 {player['Player_Num']} - {player['Player_Name']}：")
#     print(f"  比赛轮次号 (1__num): {player['1__num']}")
#     print(f"  对手编号 (1__oppo): {player['1__oppo']}")
#     print(f"  比赛结果 (1__result): {'胜利' if player['1__result'] == 1 else '失败'}")
#     print("-" * 30)

# 第二轮比赛
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print("第二轮比赛")
print("以下是第二轮对决的比赛结果。在这一轮中，128名选手将两两对决，获胜者进入下一轮。")

second_round_players = []
for key in sorted(first_round_results.keys()):
    if key.endswith('_winner'):
        second_round_players.append(first_round_results[key])

# 进行第二轮比赛
second_round_results = conduct_round(second_round_players, 2)

# 第三轮比赛
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print("第三轮比赛")
print("以下是第三轮对决的比赛结果。在这一轮中，64名选手将两两对决，获胜者进入下一轮。")

third_round_players = []
for key in sorted(second_round_results.keys()):
    if key.endswith('_winner'):
        third_round_players.append(second_round_results[key])

# 进行第三轮比赛
third_round_results = conduct_round(third_round_players, 3)


### 接下来是第四轮比赛！
def conduct_fourth_round(players, group_number):
    # 初始化每个组
    groups = [players[i:i + 4] for i in range(0, len(players), 4)]

    # 存储每组的比赛结果
    group_results = {}
    group_winner_1 = []  # 列表来存储每个小组的第一名
    group_winner_2 = []  # 列表来存储每个小组的第二名

    for g_num, group in enumerate(groups, start=1):
        group_results[g_num] = {
            'players': [],
            'matches': [],
            'scores': {}
        }
        print("………………………………………………………………………………………………")
        print(f"\n第4轮第{g_num}小组：")
        for player in group:
            player_info = f"来自{player['MenPai']}的{player['Player_Name']}（{player['Player_Num']}号-{player['Gender']}），{player['Power']}"
            group_results[g_num]['players'].append(player_info)
            group_results[g_num]['scores'][player['Player_Num']] = 0  # 初始化分数
            player[f"4__group"] = g_num  # 记录组别
            player["match_counter"] = 0  # 初始化每位选手的比赛计数器
            player["matches_played"] = []  # 记录已参加的比赛
            print(player_info)

        print("\n…………………………………………")

        # 进行小组内比赛，每个选手对其他选手各赛一场
        match_id = 1
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                player1 = group[i]
                player2 = group[j]

                # 记录比赛序号和对手
                player1["match_counter"] += 1
                player2["match_counter"] += 1

                player1[f"4_{player1['match_counter']}_num"] = match_id
                player2[f"4_{player2['match_counter']}_num"] = match_id

                player1["matches_played"].append(match_id)
                player2["matches_played"].append(match_id)

                # 记录对手
                player1[f"4_{player1['match_counter']}_oppo"] = player2["Player_Num"]
                player2[f"4_{player2['match_counter']}_oppo"] = player1["Player_Num"]

                # 决定比赛结果
                luck1 = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
                luck2 = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
                current_power1 = player1["Power"] + luck1
                current_power2 = player2["Power"] + luck2

                if current_power1 > current_power2:
                    winner = player1
                    loser = player2
                    player1[f"4_{player1['match_counter']}_result"] = 1
                    player2[f"4_{player2['match_counter']}_result"] = 0
                    group_results[g_num]['scores'][player1['Player_Num']] += 1
                else:
                    winner = player2
                    loser = player1
                    player1[f"4_{player1['match_counter']}_result"] = 0
                    player2[f"4_{player2['match_counter']}_result"] = 1
                    group_results[g_num]['scores'][player2['Player_Num']] += 1

                match_result = f"【第4轮第{g_num}小组赛第{match_id}场】\n胜者：来自{winner['MenPai']}的{winner['Player_Name']}（{winner['Player_Num']}号-{winner['Gender']}），{winner['Power']}+{luck1 if winner == player1 else luck2}={winner['Power'] + (luck1 if winner == player1 else luck2)}\n败者：来自{loser['MenPai']}的{loser['Player_Name']}（{loser['Player_Num']}号-{loser['Gender']}），{loser['Power']}-{abs(luck1 if loser == player1 else luck2)}={loser['Power'] + (luck1 if loser == player1 else luck2)}"
                group_results[g_num]['matches'].append(match_result)
                print(match_result)

                match_id += 1

        print("\n…………………………………………")
        print(f"第4轮第{g_num}小组赛最终结果：")

        # 显示最终分数和晋级、淘汰结果
        sorted_group = sorted(group, key=lambda x: group_results[g_num]['scores'][x['Player_Num']], reverse=True)
        for idx, player in enumerate(sorted_group):
            result_str = "晋级" if idx < 2 else "淘汰"
            final_score = group_results[g_num]['scores'][player['Player_Num']]
            print(
                f"{result_str}\n来自{player['MenPai']}的{player['Player_Name']}（{player['Player_Num']}号-{player['Gender']}），{player['Power']}，{final_score}分")
            player[f"4__score"] = final_score  # 记录最终得分

        # 将小组第一名和第二名的玩家添加到列表
        if len(sorted_group) > 0:
            winner1 = sorted_group[0]
            group_winner_1.append(winner1)
        if len(sorted_group) > 1:
            winner2 = sorted_group[1]
            group_winner_2.append(winner2)

    # 返回第四轮比赛最终的 winners 和 losers
    return group_winner_1, group_winner_2






# 获取第三轮比赛胜者的玩家列表
fourth_round_players = []
for key in sorted(third_round_results.keys()):
    if key.endswith('_winner'):
        fourth_round_players.append(third_round_results[key][1])  # 只添加字典部分

# 调用 conduct_fourth_round 函数，进行第四轮比赛
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print("第四轮比赛")
print("以下是第四轮对决的比赛结果。在这一轮中，三十二强将会被分为八个小组，每一个小组内都进行两两对擂，根据胜负情况给每位选手计分，每组得分排名前二者进入第五轮比赛。")


fourth_round_winners, fourth_round_losers = conduct_fourth_round(fourth_round_players,1)

# print("\n第四轮比赛后，所有参与选手的详细信息如下：")
# for player in fourth_round_players:
#     print(f"选手编号 {player['Player_Num']} - {player['Player_Name']}：")
#     print(f"  门派: {player['MenPai']}")
#     print(f"  实力值: {player['Power']}")
#     print(f"  运气值: {player['Luck']}")
#     print(f"  当前实力: {player['CurrentPower']}")
#     print(f"  性格描述: {player['Personality_All']}")
#     print(f"  性别: {player['Gender']}")
#     # 打印比赛轮次的所有相关信息
#     for key, value in player.items():
#         if key.startswith("4__") or key.startswith("4_"):
#             print(f"  {key}: {value}")
#     print("-" * 30)



def conduct_fifth_round(group_winner_1, group_winner_2):
    # 第五轮比赛结果列表
    fifth_round_results = []

    # 随机打乱小组第二名的列表
    random.shuffle(group_winner_2)

    # 用于跟踪已使用的组索引
    used_indices = set()

    # 记录每场比赛的序号
    match_counter = 1

    # 遍历每个小组的第一名和第二名进行对擂
    for winner_1 in group_winner_1:
        # 确保每个 winner_1 是一个字典
        if isinstance(winner_1, dict):
            player1_name = winner_1["Player_Name"]
            player1_dict = winner_1
        else:
            player1_name, player1_dict = winner_1

        # 查找与当前选手不同组的第二名选手
        for i, winner_2 in enumerate(group_winner_2):
            # 跳过已经使用的索引
            if i in used_indices:
                continue

            # 确保每个 winner_2 是一个字典
            if isinstance(winner_2, dict):
                player2_name = winner_2["Player_Name"]
                player2_dict = winner_2
            else:
                player2_name, player2_dict = winner_2

            # 确保两个选手来自不同的分组
            if player1_dict["4__group"] != player2_dict["4__group"]:
                # 标记这个索引已被使用
                used_indices.add(i)

                # 随机赋予两个选手的 Luck
                player1_dict["Luck"] = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
                player2_dict["Luck"] = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)


                # 重新计算两个选手的 CurrentPower
                player1_dict["CurrentPower"] = player1_dict["Power"] + player1_dict["Luck"]
                player2_dict["CurrentPower"] = player2_dict["Power"] + player2_dict["Luck"]

                # 记录对手信息
                player1_dict[f"5__oppo"] = player2_dict["Player_Num"]
                player2_dict[f"5__oppo"] = player1_dict["Player_Num"]

                # 记录每位选手在第五轮比赛中的第几场比赛
                player1_dict[f"5__num"] = match_counter
                player2_dict[f"5__num"] = match_counter

                # 比较两个选手的 CurrentPower
                if player1_dict["CurrentPower"] > player2_dict["CurrentPower"]:
                    winner = (player1_name, player1_dict)
                    loser = (player2_name, player2_dict)
                    player1_dict[f"5__result"] = 1
                    player2_dict[f"5__result"] = 0
                else:
                    winner = (player2_name, player2_dict)
                    loser = (player1_name, player1_dict)
                    player1_dict[f"5__result"] = 0
                    player2_dict[f"5__result"] = 1

                # 更新记录
                player1_dict[f"5__trigger"] = match_counter
                player2_dict[f"5__trigger"] = match_counter

                # 将比赛结果添加到结果列表中
                fifth_round_results.append((winner, loser))

                # 一旦找到合适的对手，就跳出内循环，进行下一个第一名的选手
                match_counter += 1
                break

    # 打印第五轮比赛的所有结果
    print()
    print("………………………………………………………………………………………………")
    print("………………………………………………………………………………………………")
    print()
    print("第五轮比赛")
    print("以下是第五轮对决的比赛结果。在这一轮中，第四轮排名小组第一的选手会与其他组排名小组第二的选手进行对擂，获胜者为比赛八强，进入下一轮。")
    for match_index, (winner, loser) in enumerate(fifth_round_results):
        print(f"【第5轮第{match_index + 1}场比赛】")
        print(f"胜者：来自{winner[1]['MenPai']}的{winner[0]}（{winner[1]['Player_Num']}号-{winner[1]['Gender']}），{winner[1]['Power']}+{winner[1]['Luck']}={winner[1]['CurrentPower']}")
        print(f"败者：来自{loser[1]['MenPai']}的{loser[0]}（{loser[1]['Player_Num']}号-{loser[1]['Gender']}），{loser[1]['Power']}+{loser[1]['Luck']}={loser[1]['CurrentPower']}")
        print()  # 换行

    return fifth_round_results

# 使用 conduct_fourth_round 函数返回的 fourth_round_winners 和 fourth_round_losers 作为参数
fifth_round_results = conduct_fifth_round(fourth_round_winners, fourth_round_losers)




# 八强赛开始！
def conduct_sixth_round(winners, luck_weight):
    # 存储选手得分和比赛结果
    player_scores = {player[0]: 0 for player in winners}
    player_details = {player[0]: player[1] for player in winners}
    match_results = []

    # 初始化每位选手的比赛计数器
    for player_name, player_dict in winners:
        player_dict["match_counter"] = 1
        player_dict["6_match_list"] = []  # 存储实际参加的比赛列表

    print("\n八强赛开始！")
    match_number = 1  # 总比赛场次编号

    # 进行比赛
    for i, player1 in enumerate(winners):
        for j in range(i + 1, len(winners)):
            player1_name, player1_dict = player1
            player2_name, player2_dict = winners[j]

            # 重新给两个选手分配Luck
            luck1 = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
            luck2 = round(random.uniform(-20 * luck_weight, 20 * luck_weight), 2)
            player1_dict["Luck"] = luck1
            player2_dict["Luck"] = luck2

            # 重新计算Current_Power
            player1_dict["CurrentPower"] = player1_dict["Power"] + luck1
            player2_dict["CurrentPower"] = player2_dict["Power"] + luck2

            # 记录对手信息
            player1_dict[f"6_{match_number}_oppo"] = player2_dict["Player_Num"]
            player2_dict[f"6_{match_number}_oppo"] = player1_dict["Player_Num"]

            # 比较两个选手的Current_Power
            if player1_dict["CurrentPower"] > player2_dict["CurrentPower"]:
                # player1获胜
                player_scores[player1_name] += 1
                winner = player1_name
                player1_dict[f"6_{match_number}_result"] = 1
                player2_dict[f"6_{match_number}_result"] = 0
            else:
                # player2获胜
                player_scores[player2_name] += 1
                winner = player2_name
                player1_dict[f"6_{match_number}_result"] = 0
                player2_dict[f"6_{match_number}_result"] = 1

            # 保存比赛结果
            match_results.append((player1_name, player2_name, winner))

            # 更新实际参加的比赛列表
            player1_dict["6_match_list"].append(match_number)
            player2_dict["6_match_list"].append(match_number)

            # 打印比赛详细情况
            print(f"\n【八强赛第{match_number}场】")
            print(f"选手1：来自{player1_dict['MenPai']}的{player1_name}（{player1_dict['Player_Num']}号-{player1_dict['Gender']}），"
                  f"力量：{player1_dict['Power']}，运气：{luck1}，当前力量：{player1_dict['CurrentPower']}")
            print(f"选手2：来自{player2_dict['MenPai']}的{player2_name}（{player2_dict['Player_Num']}号-{player2_dict['Gender']}），"
                  f"力量：{player2_dict['Power']}，运气：{luck2}，当前力量：{player2_dict['CurrentPower']}")
            print(f"胜者：{winner}")

            match_number += 1

    # 根据得分从高到低排序
    sorted_scores = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)

    # 如果出现比分持平的情况，计算比分持平的两个人的current_power减去对手current_power的值的总和
    tied_players = []
    for index, (name, score) in enumerate(sorted_scores):
        if index > 0 and score == sorted_scores[index - 1][1]:
            tied_players.append((name, score))

    # 处理比分持平的情况
    if tied_players:
        # 构建current_power差值的字典
        power_diffs = {}
        for (player1_name, _), (player2_name, _) in zip(tied_players[:-1], tied_players[1:]):
            power_diff = 0
            for match in match_results:
                if (match[0] == player1_name and match[1] == player2_name) or (
                        match[0] == player2_name and match[1] == player1_name):
                    player1_dict = player_details[player1_name]
                    player2_dict = player_details[player2_name]
                    power_diff += player1_dict["CurrentPower"] - player2_dict["CurrentPower"]

            # 将current_power差值存储在字典中
            power_diffs[(player1_name, player2_name)] = power_diff

        # 根据current_power差值排序
        sorted_power_diffs = sorted(power_diffs.items(), key=lambda x: x[1], reverse=True)

        # 更新排名
        for index, ((player1_name, player2_name), _) in enumerate(sorted_power_diffs):
            if player_scores[player1_name] == player_scores[player2_name]:
                if sorted_power_diffs[index][1] > 0:
                    sorted_scores[index], sorted_scores[index + 1] = sorted_scores[index + 1], sorted_scores[index]

    # 打印每位选手的总得分
    print("\n…………………………………………………………………………………………")
    print("每位选手的总得分如下")
    for player_name, score in player_scores.items():
        print(f"{player_name}: {score}")

    # 打印最终结果
    print("\n…………………………………………………………………………………………")
    print("八强选手排名如下：")
    for rank, (name, _) in enumerate(sorted_scores, start=1):
        player = player_details[name]
        print(f"第{rank}名：来自{player['MenPai']}的{name} ({player['Player_Num']}号-{player['Gender']})")
        print(f"{player['Personality_All']}")

    return sorted_scores


# 从第五轮比赛结果中提取参与第六轮比赛的选手列表
def get_players_for_sixth_round(fifth_round_results):
    players_for_sixth_round = []
    for winner, _ in fifth_round_results:
        players_for_sixth_round.append(winner)
    return players_for_sixth_round


# 提取参与第六轮比赛的选手列表
players_for_sixth_round = get_players_for_sixth_round(fifth_round_results)

# 调用第六轮比赛函数
print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print("第六轮比赛")
print("以下是第六轮对决的比赛结果。在这一轮中，八强选手将两两对决，根据胜负计分决定最终的排名。")
conduct_sixth_round(players_for_sixth_round, luck_weight)

print()
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print("………………………………………………………………………………………………")
print()
print( "第"+ competition_n + "届"+competition_name+"圆满结束！ ")

#
# def print_player_details(players):
#     for i, (player_name, player_dict) in enumerate(players, start=1):
#         print(f"选手 {i}: {player_name}")
#         for key, value in player_dict.items():
#             print(f"  {key}: {value}")
#         print("\n" + "-" * 50 + "\n")
#
# # 调用函数打印选手详情
# print_player_details(players)


