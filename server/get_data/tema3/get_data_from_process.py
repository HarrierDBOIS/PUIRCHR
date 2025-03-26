import csv
import aiofiles


async def read_process_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema3\data_process_with_adaptive.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Организация процесса адаптации",
            "description": "Тест Организация процесса адаптации предназначен для оценки эффективности процесса адаптации новых сотрудников в вашей компании. Он помогает выявить, насколько хорошо организован этот процесс, а также какие аспекты требуют улучшения. Тест будет полезен HR-специалистам и руководителям, стремящимся создать более комфортные условия для новых сотрудников и повысить их вовлеченность и производительность.",
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


def get_result_from_process(score: int):
    if score <= 25:
        description = "Адаптация слабо структурирована. Внедрите четкий план и контроль.  Начните с малого — введите чек-листы и встречи с HR раз в 2 недели.  "
    elif 26 <= score <= 40:
        description = "Хорошая база, но можно улучшить наставничество и интеграцию в коллектив.  Добавьте feedback от коллег и цифровые метрики (например, время на выполнение стандартной задачи).  "
    else:
        description = "Отлаженная система. Делитесь опытом и оптимизируйте детали.  "
    return {"description": description}
