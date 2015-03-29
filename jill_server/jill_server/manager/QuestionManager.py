# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import User, Question, Answer, ReferencePapers, Projects


@csrf_exempt
def askQuestion(request, user_id=None):
	if request.method == "POST":
		return askWatson(request)
	

def askWatson(request):
	asked_by_user = request.POST.get('email','')
	from_project_id = models.ForeignKey('Projects', related_name="from_project_id")

	# Aziz : API call here 
	response_data = {}
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")