from django.urls import path
from ResColl import views

urlpatterns=[
    #path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logged_out.html')),
    #path('accounts/login/', auth_views.LogoutView.as_view(template_name='login.html')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('form_1/',views.form_dispatch(1),name='form1'),
    path('form_2/',views.form_dispatch(2),name='form2'),
    path('form_3/',views.form_dispatch(3),name='form3'),
    path('after/',views.form_filled,name='form_f'),
    path('fetch/',views.fetch_new_records,name='fetch')
    ]
