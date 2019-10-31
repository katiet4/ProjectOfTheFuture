from django.shortcuts import render
from django.http import HttpResponseRedirect
from Login.models import Users
def LoginDef(request):
	try:
		if request.session['Aunt'] != "TrueAunt":
			if request.POST:
				email = request.POST.get('email')
				password  = request.POST.get('password')
				print(Users.objects.filter(email = email).exists())
				if Users.objects.filter(email = email).exists() == False:
					return render(request, 'login.html', {'Answer':'Error','color':'red','proc':17})
				if Users.objects.get(email = email).password == password:
					request.session['Aunt'] = "TrueAunt"
					request.session['id'] = Users.objects.get(email = email).id
					#переход на страницу
					return HttpResponseRedirect("/mypage")
					return render(request, 'login.html', {'Answer':'Successful','color':'green','proc':15})
				else: 
					return render(request, 'login.html', {'Answer':'Error','color':'red','proc':17})
		else:
			return HttpResponseRedirect("/mypage")
	except Exception as e:
		request.session['Aunt'] = "FalseAunt"
	return render(request, "login.html")
	
