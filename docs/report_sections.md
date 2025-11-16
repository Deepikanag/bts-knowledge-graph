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
