from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def profile_view(request):
    profile = Profile.objects.first()
    return render(request, 'profiles/profile_view.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.first() or Profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})
