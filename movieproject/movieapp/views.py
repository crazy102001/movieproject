from django.shortcuts import render
from django.urls import reverse_lazy
from movieapp.models import movieapp
from movieapp.forms import Movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# def home(request):
#     m=movieapp.objects.all()
#     return render(request,'home.html',{'m':m})

class HomeView(ListView):
    model=movieapp
    template_name="home.html"
    context_object_name='m'


# def detail(request,n):
#     m=movieapp.objects.get(id=n)
#     return render(request,'detail.html',{'m':m})

class Detail(DetailView):
    model=movieapp
    template_name="detail.html"
    context_object_name='m'

# def add(request):
#
#     if(request.method=='POST'):
#
#         form=Movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#
#     form=Movieform()
#     return render(request,'add.html',{'form':form})


class AddMovie(CreateView):
    model = movieapp
    template_name = "add.html"
    fields = ['title','desc','year','image']
    success_url = reverse_lazy('movieapp:home')

# def delete(request,n):
#     s=movieapp.objects.get(id=n)
#     s.delete()
#     return home(request)

class Delete(DeleteView):
    model=movieapp
    template_name="delete.html"
    success_url=reverse_lazy('movieapp:home')
# def update(request,n):
#     s=movieapp.objects.get(id=n)
#     if (request.method == 'POST'):
#
#         form = Movieform(request.POST, request.FILES,instance=s)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form = Movieform(instance=s)
#     return render(request, 'update.html', {'form': form})

class Update(UpdateView):
    model=movieapp
    template_name= "update.html"
    fields = ['title', 'desc', 'year', 'image']
    success_url = reverse_lazy('movieapp:home')
