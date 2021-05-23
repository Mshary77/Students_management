class students_managment:

    # constructor

    def __init__(self, full_name, student_id, student_major, student_course, student_grade):
        self.full_name = full_name
        self.student_id = student_id
        self.student_major = student_major
        self.student_course = student_course
        self.student_grade = student_grade

    # an add function to add more students
    def add_student(self, full_name, student_id, student_major, student_course, student_grade):
        ob = students_managment(full_name, student_id, student_major, student_course, student_grade)
        list.append(ob)

    # a function for deleteing a student
    def delete_student(self, student):
        stue = obj.search_student(student)
        del list[stue]

    # a function to search if a student is exist or not
    def search_student(self, full_name):
        for i in range(list.__len__()):
            if list[i].full_name == full_name:
                return i



    # a function to show all the students
    def disply_student(self, ob):
        print("name: ", ob.full_name)
        print("\nid: ", ob.student_id)
        print("\nmajor: ", ob.student_major)
        print("\ncourse: ", ob.student_course)
        print("\ngrade: ", ob.student_grade)
        print("\n--------------------------")

    # a function for updating student data
    def update_student(self, student, new_student, id, new_id, major, new_major, course, new_course, grade , new_grade):
        stue = obj.search_student(student)
        list[stue].full_name = new_student

        stueid = obj.search_stuid(id)
        list[stueid].student_id = new_id

        stuemaj = obj.search_major(major)
        list[stuemaj].student_major = new_major

        stuecourse = obj.search_course(course)
        list[stuecourse].student_course = new_course

        stuegrade = obj.search_grade(grade)
        list[stuegrade].student_grade = new_grade



    #THE REST OF THESE FUNCTIONS IS FOR SEARCHING FUNCTION

    def search_stuid(self,student_id):
        for i in range(list.__len__()):
            if list[i].student_id == student_id:
                return i

    def search_major(self,student_major):
        for i in range(list.__len__()):
            if list[i].student_major == student_major:
                return i

    def search_course(self,student_course):
        for i in range(list.__len__()):
            if list[i].student_course == student_course:
                return i

    def search_grade(self,student_grade):
        for i in range(list.__len__()):
            if list[i].student_grade == student_grade:
                return i


list = []

obj = students_managment("", "0", "", "", "")
obj.add_student("Mshary alharby", "47", "computer science", "python programming", "A+")
obj.add_student("Ahmad bander", "88", "Law collage", "English", "B")
obj.add_student("Fares khaled", "75", "Graphic collage", "Mathematics", "C")

while True:

    print('''
    What would you like to do?
    1. disply all students.
    2. add a student.
    3. update a student.
    4. search for a student.
    5. delete a student. 

    ''')

    choose = input()

    if choose == "1":
        for i in range(list.__len__()):
            obj.disply_student(list[i])

    elif choose == "2":


        a = input("Enter student name:")
        b = input("Enter student id:")
        c = input("Enter student major:")
        d = input("Enter student course:")
        f = input("Enter student grade:")

        obj.add_student(a, b, c, d, f)

        for i in range(list.__len__()):
            obj.disply_student(list[i])

    elif choose == "3":


        a = input("old name:")
        b = input("new name:")
        c = input("old id:")
        d = input("new id:")
        e = input("old major:")
        f = input("new major:")
        g = input("old course:")
        h = input("new course:")
        j = input("old grade:")
        k = input("new grade:")

        obj.update_student(a, b, c, d,e,f,g,h, j, k)

        for i in range(list.__len__()):
            obj.disply_student(list[i])

    # We search for students using their names
    elif choose == "4":
        a = input("Type the name of student are you searching for?")
        look = obj.search_student(a)
        obj.disply_student(list[look])


    elif choose == "5":
        a = input("Type the name of student you want to remove from the list?")
        obj.delete_student(a)
        for i in range(list.__len__()):
            obj.disply_student(list[i])

    else :
        print("please chose number from 1 to 5")
        continue


    action = input("Would you like to do anthor task?  (y/n)")

    if action == "n":
        break
