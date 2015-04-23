
# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects
import urllib


@csrf_exempt
def getPaperPage(request, project_id=None):
	# Create Project
	return render_to_response('index.html', {'project_id':project_id})


def  getProjects(request):
	return render_to_response('projects.html', {'user_id':1})