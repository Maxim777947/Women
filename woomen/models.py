from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import get_user_model

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Woomen.Status.PUBLISHED
            )

class Woomen(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(
        max_length=255,
        )
    slug = models.SlugField(
        max_length=255,
        unique=True, db_index=True,
        validators=[
            MinLengthValidator(5, message='Минимум 5 символов'),
            MaxLengthValidator(100, message='Максимум 100 символов'),
        ])
    content = models.TextField(
        blank=True,
        )
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        default=None,
        blank=True,
        null=True,
        verbose_name='Фото',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        )
    time_update = models.DateTimeField(
        auto_now=True,
        )
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT #анонимная функция 6.2 курса
        )
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts'
        )
    tags = models.ManyToManyField(
        'TagPost',
        blank=True,
        related_name='tags',
        )
    husband = models.OneToOneField(
        'Husband', on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='wuman',
        )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        default=None
        )

    def __str__(self) -> str:
        return self.title
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
         

    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})
    

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self): 
        return reverse("tag", kwargs={"tag_slug": self.slug})   #tag - имя маршрута        
    

class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
    

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')