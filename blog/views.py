from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/new.html"
    #fields = '__all__'
    fields  = ['title', 'author', 'body']
    success_url = reverse_lazy('home')
    '''
    새로운 블로그를 생성이 성공했을때 이동하는 것은 모델에 설정하고 get_absolute_url(), 왜? 새로 등록된 블로그를 보여주려고 하니깐 pk를 알아야 한다. 
    기존 블로그를 지우는 것은 바로 home으로 가면 되니깐 success_url을 이용한다. 

    그렇다면 만일 블로그 생성에서 success_url을 설정하면 어찌 되나?
    실험해보니 새로 등록하고 바로 home으로 잘 이동한다. 
    update에서도 success_url을 등록해 놓으면 잘 업데이트 되면 get_absolute_url()을 사용하지 않고 sucess_url로 이동하게 된다. 
    '''

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/edit.html"
    fields  = ['title', 'body']    
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete.html"
    success_url = reverse_lazy('home')