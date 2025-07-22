from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestCreateCategoryIntegration:
    def test_create_category(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(category_repository=repository)
        request = CreateCategoryRequest(name="Category 1", description="Category 1 description")
        response = use_case.execute(request)
        assert response is not None
        assert len(repository.categories) == 1
        category = repository.find_by_id(response.id)
        assert category is not None
        assert category.name == "Category 1"
        assert category.description == "Category 1 description"
        assert category.is_active is True

    # def test_create_category_with_invalid_data(self):
    #     repository = InMemoryCategoryRepository()
    #     use_case = CreateCategory(category_repository=repository)
    #     request = CreateCategoryRequest(name=None, description="Category 1 description")
    #     with pytest.raises(InvalidCategoryData, match="Name is required") as exc_info:
    #         use_case.execute(request)
    #     assert exc_info.type is InvalidCategoryData
    #     assert str(exc_info.value) == "Name is required"