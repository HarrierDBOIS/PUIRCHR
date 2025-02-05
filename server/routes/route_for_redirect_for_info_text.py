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
            description = ("Этот тест предназначен для оценки ваших подходов к процессу принятия решений в "
                           "различных ситуациях. Он помогает выявить, насколько уверенно и осознанно вы принимаете"
                           " решения, а также как ваши эмоции, интуиция и логика влияют на ваш выбор.")
            data["name"] = name
            data["description"] = description
        case "Способность к делегированию полномочий":
            name = "Способность к делегированию полномочий"
            description = ("Данный тест выявляет способность руководителя организовать свой труд так, "
                           "чтобы шире привлекать к управлению производством членов коллектива,"
                           " больше использовать «делегирование» обязанностей. "
                           "Ответьте на приведенные ниже вопросы «да» или «нет».")
            data["name"] = name
            data["description"] = description
        case "Тест на определение роли в команде":
            name = "Тест на определение роли в команде"
            description = "Данный тест поможет вам выяснить какую роль вы подсознательно хотите занимать в команде."
            data["name"] = name
            data["description"] = description
    return templates.TemplateResponse("test-preview.html", {"request": request, "data": data})
