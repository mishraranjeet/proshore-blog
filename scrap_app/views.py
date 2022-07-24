from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q


# Create your views here.
from scrap_app.models import Blog


def blog_list(request):
    search = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    page = request.GET.get('page', 1)
    print("query:", search, sort)
    if len(search) > 0:
        all_blogs = Blog.objects.filter(
            Q(title__icontains=str(search).lower()) |
            Q(author_name__icontains=str(search).lower()) |
            Q(description__icontains=str(search).lower()) |
            Q(reading_time__icontains=str(search).lower()) |
            Q(designation__icontains=str(search).lower())
              )
        request.session["search"] = search
    else:
        all_blogs = Blog.objects.all()
        if "search" in request.session:
            del request.session["search"]
    sorting = {"oldest": 'updated_on', 'newest': "-updated_on", 'author': 'author_name'}
    if len(sort) > 0:
        all_blogs = all_blogs.order_by(sorting.get(sort, '-updated_on'))

    paginator = Paginator(all_blogs, 10)
    pagination_data = paginator.get_page(page)
    print("pagination_data", pagination_data)
    context = {
        "blogs": [pagination_data[i:i+3] for i in range(0, len(pagination_data), 3)],
        'page_obj': pagination_data
    }
    # print("context", context)
    return render(request, 'blog-list.html', context)


def blog_detail(request, blog_id):
    blog = Blog.objects.filter(pk=int(blog_id)).first()

    context = {
        "row": blog,
        "blog_id": blog_id
    }
    # print("context", context)
    return render(request, 'blog_detail.html', context)


def blog_delete(request, blog_id):
    blog = Blog.objects.filter(pk=int(blog_id)).delete()
    return redirect('blog_list')


def blog_edit(request, blog_id):
    blog = Blog.objects.filter(pk=int(blog_id)).first()

    context = {
        "row": blog,
        "blog_id": blog_id
    }
    # print("context", context)
    return render(request, 'blog_edit.html', context)