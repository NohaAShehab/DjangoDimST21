from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# 1- get model
from staff.models import Staff
from staff.models import Departments
from staff.forms import StaffForm, StaffModelForm


# Create your views here.


def sayWelcome(request):
    # return HttpResponse("Welcome Django")
    return render(request, "staff/welcome.html")


def displayimage(request):
    # return HttpResponse("images")
    data = {"user": ["Noha", "image2.png"]}
    return render(request, "staff/images.html", data)


def staffprofile(request, staff_id):
    # list index start from zero
    staff = [{"name": "noha", "image": "image1.jpg"},
             {"name": "Ali", "image": "image2.png"}]
    #
    # # staff_member = staff[staff_id]  # return dictionary
    if -1 < staff_id < len(staff):
        context = {"staff_member": staff[staff_id]}
        return render(request, 'staff/profile.html', context)
    else:
        return HttpResponse(" <h1> Staff member not found <h2>", status=404)


### http request throught the url

def testfunction(request):
    # responds with httpResponse
    # return HttpResponse("<h2> I am in test function </h2>")
    return render(request, "staff/test.html", status=555)


def staffindex(request):
    return render(request, "staff/index.html")


def stafflist(request):
    # staff = [
    #     {"name": "Noha", "image": "image1.jpg"},
    #     {"name": "Ali", "image": "image2.png"},
    #     {"name": "Ahmed", "image": "image3.jpg"}
    # ]

    ## get staff members from database

    # select * from staff #
    staffmembers = Staff.objects.all()
    ## http
    # return HttpResponse(staffmembers)
    context = {"staffmembers": staffmembers}
    return render(request, "staff/staffindex.html", context)


# view staff profile

def getstaffprofile(request, staff_id):
    # return HttpResponse(staff_id)
    # get object related to the passed id

    member = Staff.objects.filter(id=staff_id)  ### list of objects
    # # l = ["Ahmed","Mahmoud"]
    # # l[0] = "Ali"
    # # print(l)
    # member = list(member)
    # # return HttpResponse(member)
    # if member[0].gender == 'm':
    #     print("fff")
    #     member[0].gender = 'Male'
    #     print(member[0].gender)
    # else:
    #     print(member[0])
    #     member[0].gender = 'Female'
    #
    # context = {"member": member[0]}

    #### get

    # member = Staff.objects.get(pk=staff_id)  ## single object
    member = get_object_or_404(Staff, pk=staff_id)
    # select
    # staff.name
    # from staff, deptarments
    # where
    # staff.dept = departments.id
    staffmebers = member.dept.staff_set.all()
    print(staffmebers)
    context = {"member": member, "staff_member": staffmebers}
    return render(request, "staff/staffprofile.html", context)


def createStaff(request):
    # print(request.POST["name"])
    # print(request.POST["email"])
    ### get data sent in request body
    # name = request.POST["name"]
    # email = request.POST["email"]
    # form = StaffForm()
    form =StaffModelForm ()
    # ---> save in database
    ## get department
    departments = Departments.objects.all()
    print(departments)
    context = {"departments": departments, "form": form}
    print(request.POST)

    if request.POST:
        form = StaffModelForm(request.POST)
        form.save()
        # name = request.POST["name"]
        # image = request.POST["image"]
        #
        # dept = Departments.objects.get(pk=request.POST["dept"])
        # print(type(dept))
        #
        # stf = Staff()
        # stf.name =request.POST["name"]
        # stf.email =request.POST["email"]
        # stf.gender =request.POST["gender"]
        # stf.image = request.POST["image"]
        # stf.dept = dept
        # stf.save()
            # return redirect("http://127.0.0.1:8000/staff/staffindex")
        return redirect("list_staff")  # route name

        # return redirect("list_staff")  ## url name we want to redirect

    return render(request, "staff/create.html", context)



###
def deleteProfile(request,staff_id):
    print(request.method)

    # 1- get object and delete
    staff_mem = get_object_or_404(Staff, pk=staff_id)
    staff_mem.delete()
    # 2- redirect to the index

    return redirect("list_staff")


def editProfile(request,staff_id):
    staff_mem = get_object_or_404(Staff, pk=staff_id)
    if request.method=="GET":
        departments = Departments.objects.all()
        context= {"staff" : staff_mem, "departments": departments}
        return render(request, "staff/edit.html", context)
    elif request.method =="POST":
        print(request.method)
        staff_mem.name = request.POST["name"]
        staff_mem.email = request.POST["email"]
        staff_mem.gender = request.POST["gender"]
        staff_mem.image = request.POST["image"]
        dept = Departments.objects.get(pk=request.POST["dept"])
        staff_mem.dept = dept
        staff_mem.save()

        # get request parameters
        return redirect("list_staff")




def updateProfile(request,staff_id):
    # get object from the databse
    staff_mem = get_object_or_404(Staff, pk=staff_id)
    print(request.method)
    # get request parameters


    return HttpResponse(staff_id)

