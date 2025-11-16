1.  Project Scope

    This knowledge graph focuses on modelling BTS’s global influence across multiple domains from 2013 onwards. The scope integrates their music releases, major performances, philanthropic activities, global campaigns, collaborations with international organizations, social issues addressed, awards received, and notable records broken. The knowledge graph aims to represent the interconnected nature of BTS’s artistic, cultural, and humanitarian work in a structured and semantically rich way.

2.  Competency Questions

    The following competency questions define what the knowledge graph should be able to answer. They guide the ontology design and ensure the model captures meaningful relationships between BTS, their work, and their global impact.

    - Which BTS albums and songs were released in a given year?
    - Which BTS members participated as writers or producers for a specific song?
    - Which philanthropic donations have BTS or individual members made, and which organizations received them?
    - Which global campaigns (e.g., UNICEF “Love Myself”) involve BTS, and what social issues do they target?
    - Where and when did BTS deliver major speeches (such as UN General Assembly appearances), and what themes did they address?
    - Which awards has BTS received for specific albums, songs, or humanitarian work?
    - Which fan-organized social projects were inspired by BTS, and which causes did they support?
    - Which global records have BTS or their music releases broken (e.g., YouTube viewership, chart rankings)?

    These questions ensure coverage of music, philanthropy, campaigns, speeches, awards, social impact, and records—offering a richer and more distinctive modelling approach than a standard “music-only” knowledge graph.

3.  Ontology Classes

    To model the complex domains related to BTS, a set of core ontology classes was defined. These classes represent key concepts such as musical outputs, members, events, philanthropic actions, and global achievements. The ontology includes more than eight classes, with three subclasses as required by the specification.

    3.1. Core Classes

    | Class                     | Description                                                                           |
    | ------------------------- | ------------------------------------------------------------------------------------- |
    | **bts:Group**             | Represents the music group BTS.                                                       |
    | **bts:Member**            | Represents an individual BTS member.                                                  |
    | **bts:MusicRelease**      | Abstract class for musical outputs such as albums and songs.                          |
    | **bts:Event**             | Represents events including concerts, speeches, award ceremonies.                     |
    | **bts:Campaign**          | Represents global or social campaigns BTS participates in (e.g., UNICEF Love Myself). |
    | **bts:Donation**          | Represents philanthropic donations made by BTS or its members.                        |
    | **bts:Organization**      | Represents organizations such as UNICEF, HYBE, and charities.                         |
    | **bts:SocialIssue**       | Represents social issues like mental health, anti-violence, education.                |
    | **bts:Award**             | Represents awards given to BTS or its music (e.g., Billboard Music Awards).           |
    | **bts:FanProject**        | Represents ARMY-led social impact or charity initiatives.                             |
    | **bts:RecordAchievement** | Represents global records broken by BTS or specific releases.                         |

    ***

    3.2. Subclasses
    The ontology includes three subclasses to refine specific categories:

    ***

    | Subclass            | Parent Class     | Description                                                                 |
    | ------------------- | ---------------- | --------------------------------------------------------------------------- |
    | **bts:Album**       | bts:MusicRelease | Represents full albums or EPs released by BTS.                              |
    | **bts:Song**        | bts:MusicRelease | Represents individual songs or tracks.                                      |
    | **bts:SpeechEvent** | bts:Event        | Represents notable speeches delivered by BTS (e.g., at the United Nations). |

    ***

    These subclasses allow more detailed querying and classification of BTS’s diverse activities.

    3.3. Alignment with Requirements

    ✔At least 8 classes are included
    ✔ No more than 3 subclasses (exactly 3 used)
    ✔ Classes cover music, philanthropy, campaigns, organizations, social issues, awards, records, and events
    ✔ Supports all competency questions defined in Step 1

