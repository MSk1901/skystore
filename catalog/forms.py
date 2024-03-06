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
        exclude = ('created_at', 'updated_at',)

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


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_current(self):
        cleaned_data = self.cleaned_data.get('is_current')
        product = self.cleaned_data.get('product')

        if cleaned_data and product.versions.filter(is_current=True).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Текущая версия может быть только одна')
        return cleaned_data
