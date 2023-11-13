# Generated by Django 4.2.5 on 2023-09-24 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.vendor'),
        ),
    ]