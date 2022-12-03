def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().split("\n")


def convert(strategy_list: list[str], RPS) -> list[int]:
    return sum([RPS.get(x) for x in strategy_list])


def task1(strategy_list: list[int]) -> int:
    RPS = {"A X": 4,
           "A Y": 8,
           "A Z": 3,
           "B X": 1,
           "B Y": 5,
           "B Z": 9,
           "C X": 7,
           "C Y": 2,
           "C Z": 6}

    score = convert(strategy_list, RPS)

    return score


def task2(strategy_list: list[int]) -> int:
    RPS = {"A X": 3,
           "A Y": 4,
           "A Z": 8,
           "B X": 1,
           "B Y": 5,
           "B Z": 9,
           "C X": 2,
           "C Y": 6,
           "C Z": 7}

    score = convert(strategy_list, RPS)

    return score


if __name__ == "__main__":
    strategy_list = read_data("input02.txt")

    print(task1(strategy_list)) #11386

    print(task2(strategy_list)) #13600
