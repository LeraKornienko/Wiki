from django.shortcuts import render
from . import util
import markdown
import random as stdlib_random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_md_to_hyml(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def entry(request, title):
    html_content = convert_md_to_hyml(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This page does not exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method == "POST":
        search_by_title = request.POST['q']
        html_content = convert_md_to_hyml(search_by_title)
        if html_content is not None: 
            return render(request, "encyclopedia/entry.html", {
            "title": search_by_title,
            "content": html_content
            })
        else:
            all_entries = util.list_entries()
            search_res =[]
            for entry in all_entries:
                if search_by_title.lower() in entry.lower():
                    search_res.append(entry)
            return render (request, "encyclopedia/search.html", {
                "recommendation": search_res
            })

def newPage(request):
    if request.method == "GET":
        return render (request, "encyclopedia/newPage.html")
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
            "message": "Entry page already exists!"
        })
        else: 
            util.save_entry(title, content)
            html_content = convert_md_to_hyml(title)
            return render(request, "encyclopedia/entry.html",{
                title: title, 
                "content": html_content
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['entryTitle']
        content = util.get_entry(title)
        return render (request, "encyclopedia/edit.html",{
            "title": title, 
            "content": content
        })

def subEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_hyml(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title, 
            "content": html_content
        })

def rand(request):
    all_entries = util.list_entries()
    randomEntry = stdlib_random.choice(all_entries)
    html_content = convert_md_to_hyml(randomEntry)
    return render(request, "encyclopedia/entry.html",{
            "title": randomEntry, 
            "content": html_content
        })
