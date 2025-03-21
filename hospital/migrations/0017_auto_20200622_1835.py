# Generated by Django 

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_auto_20200622_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor'),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient'),
        ),
    ]
