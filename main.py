from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from server.routes.main_site_route import router as main_site_router
from server.routes.route_for_redirect_for_next_text import router as route_for_redirect_for_next_text
from server.routes.solving_test_route import router as solving_test_route


app = FastAPI()

app.mount("/static", StaticFiles(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR\media"), name="static")

app.include_router(solving_test_route)
app.include_router(main_site_router)
app.include_router(route_for_redirect_for_next_text)
