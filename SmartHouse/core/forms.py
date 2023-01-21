from django import forms


class Userdatainput(forms.Form):
    text1 = forms.CharField(label='Имя', max_length=15, min_length=2)
    text2 = forms.CharField(label='Фамилия', max_length=20, min_length=2)
    text_username = forms.CharField(label='Имя пользователя', max_length=10, min_length=5)
    text_mail = forms.EmailField(label='Почта', min_length=3)
    num_pass1 = forms.CharField(label='Пароль', min_length=8)
    num_pass2 = forms.CharField(label='Повторите пароль')
    photo = forms.FileField(label='Фотография', required=False)
    text3 = forms.CharField(label='Пожелания, предложения', min_length=3, max_length=10)
    num = forms.IntegerField(label='Оценка', max_value=5, min_value=0, required=False)

    def clean_text(self):
        if "abc" not in self.cleaned_data['text1']:
            raise forms.ValidationError('Похоже вы указали что-то не корректно')
        else:
            raise forms.ValidationError('Похоже вы указали что-то не корректно1')
