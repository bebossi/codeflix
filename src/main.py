from fastapi import FastAPI
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.use_cases.list_category import ListCategory, ListCategoryRequest
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

category_repository = InMemoryCategoryRepository()

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = ""
    is_active: Optional[bool] = True

class CategoryResponse(BaseModel):
    id: str
    name: str
    description: str
    is_active: bool

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeFlix API"}

@app.post("/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate):
    use_case = CreateCategory(category_repository=category_repository)
    request = CreateCategoryRequest(
        name=category.name,
        description=category.description or "",
        is_active=category.is_active
    )
    response = use_case.execute(request)
    
    get_use_case = GetCategory(category_repository=category_repository)
    category_response = get_use_case.execute(GetCategoryRequest(id=response.id))
    
    return CategoryResponse(
        id=str(category_response.id),
        name=category_response.name,
        description=category_response.description,
        is_active=category_response.is_active
    )

@app.get("/categories/", response_model=list[CategoryResponse])
def list_categories():
    use_case = ListCategory(category_repository=category_repository)
    response = use_case.execute(ListCategoryRequest())
    return [
        CategoryResponse(
            id=str(category.id),
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )
        for category in response.data
    ]

@app.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: str):
    use_case = GetCategory(category_repository=category_repository)
    try:
        uuid_id = UUID(category_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    response = use_case.execute(GetCategoryRequest(id=uuid_id))
    return CategoryResponse(
        id=str(response.id),
        name=response.name,
        description=response.description,
        is_active=response.is_active
    )

@app.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(category_id: str, category: CategoryCreate):
    use_case = UpdateCategory(category_repository=category_repository)
    try:
        uuid_id = UUID(category_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    request = UpdateCategoryRequest(
        id=uuid_id,
        name=category.name,
        description=category.description or "",
        is_active=category.is_active
    )
    response = use_case.execute(request)
    return CategoryResponse(
        id=str(response.id),
        name=response.name,
        description=response.description,
        is_active=response.is_active
    )

@app.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: str):
    use_case = DeleteCategory(category_repository=category_repository)
    try:
        uuid_id = UUID(category_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    use_case.execute(DeleteCategoryRequest(id=uuid_id)) 