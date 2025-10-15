from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    articles = Article.objects.all().order_by('-created_at')  # новые сначала
    categories = Category.objects.all()
    return render(request, 'articles/home.html', {'articles': articles, 'categories': categories})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()

    comments = article.comments.all().order_by('-created_at')

    if request.method == "POST":
        if request.user.is_authenticated:
            text = request.POST.get("text")
            if text.strip():
                Comment.objects.create(article=article, author=request.user, text=text)
                messages.success(request, "Комментарий добавлен!")
                return redirect('article_detail', slug=slug)
            else:
                messages.error(request, "Комментарий не может быть пустым.")
        else:
            messages.error(request, "Авторизуйтесь, чтобы оставить комментарий.")

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments
    })

from django.shortcuts import render, get_object_or_404
from .models import Article, Category

from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def categories_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'articles/categories.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).order_by('-created_at')
    return render(request, 'articles/category_detail.html', {
        'category': category,
        'articles': articles
        
    })

def about_view(request):
    return render(request, 'articles/about.html')

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from tests_app.models import Test
from .models import Article, Comment, Category

@user_passes_test(lambda u: u.is_superuser)
def dashboard_view(request):
    total_articles = Article.objects.count()
    total_tests = Test.objects.count()
    total_users = User.objects.count()
    total_comments = Comment.objects.count()

    latest_articles = Article.objects.order_by('-created_at')[:5]
    latest_comments = Comment.objects.order_by('-created_at')[:5]

    context = {
        'total_articles': total_articles,
        'total_tests': total_tests,
        'total_users': total_users,
        'total_comments': total_comments,
        'latest_articles': latest_articles,
        'latest_comments': latest_comments,
    }

    return render(request, 'articles/dashboard.html', context)



