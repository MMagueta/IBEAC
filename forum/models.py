from django.db import models

# Create your models here.

class Usuario(models.Model):
    Usuario_nome = models.CharField(max_length=200)
    Usuario_email = models.EmailField(max_length=254, unique=True)
    Usuario_senha = models.CharField(max_length=200)
    Usuario_endereco = models.CharField(max_length=254)
    Usuario_enderecoNum = models.CharField(max_length=20)
    Usuario_CEP = models.CharField(max_length=20)
    Usuario_dtNascimento = models.DateField()
    Usuario_dtEntrada = models.DateField(auto_now_add=True, blank=True)
    Usuario_telefone1 = models.CharField(max_length=25, blank=True)
    Usuario_telefone2 = models.CharField(max_length=25, blank=True)
    Usuario_telHabilita = models.BooleanField()
    Usuario_nivel = models.IntegerField()
    Usuario_descricao = models.TextField(max_length=500)
    Usuario_foto = models.ImageField(upload_to='images/usuarios/')
    #Usuario_indicador = models.ForeignKey('Usuario', on_delete=models.PROTECT)

    def __str__(self):
        return self.Usuario_nome + " - " + self.Usuario_email

class Categoria(models.Model):
    Categoria_nome = models.CharField(max_length=200)
    def __str__(self):
        return self.Categoria_nome

class Topico(models.Model):
    Topico_tipo = models.IntegerField()
    Topico_titulo = models.CharField(max_length=200)
    Topico_data = models.DateTimeField(auto_now_add=True)
    Topico_interesses = models.IntegerField()
    Topico_texto = models.TextField()
    Topico_Usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Topico_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    def __str__(self):
        return self.Topico_Usuario + " - " + self.Topico_data

class ImagemTopico(models.Model):
    ImagemTopico_src = models.ImageField(upload_to='images/topicos/')
    ImagemTopico_topico = models.ForeignKey('Topico', on_delete=models.PROTECT)

class Interesse(models.Model):
    Interesse_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Interesse_topico = models.ForeignKey('Topico', on_delete=models.PROTECT)

class Comentario(models.Model):
    Comentario_data = models.DateTimeField(auto_now_add=True)
    Comentario_selo = models.BooleanField()
    Comentario_texto = models.TextField()
    Comentario_curtidas = models.IntegerField()
    Comentario_tipo = models.IntegerField()
    Comentario_topico = models.ForeignKey('Topico', on_delete=models.PROTECT)
    Comentario_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)

class SubComentario(models.Model):
    SubComentario_comentario = models.ForeignKey('Comentario', on_delete=models.PROTECT)

class Report(models.Model):
    Report_motivo = models.CharField(max_length=200)
    Report_tipo = models.IntegerField()

class ReportComentario(models.Model):
    ReportComentario_Comentario = models.ForeignKey('Comentario', on_delete=models.PROTECT)
    ReportComentario_Report = models.ForeignKey('Report', on_delete=models.PROTECT)
    ReportComentario_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    ReportComentario_Subcomentario = models.ForeignKey('Subcomentario', on_delete=models.PROTECT)
    ReportComentario_Subcomentario_Comentario = models.ForeignKey('SubComentario_comentario', on_delete=models.PROTECT)


class Curtida(models.Model):
    Curtida_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Curtida_comentario = models.ForeignKey('Comentario', on_delete=models.PROTECT)

class ReportTopico(models.Model):
    ReportTopico_topico = models.ForeignKey('Topico', on_delete=models.PROTECT)
    ReportTopico_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)

class Convite(models.Model):
    Convite_email = models.CharField(max_length=200)
    Convite_aceito = models.CharField(max_length=200)
    Convite_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)

class Mae(models.Model):
    Mae_tipo = models.IntegerField()
    Mae_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)

class Intimo(models.Model):
    Intimo_Usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Intimo_Mae= Usuario = models.ForeignKey('Mae', on_delete=models.PROTECT)

class Especialista(models.Model):
    Especialista_Usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Especialista_Especialidade = models.ForeignKey('Especialidade', on_delete=models.PROTECT)

class Especialidade(models.Model):
    Especialidade_nome = models.CharField(max_length=200)

class Bloqueio(models.Model):
    Bloqueio_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    Bloqueio_comentario = models.ForeignKey('Report', on_delete=models.PROTECT)
