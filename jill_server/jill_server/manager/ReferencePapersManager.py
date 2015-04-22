# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects

import urllib

# Watson Specific Imports
import requests


@csrf_exempt
def paperRequest(request, project_id=None):
	# Create Project
	if request.method == "POST":
		if project_id is None:
			if request.POST.get('reference_id','') == '':
				return createReference(request)
			elif request.POST.get('reference_id','') != '' and request.POST.get('post_type','')=="DELETE":
				return deleteReference(request)
	
	# Get All References from Project ID
	elif request.method == "GET":
		return getReference(request, project_id)

	# elif request.method == "DELETE":
	# 	return deleteReference(request)

@csrf_exempt
def createReference(request):
	evidence_text =  request.POST.get('evidence_text','')
	paper_title =  request.POST.get('paper_title','')
	paper_author = request.POST.get('paper_author','')
	paper_link =  request.POST.get('paper_link','')
	project_id = request.POST.get('project_id','')
	question_id = request.POST.get('question_id','')

	paper = None
	
	existing_projects = CCProjects.objects.filter(id=project_id)
	existing_question = CCQuestion.objects.filter(id=question_id)
	if len(existing_projects) == 0:
		#Project doesn't exist!
		errorMessage = "Error! This project doesn't exist"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	existing_papers = CCReferencePapers.objects.filter(paper_title=paper_title)
	if len(existing_papers) > 0:
		# Ref. Paper exists! Edit the evidence text showing to point to the new evidence text?
		errorMessage = "Error! This paper has already been added"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	referencePaper = CCReferencePapers()
	referencePaper.evidence_text = evidence_text
	referencePaper.paper_title = paper_title
	referencePaper.paper_author = paper_author
	referencePaper.paper_link = paper_link
	
	referencePaper.question_id = existing_question[0]
	referencePaper.save()
	referencePaper.referenced_by_project.add(existing_projects[0])

	return HttpResponse(json.dumps({'success': True}), content_type="application/json")

	
def returnReferenceInFormat(request):
	pass

@csrf_exempt
def deleteReference(request):
	reference_id =  request.POST.get('reference_id','')

	instance = CCReferencePapers.objects.filter(id=reference_id)
	
	if len(instance) == 0:
		# Ref. Paper exists! Edit the evidence text showing to point to the new evidence text?
		errorMessage = "Error! No reference you are deleting"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")	

	instance.delete()	

	return HttpResponse(json.dumps({'success': True}), content_type="application/json")	

@csrf_exempt
def getReference(request, project_id):
	existing_projects = CCProjects.objects.filter(id=project_id)
	
	if len(existing_projects) == 0:
		#Project doesn't exist!
		errorMessage = "Error! This project doesn't exist"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	existing_papers = CCReferencePapers.objects.filter(referenced_by_project=existing_projects[0]).all()

	response_data = []
	if len(existing_papers) > 0:
		for eachPaper in existing_papers: 
			response_data.append(eachPaper.getResponseData())
	else:
		errorMessage = "No references papers added to project."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")	

	# data = serializers.serialize('json', existing_papers)		
	# return HttpResponse(data, content_type="application/json")

	return HttpResponse(json.dumps(response_data), content_type="application/json")
