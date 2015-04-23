from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, QuestionManager, AnswerManager, ReferencePapersManager, ProjectsManager, PageManager

urlpatterns = patterns('',

# UserManager API Calls
	url(r'^api/user/$', UserManager.userRequest, name='userrequest'),
	url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest, name='userdata'),

# QuestionManager API Calls
	url(r'^api/question/$', QuestionManager.askQuestion, name='question'),
	
	# url(r'^api/addquestion/$', QuestionManager.addQuestion, name='questionCreate'),	

# ProjectsManager API Calls
	url(r'^api/project/$', ProjectsManager.projectRequest, name='project'),	
	url(r'^api/project/(?P<project_id>\d*)/$', ProjectsManager.projectRequest, name='projectReturn'),
	url(r'^api/project/(?P<project_id>\d*)/history/$', ProjectsManager.getProjectHistory, name='historyForProject'),
	url(r'^api/project/delete/$', ProjectsManager.deleteProject, name='delete_project'),

#ReferencePaperManager API alls
	url(r'^api/reference/$',ReferencePapersManager.paperRequest, name='reference'),
	url(r'^api/reference/(?P<project_id>\d*)/$', ReferencePapersManager.paperRequest, name='getreference'),

# Other API Calls?
	url(r'^home/$',PageManager.getPaperPage, name='home'),
	url(r'^home/(?P<project_id>\d*)/$',PageManager.getPaperPage, name='home'),
	url(r'^home/project$', 'jill_server.views.index', name='currentProject'),
	url(r'^$', 'jill_server.views.login', name='login'),
	url(r'^projects/$',PageManager.getProjects, name='projects'),
	url(r'^signup/$', 'jill_server.views.signup', name='signup')
)
