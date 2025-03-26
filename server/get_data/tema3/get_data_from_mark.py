import csv
import aiofiles


async def read_mark_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema3\get_mark_result.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Оценка результатов адаптации",
            "description": 'Тест "Оценка результатов адаптации" предназначен для оценки методов измерения успешности процесса адаптации новых сотрудников в вашей компании. Он помогает выявить, насколько эффективно вы отслеживаете прогресс новичков и используете полученные данные для улучшения адаптационного процесса. Тест будет полезен HR-специалистам и руководителям, стремящимся повысить качество адаптации и обеспечить лучшую интеграцию новых сотрудников в команду.',
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
                    "answer_D": row[5],
                }
            )

        return data


def get_result_from_mark(score: int):
    if score <= 20:
        description = (
            "Результаты адаптации не отслеживаются. Внедрите регулярную оценку.  "
        )
    elif 21 <= score <= 30:
        description = "Частичный анализ. Добавьте объективные метрики (KPI, опросы).  "
    else:
        description = "Системный подход. Используйте данные для прогнозирования успешности найма.   Внедрите AI-аналитику (например, оценку тональности чатов новичка) или индивидуальные планы развития."
    return {"description": description}
