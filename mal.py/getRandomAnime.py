from jikanpy import Jikan
jikan = Jikan()

urls = []
want = set(["Harem"])
num = 0

while True:
    _this = set()
    randomAnime = jikan.random(type="anime")

    for key in randomAnime["data"]["genres"]:
        _this.add(key["name"])
    for key in randomAnime["data"]["themes"]:
        _this.add(key["name"])

    print(_this)

    if want.issubset(_this) and "Ecchi" not in _this:
        urls.append(randomAnime["data"]["url"])
        num += 1

    if num == 5:
        break
    
for i in urls:
    print(i)

