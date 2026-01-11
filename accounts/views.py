from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "⚠️ Please fix the errors.")
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, "✅ Logged in successfully!")
        response = super().form_valid(form)

        # Redirect to ?next= if available
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return redirect(next_url)

        return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """
    Returns current logged-in user info using JWT authentication
    """
    return Response({
        "username": request.user.username,
        "is_staff": request.user.is_staff
    })
