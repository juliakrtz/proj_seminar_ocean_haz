import pandas as pd
import geocoder 
shark_attacks = "data\original\shark_attacks.csv"
df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=",", header="infer")


def geocoding(input_island):
    g = geocoder.osm(input_island)
    return g.osm['x'], g.osm['y']

df['locations'] = df['island'].apply(geocoding)
df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
        index = df.index)

df.head()