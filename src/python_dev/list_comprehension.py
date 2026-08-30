square = [n ** 2 for n in range(1, 11)]
print(square)

shows_lists = ["frieNds", "the oFfice", "meNtalist", "walKing deAd"]
tv_shows_list = [shows.title() for shows in shows_lists if len(shows) > 8]
print(tv_shows_list)
