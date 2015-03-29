
# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import User, Question, Answer, ReferencePapers, Projects


@csrf_exempt
def userRequest(request, user_id=None):
	# if (user_id is None):
	# 	user = getCurrentUser(request)
	# 	if user:
	# 		user_id = user.id

	if request.method == "POST":
		return createUser(request)
	else:
		return getUser(request, user_id)


def createUser(request):
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	email = request.POST.get('email','')

	user = None
	existing_users = User.objects.filter(email=email)

	if len(existing_users) > 0:
		# User Exists!
		existing_user = existing_users[0]
		# we already have a user with that email.
		return HttpResponse(json.dumps({'success': False, "error":"Error! User already exists"}), content_type="application/json")

	if user is None:
		user = User()
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.save()

	if len(existing_users) > 0:
		#reassign incompleted chores
		projects = {}
		# projects = list(Projects.objects.all())
		# for p in projects:
		# 	if p.created_by_user.id = user.id:
		# 		current_project = p
		# 		break

	response_data = user.getResponseData()
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def getUser(request, user_id):
	response_data = {}
	if user_id:
		users = User.objects.filter(id=user_id)
		#Ideally there shouldn't be duplicate users.
		if len(users)>0:
			user = users[0]
			response_data = user.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")

