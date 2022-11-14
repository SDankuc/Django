from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april" : "Learn new language at least 20 minutes every day!",
    "may": "Go on a run every morning!",
    "june": "Read a Chapter of a Book a Day",
    "july": "Take the Stairs instead of eleveators every day",
    "august": "Cook a New Recipe a Week",
    "september": "Wake up 30 minutes before you have to",
    "october": "Walk 10,000 steps a day",
    "november": "Sit at a table to eat for every meal",
    "december": "Write a letter to someone new every evening"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # <li><a href="/challenges/january">January</a></li><li><a href="/challenges/february">February</a></li>...

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name":month
        })
        #response_data = render_to_string("challenges/challenge.html", {"text": challenge_text})
        #return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>") 