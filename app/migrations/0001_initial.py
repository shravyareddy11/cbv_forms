# Generated by Django 4.1.7 on 2023-05-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=100)),
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('saddress', models.TextField()),
            ],
        ),
    ]
