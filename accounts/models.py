from django.contrib.auth.models import AbstractUser

class PostifyUser(AbstractUser):
    # Campos adicionales específicos del Proyecto
    class Meta:
        db_table = 'postify_user'  # Prefijo para diferenciar
