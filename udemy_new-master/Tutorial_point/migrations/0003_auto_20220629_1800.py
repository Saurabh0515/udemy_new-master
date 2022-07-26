# Generated by Django 3.1.14 on 2022-06-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_point', '0002_auto_20220628_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_dtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]