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
    "december": None
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
    return render(request,"challenges/index.html", {
        "month_list": month_list
    })
