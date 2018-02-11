# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from newsapi import NewsApiClient
from .models import Article
from .models import Source
from decouple import config
from django.http import HttpResponse

#like the controller 
def index(request):
    
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context); 


def getArticles(request): 
    #get articles from api 
    NEWSAPIKEY = config('NEWSAPIKEY')
    newsapi = NewsApiClient(api_key=NEWSAPIKEY)
    all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='publishedAt',
                                      page=1)
    
    # check 
    if all_articles["status"] == "ok": 
        articles = all_articles["articles"]
        for article in articles: 
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

    import pdb; pdb.set_trace()

    pass 