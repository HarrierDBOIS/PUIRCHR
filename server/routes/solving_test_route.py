from ..get_data.tema1.get_data_from_decision_making_data import (
    read_decision_making_data,
)
from ..get_data.tema1.get_data_from_delineation import read_delineation_data
from ..get_data.tema1.get_data_from_role_in_team import read_role_data
from ..get_data.tema2.get_data_from_difining_staff_skills import read_defining_data
from ..get_data.tema2.get_data_from_effectiveness import read_effectiveness_data
from ..get_data.tema2.get_data_from_rejections import read_rejections_data
from ..get_data.tema3.get_data_from_support import read_support_data
from ..get_data.tema4.get_data_from_motivation import read_motivation_data
from ..get_data.tema3.get_data_from_process import read_process_data
from ..get_data.tema3.get_data_from_mark import read_mark_data
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

        case "Определение навыков рекрутера":
            data = await read_defining_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Эффективность собеседований":
            data = await read_effectiveness_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Работа с отказами и кандидатами":
            data = await read_rejections_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Организация процесса адаптации":
            data = await read_process_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Поддержка новичков":
            data = await read_support_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Оценка результатов адаптации":
            data = await read_mark_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Система мотивации в компании":
            data = await read_motivation_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Индивидуальная мотивация":
            from ..get_data.tema4.get_data_from_idividual_motivation import (
                read_individual_motivation_data,
            )

            data = await read_individual_motivation_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Профилактика демотивации":
            from ..get_data.tema4.get_data_from_demotivation import (
                read_demotivation_data,
            )

            data = await read_demotivation_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Базовая система компенсаций":
            from ..get_data.tema5.get_data_from_system_credit import read_credit_data

            data = await read_credit_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Гибкие системы стимулирования":
            from ..get_data.tema5.get_data_from_stimylate_system import (
                read_stimylate_data,
            )

            data = await read_stimylate_data()
            count = 0
            for _ in data["data"]:
                count += 1
        case "Оценка эффективности компенсаций":
            from ..get_data.tema5.get_data_from_effictivity_credit import (
                read_effictiviti_credit_data,
            )

            data = await read_effictiviti_credit_data()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Диагностика проблемного поведения":
            from ..get_data.tema6.get_data_from_problem_atention import (
                read_problem_atention,
            )

            data = await read_problem_atention()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Методы работы с проблемными сотрудникам":
            from ..get_data.tema6.get_data_from_cases import (
                read_cases,
            )

            data = await read_cases()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Профилактика проблемного поведения":
            from ..get_data.tema6.get_data_from_res_prob_at import (
                read_resolve_problem_atention,
            )

            data = await read_resolve_problem_atention()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Формирование команды: подбор и роли":
            from ..get_data.tema7.get_data_from_create_a_team import (
                read_creat_a_team,
            )

            data = await read_creat_a_team()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Командная динамика и взаимодействие":
            from ..get_data.tema7.get_data_from_dinamyc_team import (
                read_dynamyc_team,
            )

            data = await read_dynamyc_team()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Развитие и результативность команды":
            from ..get_data.tema7.get_data_from_develop_team import (
                read_develop_team,
            )

            data = await read_develop_team()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Оценка потребностей в развитии персонала":
            from ..get_data.tema8.get_data_from_mark_develop import (
                read_mark_develop,
            )

            data = await read_mark_develop()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Методы развития персонала":
            from ..get_data.tema8.get_data_from_methods_develop import (
                read_mark_methods_develop,
            )

            data = await read_mark_methods_develop()
            count = 0
            for _ in data["data"]:
                count += 1

        case "Оценка эффективности программ развития":
            from ..get_data.tema8.get_data_from_program_develop import (
                read_mark_program_develop,
            )

            data = await read_mark_program_develop()
            count = 0
            for _ in data["data"]:
                count += 1

    return templates.TemplateResponse(
        "test.html", {"request": request, "data": data, "count": count}
    )
