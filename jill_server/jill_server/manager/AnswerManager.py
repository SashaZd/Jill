# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta


# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects
from ..manager import UserManager, QuestionManager

import urllib

# Watson Specific Imports
import requests


@csrf_exempt
def addAnswer(request):
	pass
	

def getAnswer(request):
	pass