# from backend.apps.people.models import People, PeopleImage
# from django.forms import (
#     ModelForm, TextInput,
#     DateTimeInput, Textarea,
#     ClearableFileInput, NumberInput,
#     DateInput, SelectMultiple
# )
#
#
# class PeopleForm(ModelForm):
#     class Meta:
#         model = People
#         fields = '__all__'
#         widgets = {
#             "inn": NumberInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'ИНН'
#             }),
#             "last_name": TextInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Фамилия',
#             }),
#             "first_name": TextInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Имя'
#             }),
#             "middle_name": TextInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Отчество'
#             }),
#             "city": SelectMultiple(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Город'
#             }),
#             "address": TextInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Адрес'
#             }),
#             "date": DateInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'data-date-format': 'mm/dd/yyyy',
#                 'placeholder': 'ММ/ДД/ГГГГ',
#                 'readonly': 'readonly',
#             }),
#             "nationality": TextInput(attrs={
#                 'class': 'u-input u-input-rectangle',
#                 'placeholder': 'Национальность'
#             }),
#             "image": ClearableFileInput(attrs={
#                 'class': 'u-btn u-btn-primary',
#                 'placeholder': 'Фото',
#             }),
#             "file": ClearableFileInput(attrs={
#                 'class': 'u-btn u-btn-primary',
#                 'placeholder': 'Файл',
#             }),
#         }
