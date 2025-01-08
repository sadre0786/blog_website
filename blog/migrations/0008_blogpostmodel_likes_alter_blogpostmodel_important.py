# Generated by Django 5.1.4 on 2024-12-24 06:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpostmodel_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpostmodel',
            name='important',
            field=models.TextField(blank=True, default='Thanks for visit Mera News', max_length=120, null=True),
        ),
    ]
