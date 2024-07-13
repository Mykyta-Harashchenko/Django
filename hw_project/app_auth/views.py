from django.shortcuts import render

from django.views import View

from django import forms





class RegisterView(View):

    template_name = 'app_auth/register.html'

    def get(self, request):
        pass

    def post(self, request):
        pass


# Create your views here.
