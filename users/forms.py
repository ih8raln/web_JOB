from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        # , 'surname', 'middle_name'
        fields = ['name', 'surname', 'middle_name', 'email', 'username',
                  'city', 'bio', 'intro', 'image']
                  # 'github', 'linkedin', 'twitter',
                  # 'youtube', 'website']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'middle_name': 'Отчество',
            'email': 'E-mail',
            'username': 'Логин',
            'city': 'Город',
            'bio': 'Описание',
            'image': 'Фото',
            'intro': 'Специальность',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})




class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        labels = {
            'name': 'Имя',
            'email': 'E-mail',
            'subject': 'Тема письма',
            'body': 'Письмо'
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})