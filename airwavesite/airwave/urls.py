# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:04:05 2019

@author: Ullampuzha.Nizar
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



app_name = 'airwave'
urlpatterns = [
    # ex: /polls/
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('start/',views.start, name='start'),
    path('upload/<str:filetype>/', views.UploadView.upload, name='upload'),    
    path('employee/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/list/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('tariffplan/add/', views.TariffplanCreateView.as_view(), name='tariffplan_add'),
    path('tariffplan/list/', views.TariffplanListView.as_view(), name='tariffplan_list'),
    path('tariffplan/<int:pk>/', views.TariffplanUpdateView.as_view(), name='tariffplan_edit'),
    path('tariffplan/delete/<int:pk>/', views.TariffplanDeleteView.as_view(), name='tariffplan_delete'),
    path('config/add/', views.AirwaveconfigCreateView.as_view(), name='airwaveconfig_add'),
    path('config/list/', views.AirwaveconfigListView.as_view(), name='airwaveconfig_list'),
    path('config/<int:pk>/', views.AirwaveconfigUpdateView.as_view(), name='airwaveconfig_edit'),
    path('config/delete/<int:pk>/', views.AirwaveconfigDeleteView.as_view(), name='airwaveconfig_delete'),
    path('area/add/', views.AreaCreateView.as_view(), name='area_add'),
    path('area/list/', views.AreaListView.as_view(), name='area_list'),
    path('area/<int:pk>/', views.AreaUpdateView.as_view(), name='area_edit'),
    path('area/delete/<int:pk>/', views.AreaDeleteView.as_view(), name='area_delete'),
    path('operator/add/', views.OperatorCreateView.as_view(), name='operator_add'),
    path('operator/list/', views.OperatorListView.as_view(), name='operator_list'),
    path('operator/<int:pk>/', views.OperatorUpdateView.as_view(), name='operator_edit'),
    path('operator/delete/<int:pk>/', views.OperatorDeleteView.as_view(), name='operator_delete'),
    path('customer/add/', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customer/list/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('customerplan/add/<int:customer>', views.CustomerplanCreateView.as_view(), name='customerplan_add'),
    path('customerplan/list/', views.CustomerplanListView.as_view(), name='customerplan_list'),    
    #path('customerplan/list/search', views.CustomerplanListView.search, name='customerplan_search'),
    path('customerplan/<int:pk>/', views.CustomerplanUpdateView.as_view(), name='customerplan_edit'),
    path('customerplan/delete/<int:pk>/', views.CustomerplanDeleteView.as_view(), name='customerplan_delete'),

    path('customeruserid/add/<int:customer>', views.CustomerUseridCreateView.as_view(), name='customeruserid_add'),
    path('customeruserid/list/', views.CustomerUseridListView.as_view(), name='customeruserid_list'),  
    path('customeruserid/<int:pk>/', views.CustomerUseridUpdateView.as_view(), name='customeruserid_edit'),
    path('customeruserid/delete/<int:pk>/', views.CustomerUseridDeleteView.as_view(), name='customeruserid_delete'),

    path('payments/add/<int:customer>', views.PaymentsCreateView.as_view(), name='payments_add'),
    path('payments/list/', views.PaymentsListView.as_view(), name='payments_list'),  
    path('payments/<int:pk>/', views.PaymentsUpdateView.as_view(), name='payments_edit'),
    path('payments/delete/<int:pk>/', views.PaymentsDeleteView.as_view(), name='payments_delete'),

#    path('collections/add/', views.AirwaveCollectionCreateView.as_view(), name='airwavecollection_add'),
    path('collections/add/<int:customer>', views.AirwaveCollectionCreateView.as_view(), name='airwavecollection_add'),
    path('collections/list/', views.AirwaveCollectionListView.as_view(), name='airwavecollection_list'),  
    path('collections/<int:pk>/', views.AirwaveCollectionUpdateView.as_view(), name='airwavecollection_edit'),
    path('collections/delete/<int:pk>/', views.AirwaveCollectionDeleteView.as_view(), name='airwavecollection_delete'),





    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
