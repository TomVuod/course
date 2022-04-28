import datetime
from django.shortcuts import render
from ResColl.forms import ExerciseForm_1, ExerciseForm_2, ExerciseForm_3
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ResColl.models import Response
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Create your views here.

def form_dispatch(numb):
    @login_required
    def process_form(request):
        form_name="ExerciseForm_"+str(numb)
        student_id=request.user.username
        student=User.objects.get(username=student_id)
        if request.method=="GET":
            last_record=dict()
            if student.response_set.filter(part=numb).count()>0:
                last_record=student.response_set.filter(part=numb).latest('timestamp').__dict__
            form=globals()[form_name](last_record)
        else:
            form=form=globals()[form_name](request.POST)
            resp_dict=dict()
            if form.is_valid():
                for key in form.cleaned_data.keys():
                    resp_dict[key]=form.cleaned_data[key]
                resp_dict['timestamp']=datetime.datetime.now()+datetime.timedelta(hours=1)
                resp_dict['part']=numb
                student.response_set.create(**resp_dict)
                return HttpResponseRedirect('/ResColl/after/')
        return render(request, "response_form.html", context={'form':form,
        'part':numb})
    return process_form


def form_filled(request):
    return render(request, "success_page.html")

class MyLoginView(LoginView):
    def post(self, request):
        return HttpResponse('ok')

def fetch_new_records(request):
    http_res=HttpResponse()
    n=int(request.headers['n'])
    if Response.objects.count()<n:
        http_res.headers['student_id']=''
        return(http_res)
    resp_dict=Response.objects.get(id=n).__dict__
    http_res.headers['timestamp']=resp_dict['timestamp'].replace(microsecond=0).isoformat()
    part=resp_dict['part']
    http_res.headers['part']=part
    form_name="ExerciseForm_"+str(part)
    for key in globals()[form_name].base_fields.keys():
        if resp_dict[key]==None:
            http_res.headers[key]=''
        else:
            http_res.headers[key]=str(resp_dict[key])
    http_res.headers['student_id']= User.objects.get(id=resp_dict['user_id']).username
    http_res.headers['part']=http_res.headers['part']
    print(http_res.headers)
    return(http_res)
