from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get('/health').json()['status']=='ok'
def test_price_normalization():
 r=client.post('/api/fertilizer-prices/compare',json={'observations':[{'product':'Urea','pack_kg':50,'price':1200,'source':'seller','observed_at':'2026-10-08T00:00:00Z'}]});assert r.status_code==200;assert r.json()['items'][0]['price_per_kg']==24.0
