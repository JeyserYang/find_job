import math_utils
import sys


def read_numbers_from_file(file_path):
    '''从文件中读取数字并返回数字列表'''
    numbers = []
    try:
        # 打开文件，以只读模式
        with open(file_path, 'r', encoding='utf-8') as fin:
            for line in fin:
                try:
                    # 尝试将每行内容转换为浮点数
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"跳过非数字行：{line.strip()}")
    except FileNotFoundError:
        print(f"文件未找到：{file_path}")

    return numbers


def write_result_to_file(file_path, sum_result, average_result):
    '''将计算结果写入文件'''
    try:
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as fout:
            fout.write(f"总和：{sum_result}")
            fout.write(f"平均值：{average_result}")
    except Exception as e:
        print(f"写入文件时出错：{e}")


if __name__ == "__main__":

    # 输入输出文件
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    numbers = read_numbers_from_file(input_file)
    if numbers:
        sum_result = math_utils.sum_numbers(numbers)
        average_result = math_utils.average_numbers(numbers)

        write_result_to_file(output_file, sum_result, average_result)
    else:
        print("未找到有效数字")
