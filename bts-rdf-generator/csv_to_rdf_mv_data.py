import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/mv_data.csv"
OUTPUT_PATH = "../data/generated/mv_data_instances.ttl"


def lit(value):
    if pd.isna(value):
        return ""
    s = str(value)
    return s.replace("\\", "\\\\").replace('"', '\\"')


df = pd.read_csv(CSV_PATH)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

prefixes = """@prefix bts: <http://example.org/bts#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""

triples = []

for _, row in df.iterrows():
    mv_uri = f"<http://example.org/bts/mv/{lit(row['mv_id'])}>"
    title = f"\"{lit(row['title'])}\""
    release_date = f"\"{lit(row['release_date'])}\"^^xsd:date"
    director = f"\"{lit(row['director'])}\""
    views_24h = f"\"{lit(row['views_24h_millions'])}\"^^xsd:decimal"
    platform_record = f"\"{lit(row['platform_record'])}\""
    notes = f"\"{lit(row['notes'])}\""

    # Link to song via song_id
    song_id_val = lit(row['song_id'])
    if song_id_val:
        song_uri = f"<http://example.org/bts/song/{song_id_val}>"
        song_line = f"    bts:forSong {song_uri} ;\n"
    else:
        song_line = ""

    triple_block = f"""{mv_uri}
    a bts:MusicVideo ;
    bts:title {title} ;
{song_line}    bts:releaseDate {release_date} ;
    bts:director {director} ;
    bts:views24hMillions {views_24h} ;
    bts:platformRecord {platform_record} ;
    bts:notes {notes} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
