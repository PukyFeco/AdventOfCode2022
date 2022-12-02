from itertools import groupby

def read_data(input_file: str) -> list[int]:
    with open(input_file) as IN:
        return IN.read().split("\n")

def sort_calorie(calorie_data: list[int]):
    sum_list = []
    for l, g in groupby(calorie_data, key=''.__ne__):
        a = 0
        g = list(g)
        if g != ['']:    
            for i in g:
                a = a + int(i)
            sum_list.append(a)
    return sum_list 

def task1(sorted_calorie_list: int):
    print(max(sorted_calorie_list))

def task2(sorted_calorie_list: int, elf_num: int):
    max_calorie_n = 0
    for i in range(elf_num):
        max_calorie_n = max_calorie_n + max(sorted_calorie_list)
        sorted_calorie_list.remove(max(sorted_calorie_list))
    print(max_calorie_n)

if __name__ == "__main__":
    
    calorie_list = read_data("input01.txt")
    
    sorted_calorie_list = sort_calorie(calorie_list)
    
    task1(sorted_calorie_list) #70509
    
    task2(sorted_calorie_list, 3) #208567