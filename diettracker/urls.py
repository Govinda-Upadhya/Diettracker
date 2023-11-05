from django.urls import path
from . import views

urlpatterns = [
    path("",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("tracker",views.tracker,name="tracker"),
    path("delete<int:id>",views.delete,name="delete")
]
