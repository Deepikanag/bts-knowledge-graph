import pandas as pd
import os

CSV_PATH = r"C:/Users/Deepika/Desktop/Projects/bts-knowledge-graph/data/csv/bts_donations.csv"
OUTPUT_PATH = "../data/generated/bts_donations_instances.ttl"


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
    donation_uri = f"<http://example.org/bts/donation/{lit(row['donation_id'])}>"
    donor_label = f"\"{lit(row['donor_label'])}\""
    donor_type = f"\"{lit(row['donor_type'])}\""
    donation_label = f"\"{lit(row['donation_label'])}\""
    amount_krw = f"\"{lit(row['amount_krw'])}\"^^xsd:decimal"
    amount_usd = f"\"{lit(row['amount_usd'])}\"^^xsd:decimal"
    donation_date = f"\"{lit(row['donation_date'])}\"^^xsd:date"
    org_name = f"\"{lit(row['org_name'])}\""
    org_type = f"\"{lit(row['org_type'])}\""
    issue_key = f"\"{lit(row['issue_key'])}\""
    campaign_label = f"\"{lit(row['campaign_label'])}\""
    country = f"\"{lit(row['country'])}\""

    triple_block = f"""{donation_uri}
    a bts:Donation ;
    bts:donorLabel {donor_label} ;
    bts:donorType {donor_type} ;
    bts:donationLabel {donation_label} ;
    bts:amountKRW {amount_krw} ;
    bts:amountUSD {amount_usd} ;
    bts:donationDate {donation_date} ;
    bts:orgName {org_name} ;
    bts:orgType {org_type} ;
    bts:issueKey {issue_key} ;
    bts:campaignLabel {campaign_label} ;
    bts:country {country} ."""

    triples.append(triple_block)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(prefixes + "\n\n".join(triples))

print(f"✅ RDF triples saved to: {OUTPUT_PATH}")
