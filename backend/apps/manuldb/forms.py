from backend.apps.weapons.models import Weapons

from django.forms import (
    ModelForm, TextInput,
    DateTimeInput, Textarea,
    FileInput, ImageInput,
    DecimalInput, DateInput,)


class WeaponsForm(ModelForm):
    class Meta:
        model = Weapons
        fields = '__all__'

        widgets = {
            "first_name": TextInput(attrs={

                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={

                'placeholder': 'Фамилия'
            }),
            "middle_name": TextInput(attrs={

                'placeholder': 'Отчество'
            }),
            "inn": DecimalInput(attrs={

                'placeholder': 'ИНН'
            }),
            "adress": TextInput(attrs={

                'placeholder': 'Адрес'
            }),
            "city": TextInput(attrs={

                'placeholder': 'Город'
            }),
            "age": DateInput(attrs={

                'placeholder': 'Отчество'
            }),
            "title": TextInput(attrs={

                'placeholder': 'Модель оружии'
            }),
            "code": TextInput(attrs={

                'placeholder': 'Серийный Номер'
            }),
            "description": TextInput(attrs={

                'placeholder': 'Примичание'
            }),
            "initiator": TextInput(attrs={

                'placeholder': 'ФИО Иницатора'
            }),
            "rank": TextInput(attrs={

                'placeholder': 'Звание'
            }),
            "organ": TextInput(attrs={

                'placeholder': 'ГОС орган'
            }),

        }