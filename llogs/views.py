from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic

def index(request):
    return render(request, 'llogs/index.html')

def topics(request):
    '''Display all topics'''
    topics = Topic.objects.order_by('time_added')
    context = {'topics': topics}
    return render(request, 'llogs/topics.html', context)

def topic(request, topic_id):
    '''Display memos for a spcific topic'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-time_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'llogs/topic.html', context)