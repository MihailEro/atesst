from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='название продукта')
    product_model = models.CharField(max_length=100, verbose_name='модель продукта')
    release_date = models.DateField(verbose_name='дата выхода продукта')

    def __str__(self):
        return f'{self.title}({self.product_model}, {self.release_date})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Participant(models.Model):

    SUPPLIER_TYPES = (
        ('factory', 'завод'),
        ('retail', 'розничная сеть'),
        ('individual entrepreneur', 'индивидуальный предприниматель')
    )

    title = models.CharField(max_length=50, verbose_name='название')
    supplier_type = models.CharField(max_length=50, choices=SUPPLIER_TYPES, verbose_name='тип участника')
    products = models.ManyToManyField(Product, **NULLABLE)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,  verbose_name='задолженость')
    level = models.IntegerField(default=None, **NULLABLE, verbose_name='уровень в цепочке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title}-{self.supplier_type}'

    def save(self, *args, **kwargs):

        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'


class Contacts(models.Model):

    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.CharField(max_length=25, verbose_name='номер дома')
    supplier = models.OneToOneField(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}, {self.country}({self.city},{self.street} {self.house_number}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'
