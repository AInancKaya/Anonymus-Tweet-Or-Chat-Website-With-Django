from django.shortcuts import render,redirect
from . import models
from django.urls import reverse 
from tweetapp.forms import addtweetform

# Create your views here.
def viewtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render (request,'tweetapp/viewtweet.html',context=tweet_dict)
def tweetadd(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nickname , message=message)
        return redirect(reverse('tweetapp:ViewTweet'))
    else:
        return render (request, 'tweetapp/tweetadd.html')

def addtweetbyform(request):
    if request.method == "POST":
        pass
    else:
        form = addtweetform()
        return render(request,'tweetapp/tweetadd.html', context={"form":form})
