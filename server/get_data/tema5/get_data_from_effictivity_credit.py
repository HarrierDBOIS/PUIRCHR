import csv
import aiofiles


async def read_effictiviti_credit_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema5\data_from_effictiviti_credit.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Оценка эффективности компенсаций",
            "description": 'Тест "Оценка эффективности компенсаций" предназначен для оценки того, как ваша организация измеряет влияние системы оплаты труда на продуктивность сотрудников. Он помогает выявить, насколько глубоко и системно вы анализируете данные, связанные с компенсациями, и как это влияет на общую эффективность работы. Тест будет полезен HR-менеджерам и руководителям, стремящимся оптимизировать систему оплаты и повысить производительность команды.',
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


def get_result_from_effictiviti_credit(score: int):
    if score <= 20:
        description = (
            "Данные не используются. Начните с pulse-опросов и анализа turnover rate.  "
        )
    elif 21 <= score <= 30:
        description = "Частичный анализ. Внедрите A/B-тестирование бонусных программ.  "
    else:
        description = "Data-driven подход. Используйте predictive analytics для прогнозирования эффекта изменений."
    return {"description": description}
