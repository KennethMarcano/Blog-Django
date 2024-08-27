from django.shortcuts import render, redirect, get_object_or_404  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  

def post_list(request):  
    posts = Post.objects.all()
    post_form = PostForm()
    
    if request.method == 'POST':  
        if 'post_form' in request.POST:  
            post_form = PostForm(request.POST)  
            if post_form.is_valid():  
                post_form.save()  
                return redirect('post_list')  
    else:  
        post_form = PostForm()  

    return render(request, 'blog/post_list.html', {  
        'posts': posts,  
        'post_form': post_form,  
    })  

def post_detail(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    comment_form = CommentForm(request.POST or None)  

    if request.method == 'POST' and comment_form.is_valid():  
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
    if request.method == 'POST':  
        post_form = PostForm(request.POST, instance=post)  
        if post_form.is_valid():  
            post_form.save()  
            return redirect('post_list')  
    else:  
        post_form = PostForm(instance=post)  

    return render(request, 'blog/post_edit.html', {  
        'post_form': post_form,  
        'post': post,  
    })  

def post_delete(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':  
        post.delete()  
        return redirect('post_list')  

    return render(request, 'blog/post_delete.html', {  
        'post': post,  
    })

def comment_edit(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':  
        comment_form = CommentForm(request.POST, instance=comment)  
        if comment_form.is_valid():  
            comment_form.save()  
            return redirect('post_detail', post_id=post_id)  
    else:  
        comment_form = CommentForm(instance=comment)  

    return render(request, 'blog/comment_edit.html', {  
        'comment_form': comment_form,  
        'comment': comment,  
    })

def comment_delete(request, post_id, comment_id):  
    comment = get_object_or_404(Comment, id=comment_id)  
    if request.method == 'POST':  
        comment.delete()  
        return redirect('post_detail', post_id=post_id)  

    return render(request, 'blog/comment_delete.html', {  
        'comment': comment,  
    })