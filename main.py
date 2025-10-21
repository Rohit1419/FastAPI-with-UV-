from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine
from app.models import user_model, product_model
from app.routes import products_routes



# create tables 

product_model.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FastAPI",
    description="API for my Ecommerce Application",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def  read_root():
    return {"welcome to my app"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

#Product Routes

app.include_router(products_routes.router, prefix="/api/v1")





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
