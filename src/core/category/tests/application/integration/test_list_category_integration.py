from src.core.category.application.use_cases.list_category import CategoryOutput, ListCategory, ListCategoryRequest, ListCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestListCategoryIntegration:
    def test_list_category(self):
        category = Category(name="Category 1", description="Category 1 description")
        category_2 = Category(name="Category 2", description="Category 2 description")
        repository = InMemoryCategoryRepository()
        repository.save(category)
        repository.save(category_2)
        use_case = ListCategory(category_repository=repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)
        assert response == ListCategoryResponse(data=[
            CategoryOutput(id=category.id, name=category.name, description=category.description, is_active=category.is_active),
            CategoryOutput(id=category_2.id, name=category_2.name, description=category_2.description, is_active=category_2.is_active)
        ]
            )
        

    def test_when_no_categories_are_found_should_return_empty_list(self):
        repository = InMemoryCategoryRepository()
        use_case = ListCategory(category_repository=repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)
        assert response == ListCategoryResponse(data=[])