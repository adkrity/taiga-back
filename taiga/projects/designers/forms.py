from django.forms import ModelForm, ClearableFileInput, FileField
from django import forms

# from utils.form_view import MultipleFileField, MultipleFileInput
from .models import DesignerFontMaster, DesignerMedia, DesignerMediaCategories


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)

class MultipleFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        files = data or []
        cleaned = []
        for f in files:
            cleaned.append(super().clean(f, initial))
        return cleaned


class UploadDesignerFontsForm(ModelForm):
    class Meta:
        model = DesignerFontMaster
        fields = ["name","font_file"]


class DesignerMediaCategoriesForm(ModelForm):
    class Meta:
        model = DesignerMediaCategories
        fields = ["name", "notes"]


class UploadDesignerMediaForm(ModelForm):
    class Meta:
        model = DesignerMedia
        fields = ["category", "image", "media"]


class MultiUploadDesignerMediaForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=DesignerMediaCategories.objects.all(),
        required=True
    )
    images = MultipleFileField(
        required=False,
        label="Image (Jpg or Png)",
        widget=MultipleFileInput(
            attrs={
                'multiple': True,
                'class': 'form-control',
            }
        ),
    )
    medias = MultipleFileField(
        required=False,
        label="Vector (Psd)",
        widget=MultipleFileInput(
            attrs={
                'multiple': True,
                'class': 'form-control',
            }
        ),
    )


class GetDesignerMediaForm(forms.Form):
    # category = forms.ModelChoiceField(
    #     queryset=DesignerMediaCategories.objects.all(),
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     }),
    #     required=False,
    #     label="Select Category"
    # )
    category = forms.ModelMultipleChoiceField(
        queryset=DesignerMediaCategories.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'size': 10,
            'style': 'min-height: 120px;'
        }),
        required=False,
        label="Select Categories"
    )