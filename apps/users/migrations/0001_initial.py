# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-25 12:24
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('profile', models.TextField(blank=True, max_length=200, null=True, verbose_name='简介')),
                ('image', models.ImageField(default='default.png', max_length=200, upload_to='user_images/%Y/%m/%d', verbose_name='用户头像')),
                ('au', models.IntegerField(default=0, verbose_name='用户活跃度')),
                ('topic_num', models.IntegerField(default=0, verbose_name='文章数')),
                ('visit_num', models.IntegerField(default=0, verbose_name='访问量')),
                ('comment_num', models.IntegerField(default=0, verbose_name='总评论数')),
                ('is_active', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner_images/%Y/%m/%d', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('rank', models.IntegerField(default=100, verbose_name='顺序')),
                ('create_time', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]
