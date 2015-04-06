# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects
import urllib

# Watson Specific Imports
import requests


@csrf_exempt
def addReference(request):
	project_id = request.POST.get('project_id','')
	user_id = request.POST.get('user_id','')
	reference_id=request.POST.get('reference_id','')
	existing_reference = CCProjects.objects.filter(project_id=project_id).filter(created_by_user = user[0])

	if len(existing_projects) > 0:
		# Project Exists!
		project = existing_projects[0]
		errorMessage = "Error! You have already created this project."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")


	return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

def deleteReference(request):


def returnReferenceInFormat(request)
	

