# Generated by Django 2.0 on 2018-08-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goods_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='Fabric_content',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='care_instructions_and_other_details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='img_url1',
            field=models.ImageField(null=True, upload_to='goods'),
        ),
        migrations.AddField(
            model_name='goods',
            name='img_url2',
            field=models.ImageField(null=True, upload_to='goods'),
        ),
        migrations.AddField(
            model_name='goods',
            name='item_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='size',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='style_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='weight',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='img_url',
            field=models.ImageField(upload_to='goods'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='type_name',
            field=models.CharField(max_length=30),
        ),
    ]
