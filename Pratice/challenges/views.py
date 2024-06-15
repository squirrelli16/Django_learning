from django.middleware import http
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


m = {
    "january": "study",
    "february": "practice",
    "march": "expand",
    "april": "say",
    "may": "laugh",
    "june": "run",
    "july": "rush",
    "august": "dig",
    "september": "meet",
    "october": "execute",
    "november": "refresh",
    "december": "terminate"
}


# Create your views here.
def monthly_by_number(request, month):
    tranfer = list(m.keys())
    if month > len(tranfer):
        return HttpResponseNotFound("this month does not exist")
    else:
        forward_month = tranfer[month - 1]
    redirect_path = reverse("monthly_by_month", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly(request, month):
    try:
        challenge = m[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge,
            "month": month.capitalize(),
        })
    except:
        return HttpResponseNotFound("<h1>this month does not exist</h1>")


def Listmonth(request):
    list_month = ""
    month_list = list(m.keys())
    for month in month_list:
        capitalize_month = month.capitalize()
        month_path = reverse("monthly_by_month", args=[month])
        list_month += f"<li><a href=\"{month_path}\">{capitalize_month}</li>"
    response_data = list_month
    return HttpResponse(response_data)
