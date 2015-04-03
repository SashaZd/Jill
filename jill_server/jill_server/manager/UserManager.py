
# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects


@csrf_exempt
def userRequest(request, user_id=None):
	if request.method == "POST":
		return createUser(request)
	else:
		return getUser(request, user_id)


def createUser(request):
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	email = request.POST.get('email','')

	user = None
	existing_users = CCUser.objects.filter(email=email)

	if len(existing_users) > 1:
		# User Exists!
		existing_user = existing_users[0]
		errorMessage = "Error! User with this email already exists."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if user is None:
		user = CCUser()
	user.first_name = first_name
	user.last_name = last_name
	user.email = email

	if len(existing_users) > 0:
		user.projects = CCProjects()

	user.save()

	response_data = user.getResponseData()
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def getUser(request, user_id):
	response_data = {}
	if user_id:
		users = CCUser.objects.filter(id=user_id)
		#Ideally there shouldn't be duplicate users.
		if len(users)>0:
			user = users[0]
			response_data = user.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")

