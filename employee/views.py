from django.shortcuts import render, HttpResponseRedirect
from employee.models import Employee
from employee.forms import EmployeeForm


def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
                form.save() 
                print(form)
                form = EmployeeForm()
                return HttpResponseRedirect("/")               
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employee':employees})




def update(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
            pi = Employee.objects.get(pk=id)
            fm = EmployeeForm(instance=pi)
    return render(request, 'edit.html', {'employee':fm})



def deletedata(request ,id):
    if request.method=="POST":
        pi=Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
