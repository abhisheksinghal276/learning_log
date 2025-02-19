from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# View for Logout
def logout_view(request):
    """Logging out the user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

# View for registering new users

# Importing required modules
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display Blank registeration form
        form = UserCreationForm()
    else:
        # Process Completed Form
        form = UserCreationForm(data= request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
