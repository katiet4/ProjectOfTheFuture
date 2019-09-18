from django.shortcuts import render


def license(request):
	return render(request, 'license.html')
