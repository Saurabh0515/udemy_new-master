# Generated by Django 3.1.14 on 2022-07-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_point', '0010_payment_usercourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tutorial_point.usercourse'),
        ),
    ]
