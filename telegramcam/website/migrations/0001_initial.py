# Generated by Django 4.2.7 on 2023-11-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chat_id",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("chat_idname", models.CharField(max_length=100)),
            ],
        ),
    ]