Years = {}

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

def search_year(value):
  for x,y in Years.items():
    if y == value:
      print(x)

def most_prolific():
    value = 0
    for album_title in Beatles_Discography:
        if Beatles_Discography[album_title] in Years:
            Years[Beatles_Discography[album_title]] += 1
            value = max(value,Years[Beatles_Discography[album_title]])
        else :
            Years[Beatles_Discography[album_title]] = 1
    search_year(value)

most_prolific()

#print(Years)
#print(value)
#print(Years[3])
#print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))
