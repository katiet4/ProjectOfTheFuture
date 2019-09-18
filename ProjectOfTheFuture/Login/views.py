from django.shortcuts import render
from .models import Users
def LoginDef(request):

	if request.POST:
		pass

	return render(request, "index.html")