4.  Object Properties
    The ontology defines a set of object properties that capture the relationships between BTS, its members, music releases, philanthropic activities, campaigns, organizations, awards, records, and fan-led projects. These properties express how different entities in the knowledge graph are connected.

    4.1. Membership Relationships (with Inverse Property)

        | Property          | Description                                  | Domain | Range  | Notes                      |
        | ----------------- | -------------------------------------------- | ------ | ------ | -------------------------- |
        | **bts:hasMember** | Indicates a member belonging to BTS          | Group  | Member | Has inverse                |
        | **bts:memberOf**  | Indicates the group an individual belongs to | Member | Group  | Inverse of `bts:hasMember` |

        ***

        InverseOf Pair:
        bts:hasMember owl:inverseOf bts:memberOf

    4.2. Music-Related Properties

            ---------------------------------------------------------------------------------------------
            | Property               | Description                        | Domain       | Range        |
            | ---------------------- | ---------------------------------- | ------------ | ------------ |
            | **bts:createdRelease** | Group created a music release      | Group        | MusicRelease |
            | **bts:featuresMember** | Member featured in a song or album | MusicRelease | Member       |
            | **bts:performedAt**    | Group performed at an event        | Group        | Event        |
            ---------------------------------------------------------------------------------------------

    4.3. Structural / Hierarchical Properties

            | Property        | Type       | Notes                                                                                               |

        | --------------- | ---------- | --------------------------------------------------------------------------------------------------- |
        | **bts:hasPart** | Transitive | Used for multi-part events, albums with multiple songs, or campaigns consisting of multiple actions |

        Transitive Property:
        bts:hasPart a owl:TransitiveProperty

    4.4. Philanthropy, Campaigns, and Social Issues

        | Property               | Description                          | Domain   | Range        |
        | ---------------------- | ------------------------------------ | -------- | ------------ |
        | **bts:partOfCampaign** | Event belonging to a campaign        | Event    | Campaign     |
        | **bts:targetsIssue**   | Social issue targeted by a campaign  | Campaign | SocialIssue  |
        | **bts:addressesIssue** | Social issue addressed by a donation | Donation | SocialIssue  |
        | **bts:donatedTo**      | Donation made to an organization     | Donation | Organization |
        | **bts:madeBy**         | Donation made by a BTS member        | Donation | Member       |

        ***

    4.5. Awards and Records

        | Property          | Description                       | Domain       | Range             | Notes                      |
        | ----------------- | --------------------------------- | ------------ | ----------------- | -------------------------- |
        | **bts:hasAward**  | Group has received an award       | Group        | Award             | Inverse of `bts:awardedTo` |
        | **bts:awardedTo** | Award given to a group            | Award        | Group             | Inverse relationship       |
        | **bts:hasRecord** | Music release that broke a record | MusicRelease | RecordAchievement |                            |

        ***

        InverseOf Pair:
        bts:hasAward owl:inverseOf bts:awardedTo

    4.6. Organizational Collaborations (Symmetric)
    | Property | Description | Domain | Range | Notes |

    | ------------------------ | ----------------------------------------------------------- | ------------ | ------------ | ------------------ |
    | **bts:collaboratesWith** | Collaboration between organizations (e.g., HYBE and UNICEF) | Organization | Organization | Symmetric property |

        Symmetric Property:
        bts:collaboratesWith a owl:SymmetricProperty

    4.7. Summary of Specification Compliance

        - At least six object properties are defined (in fact, more than six).
        - There is a transitive property (bts:hasPart).
        - There is a symmetric property (bts:collaboratesWith).
        - There are inverseOf pairs (bts:hasMember / bts:memberOf and bts:hasAward / bts:awardedTo).
        - Each object property has appropriate domain and range declarations supporting the BTS use case (music, philanthropy,  campaigns, awards, records, and collaborations).

