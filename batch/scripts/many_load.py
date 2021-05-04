import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Iso, Category, Region, State


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        #print(row)
        cat, created = Category.objects.get_or_create(name=row[7])
        sta, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None
        try:
            lon = float(row[4])
        except:
            lon = None
        try:
            lat = float(row[5])
        except:
            lat = None
        try:
            area = float(row[6])
        except:
            area = None

        site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=lon, latitude=lat, area_hectares=area, category=cat, state=sta,region=reg,iso=iso)
        site.save()