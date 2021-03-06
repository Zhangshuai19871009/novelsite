# Generated by Django 2.0.5 on 2018-07-11 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='章节标题')),
                ('chapter_url', models.CharField(max_length=100, verbose_name='章节源')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id_book', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='书编')),
                ('book_name', models.CharField(max_length=20, verbose_name='书名')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('category', models.CharField(max_length=20, verbose_name='类型')),
                ('status', models.CharField(max_length=20, verbose_name='状态')),
                ('image', models.CharField(max_length=100, verbose_name='封面图片')),
                ('description', models.CharField(max_length=500, verbose_name='描述')),
                ('novel_url', models.CharField(max_length=100, verbose_name='链接源')),
                ('update_time', models.CharField(max_length=20, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '小说',
                'verbose_name_plural': '小说',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Novel', verbose_name='书编'),
        ),
    ]
