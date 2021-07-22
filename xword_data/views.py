from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from .models import Clue

def drill_get(request):
    clue = Clue.objects.order_by("?").first()
    clue_text = clue.clue_text
    clue_id = clue.pk
    return render(request, 'xword_data/drill.html', {'clue_id':clue_id, 'clue_text':clue_text})


def drill_post_incorrect(request, clue):
    text = "not correct"
    clue_id = clue.pk
    clue_text = clue.clue_text
    return render(request, 'xword_data/drill.html', {'clue_id':clue_id, 'clue_text':clue_text, 'text':text})


def answer_view(request, clue_id):
    clue = get_object_or_404(Clue,pk=clue_id)
    clues = Clue.objects.filter(clue_text=clue.clue_text)
    dic = {}
    for c in clues:
         count = len(Clue.objects.filter(clue_text=clue.clue_text).filter(entry=c.entry))
         dic[count]=c.entry.entry_text

    num_of_clue = len(dic)
    if num_of_clue == 1:
        text = "only appearance of this clue: "
        return render(request, 'xword_data/answer.html', {"text": text, 'clues':dic})
    else:
        text = f"{clue.entry.entry_text} is the correct answer! You have now answered 1 (of {num_of_clue}) clues correctly"
        return render(request, 'xword_data/answer.html', {"text": text, 'clues':dic})

def drill_post(request):
    guess = request.POST.get('answer')
    pk = request.POST.get('clue_id')
    clue = get_object_or_404(Clue,pk=int(pk))
    if guess != clue.entry.entry_text.lower():
        return drill_post_incorrect(request,clue)
    else:
        clue_id = clue.id
        return HttpResponseRedirect(reverse('xword-answer', args=(clue_id,)))