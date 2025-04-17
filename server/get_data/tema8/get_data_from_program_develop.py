import csv
import aiofiles


async def read_mark_program_develop(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema8\data_from_program_develop.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Оценка эффективности программ развития",
            "description": 'Тест "Оценка эффективности программ развития" позволяет оценить, насколько системно вы измеряете результаты обучения и его влияние на бизнес. Он помогает выявить, используете ли вы метрики, такие как ROI, KPI и обратная связь, для анализа эффективности программ. Тест будет полезен HR-аналитикам и руководителям, стремящимся к data-driven управлению развитием персонала.',
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


def get_result_from_program_develop(score: int):
    if score <= 20:
        description = " Результаты не отслеживаются.  Введите обязательные post-training отчеты от сотрудников и руководителей.  "
    elif 21 <= score <= 30:
        description = 'Частичная оценка.  Добавьте "контрольные точки" через 1/3/6 месяцев после обучения.  '
    else:
        description = "Полный цикл анализа.  Автоматизируйте сбор данных через интеграцию LMS (системы управления обучением) с HRM."
    return {"description": description}
