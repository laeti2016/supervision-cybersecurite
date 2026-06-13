from fastapi import FastAPI, Request
app = FastAPI()

@app.post('/{canal}')
async def recevoir(canal: str, request: Request):
    data = await request.json()
    for alerte in data.get('alerts', []):
        nom = alerte['labels'].get('alertname', '?')
        sev = alerte['labels'].get('severity', '?')
        print(f'[{canal}] {nom} (severity={sev}) statut={alerte["status"]}',
              flush=True)
    return {'recu': len(data.get('alerts', []))}
