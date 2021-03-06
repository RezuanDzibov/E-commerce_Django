# Generated by Django 3.2.8 on 2021-11-18 19:22

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import src.product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='product.category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, help_text='You can leave it blank.', unique=True, verbose_name='Slug')),
                ('small_description', models.TextField(blank=True, help_text='Small description about product', max_length=5000, verbose_name='Small description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('available', models.BooleanField(default=True, help_text='Is the product available', verbose_name='Available')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Created date and time', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated date and time', verbose_name='Updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='product.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=src.product.models.get_upload_path)),
                ('alt_text', models.CharField(max_length=255, null=True, verbose_name='Alternative text')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
