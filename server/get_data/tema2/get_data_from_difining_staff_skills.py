import csv
import aiofiles


async def read_defining_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema2\defining_staff_skills_data.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Определение навыков рекрутера",
            "description": "Тест 'Определение навыков рекрутера' предназначен для оценки уровня знаний и навыков в области подбора персонала. Он помогает рекрутерам и HR-специалистам определить свои сильные и слабые стороны в процессе рекрутинга, включая методы интервьюирования, оценку кандидатов и взаимодействие с нанимающими менеджерами. Этот тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся улучшить свою практику.",
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


def get_result_from_defining(score: int):
    if score <= 25:
        description = "0–25 балла: Новичок. Вам стоит углубиться в основы рекрутинга, пройти курсы и больше практиковаться."
    elif 26 <= score <= 40:
        description = "26–40 баллов – Опытный специалист. У вас хорошая база, но есть зоны для роста (например, сложные подборы или новые инструменты). "
    else:
        description = "Эксперт. Продолжайте развиваться, делитесь знаниями и внедряйте инновации в процесс. "
    return {"description": description}
