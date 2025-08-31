from . import views
from django.urls import path

app_name = 'SocialApp'

urlpatterns = [
    path('tweetadd/', views.tweetadd,name="AddTweet"),
    path('viewtweet/',views.viewtweet,name="ViewTweet"),
    path('addtweetbyform/', views.addtweetbyform,name='addtweetbyform'),
]
