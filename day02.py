def read_data(input_file: str) -> list[str]:
    with open(input_file) as IN:
        return IN.read().split("\n")

def convert(strategy_list: list[str], RPS) -> list[int]:
    templist = []
    for x in strategy_list:
        templist.append(RPS.get(x))
    return templist

def task(strategy_score: list[int]) -> int:
    print(sum(strategy_score))
    return sum(strategy_score)

if __name__ == "__main__":
    
    RPS1 = {
        "A X": 4,
        "A Y": 8, 
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }   
     
    RPS2 = {
        "A X": 3,
        "A Y": 4, 
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    
    strategy_list = read_data("input02.txt")
    
    strategy_score = convert(strategy_list, RPS1)
    
    task(strategy_score) #11386
    
    strategy_score2 = convert(strategy_list, RPS2)
    
    task(strategy_score2) #13600