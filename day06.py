def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read()


def get_code(data: str, length: int) -> int:
    for i in range(len(data) - length):
        if len(set(data[i: i+length])) == length:
            return i + length
    return 0


def task1(data: str) -> int:  
    return get_code(data, 4)
            

def task2(data: str) -> int:
    return get_code(data, 14)

    
if __name__ == "__main__":
    input = read_data("input06.txt")
    
    print("task1: ", task1(input)) # 1912
    
    print("task2: ", task2(input)) # 2122