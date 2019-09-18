from django.shortcuts import render

def LoginDef(request):

	if request.POST:
		pass

	return render(request, "index.html")
