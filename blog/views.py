from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegistrationForm
from .models import BlogPostModel
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def UserRegisterView(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Login successfull !")
            return redirect('index')        
        else:
            messages.error(request, 'Please fill correctly')

    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form':form})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Login successfully !')
            return redirect('index')
    
        else:
            messages.error(request, "invalid username or password")
    
    return render(request, 'accounts/login.html')


def LogoutView(request):
    logout(request)
    messages.success(request, 'Logout successfully !')
    return redirect('index')


def IndexPage(request):
    random_blog = BlogPostModel.objects.filter(published=True).order_by('?').first()
    six_blog = BlogPostModel.objects.filter(published=True).order_by('?')[:6]
    blogs = BlogPostModel.objects.filter(published=True)
    return render(request, 'pages/index.html', {'blogs':blogs, 'random_blog':random_blog, 'six_blog':six_blog})


def SearchBlogPage(request):
    query = request.GET.get('query')
    search_blogs = BlogPostModel.objects.filter(title__icontains=query)
    return render(request, 'pages/blog_search.html', {'query':query, 'search_blogs':search_blogs})


def DetailBlog(request, slug):
    blog = get_object_or_404(BlogPostModel, slug=slug)
    recent_blogs = BlogPostModel.objects.exclude(slug=slug).order_by('-created_at')[:5]  # Fetch 5 recent blogs
    paragraphs = blog.title.split('\n')
    words = blog.content.split()
    words2 = blog.heading2Content.split() if blog.heading2Content else ''
    paragraphs = [" ".join(words[i:i+60]) for i in range(0, len(words), 60)]
    paragraphs2 = [" ".join(words2[i:i+60]) for i in range(0, len(words2), 60)]
    return render(request, 'pages/detail_blog.html',
                   {"blog":blog, 
                    "paragraphs":paragraphs,
                    "paragraphs2":paragraphs2,
                    'recent_blogs': recent_blogs,
                    'paragraphs': paragraphs,})


@login_required
def CreateBlogView(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, "Blog create successfuly !")
            return redirect('index')
        
    else:
        form = BlogPostForm()
    
    return render(request, 'pages/create_blog.html', {'form':form})

def category_filter_view(request, category):
    blogs = BlogPostModel.objects.filter(category=category,
                                        published=True).order_by('-created_at')
    return render(request, 
                  'pages/category_filter.html', 
                  {"blogs": blogs, 
                   "category": category})



def AboutPage(request):
    return render(request, 'pages/about.html')


def ContactPage(request):
    return render(request, 'pages/contact.html')


def handler404(request,exception):
    return render(request, "404.html", status=404)


