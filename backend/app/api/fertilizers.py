from datetime import datetime,timezone
from math import radians,sin,cos,sqrt,atan2
from fastapi import APIRouter
from pydantic import BaseModel,Field
router=APIRouter(tags=['fertilizers'])
class PriceObservation(BaseModel):
 product:str=Field(min_length=1,max_length=120);pack_kg:float=Field(gt=0);price:float=Field(ge=0);currency:str='INR';source:str=Field(min_length=1,max_length=200);verification_status:str='seller_provided';observed_at:datetime
class CompareRequest(BaseModel): observations:list[PriceObservation]=Field(min_length=1)
def distance_km(lat1,lon1,lat2,lon2):
 r=6371.0088;dlat=radians(lat2-lat1);dlon=radians(lon2-lon1);a=sin(dlat/2)**2+cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2;return 2*r*atan2(sqrt(a),sqrt(1-a))
@router.get('/fertilizers')
def fertilizers(): return {'items':['Urea','DAP','MOP','NPK','Organic manure','Micronutrients']}
@router.post('/fertilizer-prices/compare')
def compare(req:CompareRequest): return {'items':[{'product':o.product,'pack_kg':o.pack_kg,'price':o.price,'currency':o.currency,'price_per_kg':round(o.price/o.pack_kg,2),'source':o.source,'verification_status':o.verification_status,'observed_at':o.observed_at.isoformat()} for o in req.observations]}
@router.get('/fertilizer-prices/nearby')
def nearby(): return {'items':[],'message':'No verified local prices configured'}
@router.post('/fertilizer-recommendations')
def recommendation(hectares:float=Field(gt=0),nutrient_rate_kg_ha:float=Field(gt=0),nutrient_fraction:float=Field(gt=0,le=1)):
 nutrient=hectares*nutrient_rate_kg_ha;product=nutrient/nutrient_fraction;return {'required_nutrient_kg':round(nutrient,3),'theoretical_product_kg':round(product,3),'generated_at':datetime.now(timezone.utc).isoformat(),'rule_source':'configuration required'}