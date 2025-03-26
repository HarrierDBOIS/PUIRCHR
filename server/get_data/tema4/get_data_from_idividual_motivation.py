import csv
import aiofiles


async def read_individual_motivation_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema4\data_from_idivisual_motivation.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Индивидуальная мотивация",
            "description": 'Тест "Индивидуальная мотивация" предназначен для оценки того, насколько эффективно ваша организация учитывает личные интересы и мотивацию сотрудников. Он позволяет выявить, насколько персонализирован подход к мотивации, и насколько сотрудники чувствуют свою ценность в команде. Тест будет полезен HR-менеджерам и руководителям, стремящимся создать более индивидуализированные условия работы и повысить вовлеченность сотрудников.',
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


def get_result_from_individual_motivation(score: int):
    if score <= 17:
        description = (
            "Персонализация отсутствует. Начните с регулярных встреч и анкетирования.  "
        )
    elif 18 <= score <= 24:
        description = "Частичный учет. Внедрите индивидуальные планы мотивации.  "
    else:
        description = "Отличный подход. Сотрудники чувствуют ценность своего вклада.  Внедрите AI-аналитику engagement (анализ тональности переписок, чат-боты для сбора анонимного фидбека).  "
    return {"description": description}
