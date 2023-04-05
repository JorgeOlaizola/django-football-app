from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Team

# Create your views here.


def index(request):
    team_list = Team.objects.all()
    context = {
        'team_list': team_list
    }
    return render(request, 'football/index.html', context)

def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'football/detail.html', {'team': team})

def results(request, team_id):
    response = "You're looking at the results of team %s."
    return HttpResponse(response % team_id)

def vote(request, team_id):
    return HttpResponse("You're voting on team %s." % team_id)