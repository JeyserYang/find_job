# 自定义模块，用于数值计算

def sum_numbers(numbers):
    '''计算数字总和'''
    return sum(numbers)


def average_numbers(numbers):
    '''计算平均值'''
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
