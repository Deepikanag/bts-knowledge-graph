import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/tours.csv"
OUTPUT_PATH = "../data/generated/tours_instances.ttl"


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
    tour_uri = f"<http://example.org/bts/tour/{lit(row['tour_id'])}>"
    tour_name = f"\"{lit(row['tour_name'])}\""
    tour_type = f"\"{lit(row['tour_type'])}\""
    start_date = f"\"{lit(row['start_date'])}\"^^xsd:date"
    end_date = f"\"{lit(row['end_date'])}\"^^xsd:date"
    regions = f"\"{lit(row['regions'])}\""
    member_label = f"\"{lit(row['member_label'])}\""
    notes = f"\"{lit(row['notes'])}\""

    triple_block = f"""{tour_uri}
    a bts:Tour ;
    bts:tourName {tour_name} ;
    bts:tourType {tour_type} ;
    bts:startDate {start_date} ;
    bts:endDate {end_date} ;
    bts:regions {regions} ;
    bts:memberLabel {member_label} ;
    bts:notes {notes} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
