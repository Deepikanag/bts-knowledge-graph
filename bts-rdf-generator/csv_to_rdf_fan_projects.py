import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/fan_projects.csv"
OUTPUT_PATH = "../data/generated/fan_projects_instances.ttl"


def lit(value):
    """Escape value for safe use as an RDF literal."""
    if pd.isna(value):
        return ""
    s = str(value)
    return s.replace("\\", "\\\\").replace('"', '\\"')


# Load CSV
df = pd.read_csv(CSV_PATH)

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# RDF prefixes
prefixes = """@prefix bts: <http://example.org/bts#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""

triples = []

for _, row in df.iterrows():
    project_uri = f"<http://example.org/bts/fanProject/{lit(row['project_id'])}>"
    project_name = f"\"{lit(row['project_name'])}\""
    fan_community = f"\"{lit(row['fan_community'])}\""
    country = f"\"{lit(row['country'])}\""
    start_date = f"\"{lit(row['start_date'])}\"^^xsd:date"
    issue_key = f"\"{lit(row['issue_key'])}\""
    donation_amount = f"\"{lit(row['donation_amount_usd'])}\"^^xsd:decimal"
    description = f"\"{lit(row['description'])}\""

    triple_block = f"""{project_uri}
    a bts:FanProject ;
    bts:projectName {project_name} ;
    bts:fanCommunity {fan_community} ;
    bts:country {country} ;
    bts:startDate {start_date} ;
    bts:issueKey {issue_key} ;
    bts:donationAmountUSD {donation_amount} ;
    bts:description {description} ."""

    triples.append(triple_block)

# Write TTL file
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
