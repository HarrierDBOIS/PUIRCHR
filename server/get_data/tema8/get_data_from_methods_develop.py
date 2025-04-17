import csv
import aiofiles


async def read_mark_methods_develop(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema8\data_from_methods_develop.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Методы развития персонала",
            "description": 'Тест "Методы развития персонала" направлен на оценку инструментов и подходов, которые вы используете для обучения сотрудников. Он помогает определить, насколько разнообразны и эффективны ваши методы, от внутренних тренингов до геймификации. Тест будет полезен лидерам команд и HR-менеджерам, заинтересованным в создании современной и гибкой системы обучения.',
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


def get_result_from_methods_develop(score: int):
    if score <= 17:
        description = 'Обучение фрагментарное.  Запустите "Месяц развития" с обязательными курсами и финальным тестированием.  '
    elif 26 <= score <= 40:
        description = 'Разнообразие есть, но нет системы.  Создайте "меню обучения" с обязательными и опциональными модулями.  '
    else:
        description = " Инновационные методы.  Внедрите VR-тренажеры для сложных навыков (например, переговоры, управление кризисами).  "
    return {"description": description}
