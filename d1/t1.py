import fileinput
import copy

def split_list_by_elves(calories):
    split_list = []
    inventory = []
    for item in calories:
        if item:
            inventory.append(int(item))
        else:
            split_list.append(copy.copy(inventory))
            inventory.clear()
    return split_list

def get_sum_by_each_elf(split_list):
    sum_by_elf = []
    for elem in split_list:
        sum_by_elf.append(sum(elem))
    return sorted(sum_by_elf, reverse=True)

if __name__ == "__main__":
    calories = [line.strip() for line in fileinput.input(files="d1/input/input.txt")]
    split_list = split_list_by_elves(calories)
    sum_by_elf = get_sum_by_each_elf(split_list)
    print(sum_by_elf[0] + sum_by_elf[1] + sum_by_elf[2])