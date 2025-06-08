from sqlmodel import SQLModel, Field 
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import Column 
from sqlalchemy.types import JSON 

class FragranceBase(SQLModel):
    """
    Базовая модель для свойств аромата
    """
    name: str = Field(..., max_length=255, index=True)
    brand: Optional[str] = Field(default=None, max_length=255, index=True)

    accords: List[str] = Field(default_factory=list, sa_column=Column(JSON))
    main_notes: List[str] = Field(default_factory=list, sa_column=Column(JSON))
    
    year: Optional[int] = Field(default=None)
    gender: Optional[str] = Field(default=None, max_length=50)

class Fragrance(FragranceBase, table=True):
    """
    Модель аромата для хранения в бд
    """
    id: Optional[int] = Field(default=None, primary_key=True)

    def __str__(self) -> str:
        return f"id: {self.id}, Name: {self.name} ({self.brand or 'Unknown'})"


class FragranceSearchResponse(BaseModel):
    """
    Модель для элемента выпадающего списка при поиске пользователем ароматов
    """
    id: int
    name: str

class RecommendationRequest(BaseModel):
    """
    Модель входных данных для запроса рекомендаций
    Содержит список id ароматов, на которые надо ориентироваться при поиске
    """
    liked_frag_ids: List[int] = Field(..., min_items=1)

class RecommendedFragrance(BaseModel):
    """
    Модель для одного рекомендованного аромата
    """
    frag: FragranceBase
    relevance_score: Optional[float] = Field(default=None, ge=0.0, le=1.0, description="релевантность")

class RecommendationResult(BaseModel):
    """
    Модель списка рекомендаций
    """
    recommended_frags: List[RecommendedFragrance] = Field(default_factory=list)
    message: str = "recommendations list created"
