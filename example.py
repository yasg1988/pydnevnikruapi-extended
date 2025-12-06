"""
Пример использования ExtendedDiaryAPI
"""

import aiohttp
import asyncio
from extended_api import ExtendedDiaryAPI
from datetime import datetime, timedelta

# Вставьте свои данные
TOKEN = "ваш_токен_здесь"
SCHOOL_ID = 1234567890  # ID вашей школы
GROUP_ID = 1234567890   # ID класса
PERSON_ID = 1234567890  # ID ученика


async def main():
    async with aiohttp.ClientSession() as session:
        dn = ExtendedDiaryAPI(session=session, token=TOKEN)
        
        # Информация о пользователе (оригинальный метод)
        print("=" * 50)
        print("Информация о пользователе:")
        user = await dn.get_info()
        print(f"  Имя: {user.get('lastName')} {user.get('firstName')}")
        print(f"  ID: {user.get('id')}")
        
        # Все классы школы (новый метод)
        print("\n" + "=" * 50)
        print("Все классы школы:")
        all_groups = await dn.get_school_groups(SCHOOL_ID)
        for group in all_groups[:10]:  # Первые 10
            print(f"  - {group.get('name')} (ID: {group.get('id')})")
        if len(all_groups) > 10:
            print(f"  ... и ещё {len(all_groups) - 10} классов")
        
        # Расписание через v2 API (новый метод)
        print("\n" + "=" * 50)
        print("Расписание класса (v2 API):")
        today = datetime.now()
        start = today.strftime("%Y-%m-%d")
        end = (today + timedelta(days=7)).strftime("%Y-%m-%d")
        
        try:
            schedule = await dn.get_group_schedule_v2(GROUP_ID, start, end)
            print(f"  Получено уроков: {len(schedule) if isinstance(schedule, list) else 'см. данные'}")
        except Exception as e:
            print(f"  Ошибка: {e}")
        
        # Учителя класса (новый метод)
        print("\n" + "=" * 50)
        print("Учителя класса:")
        try:
            teachers = await dn.get_group_teachers(GROUP_ID)
            for t in teachers[:5]:
                print(f"  - {t.get('lastName')} {t.get('firstName')}")
        except Exception as e:
            print(f"  Ошибка: {e}")
        
        print("\n" + "=" * 50)
        print("Готово!")


if __name__ == "__main__":
    asyncio.run(main())
