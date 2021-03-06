# Generated by Django 3.0.3 on 2020-03-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialVarification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50, unique=True)),
                ('Email_varification_code', models.CharField(max_length=200, null=True)),
                ('phone_otp_code', models.IntegerField()),
                ('email_otp_code', models.IntegerField()),
                ('varification_status', models.BooleanField()),
                ('code_sent_counter', models.IntegerField()),
            ],
        ),
    ]
