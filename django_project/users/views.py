from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create registration form so users can log into site
# user register form is a class built-in to Django, just need to import it

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # where django does back-end checks/validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Messages available from imported messages:

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
