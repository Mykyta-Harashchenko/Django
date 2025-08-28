import os
import json
import django
from dotenv import load_dotenv
from pymongo import MongoClient

# Завантаження змінних середовища
load_dotenv()

# Встановлення налаштувань Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Налаштування Django
django.setup()

from core.quotes.models import Quote, Tag, Author

def load_data_from_json():
    # путь к твоему JSON-файлу
    json_path = os.path.join(os.path.dirname(__file__), "quotes.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for q in data:
        try:
            author = Author.objects.get(fullname=q["author"])
        except Author.DoesNotExist:
            print('Author: {author} not found')
            continue
        
        quote, _ = Quote.objects.get_or_create(
            quote=q["quote"],
            author=author
        )
        for tag_name in q.get('tags', []):
            tag, _ = Tag.objects.get_or_create(
                name=tag_name
            )
            quote.tags.add(tag)


if __name__ == "__main__":
    load_data_from_json()
    print("✅ Данные успешно перенесены из JSON в БД")