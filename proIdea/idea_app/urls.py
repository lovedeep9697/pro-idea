from  django.conf.urls import url
from . import views

app_name = 'idea_app'

urlpatterns = [
	# listing ideas
	url(r'list/$',views.ListIdeaView.as_view(),name="list"),
	# creating ideas
	url(r'create/$',views.CreateIdeaView.as_view(),name="create"),
	# updating ideas
	url(r'^update/(?P<pk>[-\w]+)/$',views.IdeaUpdateView.as_view(),name="update"),
	# deleting ideas
	url(r'^delete/(?P<pk>\d+)/$',views.IdeaDeleteView.as_view(),name='delete'),
	# sharing ideas
	url(r'^share/(?P<pk>[-\w]+)/$',views.share,name="share"),
	# detail of idea
	url(r'(?P<pk>[-\w]+)/$',views.IdeaDetailView.as_view(),name="detail"),

	
	

	
	

]