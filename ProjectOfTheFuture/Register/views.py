from django.shortcuts import render
from Login.models import Users
def register(request):
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
		user = Users(FirstName = Fname, LastName = Lname, NickName = nick, 
						email = email, password = password, Sex = 'M' if sex == 'Male' else "F",
						bYear = BYear, bMonth = BMonth, bDay = BDay)
		user.save()

		# print(email)
		# print(password)
		# print(nick)
		# print(Fname)
		# print(Lname)
		# print(sex)
		# print(Bday)
		# print(Bmonth)
		# print(Byear)
	return render(request, 'register.html')

