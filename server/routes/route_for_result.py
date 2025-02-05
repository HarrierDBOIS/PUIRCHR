from ..get_data.get_data_from_decision_making_data import get_result_from_decision
from ..get_data.get_data_from_delineation import get_result_from_delineation
from ..get_data.get_data_from_role_in_team import get_result_from_role
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")

@router.post("/api/main/test/result/")
async def receive_test_data(request: Request):

    data = await request.json()
    answers = data.get("answers")
    test_name = data.get("test_name")

    math_res = 0
    match test_name:
        case "Тест на навык принятия решений":
            for answer in answers:
                if answer == "answer_A":
                    math_res += 3
                elif answer == "answer_B":
                    math_res += 2
                else:
                    math_res += 1
            result = get_result_from_decision(math_res)
            description = result.get("description")

            wishing_answer = result.get("wishing")

            return templates.TemplateResponse("results.html", {"request": request, "math_res": math_res,
                                                       "description": description, "wishing_answer": wishing_answer,
                                                       "test_name": test_name})
        case "Способность к делегированию полномочий":
            for answer in answers:
                if answer == "answer_A":
                    math_res += 1
            result = get_result_from_delineation(math_res)
            description = result.get("description")
            return templates.TemplateResponse("results.html", {"request": request, "math_res": math_res,
                                                               "description": description,

                                                               "test_name": test_name})
        case "Тест на определение роли в команде":
            data = {"a": 0,
                    "b": 0,
                    "c": 0,
                    "d": 0}
            for answer in answers:
                if answer == "answer_A":
                    data["a"] += 1
                elif answer == "answer_B":
                    data["b"] += 1
                elif answer == "answer_C":
                    data["c"] += 1
                else:
                    data["d"] += 1
            result = get_result_from_role(data)
            description = result.get("description")
            return templates.TemplateResponse("results.html", {"request": request, "math_res": math_res,
                                                               "description": description,

                                                               "test_name": test_name})


