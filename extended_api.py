"""
Расширенная обёртка для pydnevnikruapi

Добавляет недостающие методы v1/v2 API Дневник.ру
Наследуется от AsyncDiaryAPI, поэтому все оригинальные методы работают.

Использование:
    from extended_api import ExtendedDiaryAPI
    
    async with aiohttp.ClientSession() as session:
        dn = ExtendedDiaryAPI(session=session, token=TOKEN)
        all_groups = await dn.get_school_groups(SCHOOL_ID)
"""

from typing import List, Dict, Any, Optional
from pydnevnikruapi import AsyncDiaryAPI


class ExtendedDiaryAPI(AsyncDiaryAPI):
    """
    Расширенный клиент API Дневник.ру
    
    Наследует все методы из pydnevnikruapi.AsyncDiaryAPI
    и добавляет недостающие методы v1/v2 API.
    """
    
    # ==========================================
    # Методы для работы со школой целиком
    # ==========================================
    
    async def get_school_groups(self, school_id: int) -> List[Dict[str, Any]]:
        """
        Получить все классы (учебные группы) школы.
        
        Args:
            school_id: ID школы
            
        Returns:
            Список всех классов школы
        """
        return await self._get(f"v1/schools/{school_id}/edu-groups")
    
    async def get_school_persons(self, school_id: int) -> List[Dict[str, Any]]:
        """
        Получить всех учеников школы.
        
        Args:
            school_id: ID школы
            
        Returns:
            Список всех персон (учеников) школы
        """
        return await self._get(f"v1/schools/{school_id}/persons")
    
    async def get_school_memberships(self, school_id: int) -> List[Dict[str, Any]]:
        """
        Получить информацию о членстве в школе.
        
        Args:
            school_id: ID школы
            
        Returns:
            Список членств (связей пользователь-школа)
        """
        return await self._get(f"v1/schools/{school_id}/memberships")
    
    # ==========================================
    # v2 API методы
    # ==========================================
    
    async def get_person_edu_groups_v2(self, person_id: int) -> Dict[str, Any]:
        """
        Получить классы ученика (v2 API).
        
        Args:
            person_id: ID персоны (ученика)
            
        Returns:
            Информация о классах ученика в формате v2
        """
        return await self._get(f"v2/persons/{person_id}/edu-groups")
    
    async def get_group_schedule_v2(
        self, 
        group_id: int, 
        start: str, 
        end: str
    ) -> Dict[str, Any]:
        """
        Получить расписание класса (v2 API).
        
        Args:
            group_id: ID класса (учебной группы)
            start: Начальная дата (YYYY-MM-DD)
            end: Конечная дата (YYYY-MM-DD)
            
        Returns:
            Расписание уроков класса
        """
        return await self._get(f"v2/edu-groups/{group_id}/lessons/{start}/{end}")
    
    async def get_group_subjects_v2(self, group_id: int) -> Dict[str, Any]:
        """
        Получить предметы класса (v2 API).
        
        Args:
            group_id: ID класса
            
        Returns:
            Список предметов класса
        """
        return await self._get(f"v2/edu-groups/{group_id}/subjects")
    
    async def get_person_marks_v2(
        self, 
        person_id: int, 
        start: str, 
        end: str
    ) -> Dict[str, Any]:
        """
        Получить оценки ученика (v2 API).
        
        Args:
            person_id: ID персоны
            start: Начальная дата (YYYY-MM-DD)
            end: Конечная дата (YYYY-MM-DD)
            
        Returns:
            Оценки ученика за период
        """
        return await self._get(f"v2/persons/{person_id}/marks/{start}/{end}")
    
    async def get_school_memberships_v2(self, school_id: int) -> Dict[str, Any]:
        """
        Получить членство в школе (v2 API).
        
        Args:
            school_id: ID школы
            
        Returns:
            Информация о членстве
        """
        return await self._get(f"v2/schools/{school_id}/memberships")
    
    # ==========================================
    # Дополнительные методы v1
    # ==========================================
    
    async def get_criteria_marks(self, work_id: int) -> Dict[str, Any]:
        """
        Получить критериальные оценки работы.
        
        Args:
            work_id: ID работы
            
        Returns:
            Критериальные оценки
        """
        return await self._get(f"v1/works/{work_id}/criteria-marks")
    
    async def get_lesson_details(self, lesson_id: int) -> Dict[str, Any]:
        """
        Получить детальную информацию об уроке.
        
        Args:
            lesson_id: ID урока
            
        Returns:
            Детали урока
        """
        return await self._get(f"v1/lessons/{lesson_id}")
    
    async def get_work_details(self, work_id: int) -> Dict[str, Any]:
        """
        Получить детали работы (домашнего задания).
        
        Args:
            work_id: ID работы
            
        Returns:
            Детали работы
        """
        return await self._get(f"v1/works/{work_id}")
    
    async def get_person_classmates(self, person_id: int) -> List[Dict[str, Any]]:
        """
        Получить одноклассников ученика.
        
        Args:
            person_id: ID персоны
            
        Returns:
            Список одноклассников
        """
        return await self._get(f"v1/persons/{person_id}/classmates")
    
    async def get_group_teachers(self, group_id: int) -> List[Dict[str, Any]]:
        """
        Получить учителей класса.
        
        Args:
            group_id: ID класса
            
        Returns:
            Список учителей класса
        """
        return await self._get(f"v1/edu-groups/{group_id}/teachers")
    
    async def get_group_parallel(self, group_id: int) -> List[Dict[str, Any]]:
        """
        Получить параллельные классы.
        
        Args:
            group_id: ID класса
            
        Returns:
            Список классов той же параллели
        """
        return await self._get(f"v1/edu-groups/{group_id}/parallel")
    
    # ==========================================
    # Посещаемость (расширенные методы)
    # ==========================================
    
    async def get_lesson_attendance(self, lesson_id: int) -> List[Dict[str, Any]]:
        """
        Получить данные о посещаемости урока.
        
        Args:
            lesson_id: ID урока
            
        Returns:
            Записи посещаемости урока
        """
        return await self._get(f"v1/lessons/{lesson_id}/log-entries")
    
    async def get_person_attendance(
        self, 
        person_id: int, 
        start: str, 
        end: str
    ) -> List[Dict[str, Any]]:
        """
        Получить посещаемость ученика за период.
        
        Args:
            person_id: ID персоны
            start: Начальная дата (YYYY-MM-DD)
            end: Конечная дата (YYYY-MM-DD)
            
        Returns:
            Записи посещаемости ученика
        """
        return await self._get(
            f"v1/persons/{person_id}/lesson-log-entries/{start}/{end}"
        )
    
    # ==========================================
    # Отчёты
    # ==========================================
    
    async def get_group_marks_report(
        self, 
        group_id: int, 
        start: str, 
        end: str
    ) -> Dict[str, Any]:
        """
        Получить отчёт по оценкам класса.
        
        Args:
            group_id: ID класса
            start: Начальная дата (YYYY-MM-DD)
            end: Конечная дата (YYYY-MM-DD)
            
        Returns:
            Сводный отчёт по оценкам класса
        """
        return await self._get(
            f"v1/edu-groups/{group_id}/reporting-period-marks/{start}/{end}"
        )
    
    async def get_person_average_marks(
        self, 
        person_id: int, 
        start: str, 
        end: str
    ) -> Dict[str, Any]:
        """
        Получить средние оценки ученика.
        
        Args:
            person_id: ID персоны
            start: Начальная дата (YYYY-MM-DD)
            end: Конечная дата (YYYY-MM-DD)
            
        Returns:
            Средние оценки по предметам
        """
        return await self._get(
            f"v1/persons/{person_id}/average-marks/{start}/{end}"
        )
