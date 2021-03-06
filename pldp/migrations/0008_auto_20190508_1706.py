# Generated by Django 2.1.5 on 2019-05-08 17:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pldp', '0007_auto_20190501_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='agency',
            field=models.ForeignKey(help_text='Agency conducting the study.', on_delete=django.db.models.deletion.CASCADE, to='pldp.Agency'),
        ),
        migrations.AlterField(
            model_name='study',
            name='areas',
            field=models.ManyToManyField(blank=True, help_text='Area geometries for surveys bundled together within one larger study. Leave blank if no such sub-division is necessary.', to='pldp.StudyArea'),
        ),
        migrations.AlterField(
            model_name='study',
            name='end_date',
            field=models.DateField(blank=True, help_text='Date of the last survey taking place within a study', null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='scale',
            field=models.CharField(blank=True, choices=[('district', 'District'), ('city', 'City'), ('city center', 'City center'), ('neighborhood', 'Neighborhood'), ('block scale', 'Block scale'), ('single site', 'Single site')], help_text='Approximate scale of the entire study area, regardless of the number of survey locations within that study area.', max_length=12),
        ),
        migrations.AlterField(
            model_name='studyarea',
            name='area',
            field=django.contrib.gis.db.models.fields.PolygonField(help_text='Draw boundaries above to create a new study area. Studies can be linked to multiple areas, and a study can be made up of multiple surveys.', srid=4326),
        ),
    ]
