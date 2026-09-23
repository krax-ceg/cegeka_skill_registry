"""
Client Closing Strategy Catalog for all 64 Nordic Enterprise Accounts
Cegeka & Databricks Strategic Alliance (vm-nor-dev)

Provides structured deal closing blueprints:
- 4-Phase Deal Execution Roadmap (Day 1-15, 16-30, 31-60, 61-90)
- Stakeholder Engagement Matrix (Economic Buyer, Technical Champion, Operational Sponsor, Procurement/InfoSec)
- When to Involve Databricks & What Databricks Can Do For Us
- Immediate Tactical Opening Move for Account Executive Thomas Dinsen
"""

from typing import Dict, Any, List

CLOSING_CATALOG: Dict[str, Dict[str, Any]] = {
    # 1. JYSK
    "JYSK": {
        "target_contract_value_eur": "€9,620,000",
        "target_contract_value_num": 9620000,
        "win_probability_pct": 82,
        "expected_value_eur": "€7,888,400",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Core SAP Data Warehouse Displacement & Omnichannel Lakehouse",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": "Brief CDO & VP Logistics on weekend promotional out-of-stocks caused by overnight SAP batch bottlenecks. Run rapid Azure assessment scan.",
                "deliverable": "Approved 1-Page Problem Statement & Signed NDA"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": "Joint whiteboard session with Databricks Lead SA demonstrating Delta Live Tables CDC on SAP POS streams. Present McKinsey Lakehouse TCO model to CFO.",
                "deliverable": "Validated Lakehouse Reference Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": "Submit Microsoft Partner Center ECIF request ($50,000 subsidy). Deploy Cegeka 4-Week Jumpstart in JYSK's Azure tenant with Databricks DBU vouchers.",
                "deliverable": "Live Delta Lake prototype ingesting 50 store POS feeds with <1.5s refresh"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": "Present PoV benchmark results to JYSK Executive Board. Structure 3-year Enterprise Agreement drawing down Azure Consumption Commitment (MACC).",
                "deliverable": "Signed 3-Year Strategic Agreement & Production Statement of Work"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Quantified TCO reduction (47%), serverless compute savings, and 6-month payback.",
                "objection_handler": "Emphasize Microsoft ECIF absorbs $50k in onboarding fees; Databricks replaces expensive proprietary database licenses."
            },
            "technical_champion": {
                "role": "Chief Information Officer (CIO) / VP IT",
                "focus": "Replacing fragile overnight batch ETL with governed, auto-scaling Delta Live Tables.",
                "objection_handler": "Demonstrate automated legacy SQL-to-PySpark code migration tools and out-of-the-box SAP connectors."
            },
            "operational_sponsor": {
                "role": "Executive VP Logistics & Supply Chain",
                "focus": "Sub-minute inventory visibility across 3,300 stores to eliminate weekend out-of-stocks.",
                "objection_handler": "Share Cegeka's Bridgestone case study showing automated supply chain pipeline stabilization."
            },
            "procurement_infosec": {
                "role": "Head of Procurement & CISO",
                "focus": "Microsoft Azure MACC commitment drawdown, GDPR compliance, and enterprise DPA.",
                "objection_handler": "Highlight that Databricks runs inside JYSK's existing Azure boundary; Unity Catalog manages data access."
            }
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Databricks Partner Specialist at Day 10 for co-selling alignment; deploy Databricks Enterprise Solution Architect at Day 20 for SAP architecture whiteboarding; invite CIO to Databricks Amsterdam EBC at Day 45.",
            "what_databricks_does": "Allocate $30k in free PoV DBU compute vouchers; provide specialized retail field SA support; endorse Cegeka as the preferred Nordic implementation partner."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with JYSK's CDO focusing on promotional store stockouts and share Cegeka's Austrotherm Lakehouse reference story.",
        "deal_blocker_mitigation": "Blocker: Entrenched SAP ecosystem inertia. Mitigation: Position Databricks as a complementary analytics accelerator rather than an immediate SAP ERP replacement."
    },

    # 2. ATP
    "Arbejdsmarkedets Tillaegspension (ATP)": {
        "target_contract_value_eur": "€10,750,000",
        "target_contract_value_num": 10750000,
        "win_probability_pct": 68,
        "expected_value_eur": "€7,310,000",
        "target_close_quarter": "Q1 2027",
        "deal_motion": "Legacy SAS Replacement & High-Performance Actuarial Lakehouse",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": "Meet CRO and Head of Actuarial Modeling. Expose computational limits of legacy SAS grids during macro market shocks across €100B+ pension reserves.",
                "deliverable": "Problem Diagnostic Document & Governance Prerequisite Plan"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": "Joint benchmark modeling session with Databricks quants showing Photon-accelerated Monte Carlo simulations vs. SAS batch runtimes.",
                "deliverable": "Photon Benchmark Briefing & EIOPA Compliance Blueprint"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": "Lock in $50,000 Microsoft ECIF funding. Deploy 4-week proof of value running active actuarial portfolio stress-testing on Azure Databricks.",
                "deliverable": "Production-ready actuarial model executing in 12 mins vs. 8 hours on SAS"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": "Board presentation to ATP Investment Committee and Director of Udbetaling Danmark. Finalize multi-year Azure enterprise consumption framework.",
                "deliverable": "Signed Enterprise Master Agreement & Phase 1 Production Migration SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO) / CRO",
                "focus": "Eliminating multi-million SAS recurring licensing fees and accelerating risk simulation turnaround.",
                "objection_handler": "Present financial model demonstrating €3.8M annual savings and a 7-month full payback period."
            },
            "technical_champion": {
                "role": "Chief Technology Officer (CTO) / Head of Quant IT",
                "focus": "Modernizing legacy mainframe/SAS infrastructure into an open, Python/PySpark enabled Lakehouse.",
                "objection_handler": "Highlight native support for Python, R, and SQL, allowing quant analysts to use existing skills."
            },
            "operational_sponsor": {
                "role": "Director of Udbetaling Danmark",
                "focus": "Automating social welfare fraud detection and streamlining monthly citizen disbursements.",
                "objection_handler": "Demonstrate GraphFrames anomaly detection identifying complex welfare fraud rings."
            },
            "procurement_infosec": {
                "role": "Chief Information Security Officer (CISO) & Legal",
                "focus": "Strict Danish financial secrecy, GDPR compliance, and Finanstilsynet regulatory audit trails.",
                "objection_handler": "Unity Catalog cryptographic lineage and role-based masking guarantee complete regulatory compliance."
            }
        },
        "databricks_involvement": {
            "when_to_involve": "Involve Databricks Global FSI Strategic Lead at Day 12; deploy FSI Quantitative Specialist SA at Day 22 for benchmark validation; host ATP CRO at Databricks Financial Services Executive Exchange at Day 50.",
            "what_databricks_does": "Provide specialized financial services reference architectures; fund $40k in PoV compute credits; guarantee senior leadership alignment with ATP board."
        },
        "immediate_next_action": "Send briefing paper to ATP's CRO contrasting SAS batch runtimes against Photon serverless clusters for Solvency II stress tests.",
        "deal_blocker_mitigation": "Blocker: Deeply rooted actuarial SAS code libraries. Mitigation: Offer automated SAS-to-PySpark translation accelerators as part of Cegeka's 4-Week Jumpstart."
    },

    # 3. Norwegian Air Shuttle ASA
    "Norwegian Air Shuttle ASA": {
        "target_contract_value_eur": "€8,750,000",
        "target_contract_value_num": 8750000,
        "win_probability_pct": 78,
        "expected_value_eur": "€6,825,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Airline Flight Ops Telemetry & Dynamic Yield Management Modernization",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": "Engage COO and VP Flight Operations. Expose the quantifiable cost of Aircraft on Ground (AOG) turnarounds and delayed ancillary yield adjustments.",
                "deliverable": "AOG Financial Impact Summary & Operational Assessment Plan"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": "Architecture session with VP IT and Databricks SA demonstrating real-time ingestion of aircraft ACARS engine logs and dynamic seat booking velocity.",
                "deliverable": "Consolidated Norwegian + Widerøe Data Architecture Blueprint"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": "Initiate 120-day countdown with $50,000 Microsoft ECIF funding. Deploy 4-week Lakehouse PoV connecting AMOS maintenance logs and reservation feeds.",
                "deliverable": "Live predictive maintenance model flagging APU failure signals 48 hours early"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": "Executive briefing with CEO and Commercial Director. Present verified ancillary yield lift and fuel burn savings. Close multi-year enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Contract & Flight Operations Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Fuel burn reduction, ancillary seat revenue uplift, and eliminating unplanned AOG delay penalties.",
                "objection_handler": "Point to €3.1M projected annual operational savings and 7-month payback."
            },
            "technical_champion": {
                "role": "Chief Information Officer (CIO) / VP IT",
                "focus": "Unifying disparate IT systems between Norwegian Air and newly acquired Widerøe fleet.",
                "objection_handler": "Unity Catalog establishes unified federated governance across both airline groups."
            },
            "operational_sponsor": {
                "role": "Chief Commercial Officer (CCO) / VP Revenue Management",
                "focus": "Dynamic ancillary pricing responding in real-time to competitor fare moves.",
                "objection_handler": "Databricks Model Serving allows real-time inference on passenger booking curves."
            },
            "procurement_infosec": {
                "role": "Head of Procurement & Flight Ops Compliance",
                "focus": "Aviation regulatory compliance (EASA/CAA), data sovereignty, and Microsoft contract alignment.",
                "objection_handler": "Data remains inside Norwegian's sovereign Azure tenant; complete auditability for aviation authorities."
            }
        },
        "databricks_involvement": {
            "when_to_involve": "Bring in Databricks Travel & Transportation Practice Lead at Day 12; connect Norwegian technical team with Databricks engineering specialists for ACARS streaming at Day 25.",
            "what_databricks_does": "Provide pre-built aviation predictive maintenance accelerators; allocate $30k in PoV DBU credits; co-sponsor executive airline digital transformation dinner."
        },
        "immediate_next_action": "Request a 30-minute introductory meeting with Norwegian's VP Technical Operations to discuss predictive APU telemetry and fleet reliability.",
        "deal_blocker_mitigation": "Blocker: Narrow airline operating margins and IT budget constraints. Mitigation: Leverage Microsoft ECIF to fund 100% of the PoV advisory fees."
    },

    # 4. Salmar AS
    "Salmar AS": {
        "target_contract_value_eur": "€7,560,000",
        "target_contract_value_num": 7560000,
        "win_probability_pct": 75,
        "expected_value_eur": "€5,670,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Aquaculture IoT Telemetry & Computer Vision Feeding Optimization",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": "Meet COO and Farming Director. Quantify the economic impact of a 4% feed pellet waste reduction and urgent sea lice regulatory reporting.",
                "deliverable": "Aquaculture Economic Opportunity Assessment & Scope Alignment"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": "Present edge-to-cloud Lakehouse architecture ingesting underwater video streams and water sensor telemetry into Azure Databricks.",
                "deliverable": "Edge-to-Cloud Aquaculture Lakehouse Reference Architecture"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": "Secure $35,000 Microsoft AMMP subsidy. Run 4-week PoV connecting 5 ocean cages at Ocean Farm 1 with automated pellet detection algorithms.",
                "deliverable": "Working computer vision model adjusting feed blower timing in real time"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": "Present feed savings data to SalMar executive management. Finalize group rollout across all coastal and offshore farming sites.",
                "deliverable": "Signed Enterprise Production Contract & Aquaculture Analytics SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Fish feed represents over 50% of farming opex; capturing feed savings directly enhances EBITDA.",
                "objection_handler": "Demonstrate that reducing feed waste by 3.5% pays for the entire platform investment in under 6 months."
            },
            "technical_champion": {
                "role": "Chief Information Officer (CIO) / Head of Farming IT",
                "focus": "Overcoming bandwidth constraints on remote offshore cages to stream actionable analytics onshore.",
                "objection_handler": "Databricks Edge Sync processes video locally on cage servers, uploading only summarized telemetry."
            },
            "operational_sponsor": {
                "role": "Chief Operating Officer / Farming Director",
                "focus": "Maximizing salmon growth rates while preventing biological sea lice breaches.",
                "objection_handler": "Provide predictive biomass models that forecast exact harvest weight distribution."
            },
            "procurement_infosec": {
                "role": "Head of Procurement & Biological Compliance",
                "focus": "Compliance with Norwegian Directorate of Fisheries reporting and resource rent tax documentation.",
                "objection_handler": "Unity Catalog maintains immutable, auditable harvest and mortality registers."
            }
        },
        "databricks_involvement": {
            "when_to_involve": "Bring in Databricks Manufacturing & IoT Industry Specialist at Day 14; engage Databricks Computer Vision SA at Day 24 for underwater video pipeline validation.",
            "what_databricks_does": "Supply computer vision and streaming edge reference templates; fund $25k in DBU PoV vouchers; provide co-sell documentation for Microsoft Partner Center."
        },
        "immediate_next_action": "Reach out to SalMar's Farming Director with an executive briefing on underwater camera telemetry and feed cost reduction.",
        "deal_blocker_mitigation": "Blocker: Harsh offshore environment and disconnected local barge computers. Mitigation: Design a hybrid edge architecture with local buffer storage on feed barges."
    },

    # 5. Danish Crown
    "Danish Crown": {
        "target_contract_value_eur": "€7,560,000",
        "target_contract_value_num": 7560000,
        "win_probability_pct": 74,
        "expected_value_eur": "€5,594,400",
        "target_close_quarter": "Q1 2027",
        "deal_motion": "Abattoir Yield Optimization & Farm-to-Fork Scope 3 Carbon Accounting",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": "Engage COO and Head of Sustainability. Highlight retailer contract risks (Tesco, Coop) requiring verified farm-to-fork Scope 3 carbon certificates.",
                "deliverable": "CSRD Compliance & Yield Optimization Discovery Brief"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": "Architecture session showing Delta Lake unifying abattoir cutting camera feeds with cooperative farm data from 6,000+ member farms.",
                "deliverable": "Integrated Agri-Food Lakehouse Architecture & Scope 3 Blueprint"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": "Unlock $35,000 in Microsoft AMMP funding. Deploy 4-week PoV connecting abattoir yield cutting telemetry with automated farm carbon calculations.",
                "deliverable": "Automated batch-level carbon certificate generation in <60 seconds"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": "Executive presentation to Danish Crown Management Board. Secure multi-year agreement covering all European meat processing facilities.",
                "deliverable": "Signed Master Enterprise Agreement & Global Operations SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Protecting major European supermarket contracts and capturing 0.5% carcass yield improvement.",
                "objection_handler": "Show business case where a 0.5% cutting yield lift generates €2.7M in annual bottom-line benefit."
            },
            "technical_champion": {
                "role": "Chief Information Officer (CIO) / VP IT",
                "focus": "Bridging industrial plant floor MES/SCADA networks with corporate SAP S/4HANA.",
                "objection_handler": "Delta Live Tables pipelines seamlessly ingest industrial IoT data and sync with SAP."
            },
            "operational_sponsor": {
                "role": "VP Operations & Abattoir Plant Managers",
                "focus": "Real-time carcass yield tracking to eliminate waste and optimize automated cutting robotics.",
                "objection_handler": "Share Cegeka's Austrotherm case study showing 100% real-time operational data access."
            },
            "procurement_infosec": {
                "role": "Head of Sustainability & Food Safety",
                "focus": "CSRD audit readiness and strict veterinary export traceability for international markets.",
                "objection_handler": "Unity Catalog maintains cryptographically auditable batch lineage from farm to container."
            }
        },
        "databricks_involvement": {
            "when_to_involve": "Involve Databricks ESG & Sustainability Solutions Lead at Day 12; deploy Manufacturing SA at Day 22 for abattoir IoT integration; align Databricks EMEA VP for board closing.",
            "what_databricks_does": "Provide Databricks ESG and farm-to-fork traceability blueprints; fund $25k in PoV DBU credits; co-sponsor executive presentation with Microsoft."
        },
        "immediate_next_action": "Initiate contact with Danish Crown's VP Operations to present a benchmark on automated carcass yield optimization and CSRD compliance.",
        "deal_blocker_mitigation": "Blocker: Reluctance of cooperative farmers to share raw farm data. Mitigation: Deploy Unity Catalog clean rooms so individual farm data remains private while collective emissions are modeled."
    }
}

