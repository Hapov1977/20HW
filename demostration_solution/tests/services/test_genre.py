import pytest

from demostration_solution.service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one()
        assert genre is not None
        assert isinstance(genre.id, int)
        assert genre.name == 'Comedy'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) == 2

    def test_create(self):
        genre_d = {'name': "New Name"}
        new_genre = self.genre_service.create()
        assert new_genre.id is not None
        assert new_genre.name == 'Drama'

    def test_update(self):
        self.genre_service.update(1)

    def test_delete(self):
        res = self.genre_service.delete(1)
        assert res is None


