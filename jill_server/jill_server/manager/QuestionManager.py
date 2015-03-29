# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta


# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects

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