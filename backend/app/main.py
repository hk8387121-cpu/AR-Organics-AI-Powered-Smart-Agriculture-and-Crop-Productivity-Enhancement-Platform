from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.fertilizers import router as fertilizer_router
app=FastAPI(title='AR Organics API',version='1.0.0',docs_url='/docs')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
@app.get('/health')
def health(): return {'status':'ok','service':'ar-organics-api'}
app.include_router(fertilizer_router,prefix='/api')