from django.db import models

# Create your models here.
class DEPT(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    Adr=models.CharField(max_length=100,default='Adr')

    def __str__(self):
        return self.Dname

class EMP(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    # Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    Dept_no=models.ForeignKey(DEPT,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Ename

class SALGRADE(models.Model):
    Grade=models.IntegerField(primary_key=True)
    Losal=models.IntegerField()
    Hisal=models.IntegerField()

    def __str__(self):
        return str(self.Grade)
