import os
import sys

from entertainement_stuff.film import Film
from entertainement_stuff.game import Game
from entertainement_stuff.parent import EntertainmentStuff
import json

# create a class in which we can add our stuff we watch/play/read
# and through it we should be able to mark our progress
# and we can see our whole list of stuff or only a type (for example the books)

# to keep this list persistent (to not lose the data)


class Library:
    def __init__(self):
        self.__reload()

    def add(self, e: EntertainmentStuff):
        self.__content_list.append(e)
        self.__save()

    def remove(self, name: str):
        self.__content_list = [x for x in self.__content_list if x.name != name]
        self.__save()

    def get(self, stuff_type=None) -> list:
        return [
            (x.name, x.completion_percent)
            for x in self.__content_list
            if stuff_type and stuff_type.lower().strip() == x.type.lower()
        ]

    def get2(self, types=[]) -> list:
        # homework
        return [
            x.name for x in self.__content_list if types and x.type.lower() in types
        ]

    def mark_progress(self, name: str, progress: float):
        for item in self.__content_list:
            if item.name == name:
                item.add_time(progress)
                break
        self.__save()

    def __save(self):
        stuff_dict = [x.to_dict() for x in self.__content_list]
        text = json.dumps(stuff_dict, indent=1)
        f = open("library.txt", "w")
        f.write(text)
        f.close()

    def __reload(self):
        if not os.path.isfile("library.txt"):
            self.__content_list = []
            return
        f = open("library.txt")
        text = f.read()
        f.close()
        self.__content_list = [
            self.__get_class(e["type"]).create_from_dict(e) for e in json.loads(text)
        ]

    def __get_class(self, name: str):
        return getattr(sys.modules[__name__], name)


# l = Library()
# f = Film("Pale Blue Eye", "Paramount", 130)
# g = Game("Stray", "who cares", 20)
# # e = EntertainmentStuff("should", "not", 1, 1)
# l.add(f)
# l.add(g)
# # l.add(e)
# # l.mark_progress("Pale Blue Eye", 26)
# # l.remove("Bioshock")
# print(l.get2([]))
