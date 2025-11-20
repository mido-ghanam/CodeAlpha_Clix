from django.shortcuts import render, redirect
from core.MainVariables import PublishedURL
from shortener import models as m
from django.urls import reverse

def index(request): #f"{PublishedURL}/"
  return render(request, "index.html", {"shortAPI": PublishedURL + "/" + reverse("shortLinkCreateAPI"),})

def routing(request, short_code):
  ShortURL = m.ShortURL.objects.filter(short_code=short_code).first()
  if not ShortURL: return render(request, "404.html", {"shortAPI": PublishedURL + "/" + reverse("shortLinkCreateAPI"),})
  return redirect(ShortURL.full_url)
