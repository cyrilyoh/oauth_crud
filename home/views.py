from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserProfileForm

def login(request):
    """ Shows login page"""

    return render(request, 'login.html')

@login_required
def home(request):
    """ Show user profile """

    return render(request, 'home.html')

@login_required
def update_view(request):
    """ To update the user details"""

    # dictionary for initial data
    context ={}
 
    # fetch the user object
    obj = request.user
 
    # pass the object as instance in form
    form = UserProfileForm(request.POST or None, instance = obj)
 
    # save the data from the form and redirect
    if form.is_valid():
        form.save()
        return redirect("/")
 
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request):
    """ To delete the user"""
    
    user = request.user
    # delete user
    user.delete()
    # after deleting redirect login page
    return redirect("/")
