from django.conf.urls import url, include
from posts import views

urlpatterns = [
 		url(r'^$', views.PostListView.as_view(), name='list_posts'), 
 		url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail_post'), #link using primary key for post details.
 		url(r'^create/$', views.PostCreate.as_view(), name='create_post'),
 		url(r'^(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='update_post'), #specify update
 		url(r'^(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='delete_post'),

]