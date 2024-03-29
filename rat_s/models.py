from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from Rat import settings




class DadosPessoais(models.Model):

	nm_analista = models.CharField(verbose_name="Nome Profissional", max_length=50, default='')
	nm_medico = models.CharField(verbose_name="Nome Médico", max_length=100, blank=True, null=True)
	nm_hospital = models.CharField(verbose_name="Nome do Hospital", max_length=100, blank=True, null=True)
	tel_contato = models.CharField(verbose_name="Telefone Contato", max_length=100, blank=True, null=True)
	email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
	dt_atendimento = models.DateTimeField(verbose_name="Data do atendimento", blank=True, null=True)
	servico_analisado= models.TextField(blank=True, null=True,verbose_name="Tipo de validação")
	upload = models.FileField(blank=True, null=True, upload_to='images/')
	utiliza_protocolo = models.BooleanField(default=False, verbose_name="Utiliza protocolo gerenciavel ?")
	utiliza_rotina_especial = models.BooleanField(default=False, verbose_name="Utiliza rotina especial ?")
	utiliza_rotina = models.BooleanField(default=False, verbose_name="Utiliza rotina ?")
	comentarios = models.TextField(blank=True, null=True,verbose_name="Comentarios")
	upload = models.ImageField(null=True, blank=True, upload_to='dados/')
	data_insercao = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.nm_analista} | {self.nm_hospital} | {self.data_insercao}" 
	
	def upload_to(instance, filename):
		now = timezone_now()
		filename_base, filename_ext = os.path.splitext(filename)
		return "quotes/%s%s" % (
			now.strftime("%Y/%m/%Y%m%d%H%M%S"),
			filename_ext.lower(),
			)
    