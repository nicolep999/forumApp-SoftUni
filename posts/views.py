from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Index page")


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to work with templates",
                "author": "John Doe",
                "content": "How to work with templates in Django?",
                "created_at": datetime.now(),
            },
            {
                "title": "Was the lecture good?",
                "author": "",
                "content": "Should I watch?",
                "created_at": datetime.now(),
            },
            {
                "title": "What is Django?",
                "author": "Lost",
                "content": "**Tell me plz**",
                "created_at": datetime.now(),
            },
        ],
    }
    return render(request, "base.html", context)
