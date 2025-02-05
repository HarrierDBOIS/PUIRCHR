import csv
import aiofiles


async def read_decision_making_data(
        file_path: str = r'C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\server\data\decision_making_data.csv'):
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
        lines = await file.readlines()

        data = {
            "name": "Тест на навык принятия решений",
            "description": "Данный тест поможет вам узнать себя получше в вопросе принятия решений.",
            "data": [

            ]
        }
        reader = csv.reader(lines)
        reader.__next__()
        for row in reader:
            data["data"].append({
                "number": row[0],
                "question": row[1],
                "answer_A": row[2],
                "answer_B": row[3],
                "answer_C": row[4],
            })

        return data
