from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from project.accounts import views

urlpatterns = [
    url(_(r'^register/$'),
        views.UserRegisterView.as_view(),
        name='register'),
    url(_(r'^login/$'),
        views.UserLoginView.as_view(),
        name='login'),

]
