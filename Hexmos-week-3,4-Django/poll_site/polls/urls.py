import django
from django.urls import path
from . import views

app_name="polls"
urlpatterns=[ 
#    path("",views.IndexView.as_view(),name="index"),
#              path("<int:pk>/",views.DetailView.as_view(),name="detail"),
#              path("<int:pk>/results/",views.ResultsView.as_view(),name='results'),
#              path("<int:question_id>/vote/",views.vote,name="vote"),
            path("post_question/",views.post_question,name="post_question"),
            path("get_polls/",views.get_polls,name="get_polls"),
            path("get_polls_by_tags/",views.get_polls_by_tags,name="get_polls_by_tags"),
            path("<int:poll_id>/update_poll/",views.update_poll,name="update_poll"),
            path("<int:poll_id>/get_polls_by_id/",views.get_polls_by_id,name="get_polls_by_id"),
            path("list_of_tags/",views.list_of_tags,name="list_of_tags"),
            ]