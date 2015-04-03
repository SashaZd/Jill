from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, QuestionManager, AnswerManager, ReferencePapersManager, ProjectsManager

urlpatterns = patterns('',

	url(r'^api/user/$', UserManager.userRequest),
	url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest),

	url(r'^api/question/$', QuestionManager.askQuestion, name='question'),
	url(r'^index/$', 'jill_server.views.index', name='home'),
	url(r'^$', 'jill_server.views.login', name='login'),
	url(r'^projects/$', 'jill_server.views.projects', name='projects')
	# Examples:
	# url(r'^$', 'jill_server.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	# url(r'^admin/', include(admin.site.urls))
)
