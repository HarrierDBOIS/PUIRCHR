from ..get_data.get_data_from_decision_making_data import read_decision_making_data
from ..get_data.get_data_from_delineation import read_delineation_data
from ..get_data.get_data_from_role_in_team import read_role_data
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")


@router.post("/api/main/test/{name}/test/")
async def receive_test_data(request: Request, text: str = Form(...)):
    data = None
    count = 0
    match text:
        case "Тест на навык принятия решений":
            data = await read_decision_making_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Способность к делегированию полномочий":
            data = await read_delineation_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Тест на определение роли в команде":
            data = await read_role_data()
            count = 0
            for _ in data["data"]:
                count += 1

    return templates.TemplateResponse("test.html", {"request": request, "data": data, "count": count})
