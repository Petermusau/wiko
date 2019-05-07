from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Member

# Create your views here.
class MemberListView(ListView):
    model =Member
    template_name ='girl/index.html'
    context_object_name = 'profiles'

class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'
class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'
class MemberDeleteView(DeleteView):
    model =Member
    success_url =  '/'