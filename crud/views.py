from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users
from django.contrib.auth.hashers import make_password
# Create your views here.


def genderList(request):
    try:
        genders = Genders.objects.all() # select all from table
        
        data = {
            'genders':genders
        }
        
        return render(request, 'gender/GendersList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during load gender: {e}') 
    
def user_list(request):
    try:
        userObj= Users.objects.select_related('gender')
        
        data = {
            'users':userObj
        }
        return render(request,'user/UsersList.html',data)
    except Exception as e:
        return HttpResponse(f'Error occured during load Users: {e}') 

def addGender (request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')
            
            Genders.objects.create(gender=gender).save()#insert INTO tbl_genders(gender) VALUES(gender)
            messages.success(request,'Gender added Successfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html') 
    except Exception as e:
        return HttpResponse(f'Error occured during add gender: {e}') 
    
def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj= Genders.objects.get(pk=genderId)
            
            gender = request.POST.get('gender')
            
            genderObj.gender = gender
            genderObj.save() #Update
            messages.success(request, "Gender Updated Successfully!")
            
            data = {
                'gender':genderObj
            }
            return render(request,'gender/EditGender.html', data)
        else:  
            genderObj= Genders.objects.get(pk=genderId) # Select * From tbl_genders WHERE gender_id = genderId
            
            data = {
                'gender':genderObj
            }
            return render(request, 'gender/EditGender.html',data)
    except Exception as e:
        return HttpResponse (f'Error occured during editing gender: {e}') 

def edit_user(request, userId):
    try:
        userObj = Users.objects.get(pk=userId)
        genders = Genders.objects.all()

        if request.method == 'POST':
            fullName = request.POST.get('full_name')
            gender_id = request.POST.get('gender')
            birthDate = request.POST.get('birth_date')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')

            if password != confirmPassword:
                messages.error(request, "Passwords do not match, please try again!")
            else:
                userObj.fullname = fullName
                if gender_id:
                    userObj.gender = Genders.objects.get(pk=gender_id)
                userObj.birth_date = birthDate
                userObj.address = address
                userObj.contact_number = contactNumber
                userObj.email = email
                userObj.username = username
                userObj.password = make_password(password)
                userObj.save()
                messages.success(request, "User Updated Successfully!")
                return redirect(f'/user/edit/{userId}')

        data = {
            'user': userObj,
            'genders': genders
        }

        return render(request, 'user/EditUser.html', data)

    except Exception as e:
        return HttpResponse(f'Error occured during editing user: {e}')
    
    
def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj= Genders.objects.get(pk=genderId)
            
            genderObj.delete()
            messages.success(request, "Gender Deleted Successfully!")
            return redirect('/gender/list')
        else:
            genderObj= Genders.objects.get(pk=genderId) # Select * From tbl_genders WHERE gender_id = genderId
                
            data = {
                'gender':genderObj
            }
            return render(request, 'gender/DeleteGender.html',data)
        
    except Exception as e:
        return HttpResponse (f'Error occured during deleting gender: {e}') 
    
def add_user(request):
    try:
        if request.method == "POST":
            fullName = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birthDate = request.POST.get('birth_date')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')
            
            if password != confirmPassword:
                messages.error(request, "Password do not match try again!")
            
            Users.objects.create(
                fullname = fullName,
                gender = Genders.objects.get(pk=gender),
                birth_date = birthDate,
                address = address,
                contact_number = contactNumber,
                email = email,
                username = username,
                password = make_password(password),  
            ).save()
            messages.success(request, "User added Succesfully!")
            return redirect('/user/add')
        else:
            genderObj = Genders.objects.all()

            data = {
                'genders':genderObj
            }
            return render(request,'user/AddUser.html', data) 
    except Exception as e:
        return HttpResponse(f'Error occured during add user: {e}') 
    
    