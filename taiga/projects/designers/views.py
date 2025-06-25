from django.db.models import Max, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.db.models.fields.json import KeyTextTransform
from django.db.models import Func,Value,F,TextField

from settings.constants import ADKRITY_PROJECT_ID, CUSTOM_ATTRIBUTE_IDS
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
from taiga.base.api.views import APIView
from taiga.base.api.permissions import AllowAny
from taiga.base.utils.date import *
# from utils.field_definations import get_random_obj_list
# from utils.form_view import InternalFormView

from taiga.projects.designers.forms import UploadDesignerFontsForm, DesignerMediaCategoriesForm, GetDesignerMediaForm, \
    MultiUploadDesignerMediaForm
from taiga.projects.designers.functions import get_random_obj_list, success_json_response
from taiga.projects.designers.models import DesignerFontMaster, DesignerMedia, DesignerMediaCategories
from taiga.projects.designers.serializers import GetAdImageSerializer
from taiga.projects.userstories.models import UserStory
from taiga.users.models import User
from taiga.projects.custom_attributes.models import UserStoryCustomAttribute, UserStoryCustomAttributesValues

from taiga.base.api.fields import IntegerField
from taiga.users.models import Role


class DesignerFontsView(APIView):
    permission_classes = (AllowAny,)
    template_name = 'designer-fonts.html'

    def get(self, request):
        fonts = DesignerFontMaster.objects.filter(is_active=True)
        context = {
            "var": "Hello from PS Fonts!",
            "fonts": fonts,
        }
        return render(request, self.template_name, context)


