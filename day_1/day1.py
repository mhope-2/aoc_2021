import sys
sys.path.append('c:\\Users\\Michael Hope\\Documents\\projects\\aoc_2021')

from utilities.common import convert_to_list

def get_num_differences(num_list):

    if type(num_list) is not list:
        return "function argument must be of type list"

    counter = 0
    for index in range(len(num_list)):
        if num_list[index] > num_list[index-1]:
            counter+=1
    return counter


if __name__ == '__main__':
    num_list = convert_to_list('day_1\\input.txt')
    print(get_num_differences(num_list))