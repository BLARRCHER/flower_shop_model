# Generated by Django 4.0.6 on 2022-07-29 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Flower', '0002_alter_feedback_object_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='sells', to='Flower.user'),
            preserve_default=False,
        ),
    ]
