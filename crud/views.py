from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders

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