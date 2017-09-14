# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from MyApp.models import Category, Page
from MyApp.forms import CategoryForm, PageForm

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    index_page = render(request,'index.html',context_dict)
    return HttpResponse(index_page)

def category(request, category_name_slug):
    context_dict = { }
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'cagetory.html', context_dict)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request,'add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                print cat.name
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
            else:
                print 'category: %s not exist' % category_name_slug
        else:
            print form.errors
    else:
        form = PageForm()
    if cat:
        category_name = cat.name
    else:
        category_name = None
    context_dict = {'form':form,'category':cat, 'category_name':category_name}
    return render(request, 'add_page.html', context_dict)