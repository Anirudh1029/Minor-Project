import geocoder
def checkloc():
    g = geocoder.ip('me')
    lat=g.latlng[0]
    long=g.latlng[1]
    return (lat,long)
