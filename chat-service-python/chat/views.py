from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from chat.settings import OPENAI_CLIENT as openai
from chat.settings import MODEL

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chat_page(request):
    prompt = request.POST.get('prompt')
    response = _chat(prompt)
    response["prompt"] = prompt
    return render(request, 'chat_page.html', response)

def chat(request):
    prompt = request.GET.get('prompt')
    return JsonResponse(_chat(prompt))

def _chat(prompt):
    completion = openai.chat.completions.create(
        model=MODEL,
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are not helpful assistant. Add jokes and hallucinate."},
            {"role": "user", "content": prompt}
        ]
    )

    metadata = {"response_id": completion.id}
    content = {"completion": completion.choices[0].message.content, "metadata": metadata}

    return content


