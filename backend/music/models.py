from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    title = models.CharField(max_length=200)
    # Mantenha o campo antigo como estava:
    artist = models.CharField(max_length=200, verbose_name="Artista (antigo)")  
    # Adicione o novo campo como ForeignKey (inicialmente opcional):
    artist_link = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE, 
        null=True,  # Permite NULL durante a transição
        blank=True,
        verbose_name="Artista (novo)"
    )