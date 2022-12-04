import string

def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().split("\n")


def task1(sacks: list[str]) -> int:
    prio_list = string.ascii_lowercase + string.ascii_uppercase
    repeate = 0
    for sack in sacks:
        tempx = [0]*len(prio_list)
        tempy = [0]*len(prio_list)
        temp  = [0]*len(prio_list)
        for x in sack[0:int(len(sack)/2)]:
            tempx[prio_list.index(x)] =+ 1
        for y in sack[int(len(sack)/2):int(len(sack))]:
            tempy[prio_list.index(y)] =+ 1
        for i in range(len(prio_list)):            
            temp[i] = (bool(tempx[i]) & bool(tempy[i])) * (i + 1)
        repeate += sum(temp)
    return repeate

def task2(sacks: list[str]) -> int:
    prio_list = string.ascii_lowercase + string.ascii_uppercase
    repeate = 0
    for three_elfs in range(0, len(sacks), 3):
        elf1sack = [0]*len(prio_list)
        elf2sack = [0]*len(prio_list)
        elf3sack = [0]*len(prio_list)
        temp     = [0]*len(prio_list)
        for x in sacks[three_elfs]:
            elf1sack[prio_list.index(x)] =+ 1
        for y in sacks[three_elfs + 1]:
            elf2sack[prio_list.index(y)] =+ 1
        for z in sacks[three_elfs + 2]:            
            elf3sack[prio_list.index(z)] =+ 1        
        for i in range(len(prio_list)):            
            temp[i] = (bool(elf1sack[i]) & bool(elf2sack[i]) & bool(elf3sack[i])) * (i + 1)
        repeate += sum(temp)
    return repeate

    
if __name__ == "__main__":
    sacks = read_data("input03.txt")
    
    task1_result = task1(sacks)    
    print(task1_result) #7568
    
    task2_result = task2(sacks)  
    print(task2_result) #2780
