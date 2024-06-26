from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner',)

    def clean_name(self):
        restricted_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        cleaned_data = self.cleaned_data.get('name')

        for word in cleaned_data.split():
            if word in restricted_words:
                raise forms.ValidationError(f'Нельзя использовать слово "{word}" в названии продукта')

        return cleaned_data

    def clean_description(self):
        restricted_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        cleaned_data = self.cleaned_data.get('description')

        for word in cleaned_data.split():
            if word in restricted_words:
                raise forms.ValidationError(f'Нельзя использовать слово "{word}" в описании продукта')

        return cleaned_data


class ModeratorProductForm(ProductForm):
    class Meta(ProductForm.Meta):
        fields = ('description', 'category', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'is_published' in self.fields:
            is_published_value = self.instance.is_published if self.instance else None
            if is_published_value is False:
                self.fields['is_published'].widget.attrs.update({
                    'class': 'form-check-input',
                    'disabled': 'disabled'
                })

    def clean_description(self):
        cleaned_data = super().clean_description()
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
