import string

def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().split("\n")


def task1(sacks: list[str]) -> int:
    prio_list = " " + string.ascii_lowercase + string.ascii_uppercase
    repeate = 0
    for sack in sacks:
        for compartment in sack[0:len(sack)//2]:
            if compartment in sack[len(sack)//2:]:
                repeate += prio_list.index(compartment)
                break
    return repeate

def task2(sacks: list[str]) -> int:
    prio_list = " " + string.ascii_lowercase + string.ascii_uppercase
    repeate = 0
    for three_elfs in range(0, len(sacks), 3):
        for gear in sacks[three_elfs]:
            if (gear in sacks[three_elfs + 1]) and (gear in sacks[three_elfs + 2]):
                repeate += prio_list.index(gear)
                break
    return repeate

    
if __name__ == "__main__":
    sacks = read_data("input03.txt")
    
    task1_result = task1(sacks)    
    print(task1_result) #7568
    
    task2_result = task2(sacks)  
    print(task2_result) #2780
