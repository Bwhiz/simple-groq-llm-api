from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from sample import *
app = FastAPI()


@app.get('/healthcheck/')
async def healthcheck():

    return {
        "application" : "simple LLM API",
        "message" : "up & running"
    }

@app.post('/chat')
async def generate_func(request: Request):

    query = await request.json()
    model = query["model"]

    if model not in models:
        return JSONResponse(content={"error": "model not found"}, status_code=404)


    response = generate(
        model,
        query['questions'],
        temperature=query['temperature']
    )

    return JSONResponse(content={
        "status": "success",
        "response" : response
    }
    )

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8080)