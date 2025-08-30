from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm, BlogSubSectionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# def home(request):
#     return render(request, "blog/home.html",)



def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        formset = BlogSubSectionForm(request.POST)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            blog = form.save()
            subsection = formset.save(commit=False)
            subsection.blog = blog
            subsection.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        formset = BlogSubSectionForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'formset': formset})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def select_post(request):
    posts = Post.objects.all()
    selected_post = None

    if request.method == "POST":
        post_id = request.POST.get('selected_post')
        if post_id:
            selected_post = get_object_or_404(Post, id=post_id)

    return render(request, 'registration/select_post.html', {
        'posts': posts,
        'selected_post': selected_post
    })

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('select_post')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('select_post')
    return render(request, 'blog/delete_post.html', {'post': post})




