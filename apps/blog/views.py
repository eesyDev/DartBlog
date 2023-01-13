from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F
# Create your views here.


class HomeListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My first blog'
        return context


class PostByTagListView(ListView):
    model = Tag
    template_name = 'blog/tags_tpl.html'
    context_object_name = 'tags'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return context


class PostByCategoryListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwarg['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])

        return context

