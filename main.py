from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/home", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "message": "Bem-vindo à Home!"})

@app.get("/cadastro", response_class=HTMLResponse)
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request, "titulo": "Cadastro de Produto"})

@app.post("/post_cadastro")
def post_cadastro( 
    nome: str = Form(...), 
    descricao: str = Form(...),
    estoque: int = Form(...),  
    preco: float = Form(...),
    categoria: str = Form(...)):
    
    return RedirectResponse("/", status_code=303)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bem-vindo à página inicial!"})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
