from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, QuestionManager, AnswerManager, ReferencePapersManager, ProjectsManager

urlpatterns = patterns('',

	url(r'^api/user/$', UserManager.userRequest),
	url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest),

	url(r'^api/question/$', QuestionManager.askQuestion),
	url(r'^$', 'jill_server.views.index', name='home')
	# Examples:
	# url(r'^$', 'jill_server.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	# url(r'^admin/', include(admin.site.urls))
)
