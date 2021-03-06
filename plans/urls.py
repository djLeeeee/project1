from django.urls import path
from . import views

app_name = 'plans'

urlpatterns = [
    # main - 전체 페이지 조회
    path('', views.index, name='index'),

    # 30일 이후의 약속 조회
    path('coming/', views.plan_coming, name='plan_coming'),
    
    
    # 아래는 볼 필요 없음!!
    # 해당 날짜의 전체 약속 조회
    path('<int:month>/<int:day>/', views.plan_date, name='plan_date'),

    # 해당 약속 조회
    path('<int:pk>/detail/', views.plan_detail, name='plan_detail'),

    # 약속 추가
    path('create/', views.plan_create, name='plan_create'),

    # 약속 삭제
    path('<int:pk>/delete/', views.plan_delete, name='plan_delete'),

    # 약속 수정
    path('<int:pk>/update/', views.plan_update, name='plan_update'),

    # 댓글 작성
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),

    # 댓글 삭제
    path('<int:plan_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

    # 참가(좋아요) 버튼
    path('<int:plan_pk>/join_users/', views.join_users, name='join_users'),
]
