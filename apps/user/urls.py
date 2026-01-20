from django.urls import path

from apps.user.views import UserListCreateView, BlockUserView, UnblockUserView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='user_block'),
    path('/<int:pk>/unblock', UnblockUserView.as_view(), name='user_unblock'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),

]