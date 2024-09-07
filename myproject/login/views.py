from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

def loginaction(request):
    if request.method == "POST":
        card_id = request.POST.get("card_id", "")
        email = request.POST.get("email", "")
        
        try:
            # Check if the user exists with the provided card_id and email
            user = User.objects.get(username=card_id, email=email)
            # Log the user in without a password (this is not a standard practice)
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return render(request, 'welcome.html')
        except User.DoesNotExist:
            messages.error(request, 'No user found with the provided Card ID and Email.')
            return redirect('login')  # Redirect back to the login page if user does not exist

    return render(request, 'login_page.html')




