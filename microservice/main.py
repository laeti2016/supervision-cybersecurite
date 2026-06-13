import time, random
from fastapi import FastAPI, Request, Response
from prometheus_client import (Counter, Histogram,
    generate_latest, CONTENT_TYPE_LATEST)

app = FastAPI(title='Microservice Demo Telemetrie')

REQUEST_COUNT = Counter('http_requests_total',
    'Nombre total de requetes HTTP', ['method', 'endpoint', 'status'])
REQUEST_ERRORS = Counter('http_errors_total',
    'Nombre total de requetes en erreur', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds',
    'Latence des requetes HTTP en secondes', ['method', 'endpoint'],
    buckets=[.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5])

@app.middleware('http')
async def measure(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    ep = request.url.path
    REQUEST_LATENCY.labels('GET', ep).observe(elapsed)
    REQUEST_COUNT.labels('GET', ep, str(response.status_code)).inc()
    if response.status_code >= 500:
        REQUEST_ERRORS.labels('GET', ep).inc()
    return response

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/process')
def process(fail: int = 0, slow: float = 0.0):
    if slow > 0:
        time.sleep(min(slow, 10))
    if fail or random.random() < 0.05:
        return Response(status_code=500, content='Erreur simulee')
    return {'result': 'traitement OK'}

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