5.  Data Properties and Cardinality Restrictions

    In addition to object properties, the ontology defines several data properties to describe literal attributes such as dates, amounts, names, and record details. Cardinality constraints are used to express modelling assumptions, ensuring that key entities such as donations, releases, and events have complete and consistent information.

    5.1. Data Properties

    | Data Property          | Description                                | Domain            | Range       |
    | ---------------------- | ------------------------------------------ | ----------------- | ----------- |
    | **bts:name**           | Human-readable name or label for an entity | (generic)         | xsd:string  |
    | **bts:releaseDate**    | Release date of a music release            | MusicRelease      | xsd:date    |
    | **bts:eventDate**      | Date on which an event occurred            | Event             | xsd:date    |
    | **bts:donationAmount** | Monetary value of a donation               | Donation          | xsd:decimal |
    | **bts:awardYear**      | Year in which an award was given           | Award             | xsd:gYear   |
    | **bts:recordValue**    | Value or description of a record achieved  | RecordAchievement | xsd:string  |

    ***

    These properties allow the knowledge graph to support time-based and numeric queries (e.g., releases by year, sum of donations, awards over time).

    5.2. Cardinality Restrictions on Object Properties

    To satisfy the specification requirement that at least two object properties have cardinality restrictions, the following constraints were modelled:

        5.2.1. Group Membership

            - A bts:Group is constrained to have at least seven members, reflecting the fact that BTS consists of seven members.
                -Implemented as:
                    ->bts:Group ⊑ (min 7 bts:hasMember bts:Member)

        5.2.2. Donations

          - A bts:Donation:
                |- Must be made to exactly one bts:Organization.
                |- Must be made by at least one bts:Member.
                |- Implemented as:
                    -> bts:Donation ⊑ (exactly 1 bts:donatedTo bts:Organization)
                -> bts:Donation ⊑ (min 1 bts:madeBy bts:Member)

        These constraints enforce realistic assumptions in the domain: every donation is associated with a single recipient organization and at least one donor.

    5.3. Cardinality Restrictions on Data Properties

    Additional cardinality constraints ensure that important literals are always present:

        - Every bts:MusicRelease has exactly one bts:releaseDate.
        - Every bts:Event has exactly one bts:eventDate.
        - Every bts:Donation has exactly one bts:donationAmount.
        - Every bts:Award has exactly one bts:awardYear.

    These constraints help ensure that the knowledge graph can reliably answer time-based and value-based competency questions (for example, “Which albums were released in 2020?” or “What is the total amount donated by BTS in a given year?”).

