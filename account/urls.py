from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',auth_views.login,name='user_login'),
    url(r'^$', auth_views.login, name='user_login'),
    #url(r'^logout/$',auth_views.logout,name='user_logout'),
    url(r'^logout/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'^register/$',views.register,name='user_register'),
    url(r'^password_change/$',auth_views.password_change,{'post_change_redirect':'/account/password_change_done'},name='password_change'),
    url(r'^password_change_done/$',auth_views.password_change_done,name='password_change_done'),

    url(r'^password_reset/$',auth_views.password_reset,{'template_name':'account/password_reset_form.html',
        'email_template_name':'account/password_reset_email.html',
        'subject_template_name':'account/password_reset_subject.txt',
        'post_reset_redirect':'/account/password_reset_done'},name='password_reset'),
    url(r'^password_reset_done/$',auth_views.password_reset_done,{'template_name':'account/password_reset_done.html'},name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,
        {'template_name':'account/password_reset_confirm.html','post_reset_redirect':'/account/password_reset_complete'},
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$',auth_views.password_reset_complete,
        {'template_name':'account/password_reset_complete.html'},name='password_reset_complete'),
    url(r'^my_information/$',views.myself,name='my_information'),
    url(r'^edit_my_information/$',views.myself_edit,name='edit_my_information'),
    url(r'^my_image/$',views.my_image,name='my_image'),
]