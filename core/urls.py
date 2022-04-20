from django.urls import path
from core import views
# render_pdf_view from view in commended (it was for testing purpose)
from .views import ClientListView, client_render_pdf_view

# app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('client_info/<int:id>/', views.client_info, name="client_info"),
    
    path('pdf/', ClientListView.as_view(), name='client-list-view'),
    # path('test/', render_pdf_view, name='test-view'),
    path('pdf/<pk>', client_render_pdf_view, name='client-pdf-view'),

    
]
