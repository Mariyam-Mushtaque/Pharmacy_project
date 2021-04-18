from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from django.shortcuts import render, HttpResponse

from datetime import datetime
#For ongoing work
from datetime import date
from datetime import timedelta
#For ongoing work
from home.models import AddUser
from home.models import AddMedicine
from django.contrib import messages

#password for new added user, name- harry , pass- harry!!!@@@###
# Create your views here.

def landing(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'landing.html')

def loginUser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def addUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        bloodgroup = request.POST.get('bloodgroup')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        adduser= AddUser(name=name, age=age, sex=sex, bloodgroup=bloodgroup, email=email, phonenumber=phonenumber, address=address, date=datetime.today())
        adduser.save()
        messages.success(request, 'New customer added to the database!')
    return render(request,'addUser.html')

def addMedicine(request):
    if request.method == "POST":
        name = request.POST.get('name')
        batch = request.POST.get('batch')
        manufacture = request.POST.get('manufacture')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        date = request.POST.get('date')
        addmedicine= AddMedicine(name=name, batch=batch, manufacture=manufacture, quantity=quantity, price=price, date=date)
        addmedicine.save()
        messages.success(request, 'New medicine added to the database!')
    return render(request,'addMedicine.html')

def staticpages(request):
    #return HttpResponse("this is a static page, nothing is being performed here for now")
    return render(request,'loginaboutcontact.html')

def medicineExpirationInfo(request):


    # Ongoing work
    datetoday=date.today()
    print(datetoday)
    dateafter5days= datetoday + timedelta(days=5)
    print(type(dateafter5days))
    #print(datetoday<dateafter5days)
    #datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

    #data= AddMedicine.objects.all()[0].date #contains expiry date of all medicine
    #data= AddMedicine.objects.all().values('date')
    #print(data)
    #data1= AddMedicine.objects.filter(date>=datetoday and date<=dateafter5days)
    data1= AddMedicine.objects.filter(date__lte=dateafter5days, date__gte=datetoday)
    print(data1)


    # Ongoing work


    return render(request,'medicineExpirationInfo.html',{"expiringmedicines":data1})

def generateNewBill(request):
    return render(request,'generateNewBill.html')

def generatePreviousBill(request):
    return render(request,'generatePreviousBill.html')

def viewMedicineHistory(request):
    return render(request,'viewMedicineHistory.html')

def viewCustomerHistory(request):
    return render(request,'viewCustomerHistory.html')