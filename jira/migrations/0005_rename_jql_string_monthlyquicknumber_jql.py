# Generated by Django 4.2.5 on 2023-10-03 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jira', '0004_alter_monthlyquicknumber_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlyquicknumber',
            old_name='jql_string',
            new_name='jql',
        ),
    ]
