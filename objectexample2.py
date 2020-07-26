# class Series(object):
#     def __init__(self, title):
#         self.title = title
#         self.sessions = None
#         self.startDate = None
    
#     def time_left(self, currentDate, episodeNumber):
#        show_date = self.startDate + (7*(episodeNumber - 1))
#        print(show_date)
    


# got = Series("Game of thrones")
# print(got.title)
# got.sessions = 8
# got.startDate = 14
# got.time_left(15, 3)

# print(got.sessions)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()