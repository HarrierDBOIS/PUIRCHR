import csv
import aiofiles


async def read_creat_a_team(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema7\data_for_create_a_team.csv",
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
                    "answer_E": row[6],
                }
            )

        return data


def get_result_from_create_a_team(score: int):
    if score <= 25:
        description = "Команды формируются стихийно.  Внедрите оценку ролей по Белбину и тренинг по командной динамике для HR.  "
    elif 26 <= score <= 40:
        description = 'Есть система, но есть пробелы.  Добавьте "дни командной работы" на этапе подбора и инструменты для анализа совместимости.  '
    else:
        description = "Продуманный подход.  Используйте AI-алгоритмы для прогнозирования успешности командных комбинаций.  "
    return {"description": description}
