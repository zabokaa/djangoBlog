from django.db import models

@admin.register(About)
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

# str magic method
    def __str__(self):
        return self.title


# register model
