# Generated by Django 2.0.5 on 2018-08-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_addshelfnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='update_chapter',
            field=models.IntegerField(default=0, verbose_name='最新章节'),
        ),
    ]