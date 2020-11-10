from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_("name")
    )
    related_category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="related_categories",
        null=True,
        blank=True,
        verbose_name=_("related category"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("creation date"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return "{} => {}".format(self.name, self.related_category)

    def related_count(self):
        return self.related_categories.count()


class Product(models.Model):
    categories = models.ManyToManyField(
        Category,
        verbose_name=_("product categories"),
    )
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("code"),
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_("name"),
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.1), ],
        verbose_name=_("price"),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("quantity"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("creation date"),
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return "{}: {}".format(self.name, self.price)
