albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for albums in albums:
    print("Album: {}, Artist: {}, Year:{}".
          format(albums[0], albums[1], albums[2]))

print()

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year:{}".
          format(name, artist, year))


print()

name, artist, year = albums
for albums in albums:
    print("Album: {}, Artist: {}, Year:{}".
          format(name, artist, year))







# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)
