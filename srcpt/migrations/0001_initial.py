# Generated by Django 4.1.6 on 2023-03-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1100)),
                ('summary', models.CharField(max_length=1200)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('mobile', models.IntegerField()),
                ('purpose', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('subject', models.TextField(max_length=1000)),
                ('desc', models.TextField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
    ]