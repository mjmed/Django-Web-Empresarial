from django.shortcuts import render, get_object_or_404

from .models import Post, Category


def blog(request):
    """Renderiza la vista que contiene los posts"""
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

# manera rudimentaria
# def category(request, category_id):
#     """Renderiza los post por categoría seleccionada"""
#     _category = get_object_or_404(Category, id=category_id)
#     posts = Post.objects.filter(categories=_category)
#     return render(request, 'blog/category.html', {'category': _category, 'posts': posts})

# forma optimizada
def category(request, category_id):
    """Renderiza por categoría seleccionada sus posts"""
    _category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category': _category})
