from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # this line of code filters the database based on some criteria and stores the result in a variable
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})