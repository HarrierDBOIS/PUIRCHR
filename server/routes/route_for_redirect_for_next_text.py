from fastapi import routing, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from ..get_data.get_data_from_decision_making_data import read_decision_making_data

router = routing.APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")


@router.post("/api/main/test/{name}/")
async def all_test(request: Request, name: str, text: str = Form(...)):
    if text is None:
        raise HTTPException(status_code=404, detail="Где-то я обосрался")
    data = {

    }
    match text:
        case "Тест на навык принятия решений":
            name = "Тест на навык принятия решений"
            description = "Данный тест поможет вам узнать себя получше в вопросе принятия решений"
            data["name"] = name
            data["description"] = description
        case "Способность к делегированию полномочий":
            ...
        case "Тест на определение роли в команде":
            ...
    return templates.TemplateResponse("test-preview.html", {"request": request, "data": data})
