import requests
import json
from datetime import datetime


def getSeason():
    today = datetime.now()
    month = today.month
    if 1 <= month <= 3:
        return 'WINTER'
    if 4 <= month <= 6:
        return 'SPRING'
    if 7 <= month <= 9:
        return 'SUMMER'
    else:
        return 'FALL'

def getYear():
    today = datetime.now()
    return today.year

def getAnime():
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
      startDate_like: $startDate,
      endDate_like: $endDate,
      season: $season,
      type: $type,
      format: $format,
      sort: $sort,
      
    ) {
      id
      title {
        userPreferred
      }
      type
      format
      episodes
      genres
      averageScore
      popularity
      startDate {
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
        'season' : getSeason(),
              
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    return data

print(getAnime())