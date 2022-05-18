from django.shortcuts import get_object_or_404, render
from .models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

def Likeview(request, pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False 
    else:
        post.likes.add(request.user) 
        liked = True
    return HttpResponseRedirect(reverse('blog:article-detail', args=[str(pk)]))

class ListPostsView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    
class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post' 

    def get_context_data(self, **kwargs):
        total = get_object_or_404(Post,id=self.kwargs['pk'])
        
        liked = False
        if total.likes.filter(id=self.request.user.id).exists():
            liked = True
    
        total_likes = total.total_likes()
        context = super(DetailPostView,self).get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

class AddPostView(CreateView):
    model = Post 
    template_name = 'add_post.html'
    fields = ['title','description','body','img','category']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPostView, self).form_valid(form)
    

class UpdatePostView(UpdateView):
    model = Post 
    template_name = 'update_post.html'
    fields = ['title','description','body','category']
   

class DeletePostView(DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:posts')
    
#class AddCategoryView(CreateView):
#    model = Category 
#    template_name = 'add_category.html'
#    fields = '__all__'

#def category(request, cats):
#    category_posts = Post.objects.filter(category=cats)
#    return render(request, 'categories.html', {'category_posts':category_posts})


class AddCommentView(CreateView):
    model = Comment 
    template_name = 'add_comment.html'
    fields = ['name','body']
    
    def get_success_url(self):
        return reverse('blog:article-detail', args=[str(self.kwargs['pk'])])
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super(AddCommentView, self).form_valid(form)
    
    