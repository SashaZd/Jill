from django.http import HttpResponse
from django.template import RequestContext, loader




def index(request):
	template = loader.get_template('ux ui/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

