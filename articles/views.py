# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from newsapi import NewsApiClient
from .models import Article
from .models import Source
from decouple import config
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect


def index(request):
    
    articles_all = Article.objects.all().order_by("publishedAt")

    paginator = Paginator(articles_all, 12)
    page = request.GET.get('page')
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context); 


def getArticles(request): 
    if request.method == "GET":
        keysearch =  request.GET["q"]
    NEWSAPIKEY = config('NEWSAPIKEY')
    newsapi = NewsApiClient(api_key=NEWSAPIKEY)
    all_articles = newsapi.get_everything(q=keysearch,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com,Cnet.com,Mashable.com,Theverge.com,Thenextweb.com,Wired.com',
                                      language='en',
                                      sort_by='publishedAt',
                                      page=1)
    
    # check 
    if all_articles["totalResults"] > 0: 
        articles = all_articles["articles"]
        for article in articles: 
            if not Article.objects.filter (title=article["title"]).exists ():
                #insert source 
                source_model = Source() 
                source_from_api = article["source"]
                source_model.source_id =  source_from_api["id"]
                source_model.name = source_from_api["name"]
                source_model.save(); 
                #insert Articles 
                article_model = Article()
                article_model.source = source_model
                article_model.author = article["author"]
                article_model.title = article["title"]
                article_model.description = article["description"]
                article_model.publishedAt = article["publishedAt"]
                article_model.url = article["url"]
                article_model.urlToImage = article["urlToImage"]
                article_model.save()
            else:
                pass 
                
        
    else: 
        print "there is no up date"
    return  redirect('/articles/')