# Generated by Django 3.2.8 on 2022-01-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220109_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='category/')),
                ('image2', models.ImageField(blank=True, upload_to='category/')),
                ('image3', models.ImageField(blank=True, upload_to='category/')),
                ('image4', models.ImageField(blank=True, upload_to='category/')),
                ('image5', models.ImageField(blank=True, upload_to='category/')),
                ('image6', models.ImageField(blank=True, upload_to='category/')),
                ('image7', models.ImageField(blank=True, upload_to='category/')),
                ('image8', models.ImageField(blank=True, upload_to='category/')),
                ('image9', models.ImageField(blank=True, upload_to='category/')),
                ('image10', models.ImageField(blank=True, upload_to='category/')),
                ('image11', models.ImageField(blank=True, upload_to='category/')),
                ('image12', models.ImageField(blank=True, upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='Pans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pans/')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(choices=[(1, 'NAQD'), (2, 'Karta')], max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.AddField(
            model_name='pans',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.payment'),
        ),
    ]