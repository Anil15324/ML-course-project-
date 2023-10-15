from tkinter import *
from tkinter import messagebox


root = Tk()  # tkinter window
root.title("Student Result Project- GUI")
root.geometry("644x500")
root.minsize(300, 100)
root.maxsize(1920, 1080)


def load_data(filename):
    """Function for reading csv file and storing it in a list """
    course = open('D:\python\ML project\sem1.csv', "r+")
    storage_list = []
    for rows in course:
        # print(rows.split(","))
        storage_list.append(rows.split(","))
    strip_list = [[p, q, r, s.rstrip()] for p, q, r, s in storage_list]
    return strip_list


def performance(marks):
    """Function to evaluate the performance based on the marks."""
    if marks == 100:
        return "Congratulations!, You have got 'O' grade in the course."
    elif (marks >= 90) and (marks < 100):
        return "Congratulations!, You have got 'A+' grade in the course."
    elif (marks >= 80) and (marks < 90):
        return "Congratulations!, You have got 'A' grade in the course."
    elif (marks >= 70) and (marks < 80):
        return "You have got 'B+' grade in the course."
    elif (marks >= 60) and (marks < 70):
        return "You have got 'B' grade in the course."
    elif (marks >= 50) and (marks < 60):
        return "You have got 'C+' grade in the course. Work Hard!"
    elif (marks >= 40) and (marks < 50):
        return "You have got 'C' grade in the course. Work Hard!"
    else:
        return "Fail. Don't lose hope , Work Hard"


# Reading file through function filename
course_1 = load_data("D:\python\ML project\sem1.csv")  #absolute path
course_2 = load_data("D:\python\ML project\sem2.csv")
course_3 = load_data("D:\python\ML project\sem3.csv")
course_4 = load_data("D:\python\ML project\sem4.csv")


def store_dict(nested_list):
    """Function for storing values in the dictionary"""
    storage_dict = {}
    for sublist in nested_list[1:]:
        for i, key in enumerate(nested_list[0]):
            if key == 'Subject':
                if key not in storage_dict:
                    storage_dict[key] = []
                storage_dict[key].append(int(sublist[i]))
            elif key == 'RollNumber':
                if key not in storage_dict:
                    storage_dict[key] = []
                storage_dict[key].append(int(sublist[i]))
            else:
                if key not in storage_dict:
                    storage_dict[key] = []
                storage_dict[key].append(sublist[i])
    return storage_dict


# Storing dara in the dictionary using function store_dict.
course_1_dict = store_dict(course_1)
course_2_dict = store_dict(course_2)
course_3_dict = store_dict(course_3)
course_4_dict = store_dict(course_4)


def search(StudentName, RollNumber, course_name):
    """Function to print the information of a particular student (with name and information)"""
    if (StudentName in course_name['Name'] and RollNumber in course_name['RollNumber'] and
            course_name['Name'].index(StudentName) == course_name['RollNumber'].index(RollNumber)):
        student_index = course_name['Name'].index(StudentName)
        student_trade = course_name['Trade'][student_index]
        student_marks = course_name['Subject'][student_index]
        grade = performance(student_marks)
        sgpa = student_marks / 10
        info = (f"'{StudentName}' has enrolled in '{student_trade}' with roll no '{RollNumber}' "
                f"has got '{student_marks}' marks with SGPA {sgpa}.\n{grade}")

        return info

    else:
        notfound = (f"Ensure that you have entered the correct name and roll no as '{StudentName}' "
                    f"is not found in the database.")
        return notfound


def cgpa(s_name, roll_no):
    """To calculate cgpa"""
    all_files = [course_1_dict, course_2_dict, course_3_dict, course_4_dict]
    all_marks = []
    for mark in all_files:
        if (s_name in mark['Name'] and roll_no in mark['RollNumber'] and
                mark['Name'].index(s_name) == mark['RollNumber'].index(roll_no)):
            student_index = mark['Name'].index(s_name)
            student_marks = mark['Subject'][student_index]
            all_marks.append(student_marks)

        else:
            not_found = (f"Ensure that you have entered the correct name and roll no as '{s_name}' "
                         f"is not found in the database.")
            return not_found
    sum_all_marks = 0
    for a in range(len(all_marks)):
        sum_all_marks += all_marks[a]
    average = float(sum_all_marks / (len(all_marks) * 10))
    return f"Your cgpa is {average}."


def show_result():
    try:
        input_semester = semester_var.get()
        input_name = name_entry.get()
        input_roll_number = int(roll_number_entry.get())

        if input_semester == "Overall CGPA":
            result = cgpa(input_name, input_roll_number)
        elif input_semester in semester_names:
            semester_index = semester_names.index(input_semester)
            course_dict = course_dicts[semester_index]
            result = search(input_name, input_roll_number, course_dict)
        else:
            result = "Select a valid semester or 'Overall CGPA'."

        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Enter valid input.")


course_dicts = [course_1_dict, course_2_dict, course_3_dict, course_4_dict]
semester_names = ["Semester 1", "Semester 2", "Semester 3", "Semester 4"]

semester_label = Label(root, text="Student Result:")
semester_label.pack()

semester_var = StringVar()
semester_var.set("Select Semester")
semester_combobox = OptionMenu(root, semester_var, *semester_names, "Overall CGPA")
semester_combobox.pack()

name_label = Label(root, text="Enter the Student Name:")
name_label.pack()

name_entry = Entry(root)
name_entry.pack()

roll_number_label = Label(root, text="Enter Student Roll Number:")
roll_number_label.pack()

roll_number_entry = Entry(root)
roll_number_entry.pack()

submit_button = Button(root, text="Submit", command=show_result)
submit_button.pack()

photo = PhotoImage("D:\python\ML project\images ")
image_label = Label(image=photo)
image_label.pack()

root.mainloop()



