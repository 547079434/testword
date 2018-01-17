# Generated by Django 2.0.1 on 2018-01-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('phone', models.CharField(max_length=50, verbose_name='电话')),
                ('points', models.IntegerField(verbose_name='分数')),
                ('ip', models.CharField(max_length=100, verbose_name='IP')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '分数记录',
                'verbose_name_plural': '分数记录管理',
            },
        ),
    ]
