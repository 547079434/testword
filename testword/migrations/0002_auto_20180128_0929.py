# Generated by Django 2.0.1 on 2018-01-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testword', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointshistory',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='每关分数'),
        ),
        migrations.AddField(
            model_name='pointshistory',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='pointshistory',
            name='points',
            field=models.IntegerField(null=True, verbose_name='分数'),
        ),
    ]
