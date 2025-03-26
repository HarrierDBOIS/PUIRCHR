import csv
import aiofiles


async def read_demotivation_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema4\data_from_demotivation.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Профилактика демотивации",
            "description": 'Тест "Профилактика демотивации" предназначен для оценки методов работы вашей организации с признаками снижения вовлеченности сотрудников. Он помогает выявить, насколько эффективно вы отслеживаете и реагируете на потенциальные проблемы, связанные с демотивацией. Тест будет полезен HR-менеджерам и руководителям, стремящимся создать здоровую рабочую атмосферу и минимизировать риски потери кадров.',
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


def get_result_from_demotivation(score: int):
    if score <= 20:
        description = (
            "Демотивация игнорируется. Срочно внедрите регулярные pulse-опросы.  "
        )
    elif 21 <= score <= 30:
        description = "Реакция есть, но не системная. Обучите руководителей выявлять ранние признаки.  Добавьте индивидуальные мотивационные планы и обучение руководителей.  "
    else:
        description = "Проактивный подход. Компания минимизирует риски потери кадров."
    return {"description": description}
