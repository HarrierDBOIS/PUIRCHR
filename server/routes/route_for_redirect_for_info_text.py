from fastapi import routing, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates

router = routing.APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")


@router.post("/api/main/test/{name}/")
async def all_test(request: Request, text: str = Form(...)):
    if text is None:
        raise HTTPException(status_code=404, detail="Где-то я обосрался")
    data = {}
    match text:
        case "Тест на навык принятия решений":
            name = "Тест на навык принятия решений"
            description = (
                "Этот тест предназначен для оценки ваших подходов к процессу принятия решений в "
                "различных ситуациях. Он помогает выявить, насколько уверенно и осознанно вы принимаете"
                " решения, а также как ваши эмоции, интуиция и логика влияют на ваш выбор."
            )
            data["name"] = name
            data["description"] = description
        case "Способность к делегированию полномочий":
            name = "Способность к делегированию полномочий"
            description = (
                "Данный тест выявляет способность руководителя организовать свой труд так, "
                "чтобы шире привлекать к управлению производством членов коллектива,"
                " больше использовать «делегирование» обязанностей. "
                "Ответьте на приведенные ниже вопросы «да» или «нет»."
            )
            data["name"] = name
            data["description"] = description
        case "Тест на определение роли в команде":
            name = "Тест на определение роли в команде"
            description = "Данный тест поможет вам выяснить какую роль вы подсознательно хотите занимать в команде."
            data["name"] = name
            data["description"] = description
        case "Определение навыков рекрутера":
            name = "Определение навыков рекрутера"
            description = "Тест 'Определение навыков рекрутера' предназначен для оценки уровня знаний и навыков в области подбора персонала. Он помогает рекрутерам и HR-специалистам определить свои сильные и слабые стороны в процессе рекрутинга, включая методы интервьюирования, оценку кандидатов и взаимодействие с нанимающими менеджерами. Этот тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся улучшить свою практику."
            data["name"] = name
            data["description"] = description
        case "Эффективность собеседований":
            name = "Эффективность собеседований"
            description = " Тест Эффективность собеседований предназначен для оценки ваших методов проведения собеседований и выявления сильных и слабых сторон в процессе интервьюирования кандидатов. Он помогает рекрутерам и HR-специалистам понять, насколько структурированно и эффективно они проводят собеседования, а также какие аспекты требуют улучшения. Тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся повысить качество своих интервью."
            data["name"] = name
            data["description"] = description
        case "Работа с отказами и кандидатами":
            name = ("Работа с отказами и кандидатами",)
            description = "Тест Работа с отказами и кандидатами предназначен для оценки ваших методов взаимодействия с кандидатами, которым было отказано, а также вашей способности к эффективной коммуникации. Этот тест помогает рекрутерам и HR-специалистам понять, насколько успешно они работают с отклоненными кандидатами и как это влияет на репутацию компании. Тест будет полезен как начинающим рекрутерам, так и опытным специалистам, стремящимся улучшить свою практику работы с кандидатами."
            data["name"] = name
            data["description"] = description
        case "Организация процесса адаптации":
            name = "Организация процесса адаптации"
            description = "Тест Организация процесса адаптации предназначен для оценки эффективности процесса адаптации новых сотрудников в вашей компании. Он помогает выявить, насколько хорошо организован этот процесс, а также какие аспекты требуют улучшения. Тест будет полезен HR-специалистам и руководителям, стремящимся создать более комфортные условия для новых сотрудников и повысить их вовлеченность и производительность."
            data["name"] = name
            data["description"] = description
        case "Поддержка новичков":
            name = "Поддержка новичков"
            description = 'Тест "Поддержка новичков" предназначен для оценки уровня поддержки, которую новые сотрудники получают в первые дни и недели своей работы. Он помогает выявить, насколько эффективно организована помощь новичкам в процессе их адаптации к рабочему процессу и корпоративной культуре. Тест будет полезен HR-специалистам и руководителям, стремящимся создать комфортные условия для новых сотрудников, повысить их вовлеченность и продуктивность.'
            data["name"] = name
            data["description"] = description
        case "Оценка результатов адаптации":
            name = 'Тест "Оценка результатов адаптации" предназначен для оценки методов измерения успешности процесса адаптации новых сотрудников в вашей компании. Он помогает выявить, насколько эффективно вы отслеживаете прогресс новичков и используете полученные данные для улучшения адаптационного процесса. Тест будет полезен HR-специалистам и руководителям, стремящимся повысить качество адаптации и обеспечить лучшую интеграцию новых сотрудников в команду.'
            description = "ебать"
            data["name"] = name
            data["description"] = description
        case "Система мотивации в компании":
            name = "Система мотивации в компании"
            description = 'Тест "Система мотивации в компании" предназначен для оценки эффективности методов мотивации, используемых в вашей организации. Он помогает выявить сильные и слабые стороны системы мотивации, а также понять, насколько она соответствует ожиданиям сотрудников. Тест будет полезен HR-менеджерам, руководителям и всем, кто заинтересован в повышении вовлеченности и удовлетворенности сотрудников.'
            data["name"] = name
            data["description"] = description
        case "Индивидуальная мотивация":
            name = "Индивидуальная мотивация"
            description = 'Тест "Индивидуальная мотивация" предназначен для оценки того, насколько эффективно ваша организация учитывает личные интересы и мотивацию сотрудников. Он позволяет выявить, насколько персонализирован подход к мотивации, и насколько сотрудники чувствуют свою ценность в команде. Тест будет полезен HR-менеджерам и руководителям, стремящимся создать более индивидуализированные условия работы и повысить вовлеченность сотрудников.'
            data["name"] = name
            data["description"] = description
        case "Профилактика демотивации":
            name = "Профилактика демотивации"
            description = 'Тест "Профилактика демотивации" предназначен для оценки методов работы вашей организации с признаками снижения вовлеченности сотрудников. Он помогает выявить, насколько эффективно вы отслеживаете и реагируете на потенциальные проблемы, связанные с демотивацией. Тест будет полезен HR-менеджерам и руководителям, стремящимся создать здоровую рабочую атмосферу и минимизировать риски потери кадров.'
            data["name"] = name
            data["description"] = description
        case "Базовая система компенсаций":
            name = "Базовая система компенсаций"
            description = 'Тест "Базовая система компенсаций" предназначен для оценки справедливости и прозрачности системы оплаты труда в вашей организации. Он помогает выявить, насколько эффективно вы устанавливаете заработную плату и условия премирования, а также как это соотносится с рыночными стандартами. Тест будет полезен HR-менеджерам и руководителям, стремящимся улучшить систему компенсаций и повысить удовлетворенность сотрудников.'
            data["name"] = name
            data["description"] = description
        case "Гибкие системы стимулирования":
            name = "Гибкие системы стимулирования"
            description = 'Тест "Гибкие системы стимулирования" предназначен для оценки эффективности нестандартных методов мотивации, используемых в вашей организации. Он помогает выявить, насколько разнообразны и инновационны методы стимулирования, которые вы предлагаете своим сотрудникам. Тест будет полезен HR-менеджерам и руководителям, стремящимся повысить вовлеченность и удовлетворенность сотрудников через нестандартные подходы.'
            data["name"] = name
            data["description"] = description
        case "Оценка эффективности компенсаций":
            name = "Оценка эффективности компенсаций"
            description = 'Тест "Оценка результатов адаптации" предназначен для оценки методов измерения успешности процесса адаптации новых сотрудников в вашей компании. Он помогает выявить, насколько эффективно вы отслеживаете прогресс новичков и используете полученные данные для улучшения адаптационного процесса. Тест будет полезен HR-специалистам и руководителям, стремящимся повысить качество адаптации и обеспечить лучшую интеграцию новых сотрудников в команду.'
            data["name"] = name
            data["description"] = description
        case "Диагностика проблемного поведения":
            name = "Диагностика проблемного поведения"
            description = 'Тест "Оценка методов управления проблемными сотрудниками" предназначен для анализа эффективности ваших подходов к работе с непростыми сотрудниками. Он помогает выявить, насколько четко вы определяете причины проблемного поведения и используете ли корректные инструменты для их решения. Тест будет полезен руководителям, HR-менеджерам и лидерам команд, которые стремятся улучшить рабочую атмосферу, минимизировать конфликты и повысить продуктивность сотрудников.'
            data["name"] = name
            data["description"] = description
        case "Методы работы с проблемными сотрудникам":
            name = "Методы работы с проблемными сотрудникам"
            description = 'Тест "Методы работы с проблемными сотрудниками" предназначен для оценки эффективности используемых в вашей компании подходов к управлению сложными ситуациями с персоналом. Он помогает выявить, насколько системно и продуманно вы применяете инструменты корректировки поведения сотрудников, от планов улучшения до крайних мер. Тест будет полезен руководителям, HR-специалистам и лидерам команд, стремящимся минимизировать негативное влияние проблемных ситуаций и повысить общую продуктивность команды.'
            data["name"] = name
            data["description"] = description
        case "Профилактика проблемного поведения":
            name = "Профилактика проблемного поведения"
            description = 'Тест "Профилактика проблемного поведения" предназначен для оценки мер, которые ваша компания принимает для предотвращения повторения сложных ситуаций с сотрудниками. Он помогает выявить, насколько эффективно вы анализируете прошлые ошибки и внедряете проактивные стратегии для создания здоровой рабочей среды. Тест будет полезен HR-специалистам, руководителям и лидерам команд, стремящимся минимизировать риски возникновения проблемного поведения и повысить уровень удовлетворенности сотрудников.'
            data["name"] = name
            data["description"] = description
        case "Формирование команды: подбор и роли":
            name = "Формирование команды: подбор и роли"
            description = 'Тест "Формирование команды: подбор и роли" предназначен для оценки того, насколько продуманно и эффективно вы формируете команды. Он помогает понять, учитываете ли вы ключевые факторы, такие как психологическая совместимость, распределение ролей и разнообразие команды. Тест будет полезен HR-специалистам и руководителям, стремящимся создать сбалансированные и продуктивные команды.'
            data["name"] = name
            data["description"] = description
        case "Командная динамика и взаимодействие":
            name = "Командная динамика и взаимодействие"
            description = 'Тест "Командная динамика и взаимодействие" направлен на оценку мер, которые вы принимаете для поддержания эффективной работы команды. Он помогает выявить, насколько регулярно вы проводите мероприятия для улучшения взаимодействия и решения конфликтов. Тест будет полезен руководителям и HR-менеджерам, заинтересованным в создании гармоничной командной культуры.'
            data["name"] = name
            data["description"] = description
        case "Развитие и результативность команды":
            name = "Развитие и результативность команды"
            description = 'Тест "Развитие и результативность команды" позволяет оценить, насколько системно вы измеряете и улучшаете эффективность работы команды. Он помогает определить, используете ли вы метрики, обучение и другие инструменты для повышения производительности. Тест будет полезен лидерам команд и HR-специалистам, стремящимся к data-driven управлению.'
            data["name"] = name
            data["description"] = description
        case "Оценка потребностей в развитии персонала":
            name = "Оценка потребностей в развитии персонала"
            description = 'Тест "Оценка потребностей в развитии персонала" помогает выявить, насколько системно и глубоко вы анализируете потребности в обучении сотрудников. Он позволяет понять, учитываете ли вы ключевые факторы, такие как карьерные цели, рыночные тренды и навыковые пробелы. Тест будет полезен HR-специалистам и руководителям, стремящимся создать стратегию развития персонала, соответствующую целям компании.'
            data["name"] = name
            data["description"] = description
        case "Методы развития персонала":
            name = "Методы развития персонала"
            description = 'Тест "Методы развития персонала" направлен на оценку инструментов и подходов, которые вы используете для обучения сотрудников. Он помогает определить, насколько разнообразны и эффективны ваши методы, от внутренних тренингов до геймификации. Тест будет полезен лидерам команд и HR-менеджерам, заинтересованным в создании современной и гибкой системы обучения.'
            data["name"] = name
            data["description"] = description
        case "Оценка эффективности программ развития":
            name = "Оценка эффективности программ развития"
            description = 'Тест "Оценка эффективности программ развития" позволяет оценить, насколько системно вы измеряете результаты обучения и его влияние на бизнес. Он помогает выявить, используете ли вы метрики, такие как ROI, KPI и обратная связь, для анализа эффективности программ. Тест будет полезен HR-аналитикам и руководителям, стремящимся к data-driven управлению развитием персонала.'
            data["name"] = name
            data["description"] = description

    return templates.TemplateResponse(
        "test-preview.html", {"request": request, "data": data}
    )
