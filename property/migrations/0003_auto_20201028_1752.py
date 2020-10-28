# Generated by Django 3.1.2 on 2020-10-28 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='propertyimages',
            options={'verbose_name': 'Property Image'},
        ),
        migrations.CreateModel(
            name='PropertyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_from', models.DateField(default=django.utils.timezone.now)),
                ('date_to', models.DateField(default=django.utils.timezone.now)),
                ('guest', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_book', to='property.property')),
            ],
        ),
    ]