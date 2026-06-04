from fastapi import FastAPI

app = FastAPI()

@app.get('/')

async def root():
    return {"message":"Hello World"}

@app.get('/shipment/')
def get_shipment():
    return {
        'content': 'Study Table',
        'status': 'In Transit'
    }