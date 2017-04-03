from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PortalForm, RegisterForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
#from django.template.defaulttags import csrf_token
#from django.views.decorators.csrf import requires_csrf_token
from .models import Student
from .forms import PortalForm
import logging

logr = logging.getLogger(__name__)

def welcome(request):
    language = 'en-gb'
    session_language = 'en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    students = Student.objects.all()
    args = {}
    args['students'] = Student.objects.all()
    args['language'] = language
    return render(request, 'index1.htm', {'students': students, 'language': language, 'session_language': session_language})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.htm', {'student': student})

def language(request, language='en-gb'):
    response = HttpResponse("Setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response

def login(request):
    c={}
    return render(request, 'login.htm',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/wifi/loggedin/')
    else:
        return HttpResponseRedirect('/wifi/invalid/')

def loggedin(request):
    return render(request, 'loggedin.htm')

def invalid(request):
    return render(request, 'invalid.htm')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.htm')

def wifi_registration(request):
    if request.method == 'POST':
        form = PortalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wifi/thanks/')
    else:
        form = PortalForm()
    args = {}
    args['form'] = form
    return render(request, 'formindex.htm', args)

def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wifi/register_success/')
    args = {}
    args['form'] = UserCreationForm()
    print args
    return render(request, 'register.htm', args)

def register_success(request):
    return render(request, 'register_success.htm')

def thanks(request):
    return render(request, 'thanks.htm')

def search_students(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    students = Student.objects.filter(name__contains=search_text)
    return render(request, 'ajax_search.htm', {'students': students})
