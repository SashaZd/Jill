from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def login(request):
	template = loader.get_template('login.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def projects(request):
	template = loader.get_template('projects.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def signup(request):
	template = loader.get_template('signup.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))