# Generated by Django 3.2.6 on 2021-08-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodNutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(verbose_name='열량')),
                ('f2', models.TextField(verbose_name='탄수화물')),
                ('f3', models.TextField(verbose_name='단백질')),
                ('f4', models.TextField(verbose_name='지방')),
                ('f5', models.TextField(verbose_name='당류')),
                ('f6', models.TextField(verbose_name='콜레스테롤')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(verbose_name='나물')),
                ('f2', models.TextField(verbose_name='생선')),
                ('f3', models.TextField(verbose_name='떡')),
                ('f4', models.TextField(verbose_name='국')),
                ('f5', models.TextField(verbose_name='면')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(verbose_name='채소류')),
                ('f2', models.TextField(verbose_name='과일류')),
                ('f3', models.TextField(verbose_name='곡류')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingMall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(verbose_name='마켓컬리')),
                ('f2', models.TextField(verbose_name='쿠팡')),
                ('f3', models.TextField(verbose_name='푸드슈퍼마켓')),
                ('f4', models.TextField(verbose_name='G마켓')),
            ],
        ),
    ]
