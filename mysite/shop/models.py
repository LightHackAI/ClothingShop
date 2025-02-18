from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название товара')
    type = models.ForeignKey('ProductType', on_delete=models.PROTECT, verbose_name='Тип товара')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    photo_product = models.ImageField(verbose_name='Фотография товара')
    photo_another = models.ImageField(blank=True, verbose_name='Другая фотография', )
    size = models.CharField(max_length=20, blank=True, verbose_name='Размер')
    size_two = models.CharField(max_length=20, blank=True, verbose_name='Размер_второй')
    size_three = models.CharField(max_length=20, blank=True, verbose_name='Размер_третий')
    size_four = models.CharField(max_length=20, blank=True, verbose_name='Размер_четвертый')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    about = models.ForeignKey('ProductAbout', on_delete=models.PROTECT, verbose_name='О товаре')


    STOCK = (
        ("В наличие", "В наличие"),
        ("Нет в наличие", "Нет в наличие"),
    )
    available = models.CharField(max_length=20, choices=STOCK, verbose_name='Наличие товара')

    MenClothes = (
       ("NEW", "НОВИНКИ"),
       ("COAT", "ПАЛЬТО"),
       ("SWEATER", "СВИТЕРА"),
       ("HOODIE", "ХУДИ"),
       ("SHIRT", "РУБАШКИ"),
       ("T-SHIRT", "ФУТБОЛКИ"),
       ("PANTS", "БРЮКИ"),
       ("SNEAKERS", "КРОССОВКИ"),
       ("SHOES", "ОБУВЬ"),
   )

    WomenClothes = (
        ("NEW", "НОВИНКИ"),
        ("COAT", "ПАЛЬТО"),
        ("BLAZER", "ПИДЖАКИ"),
        ("DRESS", "ПЛАТЬЯ"),
        ("SHIRT", "РУБАШКИ"),
        ("T-SHIRT", "ФУТБОЛКИ"),
        ("SWEATER", "СВИТЕРА"),
        ("PANTS", "БРЮКИ"),
        ("JEANS", "ДЖИНСЫ"),
        ("SNEAKERS", "КРОССОВКИ"),
        ("SHOES", "ОБУВЬ"),
    )

    men = models.CharField(max_length=8, blank=True, choices=MenClothes, verbose_name="Мужчины")
    women = models.CharField(max_length=8, blank=True, choices=WomenClothes, verbose_name="Женщины")

    jewerlymen = models.CharField(max_length=20, blank=True, verbose_name='Украшения для мужчин')
    jewerlywomen = models.CharField(max_length=20, blank=True, verbose_name='Украшения для женщин')
    watchmen = models.CharField(max_length=20, blank=True, verbose_name='Часы для мужчин')
    watchwomen = models.CharField(max_length=20, blank=True, verbose_name='Часы для женщин')

    BREND = (
        ('AlexanderMcQueen', 'AlexanderMcQueen'),
        ('Balenciaga', 'Balenciaga'),
        ('Moncler', 'Moncler'),
        ('Off-White', 'Off-White'),
        ('Valentino', 'Valentino'),
    )

    brand = models.CharField(max_length=20, blank=True, choices=BREND, verbose_name='Бренд')

    WATCH = (
        ('CHOPARD', 'CHOPARD'),
        ('DEGRISOGONO', 'DEGRISOGONO'),
        ('GIRARDPERREGAUX', 'GIRARDPERREGAUX'),
        ('HUBLOT', 'HUBLOT'),
        ('BREITLING', 'BREITLING'),
        ('TAGHEUER', 'TAGHEUER'),
        ('TUDOR', 'TUDOR'),
        ('CHANEL', 'CHANEL'),
    )

    watch = models.CharField(max_length=20, blank=True, choices=WATCH, verbose_name='Часы')

    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

class ProductType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ptype = models.CharField(max_length=40, verbose_name='Тип товара')

    def __str__(self):
        return self.ptype

class ProductAbout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField(verbose_name='Информация о товаре')
    material = models.CharField(max_length=20, verbose_name='Материал')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    shape = models.CharField(max_length=20, verbose_name='Форма')

    def __str__(self):
        return self.information

class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Комментарий от {self.name}"

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=20, verbose_name='Название')
    photo_news = models.ImageField(blank=True, verbose_name='Фотография')
    news = models.TextField(blank=True, verbose_name='Нововсти')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

