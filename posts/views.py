from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from posts.models import Post,Comment

def index(request):
	latest = Post.objects.order_by('-pub_date')[:25]
	new_list = sorted(latest,key=lambda x: x.score(), reverse=True)
	return render(request,'posts/index.html', {'latest' : new_list,'page' : 1})
def index_page(request,page):
	multiplyer = int(page) * 25
	first = int(multiplyer) - 25
	latest = Post.objects.order_by('-pub_date')[first:multiplyer]
	new_list = sorted(latest,key=lambda x: x.score(), reverse=True)
	return render(request,'posts/index.html', {'latest' : new_list, "page" : page})
def detail(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	return render(request,'posts/detail.html',{'post' : post})

def upvote(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	post.upvotes += 1
	post.save()
	page = request.POST['page']
	if page == '1':
		return HttpResponseRedirect(reverse('posts:index'))
	else:
		return HttpResponseRedirect(reverse('posts:index_page',args=(page,)))
def downvote(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	post.upvotes -= 1
	post.save()
	page = request.POST['page']
	if page == '1':
		return HttpResponseRedirect(reverse('posts:index'))
	else:
		return HttpResponseRedirect(reverse('posts:index_page',args=(page,)))
	

