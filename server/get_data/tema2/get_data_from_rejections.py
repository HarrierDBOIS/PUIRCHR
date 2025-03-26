import csv
import aiofiles


async def read_rejections_data(
    file_path: str = r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\tema2\dealing_with_rejections_data.csv",
):
    async with aiofiles.open(file_path, mode="r", encoding="utf-8") as file:
        lines = await file.readlines()

        data = {
            "name": "Работа с отказами и кандидатами",
            "description": "Тест Работа с отказами и кандидатами предназначен для оценки ваших методов взаимодействия с кандидатами, которым было отказано, а также вашей способности к эффективной коммуникации. Этот тест помогает рекрутерам и HR-специалистам понять, насколько успешно они работают с отклоненными кандидатами и как это влияет на репутацию компании. Тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся улучшить свою практику работы с кандидатами.",
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


def get_result_from_rejections(score: int):
    if score <= 20:
        description = (
            "Слабая работа с отказами. Риск потери репутации. Улучшите коммуникацию."
        )
    elif 21 <= score <= 30:
        description = "Удовлетворительно, но есть пробелы. Внедрите CRM для кандидатов."
    else:
        description = "Отличная практика. Вы укрепляете employer brand и создаете позитивный опыт."
    return {"description": description}
