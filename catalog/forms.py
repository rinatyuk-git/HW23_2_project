from django import forms
from django.db.models import BooleanField
from django.forms import ModelForm

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "product_name",
            "product_info",
            "product_image",
            "category",
            "product_price",
        )
        # '__all__'

    exceptions = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_product_name(self):
        cleaned_data = self.cleaned_data["product_name"]
        for exception in self.exceptions:
            if exception in cleaned_data.lower():
                raise forms.ValidationError(f"Это слово //{exception}// не применимо")
        return cleaned_data

    def clean_product_info(self):
        cleaned_data = self.cleaned_data["product_info"]
        for exception in self.exceptions:
            if exception in cleaned_data.lower():
                raise forms.ValidationError(f"Это слово //{exception}// не применимо")
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "is_published",
            "product_info",
            "category",
        )


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
