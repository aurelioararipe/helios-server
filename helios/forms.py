"""
Forms for Helios
"""

from django import forms
from models import Election
from widgets import *
from fields import *
from django.conf import settings


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40, help_text='no spaces, will be part of the URL for your election, e.g. my-club-2010')
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':60}), help_text='the pretty name for your election, e.g. My Club 2010 Election')
  description = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="type", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False, help_text='If selected, voter identities will be replaced with aliases, e.g. "V12", in the ballot tracking center')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, help_text='enable this if you want the answers to questions to appear in random order for each voter')
  private_p = forms.BooleanField(required=False, initial=False, label="Private?", help_text='A private election is only visible to registered voters.')
  help_email = forms.CharField(required=False, initial="", label="Help Email Address", help_text='An email address voters should contact if they need help.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="Election Info Download URL", help_text="the URL of a PDF document that contains extra election information, e.g. candidate bios and statements")
  
  # times
  voting_starts_at = SplitDateTimeField(help_text = 'UTC date and time when voting begins',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField(help_text = 'UTC date and time when voting ends',
                                   widget=SplitSelectDateTimeWidget, required=False)

class ScriptForm(forms.Form):
  categorias_eleitores = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':2}), help_text='Informe a quantidade de categorias de eleitores')
  categoria_1 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':10}), help_text='Informe o nome da categoria 1')
  categoria_2 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o nome da categoria 2')
  categoria_3 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o nome da categoria 3')
  peso_1 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o peso da categoria 1')
  peso_2 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o peso da categoria 2')
  peso_3 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o peso da categoria 3')
  Eleitores_categoria_1 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de eleitores aptos a votar')
  Eleitores_categoria_2 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de eleitores aptos a votar')
  Eleitores_categoria_3 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de eleitores aptos a votar')
  Quantidade_candidatos = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de candidatos')
  candidato_1 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o nome do candidato 1')
  candidato_2 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o nome do candidato 2')
  candidato_3 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), help_text='Informe o nome do candidato 3')
  Votos_Candidato_1_Categoria_1 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 1 recebeu da categoria 1')
  Votos_Candidato_2_Categoria_1 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 2 recebeu da categoria 1')
  Votos_Candidato_3_Categoria_1 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 3 recebeu da categoria 1')
  Votos_Candidato_1_Categoria_2 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 1 recebeu da categoria 2')
  Votos_Candidato_2_Categoria_2 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 2 recebeu da categoria 2')
  Votos_Candidato_3_Categoria_2 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 3 recebeu da categoria 2')
  Votos_Candidato_1_Categoria_3 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 1 recebeu da categoria 3')
  Votos_Candidato_2_Categoria_3 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 2 recebeu da categoria 3')
  Votos_Candidato_3_Categoria_3 = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'size':30}), help_text='Informe a quantidade de votos que o candidato 3 recebeu da categoria 3')
  Resultado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'size':30}), help_text='Clique em Calcular para saber o resultado')

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField(help_text = 'UTC date and time voting extended to',
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

