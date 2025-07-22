from uuid import UUID
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

from src.core.category.domain.category import Category

class TestSave:
    def test_save(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Category 1", description="Category 1 description")
        repository.save(category)
        assert len(repository.categories) == 1
        assert repository.find_by_id(category.id) == category


class TestFindById:
    def test_find_by_id(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Category 1", description="Category 1 description")
        repository.save(category)
        assert repository.find_by_id(category.id) == category

    def test_find_by_id_not_found(self):
        repository = InMemoryCategoryRepository()
        assert repository.find_by_id(UUID("00000000-0000-0000-0000-000000000000")) is None