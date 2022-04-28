from tkinter.filedialog import askopenfile
import pandas as pd
from models import Student

students_list=askopenfile()
students_list=pd.read_csv(students_list)
for i in range(students_list.shape[0]):
    record=Student(name=students_list['imie'].loc[i],
                   surname=students_list['nazwisko'].loc[i],
                   index=students_list['nr_albumu'].loc[i],
                   group=students_list['grupa'].loc[i],
                   email=students_list['email'].loc[i])
    record.save()
    
