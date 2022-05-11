# 使用二维数组存储数字-->字母的映射
Map = ["", "", "ABC", "DEF",
       "GHI", "JKl", "MNO",
       "PQRS", "TUV", "WXYX"]

# 判断输入的数字
def deep(input_number):
    # 全局映射
    global Map
    if len(input_number) == 1:
        # 用于移除列表中的一个元素（默认最后一个），函数返回值为被移除元素;
        return Map[input_number.pop(0)]
    else:
        a = input_number.pop(0)
        # print(a)
        return combine(Map[a], deep(input_number))

# 两个for循环把结果组合
def combine(left, right):
    result = list()
    for item_left in left:
        for item_right in right:
            result_str = str(item_left) + str(item_right)
            result.append(result_str)
    return result

arr = list()
input_str = input("please input number from 0 to 99:")
# input_str = "23"
for char in input_str:
    arr.append(int(char))

print("Input:", arr)
# arr = [2, 3]
print("Output", deep(arr))