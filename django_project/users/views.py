from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create registration form so users can log into site
# user register form is a class built-in to Django, just need to import it

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # where django does back-end checks/validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

# Messages available from imported messages:

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
