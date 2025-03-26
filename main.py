from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from server.routes.main_site_route import router as main_site_router
from server.routes.route_for_redirect_for_info_text import (
    router as route_for_redirect_for_next_text,
)
from server.routes.solving_test_route import router as solving_test_route
from server.routes.route_for_result import router as result_route


app = FastAPI()

app.mount(
    "/media",
    StaticFiles(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\media"),
    name="media",
)
app.mount(
    "/static",
    StaticFiles(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\static\css"),
    name="static",
)

app.include_router(solving_test_route)
app.include_router(result_route)
app.include_router(main_site_router)
app.include_router(route_for_redirect_for_next_text)


# from server.get_data.get_data_from_decision_making_data import read_decision_making_data
# import asyncio
#
# data = {}
# async def a(text="Тест на навык принятия решений"):
#     global data
#     match text:
#         case "Тест на навык принятия решений":
#             data = await read_decision_making_data()
#             count = 0
#             for _ in data["data"]:
#                 count += 1
#
#         case "Способность к делегированию полномочий":
#             ...
#         case "Тест на определение роли в команде":
#             ...
#     print(count)
#
# asyncio.run(a())
