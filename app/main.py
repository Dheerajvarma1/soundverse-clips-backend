from fastapi import FastAPI
from app.routes import clips
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()


app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

app.include_router(clips.router)
