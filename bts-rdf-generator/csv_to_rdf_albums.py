import pandas as pd
import os

# Load CSV (your existing absolute path kept exactly as-is)
df = pd.read_csv(
    r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/albums.csv"
)

# Output Turtle file (your filename kept, but folder fixed)
output_path = "../data/generated/albums_instances.ttl"

# Create output directory if missing
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Define RDF namespace prefix block
prefixes = """@prefix bts: <http://example.org/bts#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""

triples = []

# Convert each row to TTL triple block
for _, row in df.iterrows():

    album_uri = f"<http://example.org/bts/album/{row['album_id']}>"
    title = f"\"{row['title']}\""
    release_date = f"\"{row['release_date']}\"^^xsd:date"
    language = f"\"{row['language']}\""
    label = f"\"{row['label']}\""

    # FIXED: your CSV contains 'category', NOT 'album_category'
    category = f"\"{row['category']}\""

    # FIXED: there is NO 'created_by' column → removed
    # If you later add the column, you can restore it

    triple_block = f"""{album_uri}
    a bts:Album ;
    bts:title {title} ;
    bts:releaseDate {release_date} ;
    bts:language {language} ;
    bts:label {label} ;
    bts:albumCategory {category} ."""

    triples.append(triple_block)

# Write to TTL file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {output_path}")
