# Generated by Django 4.0.4 on 2022-05-19 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Utilitys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Utilitys.main')),
                ('type', models.TextField(choices=[('A', 'Admin'), ('S', 'Seller'), ('B', 'Buyer')])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('Utilitys.main',),
        ),
        migrations.CreateModel(
            name='BirthDate',
            fields=[
                ('main_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Utilitys.main')),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('Utilitys.main',),
        ),
    ]
