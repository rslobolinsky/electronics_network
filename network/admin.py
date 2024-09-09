from django.contrib import admin
from .models import NetworkNode, Product


# Включаем отображение продуктов на странице звена сети
class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


# Регистрация модели NetworkNode с кастомными настройками админ-панели
@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке объектов
    list_display = ('name', 'level', 'get_supplier_link', 'debt', 'created_at')
    # Фильтрация по городу
    list_filter = ('city',)
    # Поля для поиска
    search_fields = ('name', 'city')
    # Включаем отображение продуктов как инлайн-элементов
    inlines = [ProductInline]
    # Действия в админ-панели
    actions = ['clear_debt']

    # Метод для создания ссылки на поставщика
    def get_supplier_link(self, obj):
        if obj.supplier:
            # Создаем ссылку на объект поставщика в админ-панели
            return f'<a href="{obj.supplier.get_admin_url()}">{obj.supplier.name}</a>'
        return 'Нет поставщика'

    get_supplier_link.short_description = 'Поставщик'  # Название колонки
    get_supplier_link.allow_tags = True  # Разрешаем HTML теги

    # Admin action для очистки задолженности перед поставщиками
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'


# Регистрация модели Product в админ-панели
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
