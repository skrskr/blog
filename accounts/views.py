from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    print(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login user
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
    