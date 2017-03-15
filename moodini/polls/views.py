from django.http import HttpResponse, JsonResponse
from .models import Poll, Choice, SelectedMood
from Queue import PriorityQueue


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def start_poll(request):
    poll_id = request.POST.get('poll')
    players = request.POST.get('players')
    poll = Poll(id=poll_id, people=players)
    poll.save()

    return HttpResponse("You're user %s." % request.POST.get('user'))


def select_mood(request, poll_id):
    mood = request.POST.get('mood')
    user = request.POST.get('user')
    poll = Poll.objects.get(id=poll_id)
    mood = SelectedMood(poll=poll, mood=mood, user=user)
    mood.save()
    return HttpResponse("OK")


def get_location(request, poll_id, location_id):
    poll = Poll.objects.get(id=poll_id)
    if not poll.is_mood_selected():
        return JsonResponse({})

    if poll.selectedlocations_set.count() != 5:
        poll.generate_locations()

    location = poll.selectedlocations_set.get(num=location_id).location
    return JsonResponse({
        'name': location.location_name,
        'img': location.image,
        'description': location.description
    })


def vote_location(request, poll_id, location_id):
    vote = request.POST.get('vote')
    user = request.POST.get('user')
    poll = Poll.objects.get(id=poll_id)
    location = poll.selectedlocations_set.get(num=location_id)
    choice = Choice(location=location, vote=vote, user=user)
    choice.save()

    return HttpResponse("OK")


def get_result(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if not poll.is_closed():
        return JsonResponse({})

    q = PriorityQueue()
    for location in poll.selectedlocations_set.all():
        votes = location.choice_set.filter(vote='1').count()
        q.put((-votes, location.location))

    result = q.get()[1]

    return JsonResponse({
        'name': result.location_name,
        'img': result.image,
        'description': result.description
    })
