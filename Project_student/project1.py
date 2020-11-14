import sys
import os

def print_item():
    strFormat = '%-14s%-14s%-14s%-14s%-14s%-14s'
    strOut = strFormat % ('Stduent','Name','Midterm','Final','Average','Grade')
    print(strOut)
    print("-" * 78)
    
def print_student_info(dic, key):
    strFormat = '%-14s%-14s%-14s%-14s%-14s%-14s'
    strOut = strFormat % (key, dic[key][0], dic[key][1], dic[key][2], dic[key][3], dic[key][4])
    print(strOut)

def show(dic):
    sorted_dic = sort_by_avg(dic)
    print_item()
    for key in sorted_dic:
        print_student_info(sorted_dic, key)
        
def search():
    global info_student
    student_id = input("Student ID: ")
    if student_id in info_student.keys():
        print_item()
        print_student_info(info_student, student_id)
        
    else:
        print("NO SUCH PERSON\n")
        
def changescore():
    global info_student
    student_id = input("Student ID: ")
    if student_id not in info_student.keys():
        print("NO SUCH PERSON\n")
        return
    
    m_or_f = input("Mid/Final? ")
    m_or_f = m_or_f.lower()
    if m_or_f != "mid" and m_or_f != "final":
        return
    student_score = int(input("Input New Score : "))
    if student_score > 100 or student_score < 0:
        return
        
    print_item()
    print_student_info(info_student, student_id)
    print("Score Changed.\n")
    if m_or_f == "mid":
        info_student[student_id][1] = student_score
    else:
        info_student[student_id][2] = student_score
    print_student_info(info_student, student_id)

        
def add():
    global info_student
    student_id = input("Student ID: ")
    if student_id in info_student.keys():
        print("ALREADY EXISTS.\n")
    
    student_name = input("Student Name: ")
    midterm = int(input("Midterm Score: "))
    final = int(input("Final Score: "))
    avg = (midterm + final) / 2
    info_student[student_id] = [student_name, midterm, final, avg, get_grade(avg)]
    print("Student added.\n")
    
def searchgrade():
    global info_student
    student_grade = input("Grade to search: ")
    grades = ['A', 'B', 'C', 'D', 'F']
    if student_grade not in grades:
        print("\n")
        return
    
    flag = False
    for key in info_student:
        if info_student[key][4] == student_grade:
            if not flag:
                flag = True
                print_item()
            print_student_info(info_student, key)
            
    if not flag:
        print("NO RESULTS.\n")
        
def remove():
    global info_student
    if len(info_student) == 0:
        print("List is Empty!\n")
        return
    
    student_id = input("Student ID: ")
    if student_id not in info_student.keys():
        print("NO SUCH PERSON.\n")
        return
    
    removed = info_student.pop(student_id)
    print("Student Removed.\n")
    
        
def get_grade(avg):
    if avg >= 90:
        grade = 'A'
    elif avg >= 80 and avg < 90:
        grade = 'B'
    elif avg >= 70 and avg < 80:
        grade = 'C'
    elif avg >= 60 and avg < 70:
        grade = 'D'
    else:
        grade = 'F'
        
    return grade

def quit():
    global info_student
    y_or_n = input("Save data?[yes/no] ")
    y_or_n = y_or_n.lower()
    if y_or_n == "yes":
        fname = input("File name: ")
        write_file = open(fname, 'w')
        for key in info_student:
            write_line = key + "\t" + info_student[key][0] + "\t" + str(info_student[key][1]) + "\t" + str(info_student[key][2]) +"\n"
            write_file.write(write_line)
        write_file.close()

def sort_by_avg(dic):
    return dict(sorted(dic.items(), key = lambda k: k[1][3], reverse = True))


args = sys.argv[1]
file = open(args, 'r')
info_student = {}
messages = ["show", "search", "changescore", "searchgrade", "add", "remove", "quit"]

## 동명이인이 있을 수 있으므로 학번 기준으로 dictionary의  key 값을 설정한다.
for line in file:
    tmp_array = line.strip().split("\t")
    tmp_array[2] = int(tmp_array[2])
    tmp_array[3] = int(tmp_array[3])
    average = (tmp_array[2] + tmp_array[3]) / 2
    grade = get_grade(average)
    info_student[tmp_array[0]] = tmp_array[1:]
    info_student[tmp_array[0]].append(average)
    info_student[tmp_array[0]].append(grade)

    
file.close()

while(1):
    input_message = input("# ")
    input_message = input_message.lower()
    if input_message == "show":
        show(info_student)
    elif input_message == "search":
        search()
    elif input_message == "changescore":
        changescore()
    elif input_message == "searchgrade":
        searchgrade()
    elif input_message == "add":
        add()
    elif input_message == "remove":
        remove()
    elif input_message =="quit":
        quit()
        break
