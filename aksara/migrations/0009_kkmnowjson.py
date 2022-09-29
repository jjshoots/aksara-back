# Generated by Django 4.0.6 on 2022-09-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aksara', '0008_delete_kkmnowjson'),
    ]

    operations = [
        migrations.CreateModel(
            name='KKMNowJSON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_name', models.CharField(max_length=200)),
                ('chart_name', models.CharField(max_length=200, null=True)),
                ('chart_type', models.CharField(max_length=200, null=True)),
                ('chart_data', models.JSONField()),
            ],
        ),
    ]
