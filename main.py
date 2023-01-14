from data import getAnime

airing = getAnime()

for anime in airing['data']['Page']['media']:
    print('\n\n')
    print(anime)



# first_entry = airing['data']['Page']['media']



# print(first_entry[0]['title'])

# def organize(data):
#     eng, rom, episodes, format, genres, popularity = 

    