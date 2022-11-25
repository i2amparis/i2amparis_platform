from django.urls import path

from . import views

urlpatterns = [
    path('show_line_chart', views.show_line_chart, name='show_line_chart'),
    path('show_column_chart', views.show_column_chart, name='show_column_chart'),
    path('show_pie_chart', views.show_pie_chart, name='show_pie_chart'),
    path('show_radar_chart', views.show_radar_chart, name='show_radar_chart'),
    path('show_range_chart', views.show_range_chart, name='show_range_chart'),
    path('show_bar_range_chart', views.show_bar_range_chart, name='show_bar_range_chart'),
    path('show_stacked_column_chart', views.show_stacked_column_chart, name='show_stacked_column_chart'),
    path('show_stacked_column_line_chart', views.show_stacked_column_line_chart, name='show_stacked_column_line_chart'),
    path('show_stacked_clustered_column_chart', views.show_stacked_clustered_chart,
         name='show_stacked_clustered_chart'),
    path('show_dumbell_chart', views.show_dumbell_chart, name='show_dumbell_chart'),
    path('show_heat_map_chart', views.show_heat_map_chart, name='heat_map_chart'),
    path('show_bar_heat_map_chart', views.show_bar_heat_map, name='show_bar_heat_map_chart'),
    path('show_sankey_diagram', views.sankey_diagram, name='sankey_diagram'),
    path('show_chord_diagram', views.chord_diagram, name='chord_diagram'),
    path('show_heat_map', views.heat_map_on_map, name='heat_map'),
    # path('parallel_coordinates_chart', views.parallel_coordinates_chart, name='parallel_coordinates_chart'),
    # path('thermometer_chart', views.thermometer_chart, name='thermometer_chart'),
    # path('parallel_coordinates_chart2', views.parallel_coordinates_chart2, name='parallel_coordinates_chart2')

]
