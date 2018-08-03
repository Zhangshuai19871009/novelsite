# Generated by Django 2.0.5 on 2018-07-12 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0003_auto_20180711_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '小说类型',
                'verbose_name_plural': '小说类型',
            },
        ),
        migrations.AlterField(
            model_name='novel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.NovelType', verbose_name='类型'),
        ),
    ]