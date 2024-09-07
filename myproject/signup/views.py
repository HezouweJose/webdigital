from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from webauthin.views import *
from webauthin.settings import *

def signaction(request):
   # print('multimill')
    if request.method == "POST":
        # Extract data from the form
  
        try:
            # Check if the username (card) already exists
            if User.objects.filter(username=card).exists():
                messages.error(request, 'Card already exists. Please choose a different one.')
                return redirect('signup')
            # Create a new user
            User.objects.create_user(username=card, email=em, first_name=fn, last_name=ln)
            messages.success(request, 'Account created successfully!')

            print('argent')
            fn = request.POST.get("first_name", "")
            ln = request.POST.get("last_name", "")
            em = request.POST.get("email", "")
            card = request.POST.get("card_id", "")
            register_verify(request)

           # return redirect('login')  # Redirect to the login page after successful registration
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('signup')  # Redirect back to the signup page in case of error

    return render(request, 'signup_page.html')
    #return redirect('signup')
