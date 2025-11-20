import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/songs.csv"
OUTPUT_PATH = "../data/generated/songs_instances.ttl"


def lit(value):
    """Escape value for safe use as an RDF literal."""
    if pd.isna(value):
        return ""
    s = str(value)
    return s.replace("\\", "\\\\").replace('"', '\\"')


# Load CSV, skipping malformed lines
df = pd.read_csv(CSV_PATH, on_bad_lines="skip")

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

prefixes = """@prefix bts: <http://example.org/bts#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""

triples = []

for _, row in df.iterrows():
    song_uri = f"<http://example.org/bts/song/{lit(row['song_id'])}>"
    title = f"\"{lit(row['Title'])}\""
    primary_artist = f"\"{lit(row['Primary_Artist'])}\""
    feat_artists = f"\"{lit(row['Featuring_Artist(s)'])}\""
    release_date = f"\"{lit(row['Release_Date'])}\"^^xsd:date"
    is_title_track = f"\"{lit(row['is_title_track'])}\""
    language = f"\"{lit(row['Language'])}\""

    album_id_val = lit(row['album_id'])
    if album_id_val:
        album_uri = f"<http://example.org/bts/album/{album_id_val}>"
        album_line = f"    bts:fromAlbum {album_uri} ;\n"
    else:
        album_line = ""

    triple_block = f"""{song_uri}
    a bts:Song ;
    bts:title {title} ;
    bts:primaryArtist {primary_artist} ;
    bts:featuringArtist {feat_artists} ;
{album_line}    bts:releaseDate {release_date} ;
    bts:isTitleTrack {is_title_track} ;
    bts:language {language} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
