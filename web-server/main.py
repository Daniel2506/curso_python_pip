import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>First HTML</title>
        </head>
        <body>
            <h1>Look ma! HTML! - Daniel</h1>
        </body>
    </html>
    """

@app.get("/list")
def get_list():
    return [1,2,3,4,5]

@app.get("/contact") 
def get_contact():
    return {"name":"DANIEL TELLEZ", "email": "danieltrodriguez10@gmail.com", "phone": "+57 350"}  


def run():
    categories = store.get_categories()
    print(categories)


if __name__ == "__main__":
    run()