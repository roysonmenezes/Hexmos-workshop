
import django
from django.http import HttpResponseRedirect,HttpResponse
from .models import Question, OptionVote,Tags
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import F
from django.views import generic
from django.urls import reverse

#week 4 imports
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



   
    
# week 4

@csrf_exempt
def post_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_text = data.get('Question', '')
        option_vote = data.get('OptionVote', {})
        tags = data.get('Tags', [])

        if not question_text:
            return JsonResponse({'error': 'Question text is required'}, status=400)

        question = Question.objects.create(question_text=question_text)

        for option_text, votes in option_vote.items():
            OptionVote.objects.create(question=question, option_text=option_text, votes=int(votes))

        for tag_name in tags:
            Tags.objects.create(question=question, tag_name=tag_name)

        return JsonResponse({'message': 'Question created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_polls(request):
    polls=[]
    questions=Question.objects.all()

    for question in questions:
        options=OptionVote.objects.filter(question=question)
        option_votes={option.option_text:option.votes for option in options}
        tags = list(Tags.objects.filter(question=question).values_list('tag_name', flat=True))

        poll={
            "Question":question.question_text,
            "OptionVote":option_votes,
            "Question_ID":question.id,
            "Tags":tags,
        }
        polls.append(poll)
    return JsonResponse(polls,safe=False)

@csrf_exempt
def get_polls_by_tags(request):
    # to Get the tags from the query parameters
    tags = request.GET.get('tags', '').split(',')

    # Filter polls based on the tags
    polls = []
    questions = Question.objects.filter(tags__tag_name__in=tags).distinct()

    for question in questions:
        options = OptionVote.objects.filter(question=question)
        option_votes = {option.option_text: option.votes for option in options}
        tags = list(Tags.objects.filter(question=question).values_list('tag_name', flat=True))

        poll = {
            "Question": question.question_text,
            "OptionVote": option_votes,
            "Question_ID": question.id,
            "Tags": tags,
        }
        polls.append(poll)

    return JsonResponse(polls, safe=False)

@csrf_exempt
def update_poll(request, poll_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        increment_option = data.get('incrementOption', '')

        try:
            question = Question.objects.get(pk=poll_id)
        except Question.DoesNotExist:
            return JsonResponse({'error': 'Question does not exist'}, status=404)

        options = OptionVote.objects.filter(question=question)
        option_texts = [option.option_text for option in options]

        if increment_option not in option_texts:
            return JsonResponse({'error': 'Invalid option recheck'}, status=400)

        option = OptionVote.objects.get(question=question, option_text=increment_option)
        option.votes += 1
        option.save()

        return JsonResponse({'message': 'Vote updated successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request it is not put'}, status=400)

def get_polls_by_id(request,poll_id):
    poll={}
    question=Question.objects.get(pk=poll_id)
    options=OptionVote.objects.filter(question=question)
    option_votes={}
    for option in options:
        option_votes[option.option_text]=option.votes

    tags=list(Tags.objects.filter(question=question).values_list('tag_name', flat=True))
    poll={
        "Question":question.question_text,
        "OptionVote":option_votes,
        "Question_ID":question.id,
        "Tags":tags,

    }
    return JsonResponse(poll)

def list_of_tags(request):
    tag_list=[]
    questions=Question.objects.all()

    for question in questions:
        tags=list(Tags.objects.filter(question=question).values_list('tag_name',flat=True))
        for tag in tags:
            tag_list.append(tag)
    
    return JsonResponse({"Tags":tag_list},safe=False)