# Generated by Django 4.2.2 on 2023-07-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('group', models.CharField(choices=[('notebook', 'notebook'), ('pc', 'pc'), ('mobile', 'mobile'), ('accessories', 'accessories')], default='mobile', max_length=20)),
                ('img', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
    ]
