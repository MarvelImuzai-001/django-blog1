from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'About'
    
    def __str__(self) -> str:
        return self.about_heading
    
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    
    
    class Meta:
        verbose_name_plural = 'SocialLink'
        
        
    def __str__(self) -> str:
        return self.platform