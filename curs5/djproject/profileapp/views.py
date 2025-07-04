from django.shortcuts import render, redirect

# Create your views here.


def profile_view(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect("login")


    print("Este utilizatorul logat?:", request.user)

    return render(request, "profile.html", context)


from django.contrib.auth.decorators import login_required


@login_required
def only_logged_users_view(request):
    return render(request, "only_logged_users.html")