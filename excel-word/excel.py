import csv
from os import name
import pandas as pd
import numpy as np
from word import MeetingPaper

"""
---------- file ----------
input Header: 
"Tên" | "Lớp" | "Toán" | "Văn"

output Header: 
"Tên" | "Lớp" | "Toán" | "Văn" | "Điểm TB" | "Xếp Loại"
"""

def sent_email(email, file):
    pass


class Students:
    def __init__(self, file, file_new):
        print("____________ START ____________",end="\n\n")
        self.file = file
        self.file_new = file_new

    def print_info(name, grade, math, literature, average, rating):
        print('{:30} | {:3} | {:4} | {:3} | {:7} | {:8}'.format(name, grade, math, literature, average, rating))

    def close_file(self):
        print("_____________ DONE ____________")

    def write_file(self):
        df = pd.read_csv(self.file,encoding='UTF-8')
        students = df.drop_duplicates()
        students_data =  open(self.file_new, 'w',  newline = '', encoding="UTF-8") 
        fieldnames = ["Tên", "Lớp", "Toán", "Văn", "Điểm TB", "Xếp Loại"]
        writer = csv.DictWriter(students_data, fieldnames=fieldnames)
        writer.writeheader()
        header_dield = df.columns.values
        Students.print_info(header_dield[0],header_dield[1],header_dield[2],header_dield[3], "Điểm TB", "Xếp Loại")
        for _ , value in students.iterrows():
            average = np.average([value["Toán"], value["Văn"]]) 
            rating = lambda average: "Giỏi" if average>=8 else("Khá" if average >=6.5 else "Trung Bình")
            writer.writerow({"Tên": value["Tên"].title() , "Lớp": value["Lớp"], "Toán": value["Toán"], 
            "Văn": value["Văn"], "Điểm TB": average, "Xếp Loại": rating(average)})

            paper = MeetingPaper(value["Tên"].title(), value["Lớp"], rating(average))
            paper.content()
            Students.print_info( value["Tên"].title(),value["Lớp"],value["Toán"],value["Văn"], average, rating(average))
        students_data.close()

