# Generated by Django 3.1.4 on 2021-01-15 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docs', '0001_initial'),
        ('production', '0002_availabledocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.сustomer')),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.doc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]