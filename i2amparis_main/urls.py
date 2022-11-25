from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('main', views.redirect_to_landing),
    path('overview_comparative_assessment_doc', views.overview_comparative_assessment_doc,
         name='overview_comparative_assessment_doc'),
    path('overview_comparative_assessment_doc/global', views.overview_comparative_assessment_doc_global,
         name='overview_comparative_assessment_doc_global'),
    path('overview_comparative_assessment_doc/national_eu', views.overview_comparative_assessment_doc_national_eu,
         name='overview_comparative_assessment_doc_national_eu'),
    path('overview_comparative_assessment_doc/national_oeu', views.overview_comparative_assessment_doc_national_oeu,
         name='overview_comparative_assessment_doc_national_oeu'),
    path('detailed_model_doc', views.detailed_model_doc,
         name='detailed_model_doc'),
    path('detailed_model_doc/<model>', views.detailed_model_doc,
         name='detailed_model_doc_sel_model'),
    path('dynamic_doc/', views.dynamic_doc, name='dynamic_doc'),
    path('dynamic_doc/<str:model>/', views.dynamic_doc, name='dynamic_doc_model'),
    path('contact_form', views.contact_form, name='contact_form'),

    path('pr_wwh/landing', views.paris_reinforce_landing, name='paris_workspace_landing'),
    path('pr_wwh/harmonisation_table', views.paris_reinforce_harmonisation, name='paris_reinforce_harmonisation'),
    path('pr_wwh/scientific_module', views.paris_advanced_scientific_module, name='paris_advanced_scientific_module'),
    path('populate_detailed_analysis_datatables', views.populate_detailed_analysis_datatables,
         name='populate_detailed_analysis_datatables'),
    path('pr_wwh/conclusions', views.gw_public_ui, name='gw_public_ui'),
    path('pr_wwh/virtual_library', views.gw_virtual_library, name='gw_virtual_library'),
    path('pr_wwh/virtual_library/<section>', views.gw_virtual_library,
         name='gw_virtual_library'),

    # path('update_scientific_model_selects_strict', views.update_scientific_model_selects_strict,
    #      name='update_scientific_model_selects_strict'),
    path('update_scientific_model_selects_basic', views.update_scientific_model_selects_basic,
         name='update_scientific_model_selects_basic'),
    path('get_sdg_variables', views.get_sdg_variables, name='get_sdg_variables'),

    path('rrf_policy_intro', views.rrf_landing, name='rrf_landing'),
    path('populate_rrf_policy_datatables', views.populate_rrf_policy_datatables,
         name='populate_rrf_policy_datatables'),

    path('eu_wwh/landing', views.eu_workspace_landing, name='euw_landing'),
    path('eu_wwh/scientific_module', views.euw_scientific_module, name='euw_scientific_module'),
    path('eu_wwh/conclusions', views.euw_public_ui, name='euw_public_ui'),
    path('eu_wwh/harmonisation_table', views.euw_harmonisation, name='euw_harmonisation'),
    path('eu_wwh/virtual_library', views.euw_virtual_library, name='euw_virtual_library'),
    path('eu_wwh/virtual_library/<section>', views.euw_virtual_library,
         name='euw_virtual_library'),
    path('covid/landing', views.covid_workspace_landing, name='covid_landing'),
    path('covid/scientific_module', views.covid_scientific_module, name='covid_scientific_module'),
    path('covid/covid_public_ui', views.covid_public_ui, name='covid_public_ui'),
    path('feasibility/scientific_module', views.feasibility_scientific_module, 
     name='feasibility_scientific_module'),
    path('feasibility/back_to_landing', views.redirect_to_landing),
    path('ida/public_module', views.ida_public_ui, name='ida_public_ui'),
    path('ida/back_to_landing', views.redirect_to_landing),
]