class UploadDesignerFontsView(APIView):
    permission_classes = (AllowAny,)
    template_name = 'designer-form.html'
    form_class = UploadDesignerFontsForm
    title = "Upload PhotoShop Fonts"
    success_message = "Font Added Successfully!"
    submit_button_name = "Upload"

    # def on_form_valid(self, request, post_data):
    #     print('on_form_valid', self.__class__.__name__, post_data)
    #
    #     form = self.form_class(post_data, request.FILES)
    #     form.save()
    #     self.context = {
    #         "redirect_url": 'ps_fonts',
    #     }
    #     return self.success_message, True

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     if hasattr(self, 'context'):
    #         return redirect(self.context['redirect_url'])
    #     return response


    def get(self, request):
        form = self.form_class()
        context = {
            "title": self.title,
            "button_text": self.submit_button_name,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        post_data = request.POST
        print('post', self.__class__.__name__, post_data)

        form = self.form_class(post_data, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect("ps_fonts")

        return render(request, self.template_name, {
            "title": self.title,
            "button_text": self.submit_button_name,
            "form": form,
        })


class CreateDesignerMediaCategoryView(APIView):
    permission_classes = (AllowAny,)
    template_name = 'designer-vector-categories.html'
    form_class = DesignerMediaCategoriesForm
    title = "Create PhotoShop Vector Categories"
    success_message = "Vector Category Added Successfully!"
    submit_button_name = "Create"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['existing_categories'] = DesignerMediaCategories.objects.filter(is_active=True).order_by('name')
    #     return context
    #
    # def on_form_valid(self, request, cleaned_data, **kwargs):
    #     print('on_form_valid', self.__class__.__name__, cleaned_data)
    #
    #     try:
    #         new_category = DesignerMediaCategories.objects.create(
    #             name=cleaned_data['name'],
    #             notes=cleaned_data['notes']
    #         )
    #         return f"Category '{new_category.name}' created successfully!", True
    #     except Exception as e:
    #         return f"Error creating category: {str(e)}", False

    def get(self, request):
        form = self.form_class()
        existing_categories = DesignerMediaCategories.objects.filter(is_active=True).order_by('name')
        context = {
            "title": self.title,
            "button_text": self.submit_button_name,
            "existing_categories": existing_categories,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        post_data = request.POST
        print('post', self.__class__.__name__, post_data)

        form = self.form_class(post_data)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect("create_ps_vec_cat")

        return render(request, self.template_name, {
            "title": self.title,
            "button_text": self.submit_button_name,
            "form": form,
        })


class UploadDesignerMediaView(APIView):
    permission_classes = (AllowAny,)
    template_name = 'designer-form.html'
    # form_class = UploadDesignerMediaForm
    form_class = MultiUploadDesignerMediaForm # multiple files upload
    title = "Upload PhotoShop Vector"
    success_message = "Vector Added Successfully!"
    submit_button_name = "Upload"
    success_url = 'ps_vector'

    # def on_form_valid(self, request, post_data):
    #     print('on_form_valid', self.__class__.__name__, post_data)
    #     form = self.form_class(post_data, request.FILES)
    #     form.save()
    #     self.context = {
    #             "redirect_url": 'ps_vector',
    #     }
    #     return self.success_message, True

        # form = self.form_class(post_data, request.FILES)
        # if form.is_valid():
        #     form = form.save()
        #     self.context = {
        #         "redirect_url": 'ps_vector',
        #     }
        # return self.success_message, True


    # def on_form_valid(self, request, post_data):
    #     print('on_form_valid', self.__class__.__name__, post_data)
    #     form = self.form_class(post_data, request.FILES)
    #     if not form.is_valid():
    #         return "There was a problem with your upload.", False
    #
    #     category = form.cleaned_data['category']
    #     images   = request.FILES.getlist('images')
    #     medias   = request.FILES.getlist('medias')
    #
    #     if len(images) != len(medias):
    #         return "Please select the same number of preview images and media files.", False
    #
    #     for img_file, media_file in zip(images, medias):
    #         DesignerMedia.objects.create(category= category,image = img_file,media = media_file, media_type = None)
    #
    #     self.context = {
    #         "redirect_url": 'ps_vector',
    #     }
    #     return self.success_message, True

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     if hasattr(self, 'context'):
    #         return redirect(self.context['redirect_url'])
    #     return response

    def get(self, request):
        form = self.form_class()
        context = {
            "title": self.title,
            "button_text": self.submit_button_name,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        post_data = request.POST
        print('post', self.__class__.__name__, post_data)

        form = self.form_class(post_data, request.FILES)
        if not form.is_valid():
            messages.error(request, "There was a problem with your upload.")
            return redirect("upload_ps_vec")

        category = form.cleaned_data['category']
        images   = request.FILES.getlist('images')
        medias   = request.FILES.getlist('medias')

        if len(images) != len(medias):
            return redirect("upload_ps_vec")

        for img_file, media_file in zip(images, medias):
            DesignerMedia.objects.create(category= category,image = img_file,media = media_file, media_type = None)

        return redirect("ps_vector")


class DesignerMediaView(APIView):
    permission_classes = (AllowAny,)
    template_name = 'designer-vector.html'
    form_class = GetDesignerMediaForm
    title = "Select PhotoShop Vector Category"
    submit_button_name = "Search"

    # def on_form_valid(self, request, cleaned_data, **kwargs):
    #     print('on_form_valid', self.__class__.__name__, cleaned_data)
    #     return "Category selected successfully", True

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['vectors'] = []
    #
    #     if self.request.method == 'POST' and 'category' in self.request.POST:
    #         form = self.form_class(self.request.POST)
    #         if form.is_valid():
    #             category = form.cleaned_data.get('category')
    #             if category:
    #                 # Filter vectors by the selected category
    #                 vectors = DesignerMedia.objects.filter(category_id__in=category, deleted=False)
    #                 context['vectors'] = vectors
    #                 context['selected_category'] = category
    #
    #     return context

    def get(self, request):
        form = self.form_class()
        existing_categories = DesignerMediaCategories.objects.filter(is_active=True).order_by('name')
        context = {
            "title": self.title,
            "button_text": self.submit_button_name,
            "existing_categories": existing_categories,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        post_data = request.POST
        print('post', self.__class__.__name__, post_data)
        category = post_data.get('category')
        return render(request, self.template_name, {
            "title": self.title,
            "form": self.form_class(request.POST),
            "button_text": self.submit_button_name,
            "vectors": DesignerMedia.objects.filter(category_id__in=category, deleted=False),
            "selected_category": category,
        })


def ads_images_search_view(request, business_wise=False):
    ALL_IN_FILTER = ["videos", "images", "category", "caption", "name"]

    query_params = request.GET
    print(query_params)
    search_query = query_params.get('q', None)
    business_id = query_params.get('b_id', None)
    ad_id = query_params.get('ad_id', None)
    time_period = query_params.get('time_period', None)
    # selected_designer = query_params.get('designer', None)
    selected_designer = query_params.getlist('designer[]')
    get_json = query_params.get('json', False)

    in_filter = query_params.getlist('in[]', ALL_IN_FILTER)

    category_filter = query_params.getlist('category[]', None)
    if not category_filter and query_params.get('category'):
        category_filter = query_params.get('category', None)
        if category_filter:
            category_filter = category_filter.split(',')

    print(search_query, in_filter, category_filter)

    list_for_ads = True
    page_size = 30
    if "psd" in request.get_full_path():
        list_for_ads = False
        page_size = 100

    if get_json:
        page_size = 50

    template = loader.get_template('ads-image-portfolio.html')
    designers_role = Role.objects.filter(project_id=ADKRITY_PROJECT_ID, name="Design").last()

    designers = User.objects.filter(memberships__project_id=ADKRITY_PROJECT_ID,memberships__role=designers_role).distinct()
    print(designers, "designers list")

    context = {}
    context["designers_list"] = designers

    # self_design_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID, name__iexact="We need to create design").last()
    self_design_userstory = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(CUSTOM_ATTRIBUTE_IDS["we_need_to_create_design"]): True}).values_list("user_story_id",flat=True)

    initial_queryset = UserStory.objects.filter(project_id=ADKRITY_PROJECT_ID, id__in=self_design_userstory).exclude(status_id__in=[1,3,4,5,6,7]).order_by('-id')

    final_queryset = UserStory.objects.none()

    # business_cat_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact="Category").last()
    if business_wise:
        if not category_filter and not search_query:
            category_filter = ["Other"]

    if ad_id and not search_query:
        print('ad_id', ad_id, category_filter)
        # ad_id_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact="Ad Id").last()
        ad_attribute_values = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(CUSTOM_ATTRIBUTE_IDS["ad_id"]): int(ad_id)}).last()
        # us_category = ad_attribute_values["attribute_values"][f"{business_cat_custom_attribute.id}"]
        us_category = ad_attribute_values.attributes_values.get(str(CUSTOM_ATTRIBUTE_IDS["category"])) if ad_attribute_values else None
        us_with_same_cat = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(CUSTOM_ATTRIBUTE_IDS["category"]): us_category}).values_list("user_story_id", flat=True)

        final_queryset = initial_queryset.filter(id__in=us_with_same_cat)

    if search_query:
        search_query = search_query.strip()

        # FILTER_CUSTOM_ATTR_MAP_IDS = {
        #     "caption": "Caption",
        #     "category": "Category",
        #     "company_name": "Company Name",
        # }
        FILTER_CUSTOM_ATTR = ["caption","category","company_name"]
        if in_filter:
            for filter in in_filter:
                if filter not in FILTER_CUSTOM_ATTR:
                    continue

                # attr = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact=FILTER_CUSTOM_ATTR_MAP_IDS[filter]).last()
                # if not attr:
                #     continue
                # attr_key = str(attr.id)

                us_qs = UserStoryCustomAttributesValues.objects.annotate(
                    json_val=Func(F("attributes_values"), Value(str(CUSTOM_ATTRIBUTE_IDS[filter])), function="jsonb_extract_path_text",
                                  output_field=TextField())).filter(
                    json_val__icontains=search_query).values_list("user_story_id", flat=True).distinct()

                final_queryset |= initial_queryset.filter(id__in=us_qs)

    if time_period:
        final_queryset = final_queryset
        if not search_query:
            final_queryset = initial_queryset
        if time_period == "today":
            final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-1))[0])
        elif time_period == "week":
            final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-8))[0])
        elif time_period == "month":
            final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-30))[0])
        elif time_period == "quarter":
            final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-90))[0])
        elif time_period == "latest":
            final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-6))[0])


    if category_filter:
        if not search_query:
            final_queryset = initial_queryset

        category_us = UserStoryCustomAttributesValues.objects.annotate(
            category_name=Func(F("attributes_values"), Value(f"{str(CUSTOM_ATTRIBUTE_IDS['category'])}"),
                               function="jsonb_extract_path_text",
                               output_field=TextField())).filter(category_name__in=category_filter).values_list(
            "user_story_id", flat=True)
        final_queryset = final_queryset.filter(id__in=category_us)
        print('category_filter', final_queryset.count())



    if business_wise:
        print('business_wise')
        page_size = 1000
        # business_id_custom_attribute = UserStoryCustomAttribute.objects.filter(name__iexact="Business Id").last()

        last_us_for_business = UserStoryCustomAttributesValues.objects.annotate(
            business_id=Func(F("attributes_values"), Value(f"{str(CUSTOM_ATTRIBUTE_IDS['business_id'])}"),
                             function="jsonb_extract_path_text", output_field=IntegerField())).values(
            "business_id").annotate(last_us=Max("user_story_id")).values_list("last_us", flat=True)
        final_queryset = UserStory.objects.filter(id__in=last_us_for_business)

    if business_id:
        # business_id_custom_attribute = UserStoryCustomAttribute.objects.filter(name__iexact="Business Id").last()
        business_wise_us = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains={str(CUSTOM_ATTRIBUTE_IDS['business_id']):int(business_id)}).values_list("user_story_id",flat=True)
        final_queryset = UserStory.objects.filter(id__in=business_wise_us)

    if ad_id:
        print('ad_id before', final_queryset.count())
        # ad_obj = AdMaster.objects.get(id=ad_id)
        # final_queryset = initial_queryset.filter(business__category=ad_obj.business.category_id)
        # todo exclude used template ids

        print('ad_id', ad_id, final_queryset.count())

    if selected_designer:
        if not search_query:
            final_queryset = initial_queryset
        final_queryset = final_queryset.filter(assigned_users__id__in=selected_designer)

    final_queryset = final_queryset.annotate(attachments_count=Count('final_attachments')).filter(attachments_count__gt=0)

    if business_id:
        random_list = final_queryset.all()
    else:
        random_list = get_random_obj_list(final_queryset, size=page_size)

    print('random_list', random_list)
    list_of_ads = GetAdImageSerializer(random_list, many=True).data

    if get_json:
        return success_json_response(list_of_ads)

    if not search_query and not business_wise and not business_id and not ad_id:
        return HttpResponse(template.render(context, request))

    context['ads'] = list_of_ads
    context['q'] = search_query or ""
    context['in'] = in_filter
    context['b_id'] = business_id
    context['ad_id'] = ad_id
    context['category_list'] = []
    context['designers_list'] = designers
    context['list_for_ads'] = list_for_ads
    context['time_period'] = time_period
    context['selected_designer'] = selected_designer

    if final_queryset.count() > 0:
        available_categories = UserStoryCustomAttributesValues.objects.filter(
            user_story_id__in=final_queryset.values_list('id', flat=True)).annotate(
                    category_val=Func(F("attributes_values"), Value(f"{str(CUSTOM_ATTRIBUTE_IDS['category'])}"), function="jsonb_extract_path_text",
                                  output_field=TextField())).values_list(
            "category_val", flat=True).distinct()
        context["category_list"] = list(set(available_categories)) if available_categories else []

    return HttpResponse(template.render(context, request))


