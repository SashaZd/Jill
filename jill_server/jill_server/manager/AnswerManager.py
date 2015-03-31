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

#return answer id
#given: url to the answer, confidence, questionid, 
@csrf_exempt
def addAnswer(answer, confidence, questionId):
	answer_instance = CCAnswer();
	answer_instance.answer_text = answer
	answer_instance.confidence = confidence
	answer_instance.question_id = questionId
	answer_instance.save()

	response = answer_instance.getResponseData()

	return(response.answer_id);

	

def getAnswer(request):
	pass