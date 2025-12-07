import time

num_list = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]

def bad_algorithm():
    max_num = 0
    for x in range(0, len(num_list) - 1):
        for y in range(0, len(num_list[x]) - 1):
            if num_list[x][y] > num_list[x][y + 1]:
                if num_list[x][y] % 5 != 0:
                    max_num += num_list[x][y]
                elif num_list[x][y + 1] % 5 != 0:
                    max_num += num_list[x][y + 1]
            else:
                if num_list[x][y + 1] % 5 != 0:
                    max_num += num_list[x][y + 1]
                elif num_list[x][y] % 5 != 0:
                    max_num += num_list[x][y]
    return max_num

def good_algorithm():
    max_num = 0
    min_num = 0
    for i in range(0, len(num_list) - 1):
        max_num += max(num_list[i])
        min_num += min(num_list[i]) % 5 == 0
    return max_num - min_num

bad_time = time.time()
bad_result = bad_algorithm()
print(f"Результат плохого алгоритма: {bad_result}")
print(f"Время плохого алгоритма: {time.time() - bad_time}")

good_time = time.time()
good_result = good_algorithm()
print(f"Результат хорошего алгоритма: {good_result}")
print(f"Время хорошего алгоритма: {time.time() - good_time}")