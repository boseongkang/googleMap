# googleMap
git clone repository -> 'pip install flask' -> 'pip install requests' -> 'pip install dotenv' -> 'python app.py runserver'

## Jun 24 2025
<br>
show search results on map with markers and number list
<br>
sort by reviews&rating
<br>
autocomplete to location input 
<br>
not working: update results and map marker while user move the map(drag)


## Jun 26 2025
change display from horizontal to vertical layout
<br>
sorting results works and markers on map match the order
<br>
clicking a result centers the map and marker, keeping them in sync
<br>
add img using Google Places API and show in popup
<br>
if user clicks anywhere on the map, pop up closes
<br>
**need to do**:
popup box fix
if user drags the map, result changes as the map changes


## Jun 28 2025
sort buttons fixed
<br>
popup display fix & improved
<br>
when a user clicks on a place in the results list, the map centers on the selected location and opens a marker popup showing detailed info properly.
<br>
map drag feature added
<br> 
**Issue**
Searching "San Francisco" + "bridge" keyword, shows the correct Golden Gate Bridge photo.
But with "San Francisco" + "tourist attractions" keyword, the Golden Gate Bridge result shows a wrong photo (Taj Mahal).
This is due to the Google Places API photo data
