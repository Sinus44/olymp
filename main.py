class Student:
    def __init__(self, name, hand, vision, height, attention, compatibility):
        self.name = name
        self.hand = hand
        self.vision = vision
        self.height = height
        self.attention = attention
        self.compatibility = compatibility

def readData(path):
	with open(path, 'r', encoding='utf-8') as file:
		return file.read()

def dataToArray(data, useFirstLine=False):
    outArr = []
    for _, line in enumerate(data.split("\n")[0 if useFirstLine else 1:]):
        flag = False
        lineOut = ""
        for _, symbol in enumerate(line):
            if symbol == '"':
                flag = not flag
            elif symbol == ',':
                if not flag:
                   lineOut += '!'
                else:
                    lineOut += symbol
            else:
                lineOut += symbol
        outArr.append(lineOut.split("!"))
    return outArr

def arrStringsToArrStudents(students, compatibility):
    names = compatibility[0][1:]
    #print(names)
    
    studentCompatibility = []
    for studentIndex, studentName in enumerate(compatibility[1:]):
        studentCompatibility.append([])
        for index, student in enumerate(studentName[1:]):
            if student == "": continue
            studentCompatibility[studentIndex].append({"name":names[index], "code":student})
        #print(studentCompatibility[studentIndex])

    out = []
    for index, studentArr in enumerate(students):
        out.append(Student(studentArr[0], studentArr[1], studentArr[2], studentArr[3], studentArr[4] == "TRUE", studentCompatibility[index]))
    return out
        
def writeOut(studentsArr):
    with open("result.csv", 'w', encoding='utf-8') as file:
        outData = "Место,Имя"
        for index, student in enumerate(studentsArr):
            outData += f"\n{index+1},{student.name}"
        #print(outData)
        file.write(outData)
        #print("Файл сохранен")

def sort(students):
    for _, student in enumerate(students):
        print(f"{student.name} - {student.compatibility}")
    return []

input_data = readData("input_data.csv")
studentsArr = dataToArray(input_data, False)

compatibility_data = readData("compatibility.csv")
compatibilityArr = dataToArray(compatibility_data, True)

students = arrStringsToArrStudents(studentsArr, compatibilityArr)

room = [
    []
]

out = sort(students)
writeOut(out)