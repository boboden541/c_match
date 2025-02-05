from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import Show
from app.database import SessionLocal

# Создаем роутер для эндпоинтов Show
router = APIRouter(prefix="/shows", tags=["shows"])

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Создание нового шоу
@router.post("/", status_code=201)
def create_show(show_data: dict, db: Session = next(get_db())):
    new_show = Show(
        title=show_data.get("title"),
        description=show_data.get("description"),
        source_type=show_data.get("source_type"),
        source_id=show_data.get("source_id"),
    )
    db.add(new_show)
    db.commit()
    db.refresh(new_show)
    return {"message": "Show created successfully", "show": new_show}

# PUT: Обновление существующего шоу
@router.put("/{show_id}")
def update_show(show_id: int, update_data: dict, db: Session = next(get_db())):
    show = db.query(Show).filter(Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")

    # Обновляем поля шоу
    for key, value in update_data.items():
        setattr(show, key, value)

    db.commit()
    db.refresh(show)
    return {"message": "Show updated successfully", "show": show}