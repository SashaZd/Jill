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
	

def askWatson(request):
	asked_by_user = request.POST.get('email','')
	from_project_id = request.POST.get('from_project_id','')
	question_text = request.POST.get('question_text','')

	# print askWatson("How do pinecones work?")

	unformatted_response = askWatsonAPICall(question_text)

	question_id = unformatted_response["question"]["id"]
	evidences = unformatted_response["question"]["evidencelist"]

	response_data = {}
	response_data["question_id"]= question_id
	response_data["evidences"] = []

	trimmed_answer_base_URL = "https://watson-wdc01.ihost.com"
	response_data["tempData"] = 99

# # Waiting for Bryan to respond with base_URL for papers
	for eachEvidence in evidences:
		# evidence = CCReferencePapers()
		try:
			evidence = {}
			evidence["evidence_text"] = eachEvidence["text"][:100]
			evidence["paper_title"] = eachEvidence["metadataMap"]["title"][:100]
		
			evidence["trimmed_document"] = trimmed_answer_base_URL+eachEvidence["document"]
			evidence["originalFile"] = eachEvidence["metadataMap"]["originalfile"]
			evidence["documentPath"] = ""

			response_data["evidences"].append(evidence)

			existing_questions = CCQuestion.objects.filter(question_text=question_text)
			response_data["tempData"] = len(existing_questions)

			if len(existing_questions) > 0:
				#Question asked before
				existing_question = existing_questions[0]
				errorMessage = "Info! You've asked this question before"
			
			else:

				question = CCQuestion()
				question.question_text = question_text
				question.evidence_list = evidence
				question.asked_by_user = CCUser.objects.filter(email=email)[0].user_id
				question.from_project_id = from_project_id

				confidence = 90
				question.answers = 1 # addAnswer(trimmed_answer_base_URL, confidence, question.question_id)

				question.save()

		except: 
			pass
	# response_data = {}
	
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