from django.shortcuts import render
from Login.models import Users
def LoginDef(request):
	if request.POST:
		email = request.POST.get('email')
		password  = request.POST.get('pass')
		if Users.objects.filter(email = email).exists():
			return render(request, 'index.html', {'Answer':'Error'})
		if Users.objects.get(email = email).password == password:
			request.session['Aunt'] = "TrueAunt"
			#переход на страницу
		

	return render(request, "index.html")
