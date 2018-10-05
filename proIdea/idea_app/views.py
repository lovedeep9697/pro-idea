from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from idea_app import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from . import forms
# Create your views here.

User = get_user_model()

# view for listing ideas
class ListIdeaView(LoginRequiredMixin,ListView):
	model = models.post
	def get_queryset(self):
		queryset = super(ListIdeaView,self).get_queryset()
		queryset = queryset.filter(user = self.request.user)
		return queryset
	
        
# view for details of idea
class IdeaDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'post_detail'
	model = models.post	
	template_name = "idea_app/post_detail.html"


# view to create new idea
class CreateIdeaView(LoginRequiredMixin,CreateView):
	model = models.post
	fields = ('title','text',)

	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		send_mail("Creates","New idea created",settings.EMAIL_HOST_USER,[self.object.user.email],fail_silently=False)
		return super().form_valid(form)
# view to update existing idea
class IdeaUpdateView(LoginRequiredMixin,UpdateView):
	fields = ('text',)
	model = models.post
# view to delete idea
class IdeaDeleteView(LoginRequiredMixin,DeleteView):
	model = models.post
	success_url = reverse_lazy('idea_app:list')
	def delete(self,request,*args,**kwargs):
		

		send_mail("Deletes"," idea deleted",settings.EMAIL_HOST_USER,[self.request.user.email],fail_silently=False)
		return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

# view to share ideas
@login_required
def share(request,pk):
	form = forms.Sharing()
	model = models.post
	idea = get_object_or_404(model,pk=pk)
	if request.method == 'POST':
		form = forms.Sharing(request.POST)
		if form.is_valid():
			
			  send_mail(idea.title,idea.text,settings.EMAIL_HOST_USER,[form.cleaned_data['email']],fail_silently=False)
			  return HttpResponseRedirect(reverse_lazy('idea_app:list'))


	return render(request,'idea_app/share.html',{'form':form})

	

	
   


	




	










	
