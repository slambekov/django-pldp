# Generated by Django 2.1.5 on 2019-04-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pldp', '0005_auto_20190328_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveycomponent',
            name='saved_data',
            field=models.CharField(blank=True, help_text='The submitted answer(s) to this survey question', max_length=500, null=True),
        ),
    ]
