from django.shortcuts import render, redirect, get_object_or_404  
from django.views.decorators.http import require_POST  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  

def post_list(request):  
    posts = Post.objects.all()  
    post_form = PostForm(request.POST or None)  

    if post_form.is_valid():  
        post_form.save()  
        return redirect('post_list')  

    return render(request, 'blog/post_list.html', {  
        'posts': posts,  
        'post_form': post_form,  
    })  

def post_detail(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    comment_form = CommentForm(request.POST or None)  

    if comment_form.is_valid():  
        comment = comment_form.save(commit=False)  
        comment.post = post  
        comment.save()  
        return redirect('post_detail', post_id=post.id)  

    return render(request, 'blog/post_detail.html', {  
        'post': post,  
        'comment_form': comment_form,  
    })  

def post_edit(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    post_form = PostForm(request.POST or None, instance=post)  

    if post_form.is_valid():  
        post_form.save()  
        return redirect('post_list')  

    return render(request, 'blog/post_edit.html', {  
        'post_form': post_form,  
        'post': post,  
    })  

@require_POST  
def post_delete(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    post.delete()  
    return redirect('post_list')  

def comment_edit(request, post_id, comment_id):  
    comment = get_object_or_404(Comment, id=comment_id)  
    comment_form = CommentForm(request.POST or None, instance=comment)  

    if comment_form.is_valid():  
        comment_form.save()  
        return redirect('post_detail', post_id=post_id)  

    return render(request, 'blog/comment_edit.html', {  
        'comment_form': comment_form,  
        'comment': comment,  
    })  

@require_POST  
def comment_delete(request, post_id, comment_id):  
    comment = get_object_or_404(Comment, id=comment_id)  
    comment.delete()  
    return redirect('post_detail', post_id=post_id)  