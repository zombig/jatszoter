from fastapi import FastAPI

from .routes.create import router as create_router

PREFIX = '/api/v1'

app = FastAPI(title='Jatszoter Agent Service')

app.include_router(create_router, prefix=PREFIX)
