import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/management.csv"
OUTPUT_PATH = "../data/generated/management_instances.ttl"


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
    relation_uri = f"<http://example.org/bts/managementRelation/{lit(row['relation_id'])}>"
    entity_type = f"\"{lit(row['entity_type'])}\""
    entity_label = f"\"{lit(row['entity_label'])}\""
    company_name = f"\"{lit(row['company_name'])}\""
    company_role = f"\"{lit(row['company_role'])}\""
    start_date = f"\"{lit(row['start_date'])}\"^^xsd:date"
    end_date = f"\"{lit(row['end_date'])}\"^^xsd:date"
    ownership_type = f"\"{lit(row['ownership_type'])}\""
    ownership_detail = f"\"{lit(row['ownership_detail'])}\""
    notes = f"\"{lit(row['notes'])}\""

    triple_block = f"""{relation_uri}
    a bts:ManagementRelation ;
    bts:entityType {entity_type} ;
    bts:entityLabel {entity_label} ;
    bts:companyName {company_name} ;
    bts:companyRole {company_role} ;
    bts:startDate {start_date} ;
    bts:endDate {end_date} ;
    bts:ownershipType {ownership_type} ;
    bts:ownershipDetail {ownership_detail} ;
    bts:notes {notes} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
