from excel import Students




def main():
    file = "students.csv"
    file_new = "students_data.csv"
    students = Students(file, file_new)
    students.write_file()
    students.close_file()

if __name__ == "__main__":
    main()