from entertainement_stuff.parent import EntertainmentStuff


class Film(EntertainmentStuff):
    # films have a name, studio, length in minutes, minutes watched
    def __init__(
        self, name: str, studio: str, length: float, minutes_watched: float = 0
    ):
        super().__init__(name, studio, length, minutes_watched)

    @staticmethod
    def create_from_dict(d: dict):
        return Film(d["name"], d["studio"], d["total"], d["consumed"])


if __name__ == "__main__":
    film = Film("Matrix", "Paramount", 130)
    print(film.name)
    film.name = 1
    print(film.name)
