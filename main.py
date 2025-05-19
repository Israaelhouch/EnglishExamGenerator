import logging
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from backend.src.routes import generate_exam, get_history
from backend.src.routes.dependencies import verify_api_key



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(generate_exam.router, dependencies=[Depends(verify_api_key)])
app.include_router(get_history.router, dependencies=[Depends(verify_api_key)])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"},
    )



