import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/solo.csv"
OUTPUT_PATH = "../data/generated/solo_instances.ttl"


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
    solo_uri = f"<http://example.org/bts/solo/{lit(row['solo_id'])}>"
    title = f"\"{lit(row['Title'])}\""
    member_label = f"\"{lit(row['member_label'])}\""
    release_date = f"\"{lit(row['Release_Date'])}\"^^xsd:date"
    release_type = f"\"{lit(row['Release_Type'])}\""
    language = f"\"{lit(row['Language'])}\""
    notes = f"\"{lit(row['Notes'])}\""

    linked_album_val = lit(row['linked_album_id'])
    if linked_album_val:
        album_uri = f"<http://example.org/bts/album/{linked_album_val}>"
        album_line = f"    bts:linkedAlbum {album_uri} ;\n"
    else:
        album_line = ""

    triple_block = f"""{solo_uri}
    a bts:SoloRelease ;
    bts:title {title} ;
    bts:memberLabel {member_label} ;
    bts:releaseDate {release_date} ;
    bts:releaseType {release_type} ;
{album_line}    bts:language {language} ;
    bts:notes {notes} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
