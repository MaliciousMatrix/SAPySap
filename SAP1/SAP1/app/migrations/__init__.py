from django.db import migrations
from django.db import models
import datetime
from datetime import datetime
from datetime import date




def Populate_Employees(apps, schema_editor):
    Employee = apps.get_model("SAP1", "Employee")
    Ava1 = apps.get_model("SAP1", "Avalibility")
    avalibility = Ava1(AvaDays='M', AvaTimeStart=9, AvaTimeEnd=13)
    avalibility.save()

    avalibility2 = Ava1(AvaDays='T', AvaTimeStart=9, AvaTimeEnd=13)
    avalibility2.save()

    avalibility3 = Ava1(AvaDays='w', AvaTimeStart=9, AvaTimeEnd=13)
    avalibility3.save()

    employee = Employee(name='Grace', DOB=datetime(1996,2,1), avalibility=avalibility)
    employee.save()

    employee2 = Employee(name='Winston', DOB=datetime(1996, 8, 12), avalibility=avalibility2)
    employee2.save()

    employee3 = Employee(name='Wencel', DOB=datetime(1996, 12, 8), avalibility=avalibility3)
    employee3.save()

    for employee in Employee.object.all():
        print(employee)
  

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(Populate_Employees)
        
    ]