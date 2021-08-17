from bs4 import BeautifulSoup
import urllib.request

TicketMaster = 'https://www.ticketmaster.co.uk'


Artist = input(f"What artist do you want to find?")
ArtistParsed = Artist.replace(' ', '%20')

SearchResults = urllib.request.urlopen(f"{TicketMaster}/search?q={ArtistParsed}")
soup = BeautifulSoup(SearchResults, 'html.parser')

for link in soup.findAll('a'):
    if "/artist/" in link.get('href'):
        ArtistPage = f"{TicketMaster}{link.get('href')}"
        break
    ArtistPage = False


if ArtistPage:
    print(ArtistPage)
    SearchResultsDirect = urllib.request.urlopen(ArtistPage)
    soupDirect = BeautifulSoup(SearchResultsDirect, 'html.parser')
    for link in soup.findAll('script'):
        print(link)
else:
    print(f"No artist found relating to '{Artist}'")