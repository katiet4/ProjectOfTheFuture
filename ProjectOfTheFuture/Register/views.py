from django.shortcuts import render

def register(request):
	if request.POST:
		email = request.POST.get('index_email')
		password  = request.POST.get('index_pass')
		nick  = request.POST.get('NickName')
		Fname = request.POST.get('FirstName')
		Lname = request.POST.get('LastName')
		sex = request.POST.get('sex')
		Bday = request.POST.get('day')
		Bmonth = request.POST.get('month')
		Byear = request.POST.get('year')
		print(email)
		print(password)
		print(nick)
		print(Fname)
		print(Lname)
		print(sex)
		print(Bday)
		print(Bmonth)
		print(Byear)
	return render(request, 'register.html')

