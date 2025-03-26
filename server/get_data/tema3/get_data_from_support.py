import csv
import aiofiles


async def read_support_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema3\data_support_new.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Поддержка новичков",
            "description": 'Тест "Поддержка новичков" предназначен для оценки уровня поддержки, которую новые сотрудники получают в первые дни и недели своей работы. Он помогает выявить, насколько эффективно организована помощь новичкам в процессе их адаптации к рабочему процессу и корпоративной культуре. Тест будет полезен HR-специалистам и руководителям, стремящимся создать комфортные условия для новых сотрудников, повысить их вовлеченность и продуктивность.',
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


def get_result_from_support(score: int):
    if score <= 17:
        description = "Новички чувствуют себя потерянными. Увеличьте внимание к их потребностям.  Начните с малого — введите чек-листы и встречи с HR раз в 2 недели.  "
    elif 18 <= score <= 24:
        description = "Умеренная поддержка. Добавьте регулярные check-in встречи.  Добавьте feedback от коллег и цифровые метрики (например, время на выполнение стандартной задачи).  "
    else:
        description = "Отличная практика. Сотрудники быстро вливаются в работу.  "
    return {"description": description}
