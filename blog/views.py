from django.shortcuts import render
from blog.models import Articles, Tag, Classification, Author
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	posts = Articles.objects.all().order_by('-pub_date')
	paginator = Paginator(posts, 2) 
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.paginator(paginator.num_pages)
	return render(request,'home.html',{'post_list':post_list})
	#return render(request, 'home.html',{'blog_list' : blog_list})
# Remember to delete the migration direction, or else there will be a programming error 1146

def detail(request,id):
	try:
	    post = Articles.objects.get(id=str(id))
	except Articles.DoesNotExist:
		raise Http404
	return render(request,'post.html',{'post':post})


	
	#post = Articles.objects.all()[int(my_args)]
	#str = ("content = %s, author = %s, pub_date = %s, caption = %s, tags=%s, classification=%s" 
     #   % (post.content, post.author, post.pub_date, post.caption, post.tags, post.classification))
	#return HttpResponse(str)

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})

def archives(request) :
    try:
        post_list = Articles.objects.all()
    except Articles.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def about_me(request) :
    return render(request, 'aboutme.html')


	


	

