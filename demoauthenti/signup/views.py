from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,EditUserForm,EditAdminForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect


# Create your views here.


## addignd UserCreationForm will add only 3 fields- name, pasw, cpass
# def sign(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:

#         fm = UserCreationForm()
#     return render(request,'signup.html',{'fm':fm})

def sign(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:

        fm = SignupForm()
    return render(request,'signup.html',{'fm':fm})


def user_login(request):
    if  not request.user.is_authenticated:

        if request.method =='POST':

            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username= uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
                else:
                    #message saying user is not signd up, please sign up
                    return HttpResponseRedirect('/signup/')
        else:
            fm= AuthenticationForm()
        return render(request,'login.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/profile/')


    

def user_profile(request):
    ''' the bellow method checks is user is logined or not? only if loged in he will be allowed ion profile p
page, in [profile page there will be save button iof user wants to change data and if he clicks save, 
the data is getting saved in databse. 
The EditUserForm is a inherioted form of userChangeForm(default in django) and its inherited in form.py '''
    if request.user.is_authenticated:
        if request.method == 'POST': 
            if request.user.is_superuser == True:
                fm = EditAdminForm(request.POST,instance=request.user)
                

            else:


                fm = EditUserForm(request.POST,instance=request.user)  #basically instance = request.user is telling for whioch user
            if fm.is_valid():
                fm.save()
        else:
            if request.user.is_superuser == True:                 # admin ptofile difff
                fm = EditAdminForm(instance = request.user)

            else:




                fm = EditUserForm(instance = request.user)

        return render(request,'profile.html',{'name':request.user,'fm':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#chnage passowrd with old password
def user_change_pass(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:


            fm = PasswordChangeForm(user=request.user)
        return render(request,'chnagepass.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_change_pass1(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            fm =SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:


            fm = SetPasswordForm(user=request.user)
        return render(request,'chnagepass1.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')



