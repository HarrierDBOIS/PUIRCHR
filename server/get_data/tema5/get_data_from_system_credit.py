import csv
import aiofiles


async def read_credit_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema5\data_from_system_credit.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Система мотивации в компании",
            "description": 'Тест "Базовая система компенсаций" предназначен для оценки справедливости и прозрачности системы оплаты труда в вашей организации. Он помогает выявить, насколько эффективно вы устанавливаете заработную плату и условия премирования, а также как это соотносится с рыночными стандартами. Тест будет полезен HR-менеджерам и руководителям, стремящимся улучшить систему компенсаций и повысить удовлетворенность сотрудников.',
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
                    "answer_E": row[6],
                }
            )

        return data


def get_result_from_credit(score: int):
    if score <= 25:
        description = "Система мотивации слабая. Введите KPI и регулярные опросы потребностей.   Введите ежемесячные 'дни обратной связи' и простые бонусы (например, внеплановый выходной).  "
    elif 26 <= score <= 40:
        description = (
            "База есть, но требует доработок (например, индивидуальный подход).  "
        )
    else:
        description = (
            "Сбалансированная система. Делитесь опытом и тестируйте инновации.  "
        )
    return {"description": description}
