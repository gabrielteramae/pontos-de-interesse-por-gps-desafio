from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from app import models
from app.database import engine, get_db
from app.schemas import PoiCreate, PoiRead
from app.proximity import filter_by_proximity

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Points of Interest API",
    description="Cadastra POIs e permite busca por proximidade a partir de uma coordenada GPS",
    version="1.0.0",
)


@app.post("/pois", response_model=PoiRead, status_code=201)
def create_poi(poi: PoiCreate, db: Session = Depends(get_db)):
    db_poi = models.PointOfInterest(**poi.model_dump())
    db.add(db_poi)
    db.commit()
    db.refresh(db_poi)
    return db_poi


@app.get("/pois", response_model=list[PoiRead])
def list_pois(db: Session = Depends(get_db)):
    return db.query(models.PointOfInterest).all()


@app.get("/pois/nearby", response_model=list[PoiRead])
def nearby_pois(
    x: int = Query(..., ge=0),
    y: int = Query(..., ge=0),
    max_distance: float = Query(..., gt=0),
    db: Session = Depends(get_db),
):
    all_pois = db.query(models.PointOfInterest).all()
    return filter_by_proximity(all_pois, x, y, max_distance)
