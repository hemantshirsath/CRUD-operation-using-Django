from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User

# Create your views here.
def add_show(request):
    stud=User.objects.all()
    if request.method=="POST":
        fm=StudentRegisteration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                msg2=True
                return render(request,'enroll/addandshow.html',{'form':fm,'msg2':msg2,'stu':stud})
            password=fm.cleaned_data['password']
            obj=User(name=name,email=email,password=password)
            obj.save()
            fm=StudentRegisteration()
            msg={'message':"Data saved successfully "}
    else:
        fm=StudentRegisteration()
        msg=False
    return render(request,'enroll/addandshow.html',{'form':fm,'msg':msg,'stu':stud})

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    msg=False
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            msg=True
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm,'msg':msg})