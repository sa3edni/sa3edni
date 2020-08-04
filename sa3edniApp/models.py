from django.db import models

# Create your models here.
class Student(models.Model):
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    streamsOptions = [
        ("Scientific","Scientific"),
        ("Literature","Literature")
    ]
    stream = models.CharField(max_length=25, choices=streamsOptions)
    activated = models.BooleanField(default=False)

class News(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to = 'static/images/news', blank = True)
    class Meta:
        verbose_name_plural = "News"

class University(models.Model):
    uniName = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'static/images/unis', blank = True)
    class Meta:
        verbose_name_plural = "universities"

class Major(models.Model):
    majorName = models.CharField(max_length=150)
    minAvg = models.FloatField(default=60)
    description = models.TextField()
    university = models.ForeignKey("University",on_delete=models.CASCADE, default = "")
    majorType = models.CharField(max_length= 20, default="")
    streamsOptions = [
        ("Scientific","Scientific"),
        ("Literature","Literature"),
        ("Any","Any")
    ]
    stream = models.CharField(max_length=25, choices=streamsOptions)
    price = models.FloatField(default=0)
    #class Meta:
    def __str__(self):
        return self.majorName + " : " +self.university.uniName

# class Stream(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)

class Subject(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    maxGrade = models.FloatField()
    streamsOptions = [
        ("Scientific","Scientific"),
        ("Literature","Literature"),
        ("Any","Any")
    ]
    stream = models.CharField(max_length=25, choices=streamsOptions)
