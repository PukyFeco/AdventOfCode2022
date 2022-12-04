import string

def read_data(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().split("\n")


def convert(sections: list[list[int]]) -> list[int]:
    a = [x.split(",") for x in sections]
    b = [[y[0].split("-"), y[1].split("-")] for y in a]    
    return b


def task1(converted_sections: list[int]) -> int:
    result = 0
    for x in range(len(converted_sections)):
        sec1star = int(converted_sections[x][0][0])
        sec1end = int(converted_sections[x][0][1])
        sec2star = int(converted_sections[x][1][0])
        sec2end = int(converted_sections[x][1][1])
        if ((sec1star >= sec2star) & (sec1end <= sec2end)) | ((sec1star <= sec2star) & (sec1end >= sec2end)):
            result += 1
    return result
            

def task2(converted_sections: list[int]) -> int:
    result = 0
    for x in range(len(converted_sections)):
        sec1star = int(converted_sections[x][0][0])
        sec1end = int(converted_sections[x][0][1])
        sec2star = int(converted_sections[x][1][0])
        sec2end = int(converted_sections[x][1][1])
        if (((sec1star <= sec2star) | (sec1end <= sec2end)) & (sec2star <= sec1end)) | (((sec2end <= sec1end) | (sec2star <= sec1star)) & (sec1star <= sec2end)):
            result += 1
    return result

    
if __name__ == "__main__":
    sections = read_data("input04.txt")
        
    converted_sections = convert(sections)    
    
    task1_result = task1(converted_sections)
    print(task1_result) #413
    
    task2_result = task2(converted_sections)  
    print(task2_result) #806  
