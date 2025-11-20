import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/brand_endorsements.csv"
OUTPUT_PATH = "../data/generated/brand_endorsements_instances.ttl"


def lit(value):
    """Escape value for use as an RDF literal."""
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
    endorsement_uri = f"<http://example.org/bts/endorsement/{lit(row['endorsement_id'])}>"
    entity_type = f"\"{lit(row['entity_type'])}\""
    entity_label = f"\"{lit(row['entity_label'])}\""
    brand_name = f"\"{lit(row['brand_name'])}\""
    industry = f"\"{lit(row['industry'])}\""
    role = f"\"{lit(row['role'])}\""
    contract_start = f"\"{lit(row['contract_start'])}\"^^xsd:date"
    contract_end = f"\"{lit(row['contract_end'])}\"^^xsd:date"
    region = f"\"{lit(row['region'])}\""
    notes = f"\"{lit(row['notes'])}\""

    triple_block = f"""{endorsement_uri}
    a bts:BrandEndorsement ;
    bts:entityType {entity_type} ;
    bts:entityLabel {entity_label} ;
    bts:brandName {brand_name} ;
    bts:industry {industry} ;
    bts:role {role} ;
    bts:contractStart {contract_start} ;
    bts:contractEnd {contract_end} ;
    bts:region {region} ;
    bts:notes {notes} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