6.  CSV Data for Uplift
    To satisfy the requirement that at least one third of instance data must be uplifted from a CSV file using RML, a comprehensive donation dataset was constructed. The CSV contains curated records of philanthropic donations made by BTS and individual BTS members between 2015 and 2025, based on publicly reported information in English and Korean media, UNICEF announcements, Korean charity reports, and fan-organized documentation of member philanthropy.

    The dataset does not aim to be perfectly exhaustive, but instead provides a representative, semantically rich cross-section of BTS’s philanthropic activity suitable for knowledge graph modelling.

    The CSV file is stored in the project folder:
    data/csv/bts_donations.csv

    Each row corresponds to a single donation event and includes details about the donor (individual or group), the organization receiving the donation, the amount donated (in both KRW and USD where applicable), the targeted social issue, the associated campaign (e.g., UNICEF “Love Myself”), and the region impacted by the donation.

    6.1. CSV Schema

        The CSV has the following columns:

        | Column name        | Description                                                                                                                                |
        | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
        | **donation_id**    | Unique identifier for each donation event. Used to construct IRIs for `bts:Donation` instances.                                            |
        | **donor_label**    | Name of the donor (e.g., “RM”, “Suga”, “BTS”, “BTS+BigHit”).                                                                               |
        | **donor_type**     | Indicates whether the donor is a `Member` or the `Group`.                                                                                  |
        | **donation_label** | Short human-readable description of the donation event.                                                                                    |
        | **amount_krw**     | Donation amount in Korean won (KRW), if publicly reported.                                                                                 |
        | **amount_usd**     | Approximate equivalent in USD for normalization (0 if unknown).                                                                            |
        | **donation_date**  | Date of the donation (ISO format `YYYY-MM-DD`; approximated to month/day when reports gave only month/year).                               |
        | **org_name**       | Name of the organization receiving the donation.                                                                                           |
        | **org_type**       | Broad classification of the organization (`UN Agency`, `Charity`, `NGO`, `Government`, `Hospital`).                                        |
        | **issue_key**      | The social issue addressed (e.g., `health`, `education`, `anti-violence`, `anti-racism`, `disaster-relief`, `children-rights`, `culture`). |
        | **campaign_label** | Name of the campaign associated with the donation (e.g., “Love Myself”), or blank if none.                                                 |
        | **country**        | Country or region associated with the donation’s impact.                                                                                   |

        This structure ensures the CSV is rich enough to generate multiple interconnected RDF entities and triples per row.

    6.2. Rationale for CSV Design

        The CSV was intentionally designed to avoid simple one-to-one column-to-property mapping, supporting the requirement for meaningful RML uplift:

            6.2.1. One row → many semantic entities

            Each donation record generates:
                - A bts:Donation instance
                - A bts:Member or bts:Group donor link
                - A bts:Organization instance
                - A bts:SocialIssue instance
                - Optionally a bts:Campaign instance
                - Literal data properties (amount, date, labels)
            This results in 5–7 RDF triples per row, greatly increasing instance complexity.

            6.2.2. Column names differ from ontology properties

            The CSV uses practical, human-friendly names such as:
                - donor_label
                - amount_krw
                - issue_key

            The ontology uses semantic properties like:
                - bts:madeBy
                - bts:donationAmount
                - bts:addressesIssue
            This ensures the RML mapping must perform explicit semantic transformation, not trivial copying.

            6.2.3. Variety of entity types

            By spanning donations from group-level contributions (e.g., UNICEF Love Myself) to individual member philanthropy (e.g., Suga’s Daegu donations, Jimin’s education funds, Jungkook’s hospital support), the CSV supports modelling across:

                - Members
                - Organizations
                - Social issues
                - Campaigns
                - Countries
                - Years

            This enables richer SPARQL queries across multiple domains (philanthropy, geography, campaigns, etc.).

            6.2.4. Representative timeframe (2015–2025)
            Although BTS debuted in 2013, public reporting on donations becomes consistent from 2015 onward.

            The dataset therefore covers:
                - Early philanthropic contributions (2015–2016)
                - The start and growth of the UNICEF Love Myself campaign (2017–2023)
                - Major global events (COVID-19, Turkey/Syria earthquakes)
                - Ongoing member donations throughout BTS’s military service period (2023–2025)
            This shows temporal depth and supports time-based SPARQL queries.

    6.3 Example Donations Included in the CSV

        The CSV contains representative examples such as:
            - BTS + BigHit’s ₩500M pledge to UNICEF (2017)
            - Group’s $1M donation to Black Lives Matter (2020)
            - Multiple Suga birthday donations (Daegu, cancer patients, wildfire relief)
            - Jimin’s education-focused donations (Busan, Jeollanam-do, scholarships)
            - J-Hope’s ChildFund contributions supporting Tanzanian children
            - Jungkook’s ₩1B children’s hospital donation in 2023
            - Post-2023 military service donations (e.g., Suga, RM in 2025)

        These provide realistic, verifiable events while remaining manageable for RML processing.

    6.4 Suitability for RML Uplift

        The CSV is ideal for RML because:
            - It contains multiple entity types per row
            - It connects members, organizations, issues, campaigns, and countries
            - It supports rich, multi-hop SPARQL queries
            - It provides enough instances to exceed the minimum 30 triples requirement
            - It mirrors the real-world structure of philanthropic reporting, making the KG semantically meaningful

