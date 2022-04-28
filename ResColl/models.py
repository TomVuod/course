from django.contrib.auth.models import User
from django.db import models
from tkinter.filedialog import askopenfile
import pandas as pd

class Response(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mean_x=models.DecimalField(decimal_places=3,max_digits=10,blank=True,
    null=True)
    mean_y=models.DecimalField(decimal_places=3,max_digits=10,blank=True,
    null=True)
    sd_y=models.DecimalField(decimal_places=3,max_digits=10,blank=True,null=True)
    correlation=models.DecimalField(decimal_places=3,max_digits=10,blank=True,
    null=True)
    condition_counter=models.PositiveIntegerField(blank=True,null=True)
    a=models.DecimalField(decimal_places=3,max_digits=10,blank=True,null=True)
    b=models.DecimalField(decimal_places=3,max_digits=10,blank=True,null=True)
    max_dev_x=models.DecimalField(decimal_places=3,max_digits=7,blank=True,
    null=True)
    tss=models.DecimalField(decimal_places=3,max_digits=12,blank=True,null=True)
    sd_residual=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    mean_residual=models.DecimalField(decimal_places=3,max_digits=7,blank=True,
    null=True)
    min_y_prim=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    correlation_prim=models.DecimalField(decimal_places=3,max_digits=8,
    blank=True,null=True)
    a_prim=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    b_prim=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    angle=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    cumsum_resid_30=models.DecimalField(decimal_places=3,max_digits=8,blank=True,
    null=True)
    timestamp=models.DateTimeField()
    part=models.PositiveIntegerField(blank=True,null=True)

def create_students_list():
    students_list=pd.read_csv('ResColl/prot.csv')
    for i in range(students_list.shape[0]):
        record=User.objects.create_user(first_name=students_list['imie'].loc[i],
                       last_name=students_list['nazwisko'].loc[i],
                       username=students_list['nr_albumu'].loc[i],
                       email=students_list['email'].loc[i])
        record.set_password(students_list['haslo'].loc[i])
        record.save()

