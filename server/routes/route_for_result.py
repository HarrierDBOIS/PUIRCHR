from ..get_data.tema1.get_data_from_decision_making_data import get_result_from_decision
from ..get_data.tema1.get_data_from_delineation import get_result_from_delineation
from ..get_data.tema1.get_data_from_role_in_team import get_result_from_role
from ..get_data.tema2.get_data_from_effectiveness import get_result_from_effectiveness
from ..get_data.tema2.get_data_from_rejections import get_result_from_rejections
from ..get_data.tema3.get_data_from_process import get_result_from_process
from ..get_data.tema3.get_data_from_mark import get_result_from_mark
from ..get_data.tema4.get_data_from_motivation import get_result_from_motivation
from ..get_data.tema2.get_data_from_difining_staff_skills import (
    get_result_from_defining,
)
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

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "wishing_answer": wishing_answer,
                    "test_name": test_name,
                },
            )
        case "Способность к делегированию полномочий":
            for answer in answers:
                if answer == "answer_A":
                    math_res += 1
            result = get_result_from_delineation(math_res)
            description = result.get("description")
            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )
        case "Тест на определение роли в команде":
            data = {"a": 0, "b": 0, "c": 0, "d": 0}
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
            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Определение навыков рекрутера":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5
            info = get_result_from_defining(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Эффективность собеседований":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
            info = get_result_from_effectiveness(data)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Работа с отказами и кандидатами":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    print(f"{answer}: {1}")
                    result += 1
                elif answer == "answer_B":
                    print(f"{answer}: {2}")
                    result += 2
                elif answer == "answer_C":
                    print(f"{answer}: {3}")
                    result += 3
                elif answer == "answer_D":
                    print(f"{answer}: {4}")
                    result += 4
            info = get_result_from_rejections(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Организация процесса адаптации":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5
            info = get_result_from_process(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Поддержка новичков":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
            info = get_result_from_process(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Оценка результатов адаптации":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
            info = get_result_from_mark(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Система мотивации в компании":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_C":
                    result += 5
            info = get_result_from_motivation(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Индивидуальная мотивация":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3

            from ..get_data.tema4.get_data_from_idividual_motivation import (
                get_result_from_individual_motivation,
            )

            info = get_result_from_individual_motivation(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Профилактика демотивации":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4

            from ..get_data.tema4.get_data_from_demotivation import (
                get_result_from_demotivation,
            )

            info = get_result_from_demotivation(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Базовая система компенсаций":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5

            from ..get_data.tema5.get_data_from_system_credit import (
                get_result_from_credit,
            )

            info = get_result_from_credit(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Гибкие системы стимулирования":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3

            from ..get_data.tema5.get_data_from_stimylate_system import (
                get_result_from_stimylate,
            )

            info = get_result_from_stimylate(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Оценка эффективности компенсаций":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4

            from ..get_data.tema5.get_data_from_effictivity_credit import (
                get_result_from_effictiviti_credit,
            )

            info = get_result_from_effictiviti_credit(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Диагностика проблемного поведения":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5

            from ..get_data.tema6.get_data_from_problem_atention import (
                get_result_from_problem_atention,
            )

            info = get_result_from_problem_atention(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Методы работы с проблемными сотрудникам":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3

            from ..get_data.tema6.get_data_from_cases import (
                get_result_from_cases,
            )

            info = get_result_from_cases(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Профилактика проблемного поведения":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4

            from ..get_data.tema6.get_data_from_res_prob_at import (
                get_result_from_resolve_problem_atention,
            )

            info = get_result_from_resolve_problem_atention(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Формирование команды: подбор и роли":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5

            from ..get_data.tema7.get_data_from_create_a_team import (
                get_result_from_create_a_team,
            )

            info = get_result_from_create_a_team(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Командная динамика и взаимодействие":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3

            from ..get_data.tema7.get_data_from_dinamyc_team import (
                get_result_from_dynamic_team,
            )

            info = get_result_from_dynamic_team(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Оценка потребностей в развитии персонала":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4
                elif answer == "answer_E":
                    result += 5

            from ..get_data.tema8.get_data_from_mark_develop import (
                get_result_from_mark_develop,
            )

            info = get_result_from_mark_develop(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Методы развития персонала":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3

            from ..get_data.tema8.get_data_from_methods_develop import (
                get_result_from_methods_develop,
            )

            info = get_result_from_methods_develop(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )

        case "Оценка эффективности программ развития":
            result = 0
            for answer in answers:
                if answer == "answer_A":
                    result += 1
                elif answer == "answer_B":
                    result += 2
                elif answer == "answer_C":
                    result += 3
                elif answer == "answer_D":
                    result += 4

            from ..get_data.tema8.get_data_from_program_develop import (
                get_result_from_program_develop,
            )

            info = get_result_from_program_develop(result)
            description = info.get("description")

            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "math_res": math_res,
                    "description": description,
                    "test_name": test_name,
                },
            )
