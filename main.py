class Student:
    def __init__(self, name, hand, vision, height, attention, compatibility):
        self.name = name
        self.hand = hand
        self.vision = vision
        self.height = height
        self.attention = attention
        self.compatibility = compatibility
        self.located = False
        self.desk = 5
        
        if self.vision == "1-2 парты":
            self.desk = 0
        elif self.vision == "1-3 парты":
            self.desk = 1
        
        if self.attention == "TRUE":
            self.desk -= 1
            
        if self.height == "Низкий":
            self.desk -= 1
        elif self.height == "Средний":
            self.desk -= 2

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

    studentCompatibility = []
    for studentIndex, studentName in enumerate(compatibility[1:]):
        studentCompatibility.append([])
        for index, student in enumerate(studentName[1:]):
            if student == "": continue
            studentCompatibility[studentIndex].append({"name":names[index], "code":student})

    out = []
    for index, studentArr in enumerate(students):
        out.append(Student(studentArr[0], studentArr[1], studentArr[2], studentArr[3], studentArr[4], studentCompatibility[index]))
    return out
        
def writeOut(studentsArr):
    with open("result.csv", 'w', encoding='utf-8') as file:
        outData = "Место,Имя"
        for index, student in enumerate(studentsArr):
            if student == 1 or student == 0: continue
            if index == 34: index = 30
            if index == 35: index = 31
            outData += f"\n{index+1},{student.name}"
        file.write(outData)

def sort(students, room):
    result = []
    
    for i, student in enumerate(students):
        if student.vision == "1 парта, средний ряд":
            if room[0][1][0] == 1:
                room[0][1][0] = student
                student.located = True
            else:
                room[0][1][1] = student
                student.located = True

    students = sorted(students, key=lambda student: student.desk)
    
    for i1, i in enumerate(room):
        for j1, j in enumerate(i):
            for k1, k in enumerate(j):
                if k == 1:
                    for i2, student in enumerate(students):
                        if student.located: continue
                        if k1 == 1:
                            neighbour = room[i1][j1][k1-1]
                            if neighbour.hand.lower() == "правая" and student.hand.lower() == "левая": continue
                        
                        room[i1][j1][k1] = student
                        student.located = True
                        break
                      
    for _, i in enumerate(room):
        for _, j in enumerate(i):
            for _, k in enumerate(j):
                result.append(k)
    
    return result

input_data = readData("input_data.csv")
studentsArr = dataToArray(input_data, False)

compatibility_data = readData("compatibility.csv")
compatibilityArr = dataToArray(compatibility_data, True)

students = arrStringsToArrStudents(studentsArr, compatibilityArr)

room = [
    [[1,1], [1,1], [1,1]],
    [[1,1], [1,1], [1,1]],
    [[1,1], [1,1], [1,1]],
    [[1,1], [1,1], [1,1]],
    [[1,1], [1,1], [1,1]],
    [[0,0], [0,0], [1,1]],
]

out = sort(students, room)
writeOut(out)