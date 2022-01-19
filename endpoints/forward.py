from fastapi import APIRouter, BackgroundTasks
from api_functions import ResponseModel, ErrorResponseModel, Info
import requests
from fastapi.responses import JSONResponse

router = APIRouter()

def send_summary(summary):
    result = requests.post("https://github-chmurowekoksy-postmatebackend-vka23nnggq-uc.a.run.app/report/", summary)
    if result.status_code != 200:
        raise Exception(result.text)

def test_url(info: Info):
    try:
        summary = {"id": info.id}
        for _ in range(info.quantity):

            method = info.method.lower()
            if method == "get":
                result = requests.get(info.url)
            elif method == "post":
                result = requests.post(info.url, info.body)
            else:
                result = request.get(info.url)

            if result.status_code not in summary:
                summary[result.status_code] = 1
            else:
                summary[result.status_code] += 1
        send_summary(summary)
    except Exception as e:
        raise Exception(e)



# forward geocoding
@router.post("/test", name="Load testing", description="Tests given url")
async def forward(info: Info, background_tasks: BackgroundTasks):
    """Returns latitude and longitude of a given address."""

    try:
        background_tasks.add_task(test_url, info)
        return JSONResponse(
            status_code=200,
            content=f"{info.url} is being tested"
        )

    except Exception as e:
        return ErrorResponseModel(503, e)
