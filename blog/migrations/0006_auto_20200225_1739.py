# Generated by Django 3.0.3 on 2020-02-25 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_readed_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog')),
            ],
        ),
    ]
