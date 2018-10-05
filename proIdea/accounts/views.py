from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from . import forms
from django.views.generic import CreateView
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
 # signup view
class SignUp(CreateView):

	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.is_active = True
			user.save()
			send_mail("Subject","Message",settings.EMAIL_HOST_USER,[form.cleaned_data.get('email')],fail_silently=False)
			return HttpResponseRedirect(reverse_lazy('login'))
			# return redirect(reverse_lazy('login'))
			# return render(request,'accounts/signup.html',{'forms':form})

		else:
			return  render(request,self.template_name,{'forms':form})


