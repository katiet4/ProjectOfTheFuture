from django.shortcuts import render
from Login.models import Users, Images
from django.http import HttpResponseRedirect
def register(request):
	try:
		if request.session['Aunt'] != "TrueAunt":
			if request.POST:
				email = request.POST.get('index_email')
				password  = request.POST.get('index_pass')
				nick  = request.POST.get('NickName')
				Fname = request.POST.get('FirstName')
				Lname = request.POST.get('LastName')
				sex = request.POST.get('sex')
				BDay = request.POST.get('day')
				BMonth = request.POST.get('month')
				BYear = request.POST.get('year')
				if Users.objects.filter(NickName = nick).exists() or Users.objects.filter(email = email).exists():
					return render(request, 'register.html', {'Answer':'Error','color':'red','proc':14})
				user = Users(FirstName = Fname, LastName = Lname, NickName = nick, 
								email = email, password = password, Sex = 'M' if sex == 'Male' else "F",
								bYear = BYear, bMonth = BMonth, bDay = BDay)
				user.save()
				img = Images(NickName = nick)
				img.save()
				return render(request, 'register.html', {'Answer':'Successful','color':'green','proc':14})
			return render(request, 'register.html')
		else:
			return HttpResponseRedirect("/mypage")
	except Exception as e:
		request.session['Aunt'] = "FalseAunt"
	return HttpResponseRedirect("/login")
