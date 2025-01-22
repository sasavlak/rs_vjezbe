from fastapi import FastAPI

# Kreiranje FastAPI 
app = FastAPI()

# Lista filmova
filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

# Definiranje rute GET 
@app.get("/filmovi")
def get_filmovi():
    return filmovi
