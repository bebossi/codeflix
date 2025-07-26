from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest, UpdateCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestUpdateCategoryIntegration:
    def test_update_category(self):
        category = Category(name="Category 1", description="Category 1 description")
        repository = InMemoryCategoryRepository()
        repository.save(category)
        use_case = UpdateCategory(category_repository=repository)
        request = UpdateCategoryRequest(id=category.id, name="Category 2", description="Category 2 description")
        response = use_case.execute(request)
        assert response == UpdateCategoryResponse(id=category.id, name="Category 2", description="Category 2 description", is_active=category.is_active)