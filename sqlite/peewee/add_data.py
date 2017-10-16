# add_data.py

import datetime
import peewee

from models import Album, Artist

new_artist = Artist.create(name="Newsboys")
album_one = Album(artist=new_artist,
					title="read all about it",
					release_date=datetime.date(1988,12,2),
					publisher="refuge",
					media_type="CD")

album_one.save()
