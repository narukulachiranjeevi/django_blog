from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from taggit.models import Tag



def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',{'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day )
    comments = post.comments.filter(active=True)
    new_comment=None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            new_comment = comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    return render(request,'blog/post/detail.html',{
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form
    })


def post_list(request,tag_slug=None):
    print('hey',tag_slug)
    object_list = Post.published.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        print(tag+'tag is')
        object_list=get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
        'blog/post/list.html',
        {'page': page,
        'posts': posts,
        'tag':tag})

from django.views.generic import ListView

class PostListView(ListView):
    print('calling')
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

from .forms import EmailPostForm,CommentForm

def post_share(request, post_id):
    #Retrieve post by id
    post = get_object_or_404(Post, id=post_id,status='published')
    sent=False
    if request.method == 'POST' :
        form = EmailPostForm(request.POST)
        if(form.is_valid()):
            '''cd = form.cleaned_data
            post_url = request.bulid_absolute_url(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                            f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                            f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])'''
            sent = True
    else :
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post,'form':form,'sent':sent})

