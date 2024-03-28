from django.urls import path
from users.api.views import RegisterView, LoginView

from users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', LoginView.as_view(), name="login"),
]
