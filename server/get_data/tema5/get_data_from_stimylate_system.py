import csv
import aiofiles


async def read_stimylate_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema5\data_from_stimylate_system.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Гибкие системы стимулирования",
            "description": 'Тест "Гибкие системы стимулирования" предназначен для оценки эффективности нестандартных методов мотивации, используемых в вашей организации. Он помогает выявить, насколько разнообразны и инновационны методы стимулирования, которые вы предлагаете своим сотрудникам. Тест будет полезен HR-менеджерам и руководителям, стремящимся повысить вовлеченность и удовлетворенность сотрудников через нестандартные подходы.',
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


def get_result_from_stimylate(score: int):
    if score <= 17:
        description = "Стимулирование ограничено. Начните с малого — введите реферальные бонусы или 'бонус на выбор'.  "
    elif 18 <= score <= 24:
        description = "Умеренное разнообразие. Добавьте profit-sharing для топ-менеджеров и командные бонусы.  "
    else:
        description = "Инновационный подход. Экспериментируйте с NFT-бонусами или персональными крипто-вознаграждениями для digital-сотрудников. "
    return {"description": description}
