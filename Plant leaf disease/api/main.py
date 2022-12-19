from fastapi import FastAPI
import socket
socket.getaddrinfo('localhost', 8000)
import uvicorn
app = FastAPI()
@app.get("/ping")
async def ping():
    return "Hello, iam alive"
if __name__ == '__main__':
    uvicorn.run(app, host = 'locahost', port = 8000)
