# cooking_book/asgi.py
"""
ASGI config for cooking_book project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application

# Устанавливаем настройки для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cooking_book.settings')

# Получаем асинхронное приложение Django
application = get_asgi_application()
