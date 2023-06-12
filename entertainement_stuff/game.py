from entertainement_stuff.parent import EntertainmentStuff


class Game(EntertainmentStuff):
    # games have a name, studio, hours to finish, hours played
    # make all their variables private
    # on each object we can mark our progress and can see in percentage how much have we finished
    def __init__(
        self, name: str, studio: str, total_hours: float, played_hours: float = 0
    ):
        super().__init__(name, studio, total_hours, played_hours)

    @staticmethod
    def create_from_dict(d: dict):
        return Game(d["name"], d["studio"], d["total"], d["consumed"])


if __name__ == "__main__":
    game = Game("Overwatch", "Blizzard", 20)
    game.to_dict()
    print(game.get_completion_percent())
    game.add_time(2)
    print(game.get_completion_percent())
