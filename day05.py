import string
import itertools
import math

def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().split("\n\n")


def create_ship(ship_cargo: list[str]) -> list[str]:
    temp = ['']*len(ship_cargo[0])
    
    for row in ship_cargo:
            temp = [list(itertools.chain(*cargo)) for cargo in zip(temp, row)]  
                      
    cargo = [row for row in temp if row[-1]  in list(map(str, range(0,10)))]
    
    [row.pop() for row in cargo]
    
    for row in cargo:
        for i in range(row.count(' ')):
            row.pop(row.index(' '))

    cargo.insert(0, [])
    return cargo


def create_instructions(instructions_list: list[str]) -> list[int]:
    instructions_list = [instruction.split(" ") for instruction in instructions_list]
    instructions_list = [[int(a), int(b), int(c)]for _, a, _, b, _, c in instructions_list]
    return instructions_list

#NUMBER_OF_CARGO   FROM      TO
def task1(ship: list[int], move_list: list[int]):
    for move in move_list:
        for cargo_move in range(move[0]):
            ship[move[2]].insert(0, ship[move[1]][0])
            ship[move[1]].pop(0)
    return
            

def task2(ship: list[int], move_list: list[int]):
    for move in move_list:
        for cargo_move in range(move[0], 0, -1):
            ship[move[2]].insert(0, ship[move[1]][cargo_move-1])
            ship[move[1]].pop(cargo_move-1)
    return 

    
if __name__ == "__main__":
    input = read_data("input05.txt")
        
    ship2 = ship1 = create_ship(input[0].split("\n"))    
    move_list = create_instructions(input[1].split("\n"))
    
    task1(ship1, move_list) #ZRLJGSCTR
    
    task2(ship2, move_list) #PRTTGRFPB
    print("vége")
