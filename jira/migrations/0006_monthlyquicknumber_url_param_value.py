# Generated by Django 4.2.5 on 2023-10-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira', '0005_rename_jql_string_monthlyquicknumber_jql'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyquicknumber',
            name='url_param_value',
            field=models.TextField(default=''),
        ),
    ]
