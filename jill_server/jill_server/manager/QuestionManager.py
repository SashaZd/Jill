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
def askQuestion(request, user_id=None):
	if request.method == "POST":
		return askWatson(request)

def addQuestion(question_text, from_project_id):
	
	existing_questions = CCQuestion.objects.filter(question_text=question_text).filter(from_project_id=from_project_id)
	
	question = None

	if len(existing_questions) > 0:
		#Question already exists
		errorMessage = "Error! Question already exists."
		question = existing_questions[0]
		response_data = question.getResponseData()
		return question.id

	if question == None:
		question = CCQuestion()

	question.question_text = question_text
	from_project = CCProjects.objects.filter(id=from_project_id)

	if len(from_project) > 0:
		project = from_project[0]

	question.from_project_id = project

	question.save()

	return question.id

def askWatson(request):
	from_project_id = request.POST.get('from_project_id','')
	question_text = request.POST.get('question_text','')

	unformatted_response = askWatsonAPICall(question_text)

	question_id = unformatted_response["question"]["id"]
	evidencelist = unformatted_response["question"]["evidencelist"]

	response_data = {}
	
	response_data["evidences"] = []

	trimmed_answer_base_URL = "https://watson-wdc01.ihost.com"
	response_data["tempData"] = len(evidencelist)

# # Waiting for Bryan to respond with base_URL for papers
		# evidence = CCReferencePapers()

	temp = addQuestion(question_text, from_project_id)
	response_data["question_id"]= temp

	for eachEvidence in evidencelist:
		try:
			evidence = {}
			evidence["evidence_text"] = eachEvidence["text"]
			evidence["paper_title"] = eachEvidence["metadataMap"]["title"]
			evidence["trimmed_document"] = trimmed_answer_base_URL+eachEvidence["document"]
			evidence["originalFile"] = eachEvidence["metadataMap"]["originalfile"]
			evidence["documentPath"] = ""
			response_data["evidences"].append(evidence)

		except: 
			pass
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def askWatsonAPICall(question):
    data={"question": {"questionText" : question}}

    username="gat_administrator"
    password="KYpDpl0e"

    url="https://watson-wdc01.ihost.com/instance/522/deepqa/v1/question"
    headers={"Content-type": "application/json",
             "Accept": "application/json",
             "X-SyncTimeout": "30"}

    print("Asking Watson: " + question)

    response = requests.post(url, data=json.dumps(data), auth=(username, password), headers=headers)
    
    jsonResponse = response.json();

    return jsonResponse;