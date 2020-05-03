from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'furqan'})


def remove_pun(request):
    puncation = request.POST.get('puncation', 'off')
    texts = request.POST.get('text', "no thing")
    capitalize = request.POST.get('capital', 'off')
    line_remover = request.POST.get('line_remover', 'off')
    space_remover = request.POST.get('space_remover', 'off')


    finaltext = ""
   


    if puncation == 'on':
        puncationlist = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in texts:
            if char not in puncationlist:
                finaltext = finaltext + char
        texts = finaltext
        finaltext=''
        #return render(request, 'remove_pun.html', {'text': finaltext})

    if capitalize == 'on':
        for char in texts:
            finaltext = finaltext + char.upper()
        texts = finaltext
        finaltext = ''
        #return render(request, 'remove_pun.html', {'text': finaltext})


    if line_remover == 'on':
        line ='\n,\r'
        for char in texts:
            if char not in line:
                finaltext= finaltext+ char
        texts = finaltext
        finaltext = ''
        #return render(request,'remove_pun.html',{'text':finaltext})

    if space_remover == 'on':
        for index, char in enumerate(texts):
            if texts[index] == " " and texts[index + 1] == " ":
                pass
            else:
                finaltext = finaltext + char
        texts = finaltext
        finaltext = ''
    return render(request, 'remove_pun.html', {'text': texts})
        #return render(request, 'remove_pun.html', {'text': finaltext})


    for char in texts:
            if (char>='a' and char<='z') or (char>='A' and char<='Z'):
                characters+=1
    texts = finaltext



   # if(True):
        #return render(request, 'remove_pun.html', {'text': 'You have select ed nothing to do \n your text :'+texts})
