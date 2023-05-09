from fastapi import FastAPI, WebSocket,Request,WebSocketDisconnect,Form,Response 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List 

app = FastAPI()

# --------------------create the class for  WEBSOCKET connection------------------
class ConnectionManager:
    # creating constructor for initilizing the virable by default it is empty 
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    # creating  method for WEBSOCKET connection
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # creating  method for WEBSOCKET disconnection
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # creating  method for broadcasting the message
    async def broadcast(self, message: dict):
       
        for connection in self.active_connections:
            await connection.send_json(message)

# ---------------creating a object of ConnectionManager--------------
manager = ConnectionManager()


# ---------------Using Jinja Tamplates to return frontend--------------

templates = Jinja2Templates(directory="Fontend")

# ----------------------- signup related function,api and HTLM Response start -------------------


# User registration form is returning here HTML Response 
@app.get("/",response_class=HTMLResponse)  
async def home(request: Request):
    return templates.TemplateResponse("userRegistration.html",{"request": request})

# creating api for setting the cookie session
@app.post("/submitform")
async def Registration(response:Response,user: str = Form()):
    response.set_cookie(key="X-Authorization", value=user, httponly=True)
      
# creating  api to get the username     
@app.get("/user")
def sendUserDetails(request:Request):
    user = request.cookies.get("X-Authorization")
    return {'details':user}


#-----------------------question related function and websockets connection start -------------------

# this is the HTML Response for the question page        
@app.get("/question",response_class=HTMLResponse) 
async def question(request: Request):
    return templates.TemplateResponse("question.html",{"request": request,})


#----------creating WEBSOCKET connection---------- 
@app.websocket("/ws/question")
async def websocket_endpoint(websocket: WebSocket):
    
    # calling the connect method of managerConnection class
    await manager.connect(websocket)
    
    # for getting the user details calling sendUserDetails function
    user =  sendUserDetails(websocket)
    socket_response = {'user':user['details'], 'message':'got connected'}
    
     # calling the broadcast method for broadcasting the message
    await manager.broadcast(socket_response)
    try:
        while True:
            # reciving the data in jason format 
            data = await websocket.receive_json()
            
            # calling the broadcast method for broadcasting the message 
            await manager.broadcast(data)
    except WebSocketDisconnect:
        
        # calling the disconnect method for disconnecting the socket of managerConnection class
        manager.disconnect(websocket)
        socket_response['message'] = 'disconnected'
        
        # calling the broadcast method for broadcasting the message
        await manager.broadcast(socket_response)

