from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.landing, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path("addUser", views.addUser, name='addNewUser'),
    path("home", views.landing, name='home'),
    path("loginaboutcontact", views.staticpages, name='loginaboutcontact'),
    path("addMedicine", views.addMedicine, name='addNewMedicine'),
    path("medicineExpirationInfo", views.medicineExpirationInfo, name='medicineExpirationInfo'),
    path("generateNewBill", views.generateNewBill, name='generateNewBill'),
    path("generatePreviousBill", views.generatePreviousBill, name='generatePreviousBill'),
    path("viewMedicineHistory", views.viewMedicineHistory, name='viewMedicineHistory'),
    path("viewCustomerHistory", views.viewCustomerHistory, name='viewCustomerHistory'),
]
