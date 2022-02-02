import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewsChooser
from .models import Ask, New, Job, Show


def index(request):
    if request.method == 'POST':
        newsCategory = request.POST['newsType']
        newsCategory += "stories"
        idBase = requests.get(f'https://hacker-news.firebaseio.com/v0/{newsCategory}.json').json()
        dictStories = list()
        for i in idBase:
            stories = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json').json()
            if stories is None:
                continue
            dictStories.append(stories)
        if newsCategory == 'askstories':
            model = Ask
        elif newsCategory == 'newstories':
            model = New
        elif newsCategory == 'showstories':
            model = Show
        else:
            model = Job
        for story in dictStories:
            try:
                model.objects.get(s_id=story['id'])
            except (ObjectDoesNotExist, TypeError):
                print(model)
                if "text" not in story.keys():
                    story["text"] = None
                if "url" not in story.keys():
                    story["url"] = None
                model.objects.create(by=story['by'],
                                     s_id=story['id'],
                                     score=story['score'],
                                     time=story['time'],
                                     title=story['title'],
                                     text=story['text'],
                                     url=story['url'],
                                     type=story['type'])
        return HttpResponse("done")
    else:
        dropdown = NewsChooser()
        return render(request, "hackernews/scraper.html", {'dropdown': dropdown})
