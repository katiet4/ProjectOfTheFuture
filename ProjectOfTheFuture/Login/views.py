from django.shortcuts import render

def LoginDef(request):

	if request.POST:
		email = request.POST.get('email')
		#password  = request.POST.get('pass')

	return render(request, "index.html")
