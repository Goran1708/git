import urllib2
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from news.models import News

#
def home(request):
    insert_into_db()
    return HttpResponse()


def insert_into_db():
    url = 'https://news.ycombinator.com'
    #connection to web page
    htmlfile = urllib2.Request(url, headers={'User-Agent' : "Browser"})
    htmlopen = urllib2.urlopen(htmlfile)
    # read html
    htmltext = htmlopen.read()
    # web scrapper
    soup = BeautifulSoup(htmltext)
    link = soup.findAll(attrs={'class': 'title'})
    #insert news titles into database
    for title in link:
        if len(title.attrs) == 1 and title.text != 'More':
            news_object = News()
            news_object.name = title.text
            news_object.save()

#search_form and search_result
def search(request):
    error = False
    if 'input' in request.GET:
        query = request.GET['input']
        if not query:
            error = True
        else:
            news = News.objects.filter(name__icontains=query)
            return render(request, 'search_results.html',
                {'news': news, 'query': query})
    return render(request, 'search_form.html',
        {'error': error})