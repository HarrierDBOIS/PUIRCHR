import csv
import aiofiles


async def read_dynamyc_team(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema7\data_for_dinamyc_team.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Командная динамика и взаимодействие",
            "description": 'Тест "Командная динамика и взаимодействие" направлен на оценку мер, которые вы принимаете для поддержания эффективной работы команды. Он помогает выявить, насколько регулярно вы проводите мероприятия для улучшения взаимодействия и решения конфликтов. Тест будет полезен руководителям и HR-менеджерам, заинтересованным в создании гармоничной командной культуры.',
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


def get_result_from_dynamic_team(score: int):
    if score <= 20:
        description = "Результативность не отслеживается.  Введите 2-3 командных KPI (например, % выполнения sprint goals).  "
    elif 21 <= score <= 30:
        description = "Оценка есть, но не глубокая.  Добавьте quarterly-обзоры с разбором успехов/провалов.  "
    else:
        description = "Data-driven развитие.  Внедрите систему 360° для оценки вклада каждого в командный результат."
    return {"description": description}
