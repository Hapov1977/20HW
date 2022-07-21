import pytest

from demostration_solution.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one()
        assert movie is not None
        assert isinstance(movie.id, int)
        assert movie.title == 'Movie_1'

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 2

    def test_create(self):
        movie_d = {'name': "New Name"}
        new_movie = self.movie_service.create(movie_d)
        assert new_movie.id is not None
        assert new_movie.title == 'Movie_3'
        assert new_movie.genre_id == 1

    def test_update(self):
        self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None