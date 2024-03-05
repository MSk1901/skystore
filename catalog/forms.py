from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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