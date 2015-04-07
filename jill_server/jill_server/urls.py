from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, QuestionManager, AnswerManager, ReferencePapersManager, ProjectsManager

urlpatterns = patterns('',

# UserManager API Calls
	url(r'^api/user/$', UserManager.userRequest),
	url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest),

# QuestionManager API Calls
	url(r'^api/question/$', QuestionManager.askQuestion, name='question'),
	

# ProjectsManager API Calls
	url(r'^api/project/$', ProjectsManager.projectRequest, name='project'),	
	# url(r'^api/project/list/$', ProjectsManager.createProject, name='project'),
	url(r'^api/project/(?P<project_id>\d*)/$', ProjectsManager.projectRequest, name='projectReturn'),

#ReferebcePaperManager API alls
	url(r'^api/reference/$',ReferencePapersManager.createReference, name='reference'),
	url(r'^api/project/(?P<reference_id>\d*)/$', ReferencePapersManager.getReference, name='get_reference'),

# Other API Calls?
	url(r'^home/$', 'jill_server.views.index', name='home'),
	url(r'^home/project$', 'jill_server.views.index', name='currentProject'),
	url(r'^$', 'jill_server.views.login', name='login'),
	url(r'^projects/$', 'jill_server.views.projects', name='projects')


	# Examples:
	# url(r'^$', 'jill_server.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	# url(r'^admin/', include(admin.site.urls))
)
