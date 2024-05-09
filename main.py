from fastapi import FastAPI, HTTPException, Request
import sqlite3
import uuid
from pydantic import BaseModel


app = FastAPI()

class Inputs(BaseModel):
    nome: str
    cidade_partida: str
    cidade_chegada: str
    banda: str
    data: str

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('caronas.db')

from fastapi.responses import FileResponse

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "caronas.html"
    )

# Rota para criar uma nova carona
@app.post("/caronas/")
def create_caronas(inputs: Inputs):
    conn = connect_db()
    c = conn.cursor()
    carona_id = str(uuid.uuid4())
    c.execute("INSERT INTO caronas VALUES (?, ?, ?, ?, ?, ?)", (carona_id, inputs.nome, inputs.cidade_partida, inputs.cidade_chegada, inputs.banda, inputs.data))
    conn.commit()
    conn.close()    
    return {"id": carona_id}

# Rota para buscar caronas por cidade, banda e/ou data
@app.get("/buscar_caronas/")
def buscar_caronas(cidade_partida: str = None, banda: str = None, data: str = None):
    conn = connect_db()
    c = conn.cursor()
    query = "SELECT * FROM caronas WHERE "
    conditions = []
    if cidade_partida:
        conditions.append(f"cidade_partida = '{cidade_partida}'")
    if banda:
        conditions.append(f"banda = '{banda}'")
    if data:
        conditions.append(f"data = '{data}'")
    query += " AND ".join(conditions)
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return {"caronas": result}
    
@app.get("/caronas/")
def get_caronas():
    conn = connect_db()
    c = conn.cursor()
    query = "SELECT * FROM caronas"
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return {"caronas": result}
    

# Rota para atualizar uma carona existente
@app.put("/caronas/{carona_id}")
def update_caronas(carona_id: str, inputs: Inputs):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE caronas SET nome=?, cidade_partida=?, cidade_chegada=?, banda=?, data=? WHERE id=?", 
              (inputs.nome, inputs.cidade_partida, inputs.cidade_chegada, inputs.banda, inputs.data, carona_id))
    conn.commit()
    conn.close()
    return {"message": "Carona atualizada com sucesso"}

# Rota para deletar uma carona existente
@app.delete("/caronas/{carona_id}")
def delete_caronas(carona_id: str):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM caronas WHERE id=?", (carona_id,))
    conn.commit()
    conn.close()
    return {"message": "Carona deletada com sucesso"}


