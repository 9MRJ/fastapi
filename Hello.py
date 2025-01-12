from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def Hi():
    return {"message" : "HelloWorld"}

@app.get("/sum")

def sum(first: float ,second: float):
    return{"Total = " : first+second}

@app.get("/Auth")

def Auth(email: str,pas: str):
    exten = ["@gmail.com","@yahoo.com","@hotmail.com"]
    if (str(exten[0])) not in email:
        return{"Error"}
    else:
        return{"correct"}