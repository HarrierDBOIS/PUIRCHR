import csv
import aiofiles


async def read_mark_develop(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema8\data_from_mark_in_develop.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Оценка потребностей в развитии персонала",
            "description": 'Тест "Оценка потребностей в развитии персонала" помогает выявить, насколько системно и глубоко вы анализируете потребности в обучении сотрудников. Он позволяет понять, учитываете ли вы ключевые факторы, такие как карьерные цели, рыночные тренды и навыковые пробелы. Тест будет полезен HR-специалистам и руководителям, стремящимся создать стратегию развития персонала, соответствующую целям компании.',
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


def get_result_from_mark_develop(score: int):
    if score <= 25:
        description = "Потребности определяются стихийно.  Внедрите ежегодный Skills Gap Analysis и индивидуальные планы развития (IDP).  "
    elif 26 <= score <= 40:
        description = "Есть система, но не хватает глубины.  Добавьте регулярные кадровые прогнозы и матрицу компетенций для каждой должности.  "
    else:
        description = "Стратегический подход.  Используйте AI-аналитику для прогнозирования будущих навыков (например, для цифровой трансформации).  "
    return {"description": description}
