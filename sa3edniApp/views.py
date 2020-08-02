from django.shortcuts import render, HttpResponse, redirect
from .models import News, Student, Subject, Major, University
from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.utils import six
from random import choice
from django.contrib.auth.hashers import make_password, check_password
import math

#from django.core.mail import EmailMessage
# Create your views here.


def randomString():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
    return ''.join(choice(letters) for i in range(15))

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
            return ( six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.validated) )

def home(request):
    data = {
        "news": News.objects.all()
    }
    return render(request,"home.html",data)

def signup(request):#add stream to signup
    data = {"streams":["Scientific", "Literature"]}
    if request.method == "POST":
        #check if user exists
        users = Student.objects.filter(email = request.POST["email"])
        if len(users) > 0:
            data["error"]  = "email already in use"
            return render(request,"signup.html", data)

        if request.POST["password"] != request.POST["password2"]:
            data["error"] = "Passwords don't match"
            return render(request,"signup.html", data)
        newStudent = Student()
        newStudent.fName = request.POST["fName"]
        newStudent.lName = request.POST["lName"]
        newStudent.email = request.POST["email"]
        newStudent.password = make_password(request.POST["password"])
        newStudent.stream = request.POST["stream"]
        newStudent.save()
        return redirect("/")
    else:
        return render(request,"signup.html",data)

def signin(request):
    if request.method == "POST":
        users = Student.objects.filter(email=request.POST["email"])
        if users.count() == 0:
            return render(request, "signin.html",{"error":"The email or the password is incorrect"})
        users = users[0]
        password = request.POST["password"]
        if check_password(password,users.password):
            request.session["id"] = users.pk
            return redirect("/")
        return render(request, "signin.html",{"error":"The email or the password is incorrect"})
    else:
        return render(request, "signin.html")

def signout(request):
    if "id" in request.session:
        del request.session["id"]
    return redirect("/")

 
def profile(request):
    if "id" not in request.session:
        return redirect("/signin")
    user = Student.objects.get(pk = request.session["id"])
    data = {"user": user}
    if request.method == "POST":
        user.fName = request.POST["fName"]
        user.lName = request.POST["lName"]
        user.save()

    return render(request, "profile.html",data)

def resetPassword(request):
    if "id" not in request.session:
        return redirect("/signin")
    
    if request.method != "POST":
        return redirect("/profile")
    user = Student.objects.get(pk = request.session["id"])
    data = {"user": user}
    if not check_password(request.POST["oldPass"],user.password):
        data["error"] = "Your old password isn't correct"
        return render(request, "profile.html",data)
    if request.POST["newPass"] != request.POST["newPass2"]:
        data["error"] = "Your passwods don't match"
        return render(request, "profile.html",data)
    user.password = make_password(request.POST["newPass"])
    user.save()
    data["success"] = "Your password has been reset successfully"

    return render(request, "profile.html",data)

def majorselection(request):
    return render(request, "majorselection.html")    

def download(request):
    return render(request, "download.html")

def about(request):
    return render(request, "aboutus.html")

def unis(request):
    universities = University.objects.all()
    rows = []
    for i in range(0,len(universities),2):
        if i < len(universities)-1:
            rows.append(universities[i:i+2])
        else:
            rows.append([universities[i]])
    data = {"rows": rows}
    return render(request,"Universities.html",data)

def calculator(request):
    if "id" not in request.session:
        return redirect("/signin")
    email = request.session["id"]
    student = Student.objects.get(pk = email)
    stream = student.stream
    subjects = Subject.objects.filter(stream = stream) | Subject.objects.filter(stream = "Any")
    total = 0
    studentTotal = 0
    data = {
        "courses": subjects
    }
    if request.method == "POST":
        #if neededGPA not filled prompt an error
        #if no need to increase any grade prompt a message
        grades = []
        belowAVG = []
        neededGPA = float(request.POST["neededGPA"])
        for subject in subjects:
            total += subject.maxGrade
            grade = float(request.POST[subject.name])
            studentTotal += grade
            avg = (100*grade) / subject.maxGrade
            grades.append({
                "subject": subject.name,
                "grade": grade,
                "maxGrade": subject.maxGrade,
                "avg": avg,
                "modified": False
            })
            if avg <= neededGPA:
                belowAVG.append(grades[-1])
            grades = sorted(grades, key = lambda i: i['avg'])
        avg = (100/total) * studentTotal
        if neededGPA <= avg:
            return render(request, "gpacalculator.html", data)
        neededTotal = neededGPA / 100  * total
        neededTotal -= studentTotal
        neededGradesPerSubject = math.ceil(neededTotal/len(belowAVG))
        
        for i in belowAVG:
            i["grade"] += neededGradesPerSubject
            i["modified"] = True
        data["neededTotal"] = neededTotal
        data["currentGPA"] = (100/total) * studentTotal
        data["newGPA"] = 100/(total) * (studentTotal + neededTotal)
        data["modifiedCourses"] = belowAVG
        data ["results"] = True
        return render(request, "gpacalculator.html", data)
    else:
        return render(request,"gpacalculator.html", data)

def uniSelection(request):
    if 'id' not in request.session:
        return redirect("/signin")
    data = {"streams":["Scientific", "Literature"]}
    if request.method == "POST":
        avg = float(request.POST["AVG"])
        priceRange = int(request.POST["priceRange"])
        minPrice = 30*priceRange-30 + 1
        maxPrice = 30*priceRange
        stream = request.POST["stream"]
        filteredMajors1 = Major.objects.filter(stream = stream, price__gte = minPrice, price__lte =  maxPrice)
        filteredMajors2 = Major.objects.filter(stream = "Any", price__gte = minPrice, price__lte =  maxPrice)
        majors = filteredMajors1 | filteredMajors2
        data["majors"] = majors
        data["results"] = True
    return render(request,"uniselection.html",data)

def uniMore(request):
    uniName = request.GET["id"]
    university = University.objects.get(uniName = uniName)
    majors = Major.objects.filter(university = university)
    data = {"majors":majors, "uniName":university.uniName}
    return render(request, "majors.html",data)

def newsMore(request):
    news = News.objects.get(id=request.GET["id"])
    data = {
        "title":news.title,
        "content": news.body,
        "image": news.image
    }
    return render(request, "newsMore.html", data)