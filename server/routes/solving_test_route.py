from ..get_data.get_data_from_decision_making_data import read_decision_making_data
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")


@router.post("/api/main/test/{name}/test/")
async def receive_test_data(request: Request, name: str, text: str = Form(...)):
    data = None
    match text:
        case "Тест на навык принятия решений":
            data = await read_decision_making_data()
        case "Способность к делегированию полномочий":
            ...
        case "Тест на определение роли в команде":
            ...
    return templates.TemplateResponse("test.html", {"request": request, "data": data})
