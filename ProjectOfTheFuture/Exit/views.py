from django.shortcuts import render
from django.http import HttpResponseRedirect
def exit(request):
	try:
		if request.session['Aunt'] == "TrueAunt":
			request.session['Aunt'] = 'FalseAunt'
			return HttpResponseRedirect("/login")
		else:
			return HttpResponseRedirect("/login")
	except Exception as e:
		request.session['Aunt'] = "FalseAunt"
	return HttpResponseRedirect("/login")