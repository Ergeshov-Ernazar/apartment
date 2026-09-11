from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название города", null=True, blank=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts', verbose_name="Город", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Название района", null=True, blank=True)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return f"{self.city.name}, {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название удобства", null=True, blank=True)

    class Meta:
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"

    def __str__(self):
        return self.name


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('moderation', 'На модерации'),
        ('active', 'Активно'),
        ('sold', 'Продано/Сдано'),
        ('rejected', 'Отклонено'),
        ('archive', 'Архив'),
    ]

    DEAL_CHOICES = [
        ('sale', 'Продажа'),
        ('long_rent', 'Долгосрочная аренда'),
        ('daily_rent', 'Посуточная аренда'),
    ]

    PRICE_CHOICES = [
        ('total', 'За всё'),
        ('sq_meter', 'За кв. метр'),
        ('daily', 'За сутки'),
        ('monthly', 'За месяц'),
    ]

    BATHROOM_CHOICES = [
        ('shared', 'Совмещенный'),
        ('separate', 'Раздельный'),
        ('multiple', 'Несколько'),
    ]

    RENOVATION_CHOICES = [
        ('none', 'Без ремонта'),
        ('need_repair', 'Требует ремонта'),
        ('cosmetic', 'Косметический'),
        ('euro', 'Евроремонт'),
        ('designer', 'Дизайнерский'),
    ]

    WALL_CHOICES = [
        ('brick', 'Кирпичный'),
        ('panel', 'Панельный'),
        ('monolith', 'Монолитный'),
        ('block', 'Блочный'),
        ('wood', 'Деревянный'),
    ]

    BUILDING_CHOICES = [
        ('new', 'Новостройка'),
        ('resale', 'Вторичка'),
    ]

    ELEVATOR_CHOICES = [
        ('passenger', 'Пассажирский'),
        ('cargo', 'Грузовой'),
        ('both', 'Пассажирский и грузовой'),
        ('none', 'Нет лифта'),
    ]

    PARKING_CHOICES = [
        ('ground', 'Наземная'),
        ('underground', 'Подземная'),
        ('closed', 'Закрытый двор'),
        ('barrier', 'Шлагбаум'),
        ('none', 'Нет парковки'),
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='properties', verbose_name="Категория", null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='properties', verbose_name="Удобства", null=True)
    
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='properties', verbose_name="Город", null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='properties', null=True, blank=True, verbose_name="Район / Микрорайон")
    address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    
    title = models.CharField(max_length=255, verbose_name="Заголовок объявления", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Статус объявления", null=True, blank=True)
    
    deal_type = models.CharField(max_length=20, choices=DEAL_CHOICES, verbose_name="Тип сделки", null=True, blank=True)
    price_type = models.CharField(max_length=20, choices=PRICE_CHOICES, verbose_name="Тип цены", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    deposit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Залог / Депозит")
    utilities_included = models.BooleanField(default=False, verbose_name="Коммунальные платежи включены", null=True, blank=True)
    negotiable = models.BooleanField(default=False, verbose_name="Возможен торг", null=True, blank=True)
    
    rooms = models.PositiveIntegerField(verbose_name="Количество комнат", null=True, blank=True)
    floor = models.PositiveIntegerField(verbose_name="Этаж", null=True, blank=True)
    total_floors = models.PositiveIntegerField(verbose_name="Этажность дома", null=True, blank=True)
    
    square_meters = models.FloatField(verbose_name="Общая площадь (кв.м.)", null=True, blank=True)
    living_square_meters = models.FloatField(blank=True, null=True, verbose_name="Жилая площадь (кв.м.)")
    kitchen_square_meters = models.FloatField(blank=True, null=True, verbose_name="Площадь кухни (кв.м.)") 
    ceiling_height = models.FloatField(blank=True, null=True, verbose_name="Высота потолков (м)")
    
    bathroom = models.CharField(max_length=20, choices=BATHROOM_CHOICES, blank=True, null=True, verbose_name="Санузел")
    balcony_count = models.PositiveIntegerField(default=0, verbose_name="Количество балконов / лоджий", null=True, blank=True)
    renovation = models.CharField(max_length=20, choices=RENOVATION_CHOICES, blank=True, null=True, verbose_name="Ремонт")
    
    build_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Год постройки")
    wall_material = models.CharField(max_length=20, choices=WALL_CHOICES, blank=True, null=True, verbose_name="Материал стен")
    building_type = models.CharField(max_length=20, choices=BUILDING_CHOICES, blank=True, null=True, verbose_name="Тип дома")
    elevator = models.CharField(max_length=20, choices=ELEVATOR_CHOICES, default='none', verbose_name="Наличие лифта", null=True, blank=True)
    parking = models.CharField(max_length=20, choices=PARKING_CHOICES, default='none', verbose_name="Парковка", null=True, blank=True)
    
    floor_plan = models.ImageField(upload_to='floor_plans/', blank=True, null=True, verbose_name="Планировка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"

    def __str__(self):
        return f"{self.title} — {self.price}"


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images', verbose_name="Объект недвижимости", null=True, blank=True)
    image = models.ImageField(upload_to='apartments/', verbose_name="Фотография", null=True, blank=True)

    class Meta:
        verbose_name = "Фотография объекта"
        verbose_name_plural = "Фотографии объектов"

    def __str__(self):
        return f"Фото для {self.apartment.title}"
