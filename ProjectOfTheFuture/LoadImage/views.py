from django.shortcuts import render

def loadForm(request):
	try:
		if request.session['Aunt'] == "TrueAunt":
			user = Users.objects.get(id = request.session['id'])
			return render(request, 'myPage.html',{"FirstName":user.FirstName, "LastName":user.LastName,
													"NickName":user.NickName, "email":user.email,
													"Sex":user.Sex,  "bMonth":user.bMonth,
													"bDay":user.bDay, "bYear":user.bYear})
		else:
			pass
	except Exception as e:
		request.session['Aunt'] = "FalseAunt"
	return HttpResponseRedirect("/login")