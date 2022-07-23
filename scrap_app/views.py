from django.shortcuts import render


# Create your views here.

def blog_list(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')
    print("query:", query, sort)
    return render(request, 'blog-list.html')
