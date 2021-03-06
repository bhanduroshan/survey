# Generated by Django 2.0.10 on 2019-01-28 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_used', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('answer', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Code',
                'verbose_name_plural': 'Codes',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_number', models.AutoField(primary_key=True, serialize=False)),
                ('html', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Survey',
                'verbose_name_plural': 'Survey',
            },
        ),
        migrations.AddField(
            model_name='codes',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveyapp.Survey'),
        ),
    ]
