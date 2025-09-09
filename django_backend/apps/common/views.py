from django.shortcuts import redirect

def home_view(request):
	if not request.user.is_authenticated:
		return redirect('/api/auth/login/')
	return redirect('/api/')
