from django.shortcuts import render

from .models import Topic

# Create your views here.

# view for the home page
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

# View for the Topics page

# Importing @login_required to restrict access to topics to only logged-in users
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login')
def topics(request):
    """Show the list of topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

# View for the individual topic page

# Importing required modules to check requested entries before retriving them
# importing below modules for error handling
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404

@login_required(login_url='users:login')
def topic(request, topic_id):
    """Show the list of entries for each topic"""
    topic = get_object_or_404(Topic, id=topic_id)

    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

# View for the new topic

# Importing required modules
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm

@login_required(login_url='users:login')
def new_topic(request):

    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# View for creating new entry

# Importing required modules
from .forms import EntryForm

@login_required(login_url='users:login')
def new_entry(request, topic_id):
    """ Add a new entry for a particular topic"""
    topic = Topic.objects.get(id= topic_id)

    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

# View for editing entries

# Importing required modules
from .models import Topic, Entry

@login_required(login_url='users:login')
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # Make sure if the current user is the owner of the topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted, process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

