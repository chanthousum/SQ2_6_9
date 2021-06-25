# Generated by Django 3.2.3 on 2021-06-04 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('barcode', models.IntegerField()),
                ('unitPrice', models.FloatField()),
                ('sellPrice', models.FloatField()),
                ('qty', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]