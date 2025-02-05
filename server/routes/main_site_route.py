from fastapi import routing, Request
from fastapi.templating import Jinja2Templates


router = routing.APIRouter()
templates = Jinja2Templates(directory=r"C:\Users\kukid\PycharmProjects\puirchr\PUIRCHR")


@router.get("/api/main/all/test/")
async def all_test(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})
