import json
import requests
from datetime import date

today = date.today()

query = '''
query (
  $page: Int,
  $type: MediaType,
  $format: MediaFormat,
  $startDate: String,
  $endDate: String,
  $season: MediaSeason,
  $sort: [MediaSort],
) {
  Page (page: $page) {
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media (
      startDate_like: $startDate, # "2017%" will get all media starting in 2017, alternatively you could use the lesser & greater suffixes
      endDate_like: $endDate,
      season: $season,
      type: $type,
      format: $format,
      sort: $sort,
      status: RELEASING
    ) {
      id
      title {
        userPreferred
      }
      type
      format
      episodes
      chapters
      volumes
      genres
      averageScore
      popularity
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      nextAiringEpisode {
        airingAt
        timeUntilAiring
        episode
      }
    }
  }
}
'''

variables = {
    'type': 'ANIME',
    'startDate': '2016%'
}

url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query, 'variables': variables})

data = response.text

print(data)
