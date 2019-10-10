# Generated by Django 2.1.7 on 2019-03-03 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=300)),
                ('img_url', models.URLField()),
                ('like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('status', models.CharField(choices=[('EP', 'Examine Passed'), ('WE', 'Wait Examine')], default='WE', max_length=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WordType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('typename', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='dictionary.WordType'),
        ),
    ]
