import string

def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


def convert(sections: list[list[int]]) -> list[int]:
    section_lists = [line.split(",") for line in sections]
    b = [[list(map(int, section.split("-"))) for section in section_list] for section_list in section_lists]
    return b


def task1(converted_sections: list[int]) -> int:
    result = 0
    for ((sec1star, sec1end), (sec2star, sec2end)) in converted_sections:
        if ((sec1star >= sec2star) and (sec1end <= sec2end)) or ((sec1star <= sec2star) and (sec1end >= sec2end)):
            result += 1
    return result
            

def task2(converted_sections: list[int]) -> int:
    result = 0
    for ((sec1star, sec1end), (sec2star, sec2end))  in converted_sections:
        if ((sec1end >= sec2star) and (sec1star <= sec2end)):
            result += 1
    return result

    
if __name__ == "__main__":
    sections = read_data("input04.txt")
        
    converted_sections = convert(sections)    
    
    task1_result = task1(converted_sections)
    print(task1_result) #413
    
    task2_result = task2(converted_sections)  
    print(task2_result) #806  
