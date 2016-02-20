from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from models import Question, Choice

QuestionChoiceFormset = \
  inlineformset_factory(Question, Choice, fields=('choice_text',))

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
