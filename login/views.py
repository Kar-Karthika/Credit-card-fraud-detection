from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

email=''
pass_word=''
# Create your views here.
def loginaction(request):
    global email,pass_word
    if request.method=="POST":
        conn=sql.connect(host="localhost",user="root",password="Karthika@28", database="1styear")
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Email":
                email=value
            if key=="password":
                pass_word=value
        c="select * from minipro where Email='{}'and password='{}'".format(email,pass_word)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
        conn.commit()
    return render(request,'login.html')

def register(request):
    return render(request,'signup.html')
def logregression(request):
    return render(request,'log.html')
def dtree(request):
    return render(request,'dt.html')
def confusion(request):
    return render(request,'cm.html')
def ann(request):
    return render(request,'ann.html')