from django.shortcuts import render
from Login.models import Users, Images
from django.http import HttpResponseRedirect
def myPage(request):
	try:
		if request.session['Aunt'] == "TrueAunt":
			user = Users.objects.get(id = request.session['id'])
			img = Images.objects.get(NickName = Users.objects.get(id = request.session['id']).NickName).BackGround
			print(img)
			print(str(img))
			return render(request, 'myPage.html',{"FirstName":user.FirstName, "LastName":user.LastName,
													"NickName":user.NickName, "email":user.email,
													"Sex":user.Sex,  "bMonth":user.bMonth,
													"bDay":user.bDay, "bYear":user.bYear,
													"style":str(img)})
		else:
			return HttpResponseRedirect("/login")
	except Exception as e:
		request.session['Aunt'] = "FalseAunt"
	return HttpResponseRedirect("/login")