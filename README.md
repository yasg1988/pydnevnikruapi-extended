# pydnevnikruapi-extended

Расширенная обёртка для [pydnevnikruapi](https://github.com/kesha1225/DnevnikRuAPI) с дополнительными методами Dnevnik.ru API.

## Зачем?

Оригинальная библиотека `pydnevnikruapi` покрывает ~85% API Дневник.ру, но не включает:
- Методы v2 API
- Некоторые методы для работы со школой целиком
- Методы для получения данных всех классов

Эта обёртка **наследуется** от `AsyncDiaryAPI`, поэтому:
- ✅ Все оригинальные методы работают
- ✅ Обновления `pydnevnikruapi` подтягиваются через `pip install -U`
- ✅ Нет конфликтов при обновлении

## Установка

```bash
# Сначала установить оригинальную библиотеку
pip install pydnevnikruapi aiohttp

# Скачать extended_api.py в свой проект
curl -O https://raw.githubusercontent.com/yasg1988/pydnevnikruapi-extended/main/extended_api.py
```

Или клонировать репозиторий:
```bash
git clone https://github.com/yasg1988/pydnevnikruapi-extended.git
```

## Использование

```python
import aiohttp
import asyncio
from extended_api import ExtendedDiaryAPI

TOKEN = "ваш_токен"
SCHOOL_ID = 1234567890

async def main():
    async with aiohttp.ClientSession() as session:
        dn = ExtendedDiaryAPI(session=session, token=TOKEN)
        
        # Оригинальные методы работают
        user = await dn.get_info()
        print(f"Пользователь: {user}")
        
        # Новые методы - все классы школы
        all_groups = await dn.get_school_groups(SCHOOL_ID)
        print(f"Классов в школе: {len(all_groups)}")
        
        # v2 API
        schedule = await dn.get_group_schedule_v2(
            group_id=2421882773904846063,
            start="2025-12-01",
            end="2025-12-07"
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Добавленные методы

### Методы для работы со школой

| Метод | Описание |
|-------|----------|
| `get_school_groups(school_id)` | Все классы школы |
| `get_school_persons(school_id)` | Все ученики школы |
| `get_school_memberships(school_id)` | Членство в школе |

### v2 API методы

| Метод | Описание |
|-------|----------|
| `get_person_edu_groups_v2(person_id)` | Классы ученика (v2) |
| `get_group_schedule_v2(group_id, start, end)` | Расписание класса (v2) |
| `get_group_subjects_v2(group_id)` | Предметы класса (v2) |
| `get_person_marks_v2(person_id, start, end)` | Оценки ученика (v2) |

### Дополнительные методы

| Метод | Описание |
|-------|----------|
| `get_criteria_marks(work_id)` | Критериальные оценки |
| `get_lesson_details(lesson_id)` | Детали урока |
| `get_work_details(work_id)` | Детали работы/ДЗ |
| `get_person_classmates(person_id)` | Одноклассники |
| `get_group_teachers(group_id)` | Учителя класса |
| `get_lesson_attendance(lesson_id)` | Посещаемость урока |
| `get_person_attendance(person_id, start, end)` | Посещаемость ученика |

## Получение токена

1. Авторизоваться на https://login.dnevnik.ru/login
2. Перейти по ссылке:
   ```
   https://login.dnevnik.ru/oauth2?response_type=token&client_id=b8006d75-70a9-4291-885c-13d8511bb2ae&scope=CommonInfo,EducationalInfo
   ```
3. Нажать "Разрешить"
4. Скопировать токен из URL после `access_token=`

## Лицензия

MIT

## Связанные проекты

- [pydnevnikruapi](https://github.com/kesha1225/DnevnikRuAPI) - оригинальная библиотека
- [Dnevnik.ru API Swagger](https://api.dnevnik.ru/partners/swagger/ui/index) - документация API