# def ads_images_search_view(request, business_wise=False):
#     # from ads.functions import AdMaster, CategoryMaster
#     # from ads.serializers import GetAdImageSerializer
#
#
#     ALL_IN_FILTER = ["videos", "images", "category", "caption", "name"]
#
#     query_params = request.GET
#
#     print(query_params)
#
#     search_query = query_params.get('q', None)
#     business_id = query_params.get('b_id', None)
#     ad_id = query_params.get('ad_id', None)
#     time_period = query_params.get('time_period', None)
#     selected_designer = query_params.get('designer', None)
#     get_json = query_params.get('json', False)
#
#     in_filter = query_params.getlist('in[]', ALL_IN_FILTER)
#
#     category_filter = query_params.getlist('category[]', None)
#     if not category_filter and query_params.get('category'):
#         category_filter = query_params.get('category', None)
#         if category_filter:
#             category_filter = category_filter.split(',')
#
#     print(search_query, in_filter, category_filter)
#
#     list_for_ads = True
#     page_size = 30
#     if "psd" in request.get_full_path():
#         list_for_ads = False
#         page_size = 100
#
#     if get_json:
#         page_size = 50
#
#     template = loader.get_template('ads-image-portfolio.html')
#     designers_role = Role.objects.filter(project_id=ADKRITY_PROJECT_ID, name="Design").last()
#     designers = Membership.objects.filter(project_id=ADKRITY_PROJECT_ID, role=designers_role).values_list("user", flat=True)
#
#     designers = User.objects.filter(memberships__project_id=ADKRITY_PROJECT_ID,memberships__role=designers_role).distinct()
#     print(designers, "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGWWWWWWWWWWWWWWWW")
#
#     context = {}
#     context["designers_list"] = designers
#
#     self_design_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID, name__iexact="We need to create design").last()
#     self_design_userstory = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(self_design_custom_attribute.id): True}).values_list("user_story_id",flat=True)
#     print(self_design_userstory, "Selfffffffffffff")
#
#     # initial_queryset = AdMaster.objects.filter(design_by_adkrity=True).exclude(status_id__in=[1,9,10]).order_by('-id')
#     initial_queryset = UserStory.objects.filter(project_id=ADKRITY_PROJECT_ID, id__in=self_design_userstory).exclude(status_id__in=[1,3,4,5,6,7]).order_by('-id')
#     print(initial_queryset, "IIIIIIIIIIII")
#
#     # final_queryset = AdMaster.objects.none()
#     final_queryset = UserStory.objects.none()
#
#     business_cat_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact="Category").last()
#     if business_wise:
#         if not category_filter and not search_query:
#             # category_filter = [26]
#             category_filter = ["Other"]
#
#     if ad_id and not search_query:
#         print('ad_id', ad_id, category_filter)
#         # ad_obj = AdMaster.objects.get(id=ad_id)
#         # category_filter = [ad_obj.business.category_id]
#         # final_queryset = initial_queryset.filter(business__category=ad_obj.business.category_id)
#
#         ad_id_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact="Ad Id").last()
#         ad_attribute_values = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(ad_id_custom_attribute.id): ad_id}).values("attribute_values")
#         # business_cat_custom_attribute = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact="Category").last()
#
#         us_category = ad_attribute_values["attribute_values"][f"{business_cat_custom_attribute.id}"]
#         us_with_same_cat = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains= {str(business_cat_custom_attribute.id): us_category}).values_list("user_story", flat=True)
#
#         final_queryset = initial_queryset.filter(id__in=us_with_same_cat)
#     print(final_queryset, "&&&&&&&&&&&&&&")
#
#     if search_query:
#         search_query = search_query.strip()
#         # if in_filter:
#         #     if "category" in in_filter:
#         #         final_queryset = final_queryset | initial_queryset.filter(business__category__name__icontains=search_query).order_by('-id')
#         #         print('category', final_queryset.count())
#         #
#         #     if "caption" in in_filter:
#         #         final_queryset = final_queryset | initial_queryset.filter(caption__icontains=search_query).order_by('-id')
#         #         print('caption', final_queryset.count())
#         #
#         #     if "b_name" in in_filter:
#         #         final_queryset = final_queryset | initial_queryset.filter(business__name__icontains=search_query).order_by('-id')
#         #         print('bname', final_queryset.count())
#
#         CUSTOM_ATTR_MAP = {
#             "caption": "Caption",
#             "category": "Category",
#             "b_name": "Company Name",
#         }
#         if in_filter:
#             for filter in in_filter:
#                 if filter not in CUSTOM_ATTR_MAP:
#                     continue
#
#                 attr = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID,name__iexact=CUSTOM_ATTR_MAP[filter]).last()
#                 if not attr:
#                     continue
#                 print(filter, "FFFFFFFFFFFFFFFFF")
#                 attr_key = str(attr.id)
#                 print(attr_key, "JJJJJJJJJJJJ")
#                 # us_qs = UserStoryCustomAttributesValues.objects.annotate(json_val=KeyTextTransform(str(json_key), "attributes_values")).filter(json_val__icontains=search_query).values_list("user_story_id", flat=True).distinct()
#
#                 us_qs = UserStoryCustomAttributesValues.objects.annotate(
#                     json_val=Func(F("attributes_values"), Value(str(attr_key)), function="jsonb_extract_path_text",
#                                   output_field=TextField())).filter(
#                     json_val__icontains=search_query).values_list("user_story_id", flat=True).distinct()
#
#                 print(us_qs, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
#                 final_queryset |= initial_queryset.filter(id__in=us_qs)
#     print(final_queryset, "searchhhhhh")
#     if time_period:
#         final_queryset = final_queryset
#         if not search_query:
#             final_queryset = initial_queryset
#         if time_period == "today":
#             final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-1))[0])
#         elif time_period == "week":
#             final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-8))[0])
#         elif time_period == "month":
#             final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-30))[0])
#         elif time_period == "quarter":
#             final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-90))[0])
#         elif time_period == "latest":
#             final_queryset = final_queryset.filter(created_date__gt=get_time_range_for_date(get_future_date(-6))[0])
#
#
#     if category_filter:
#         if not search_query:
#             final_queryset = initial_queryset
#
#
#         # category_us = UserStoryCustomAttributesValues.objects.annotate(category_name=KeyTextTransform(str(business_cat_custom_attribute.id), "attributes_values")).filter(category_name__in=category_filter).values_list("user_story_id",flat=True)
#         category_us = UserStoryCustomAttributesValues.objects.annotate(
#             category_name=Func(F("attributes_values"), Value(f"{str(business_cat_custom_attribute.id)}"),
#                                function="jsonb_extract_path_text",
#                                output_field=TextField())).filter(category_name__in=category_filter).values_list(
#             "user_story_id", flat=True)
#         # final_queryset = final_queryset.filter(business__category__in=category_filter)
#         final_queryset = final_queryset.filter(id__in=category_us)
#         print('category_filter', final_queryset.count())
#
#
#
#     if business_wise:
#         print('business_wise')
#         page_size = 1000
#         # max_ad_ids = final_queryset.values('business_id').annotate(last_ad=Max('id')).values_list('last_ad', flat=True)
#         # print('business_wise max_ad_ids', max_ad_ids)
#         # final_queryset = AdMaster.objects.filter(id__in=max_ad_ids)
#         business_id_custom_attribute = UserStoryCustomAttribute.objects.filter(name__iexact="Business Id").last()
#
#         # last_us_for_business = UserStoryCustomAttributesValues.objects.annotate(
#         #     business_id=KeyTextTransform(str(business_id_custom_attribute.id), "attributes_values")).values(
#         #     "business_id").annotate(last_us=Max("user_story_id")).values_list("last_us", flat=True)
#
#         last_us_for_business = UserStoryCustomAttributesValues.objects.annotate(
#             business_id=Func(F("attributes_values"), Value(f"{str(business_id_custom_attribute.id)}"),
#                              function="jsonb_extract_path_text", output_field=IntegerField())).values(
#             "business_id").annotate(last_us=Max("user_story_id")).values_list("last_us", flat=True)
#         final_queryset = UserStory.objects.filter(id__in=last_us_for_business)
#
#     if business_id:
#         # final_queryset = AdMaster.objects.filter(business_id=business_id, status__gte=2).order_by('-id')
#         # final_queryset = initial_queryset.filter(business_id=business_id)
#         business_id_custom_attribute = UserStoryCustomAttribute.objects.filter(name__iexact="Business Id").last()
#         business_wise_us = UserStoryCustomAttributesValues.objects.filter(attributes_values__contains={str(business_id_custom_attribute.id):business_id}).values_list("user_story_id",flat=True)
#         final_queryset = UserStory.objects.filter(id__in=business_wise_us)
#
#     if ad_id:
#         print('ad_id before', final_queryset.count())
#         # ad_obj = AdMaster.objects.get(id=ad_id)
#         # final_queryset = initial_queryset.filter(business__category=ad_obj.business.category_id)
#         # todo exclude used template ids
#
#         print('ad_id', ad_id, final_queryset.count())
#     if selected_designer:
#         if not search_query:
#             final_queryset = initial_queryset
#         final_queryset = final_queryset.filter(assigned_users__id=selected_designer)
#
#     if business_id:
#         random_list = final_queryset.all()
#     else:
#         random_list = get_random_obj_list(final_queryset, size=page_size)
#
#     print('random_list', random_list)
#     list_of_ads = GetAdImageSerializer(random_list, many=True).data
#
#     if get_json:
#         return success_json_response(list_of_ads)
#
#     if not search_query and not business_wise and not business_id and not ad_id:
#         return HttpResponse(template.render(context, request))
#
#     # designers_role = Role.objects.filter(project_id=ADKRITY_PROJECT_ID,name="Design").last()
#     # designers = list(Membership.objects.filter(project_id=ADKRITY_PROJECT_ID, role=designers_role).values_list("user", flat=True))
#     # print(designers, "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGWWWWWWWWWWWWWWWW")
#
#     context['ads'] = list_of_ads
#     context['q'] = search_query or ""
#     context['in'] = in_filter
#     context['b_id'] = business_id
#     context['ad_id'] = ad_id
#     context['category_list'] = []
#     context['designers_list'] = designers
#     context['list_for_ads'] = list_for_ads
#     context['time_period'] = time_period
#     context['selected_designer'] = selected_designer
#     print(final_queryset, "FFFFFFFFFFFFF")
#     if final_queryset.count() > 0:
#
#         # available_categories = final_queryset.values_list('business__category', flat=True).distinct()
#         # available_categories_list = CategoryMaster.objects.filter(id__in=available_categories)
#         # for cat_obj in available_categories_list:
#         #     context['category_list'].append({
#         #         "id": cat_obj.id,
#         #         "name": cat_obj.name,
#         #     })
#
#         # available_categories = UserStoryCustomAttributesValues.objects.filter(
#         #     user_story_id__in=final_queryset.values_list('id', flat=True)).annotate(
#         #     category_val=KeyTextTransform(f"{str(business_cat_custom_attribute.id)}", "attributes_values")).values_list(
#         #     "category_val", flat=True).distinct()
#
#         available_categories = UserStoryCustomAttributesValues.objects.filter(
#             user_story_id__in=final_queryset.values_list('id', flat=True)).annotate(
#                     category_val=Func(F("attributes_values"), Value(f"{str(business_cat_custom_attribute.id)}"), function="jsonb_extract_path_text",
#                                   output_field=TextField())).values_list(
#             "category_val", flat=True).distinct()
#         print(available_categories, "AAAAAAAAAAAAAAAAAAAAAA")
#         context["category_list"] = list(available_categories) if available_categories else []
#
#     return HttpResponse(template.render(context, request))