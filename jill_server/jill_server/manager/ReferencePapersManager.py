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
def paperRequest(request, reference_id=None):
	if request.method == "POST":
		if reference_id is None:
			return createReference(request)
	else:
		return getReference(request, reference_id)

def createReference(request):
	evidence_text =  request.POST.get('evidence_text','')
	paper_title =  request.POST.get('paper_title','')
	paper_author = request.POST.get('paper_author','')
	paper_link =  request.POST.get('paper_link','')
	project_id = request.POST.get('project_id','')
	question_id = request.POST.get('question_id','')

	paper = None
	
	existing_projects = CCProjects.objects.filter(project_id=project_id)

	if len(existing_projects) == 0:
		#Project doesn't exist!
		errorMessage = "Error! This project doesn't exist"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	existing_papers = CCReferencePapers.objects.filter(paper_title=paper_title).filter(project_id = project_id).filter(question_id = question_id)

	if len(existing_papers) > 0:
		# Ref. Paper exists! Edit the evidence text showing to point to the new evidence text?
		errorMessage = "Error! This paper has already been added"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	







def updateReference(request):
	pass

def getReference(request, reference_id):
	pass

