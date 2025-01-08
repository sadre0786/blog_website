from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class BlogPostModel(models.Model):
    category_choices = [
        ('tech', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('travel', 'Travel'),
    ]
    title = models.CharField(max_length=150)
    content = models.TextField()
    heading2 = models.CharField(max_length=150, blank=True, null=True)
    heading2Content = models.TextField(blank=True,null=True)
    heading3 = models.CharField(max_length=150, blank=True, null=True)
    heading3Content = models.TextField(blank=True,null=True)
    important = models.TextField(max_length=120,default="Thanks for visit Mera News", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    main_image = models.ImageField(upload_to='media/', blank=True , null=True)
    image = models.ImageField(upload_to='media/', blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True) 
    category = models.CharField(choices=category_choices,max_length=100, default='tech')
    class Meta:
        ordering = ['-created_at']   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPostModel,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    



    
    
