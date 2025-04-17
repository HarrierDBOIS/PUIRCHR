import csv
import aiofiles


async def read_cases(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema6\data_from_cases_for_problem_workers.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Методы работы с проблемными сотрудниками",
            "description": 'Тест "Методы работы с проблемными сотрудниками" предназначен для оценки эффективности используемых в вашей компании подходов к управлению сложными ситуациями с персоналом. Он помогает выявить, насколько системно и продуманно вы применяете инструменты корректировки поведения сотрудников, от планов улучшения до крайних мер. Тест будет полезен руководителям, HR-специалистам и лидерам команд, стремящимся минимизировать негативное влияние проблемных ситуаций и повысить общую продуктивность команды.',
            "data": [],
        }

        reader = csv.reader(lines)
        reader.__next__()
        for row in reader:
            data["data"].append(
                {
                    "number": row[0],
                    "question": row[1],
                    "answer_A": row[2],
                    "answer_B": row[3],
                    "answer_C": row[4],
                }
            )

        return data


def get_result_from_cases(score: int):
    if score <= 17:
        description = "Нет стратегии работы.  Разработайте пошаговый алгоритм действий (например: беседа → PIP → перевод → увольнение).  "
    elif 18 <= score <= 24:
        description = 'Разрозненные методы.  Создайте "библиотеку кейсов" с решениями для типовых ситуаций (воркшопы для руководителей).  '
    else:
        description = " Гибкая и гуманная система.  Внедрите AI-аналитику для прогнозирования рисков (например, оценка риска увольнения проблемного сотрудника).  "
    return {"description": description}
