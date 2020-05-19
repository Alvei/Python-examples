"""use_census2010.py"""
import census2010

print("\nImporting 2010 census data\n")

# Create a list of places to review in the census data
places = [['AK','Anchorage'], ['CA','Santa Clara']]

print(f"County\t\tPopulation ")
print("=============================")
for place in places:
    state = place[0]
    county = place[1]
    print(f"{county}\t{census2010.all_data[state][county]['pop']:,}")