# Generic generator for the remaining 59 accounts
def get_client_closing_strategy(client_name: str, parent: str = "", sub: str = "", industry: str = "Enterprise") -> Dict[str, Any]:
    """Retrieve bespoke closing strategy or synthesize an empirical closing plan."""
    # Direct match in catalog
    for key in [sub, client_name, parent]:
        if key and key in CLOSING_CATALOG:
            return CLOSING_CATALOG[key]

    # Keyword matching to closest archetype
    lookup = f"{client_name} {parent} {sub}".lower()
    
    if "jysk" in lookup or "retail" in lookup or "normal" in lookup or "cubus" in lookup or "dressmann" in lookup or "strawberry" in lookup:
        base = dict(CLOSING_CATALOG["JYSK"])
    elif "atp" in lookup or "klp" in lookup or "pension" in lookup or "finans" in lookup:
        base = dict(CLOSING_CATALOG["Arbejdsmarkedets Tillaegspension (ATP)"])
    elif "air" in lookup or "avinor" in lookup or "norwegian" in lookup or "ocean" in lookup or "monjasa" in lookup or "ruter" in lookup:
        base = dict(CLOSING_CATALOG["Norwegian Air Shuttle ASA"])
    elif "salmar" in lookup or "bama" in lookup:
        base = dict(CLOSING_CATALOG["Salmar AS"])
    elif "crown" in lookup or "schouw" in lookup or "jotun" in lookup or "hartmann" in lookup or "ecco" in lookup or "unibrew" in lookup:
        base = dict(CLOSING_CATALOG["Danish Crown"])
    else:
        base = dict(CLOSING_CATALOG["JYSK"])

    # Personalize for this client
    display = sub if sub else (parent if parent else client_name)
    personalized = {
        "target_contract_value_eur": base["target_contract_value_eur"],
        "target_contract_value_num": base["target_contract_value_num"],
        "win_probability_pct": max(60, min(85, base["win_probability_pct"] - 5)),
        "expected_value_eur": base["expected_value_eur"],
        "target_close_quarter": "Q4 2026 / Q1 2027",
        "deal_motion": f"Enterprise Lakehouse Modernization for {display}",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Provocative Discovery & Latent Friction Exposure",
                "action": f"Conduct an executive discovery briefing with {display}'s CDO and IT leadership to expose data silo friction and quantify legacy TCO.",
                "deliverable": "Approved 1-Page Problem Statement & Signed NDA"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Architecture Validation & Value Engineering",
                "action": f"Whiteboard session with Databricks Lead SA mapping {display}'s core workloads to Unity Catalog and Delta Lakehouse. Present TCO model to CFO.",
                "deliverable": "Validated Architecture Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week PoV & Microsoft AMMP/ECIF Allocation",
                "action": f"Lock in Microsoft ECIF/AMMP co-funding ($25k-$50k). Deploy Cegeka 4-Week Jumpstart in {display}'s Azure tenant with free DBU vouchers.",
                "deliverable": f"Working production prototype running live in {display}'s environment"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Decision, Procurement & Enterprise Close",
                "action": f"Present verified PoV outcomes to {display}'s Executive Committee and close multi-year enterprise platform agreement.",
                "deliverable": "Signed Enterprise Master Agreement & Production Statement of Work"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "TCO reduction, licensing consolidation, and sub-12-month payback.",
                "objection_handler": "Emphasize Microsoft co-funding absorbs upfront fees; Databricks reduces compute spend by 45%+."
            },
            "technical_champion": {
                "role": "Chief Technology Officer (CTO) / VP Architecture",
                "focus": "Unified governance via Unity Catalog and automated migration from legacy databases.",
                "objection_handler": "Demonstrate automated code conversion tools and open Delta Lake storage with zero vendor lock-in."
            },
            "operational_sponsor": {
                "role": "Chief Data Officer (CDO) / Business Unit Leader",
                "focus": "Faster time-to-insight, real-time analytics, and governed self-service BI.",
                "objection_handler": "Share Cegeka's real case benchmarks proving 3x faster data pipeline creation."
            },
            "procurement_infosec": {
                "role": "Head of Procurement & CISO",
                "focus": "Azure MACC drawdown, GDPR/NIS2 compliance, and enterprise DPA terms.",
                "objection_handler": "Databricks runs natively within client's Azure boundary; Unity Catalog provides auditable cryptographic lineage."
            }
        },
        "databricks_involvement": {
            "when_to_involve": f"Introduce Databricks Partner Specialist at Day 10 for co-sell alignment; engage Databricks Solution Architect at Day 20 for architecture review; bring in Databricks Regional VP at Day 50 for executive board sponsorship.",
            "what_databricks_does": "Provide $25k-$40k in free PoV DBU compute vouchers; assign dedicated field SA support; endorse Cegeka as the primary implementation partner in Microsoft Partner Center."
        },
        "immediate_next_action": f"Schedule an introductory 30-minute discovery call with {display}'s CDO to discuss operational data friction and share relevant Cegeka peer reference cases.",
        "deal_blocker_mitigation": "Blocker: Internal inertia and competing digital priorities. Mitigation: Position the 4-Week Lakehouse Jumpstart as a low-risk, fully subsidized Microsoft pilot."
    }
    return personalized
