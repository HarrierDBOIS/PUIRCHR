import csv
import aiofiles


async def read_delineation_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema1\delineation_data.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Способность к делегированию полномочий",
            "description": "Данный тест выявляет способность руководителя организовать свой труд так, "
            "чтобы шире привлекать к управлению производством членов коллектива, больше использовать"
            " «делегирование» обязанностей. Ответьте на приведенные ниже вопросы «да» или «нет».",
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
                }
            )

        return data


def get_result_from_delineation(score: int):
    if score <= 3:
        description = "0–3 балла: Вы хорошо управляете своей рабочей нагрузкой, умеете распределять задачи и эффективно планируете время. Главное – не расслабляться и продолжать соблюдать баланс."
    elif score <= 6:
        description = "4–6 баллов: У вас есть некоторые проблемы с управлением временем и нагрузкой. Стоит пересмотреть свои методы работы, научиться делегировать и избегать прокрастинации."
    else:
        description = "7–10 баллов: Ваша рабочая нагрузка явно выходит из-под контроля. Возможно, Вы берете на себя слишком много задач, не умеете отказываться или не используете эффективные инструменты управления временем. Вам стоит срочно пересмотреть свои рабочие привычки, чтобы избежать выгорания."
    return {"description": description}
