# Generated by Django 4.2.11 on 2024-03-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_comment_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="field_1",),
        migrations.AddField(
            model_name="post",
            name="field_2",
            field=models.CharField(default="Hola world"),
        ),
        migrations.AddField(
            model_name="post", name="field_3", field=models.CharField(null=True),
        ),
    ]
