from django.urls import path 
from . import views

urlpatterns = [
        path('gender/list',views.genderList),
        path('gender/add',views.addGender),
        path('gender/edit/<int:genderId>',views.edit_gender),
        path('gender/delete/<int:genderId>',views.delete_gender)
       
]
 