7.  RML Mapping for CSV Uplift

    To transform the tabular donation data into RDF and populate the knowledge graph, an RML mapping file bts_donations_rml.ttl was created.
    This mapping uses the RML vocabulary (for describing data sources and mappings) and the R2RML vocabulary (for subject maps, predicate-object maps, class assertions, and template IRIs).

    The mapping converts each row in data/csv/bts_donations.csv into fully modelled semantic data, generating instances of:

        - bts:Donation
        - bts:Organization
        - bts:SocialIssue
        - bts:Campaign

    and linking them through object properties from the ontology such as bts:donatedTo, bts:addressesIssue, bts:partOfCampaign, and bts:madeBy.

    7.1. Prefixes Used in the RML Mapping

        The following namespaces are used in the mapping file:

        ---------------------------------------------------------------------------------------------
        | Prefix   | Purpose                                                                        |
        | -------- | ------------------------------------------------------------------------------ |
        | **rml:** | Core RML vocabulary for describing logical sources and reference formulations. |
        | **rr:**  | R2RML vocabulary for subject maps, templates, predicate-object maps.           |
        | **ql:**  | Reference formulation vocabulary (`ql:CSV` for CSV files).                     |
        | **bts:** | Namespace of the BTS ontology created in this project.                         |
        | **xsd:** | XML Schema datatypes used for typed literals.                                  |
        ---------------------------------------------------------------------------------------------

    These prefixes allow the mapping file to stay concise and readable while remaining standards-compliant.

    7.2. Logical Source

        All triples maps in bts_donations_rml.ttl read from the same logical source:
            - Logical Source Name: <#DonationsSource>
            - File: data/csv/bts_donations.csv
            - Reference Formulation: ql:CSV

        This is declared once and reused by each Triples Map.

        <#DonationsSource> a rml:LogicalSource ;
            rml:source "data/csv/bts_donations.csv" ;
            rml:referenceFormulation ql:CSV .

        Using a shared logical source ensures that:
            - All entity types (Donations, Organizations, Social Issues, Campaigns)
                → are generated from the same rows.
            - No data duplication occurs.
            - The mapping remains easier to maintain.

    7.3. Donation Triples Map (map:DonationTriplesMap)

        This is the central RML mapping, responsible for turning each CSV row into a bts:Donation instance.

        7.3.1 Subject Map
            Each row becomes one unique donation:
                - Template:
                    http://example.org/bts/donation/{donation_id}
                - Class:
                    bts:Donation
            This ensures each donation has an IRI derived from the donation_id column.

        7.3.2 Data Properties (Literal Values)

            -------------------------------------------------------------
            | Ontology Property      | CSV Column       | Datatype      |
            | ---------------------- | ---------------- | ------------- |
            | **bts:name**           | `donation_label` | string        |
            | **bts:donationAmount** | `amount_usd`     | `xsd:decimal` |
            | **bts:eventDate**      | `donation_date`  | `xsd:date`    |
            -------------------------------------------------------------

        This allows accurate time-based and numeric querying.

        7.3.3 Linking Donations to Donors
            bts:madeBy links each donation to a donor:
                rr:template "http://example.org/bts/{donor_label}"

            - If donor_label = RM → IRI becomes:
                http://example.org/bts/RM
            - If donor_label = BTS+BigHit → IRI becomes:
                http://example.org/bts/BTS+BigHit

        These donor individuals (Members or Group) are defined separately in the instance data

        7.3.4 Linking Donations to Organizations

            bts:donatedTo uses:
                rr:template "http://example.org/bts/org/{org_name}"

            This template:
                - Creates a single Organization instance per unique org_name.
                - Matches the subject template in the OrganizationTriplesMap.
                - Ensures all donations to the same organization link to the same IRI.

        7.3.5 Linking Donations to Social Issues

            bts:addressesIssue uses:
                rr:template "http://example.org/bts/issue/{issue_key}"

            Since the Organization, Issue, and Campaign maps use the same template, no join conditions are needed—IRI alignment ensures correct linking.

        7.3.6 Linking Donations to Campaigns

            bts:partOfCampaign uses:
                rr:template "http://example.org/bts/campaign/{campaign_label}"

                - If campaign_label = "Love Myself" → A bts:Campaign instance is created.
                - If campaign_label is blank → The campaign IRI becomes empty or neutral, so the donation is not treated as part of a campaign.

    7.4. Organization Triples Map

        This map creates an organization instance for each unique value of org_name.
            - Subject Template:
                http://example.org/bts/org/{org_name}
            - Class:
                bts:Organization
            - Data Property:
                bts:name ← org_name

        Because this template matches the template used in the Donation Triples Map, all donations referencing the same organization automatically point to the same IRI.

    7.5. Social Issue Triples Map

        This map generates a bts:SocialIssue for each issue_key:
            - Subject Template:
                http://example.org/bts/issue/{issue_key}
            - Class:
                bts:SocialIssue
            - Data Property:
                bts:name ← issue_key

        This consolidates all donations addressing the same issue (e.g., “health” or “education”) into reusable nodes.

    7.6. Campaign Triples Map

        This Triples Map generates campaign nodes such as:
            - “Love Myself”
            - (or other campaign names that may appear)
            - Subject Template:
                http://example.org/bts/campaign/{campaign_label}
            - Class:
                bts:Campaign
            - Data Property:
                bts:name ← campaign_label

        If a row has an empty campaign field, it will still generate a placeholder IRI but will not affect query results unless explicitly selected.
