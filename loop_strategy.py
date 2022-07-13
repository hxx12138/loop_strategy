# 环策略
import random
from unicodedata import name
from tqdm import tqdm

# 初始化数据
scale = 1000
max_find = 500

# 初始化环

def loop_init(scale):
    # 初始化监狱人员编号
    prisoner_card = [ i for i in range(1,scale+1)]
    # 初始化箱子中的编号
    prisoner = [ i for i in range(1,scale+1)]
    random.shuffle(prisoner)
    #print(prisoner)

    # 建立字典（代表箱子中的编号，对应的纸条编号）
    prisoner_dict = dict(zip(prisoner_card,prisoner))
    # print(prisoner_dict)
    return prisoner_dict

# 建立环搜索策略
def loop_generate(prisoner_dict):
    flag = 1 # 假设成功
    for key in prisoner_dict:
        count = 1
        ans = key
        while prisoner_dict[key] != ans:
            count += 1
            if count > max_find: # 产生大于50的环时失败
                flag = 0 # 标记失败
                break
            key = prisoner_dict[key]
        if flag == 0: # 如果失败，则停止尝试
            break
    return flag

# 建立随机搜索策略（尚未完成）
def random_strategy(prisoner_card,prisoner_dict):
    note = prisoner_dict[prisoner_card]

# 建立策略（尚未完成）
def loop_strategy(prisoner_card,prisoner_dict):
    note = prisoner_dict[prisoner_card]


if __name__ == "__main__":
    
    # 模拟次数
    num_simulate = 10000
    # 记录模拟成功次数
    num_success = 0

    # 环策略模拟
    for i in tqdm(range(num_simulate)):
        prisoner_dict = loop_init(scale)
        if loop_generate(prisoner_dict) == 1:
            num_success += 1
    print(f"环策略成功概率：{num_success/num_simulate}")
