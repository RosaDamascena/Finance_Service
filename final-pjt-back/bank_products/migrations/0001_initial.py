# Generated by Django 4.2.7 on 2023-11-21 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('join_way', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('dcls_strt_day', models.IntegerField(blank=True, null=True)),
                ('join_user', models.ManyToManyField(related_name='joined_depositproducts', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(related_name='liked_depositproducts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('join_way', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('dcls_strt_day', models.IntegerField(blank=True, null=True)),
                ('join_user', models.ManyToManyField(related_name='joined_savingsproducts', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(related_name='liked_savingsproducts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SP_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_products.savingsproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsProductsOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.TextField(max_length=100)),
                ('intr_rate', models.FloatField(blank=True, default=-1, null=True)),
                ('intr_rate2', models.FloatField(blank=True, default=-1, null=True)),
                ('save_trm', models.FloatField()),
                ('rsrv_type_nm', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_products.savingsproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DP_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_products.depositproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProductOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.TextField(max_length=100)),
                ('intr_rate', models.FloatField(blank=True, default=-1, null=True)),
                ('intr_rate2', models.FloatField(blank=True, default=-1, null=True)),
                ('save_trm', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_products.depositproducts')),
            ],
        ),
    ]
