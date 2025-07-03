from django.urls import path
from . import views

urlpatterns = [

path('design/psds/', views.ads_images_search_view, name="design_home"),

path('design/ps-fonts/', views.DesignerFontsView.as_view(), name="ps_fonts"),
path('design/ps-vector/', views.DesignerMediaView.as_view(), name="ps_vector"),
path('design/upload/ps-vectors/', views.UploadDesignerMediaView.as_view(), name="upload_ps_vec"),
path('design/upload/ps-fonts/', views.UploadDesignerFontsView.as_view(), name="upload_ps_fonts"),
# path('design/ps-fonts/', views.get_ps_fonts, name="ps_fonts"),

path('design/create/vec-category/', views.CreateDesignerMediaCategoryView.as_view(), name="create_ps_vec_cat"),
path('design/create/tags/', views.CreateAdKrityTagMasterView.as_view(), name="create_tags"),
]