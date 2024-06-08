from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    courses_taught = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Booking(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.student} booked {self.tutor} for {self.course} on {self.date}"

