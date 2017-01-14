from django.shortcuts import render

# Create your views here.
def render_home(request):
	# render home page
	context = {'template': 'user-profiles/user_login_signup.html'}
	return render(request, 'main.html', context)

def signup(request):
	# handle user signup
	return render(request, 'main.html')

def login(request):
	# handle user login
	return render(request, 'main.html')

def set_preferences(request):
	# handle setting and editing of preferences
	return render(request, 'main.html')