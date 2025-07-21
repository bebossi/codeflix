from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

from src.core.category.domain.category import Category

class TestInMemoryCategoryRepository:
    def test_save(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Category 1", description="Category 1 description")
        repository.save(category)
        assert len(repository.categories) == 1
        assert repository.find_by_id(category.id) == category