from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'description', 'city', 'kind_of_job', 'specialnost']
		labels = {
			'title': 'Должность',
			'description': 'Описание',
			'city': 'Город',
			'kind_of_job': 'Практика/стажировка/вакансия',
			'specialnost': 'Специальность',
		}