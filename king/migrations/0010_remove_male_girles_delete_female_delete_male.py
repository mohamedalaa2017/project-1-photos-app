# Generated by Django 4.1.7 on 2023-05-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("king", "0009_remove_female_men_alter_female_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="male",
            name="girles",
        ),
        migrations.DeleteModel(
            name="Female",
        ),
        migrations.DeleteModel(
            name="Male",
        ),
    ]