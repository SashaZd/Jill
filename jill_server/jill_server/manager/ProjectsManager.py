
# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects

@csrf_exempt
def projectRequest(request, project_id=None):
	if request.method == "POST":
		return createProject(request)
	else:
		return getProject(request, project_id)

def getProject(request, project_id):
	existing_projects = CCProjects.objects.filter(id=project_id)
	
	if len(existing_projects) > 0:
		foundProject = existing_projects[0]
		response_data = foundProject.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def createNewProject(request):
	project_title = request.POST.get('project_title','')
	created_by_user = request.POST.get('created_by_user','')

	project = None
	existing_projects = CCProjects.objects.filter(created_by_user=created_by_user).filter(project_title=project_title)

	if len(existing_projects) > 0:
		# Project Exists!
		existing_user = existing_users[0]
		errorMessage = "Error! You have already created this project."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if project is None:
		project = CCProjects()
	project.project_title = project_title

	user = CCUser.objects.filter(id=created_by_user)

	project.created_by_user = user
	project.save()

	response_data = project.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


# def getUser(request, user_id):
# 	response_data = {}
# 	if user_id:
# 		users = CCUser.objects.filter(id=user_id)
# 		#Ideally there shouldn't be duplicate users.
# 		if len(users)>0:
# 			user = users[0]
# 			response_data = user.getResponseData()

# 	return HttpResponse(json.dumps(response_data), content_type="application/json")

