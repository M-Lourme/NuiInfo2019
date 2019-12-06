from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.test, name='test'),
    path('aide_sociale/', views.aide_sociale, name='aide_sociale'),
    path('aides/', views.aides, name='aides'),
    path('baisse_apl/', views.baisse_apl, name='baisse_apl'),
    path('conditions_vie/', views.conditions_vie, name='conditions_vie'),
    path('difficultes/', views.difficultes, name='difficultes'),
    path('precarite/', views.precarite, name='precarite'),
    path('404',views.page_not_found_view, name='erreur')
]
