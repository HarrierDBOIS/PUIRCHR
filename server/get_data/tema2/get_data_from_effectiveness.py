import csv
import aiofiles


async def read_effectiveness_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema2\the_effectiveness_of_interviews_data.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Эффективность собеседований",
            "description": " Тест Эффективность собеседований предназначен для оценки ваших методов проведения собеседований и выявления сильных и слабых сторон в процессе интервьюирования кандидатов. Он помогает рекрутерам и HR-специалистам понять, насколько структурированно и эффективно они проводят собеседования, а также какие аспекты требуют улучшения. Тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся повысить качество своих интервью.",
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


def get_result_from_effectiveness(score: int):
    if score <= 17:
        description = "Собеседования проводятся хаотично. Внедрите структурированный подход и чек-листы."
    elif 18 <= score <= 24:
        description = "Хороший уровень, но можно улучшить глубину оценки."
    else:
        description = "Системный подход. Продолжайте оттачивать технику и адаптировать методы под разные роли."
    return {"description": description}
