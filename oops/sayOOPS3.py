# Inheritance

class Movie:
    def features(self,lang):
        self.language = lang
        return self.language


class Comedy(Movie):
    def features(self, n):
        n = n + 10
        return n

a = Comedy()
print(a.features(10))