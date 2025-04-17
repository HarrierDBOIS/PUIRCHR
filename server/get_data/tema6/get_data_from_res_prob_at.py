import csv
import aiofiles


async def read_resolve_problem_atention(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema6\data_from_resolve_proble_atention.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Профилактика проблемного поведения",
            "description": 'Тест "Профилактика проблемного поведения" предназначен для оценки мер, которые ваша компания принимает для предотвращения повторения сложных ситуаций с сотрудниками. Он помогает выявить, насколько эффективно вы анализируете прошлые ошибки и внедряете проактивные стратегии для создания здоровой рабочей среды. Тест будет полезен HR-специалистам, руководителям и лидерам команд, стремящимся минимизировать риски возникновения проблемного поведения и повысить уровень удовлетворенности сотрудников.',
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


def get_result_from_resolve_problem_atention(score: int):
    if score <= 20:
        description = 'Реактивный подход.  Запустите программу "Ранние сигналы" (ежемесячные pulse-опросы + чат-бот для жалоб).  '
    elif 21 <= score <= 30:
        description = 'Частичная профилактика.  Введите "День культуры" с разбором кейсов и ролевыми играми. '
    else:
        description = "Системная работа.  Используйте big data для выявления паттернов проблемного поведения (например, связь между перегрузкой и саботажем)."
    return {"description": description}
