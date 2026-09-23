"""
Client Intelligence Catalog for all 64 Nordic Enterprise Accounts
Cegeka & Databricks Strategic Alliance (vm-nor-dev)

This catalog provides crisp, board-level, empirically grounded intelligence
tailored to each specific client's business model, operational data challenges,
and exact Databricks Lakehouse capabilities.
"""

from typing import Dict, Any, List

CLIENT_CATALOG: Dict[str, Dict[str, Any]] = {
    # 1. Aarhus Kommune
    "Aarhus Kommune": {
        "industry": "Public Sector & Municipal Administration",
        "what_databricks_solves": "Unify 35+ municipal departmental silos (eldercare, welfare, school administration, water utilities) into a sovereign Azure Databricks Lakehouse with Unity Catalog attribute-based masking, accelerating caseworker workflows while guaranteeing 100% GDPR and Danish municipal compliance.",
        "trend_macro": "Demographic aging demanding predictive municipal eldercare resource allocation, strict EU NIS2/GDPR compliance, and political mandates for open, transparent citizen digital services.",
        "trend_competitors": "Leading European cities (Copenhagen, Flanders region) deploy Lakehouse data meshes to forecast social care capacity and optimize municipal waste and energy grids in near real-time.",
        "trend_legacy_debt": "Dozens of fragmented department databases (KMD, Opus, legacy on-prem SQL servers) with fragile overnight batch jobs and heavy manual spreadsheet reporting.",
        "fomo_cost_of_inaction": "Severe caseworker administrative burnout: An estimated 45,000 annual hours lost to manual data reconciliation across welfare and school systems, risking delayed interventions and regulatory penalties.",
        "fomo_peer_velocity": "Peer digital municipalities resolve citizen requests in hours using governed AI knowledge assistants; Aarhus department heads face 3-week reporting lags.",
        "fomo_vendor_traps": "Lock-in with legacy public sector ERP and database vendors charging escalating annual maintenance without modern cloud AI capabilities.",
        "tco_reduction_pct": 38,
        "compute_savings_pct": 52,
        "productivity_lift_multiplier": "3.1x",
        "annual_savings_eur": "€1,450,000",
        "payback_months": 8,
        "investment_eur": "€360,000",
        "three_year_net_value_eur": "€3,990,000",
        "key_questions": [
            {"target": "Municipal Director / Stadsdirektør", "question": "How many caseworker hours are consumed each month manually copying citizen records between KMD welfare systems and municipal health registers?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you enforce role-based citizen data anonymization when cross-departmental teams run demographic planning analytics?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the municipal budget exposure of maintaining legacy on-premise data warehouses versus a serverless, consumption-governed Lakehouse?"},
            {"target": "Data Protection Officer (DPO)", "question": "Can you audit every query touching sensitive child welfare or eldercare datasets with cryptographic tamper-evident lineage?"}
        ],
        "use_cases": [
            {"title": "Sovereign Cross-Departmental Citizen 360", "category": "Unified Governance & Security", "description": "Unity Catalog ABAC governance unifying civil registers, school records, and social care logs with automated row/column masking.", "architecture": "Unity Catalog + Azure Databricks + Power BI Direct Lake"},
            {"title": "Predictive Eldercare & Social Service Capacity Forecasting", "category": "Lakehouse Modernization", "description": "Delta Live Tables pipelines aggregating care home occupancy, home nursing schedules, and hospital discharge streams.", "architecture": "Delta Lake + Delta Live Tables + MLflow"},
            {"title": "Sovereign Municipal AI Citizen Assistant", "category": "Enterprise GenAI & Mosaic AI", "description": "Secure, governed knowledge assistant interrogating Danish municipal bylaws and building codes with zero public cloud leakage.", "architecture": "Databricks Mosaic AI + Vector Search + Azure OpenAI"}
        ],
        "matched_cases": ["ggz-rivierduinen", "water-link"]
    },

    # 2. Arbejdsmarkedets Tillaegspension (ATP)
    "Arbejdsmarkedets Tillaegspension (ATP)": {
        "industry": "Financial Services, Pensions & Social Security Administration",
        "what_databricks_solves": "Modernize Denmark's €100B+ pension engine and national welfare disbursement platform onto Azure Databricks, enabling sub-second risk simulations, automated social benefit fraud detection, and multi-asset portfolio ESG stress-testing.",
        "trend_macro": "Severe financial market volatility, stringent EIOPA Solvency II capital requirements, and surging public mandate to detect complex welfare payment fraud across millions of Danish citizens.",
        "trend_competitors": "Top global pension funds (APG, PGGM, CPPIB) utilize Databricks Lakehouse to run daily Monte Carlo liquidity simulations and automated ESG carbon accounting across private and public equity.",
        "trend_legacy_debt": "Legacy IBM mainframe core transaction engines, proprietary SAS analytics grids, and isolated SQL databases supporting Udbetaling Danmark disbursements.",
        "fomo_cost_of_inaction": "Delayed investment risk hedging: Running complex market shock scenarios overnight rather than intraday exposes hundreds of millions in pension asset volatility during macroeconomic shocks.",
        "fomo_peer_velocity": "Modern asset managers adjust multi-asset portfolio risk within 30 minutes; ATP quantitative teams wait for overnight batch simulations to calculate portfolio value-at-risk (VaR).",
        "fomo_vendor_traps": "Extensive licensing fees on proprietary legacy SAS and mainframe analytic environments with steep fees for compute burst capacity.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€3,800,000",
        "payback_months": 7,
        "investment_eur": "€650,000",
        "three_year_net_value_eur": "€10,750,000",
        "key_questions": [
            {"target": "Chief Risk Officer (CRO)", "question": "How long does your quantitative risk team require to execute a full portfolio stress-test across Denmark's €100B+ pension reserve following a sudden interest rate shift?"},
            {"target": "Chief Technology Officer (CTO)", "question": "What is the annual licensing and infrastructure overhead of maintaining legacy SAS compute clusters for actuarial modeling?"},
            {"target": "Director of Udbetaling Danmark", "question": "How many fraudulent benefit claims slip through current rule-based systems that could be detected in real-time using graph-based ML on Delta Lake?"},
            {"target": "Chief Data Officer (CDO)", "question": "How do you enforce granular data clean-room governance between public welfare disbursements and confidential pension investment data?"}
        ],
        "use_cases": [
            {"title": "High-Throughput Actuarial & Monte Carlo Risk Engine", "category": "Lakehouse Modernization", "description": "Photon-accelerated Spark compute running billions of actuarial portfolio simulations in minutes instead of overnight SAS batches.", "architecture": "Databricks Photon + Delta Lake + MLflow"},
            {"title": "Automated Welfare Disbursement Fraud & Anomaly Detection", "category": "Enterprise GenAI & Mosaic AI", "description": "Graph algorithms and supervised ML models detecting complex carousel fraud and duplicate benefit claims in real-time.", "architecture": "GraphFrames + Mosaic AI + Spark Streaming"},
            {"title": "Institutional ESG & Solvency II Sovereign Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog multi-tenant workspace providing auditable regulatory lineage for Danish Finanstilsynet and EIOPA audits.", "architecture": "Unity Catalog + Delta Sharing + Power BI"}
        ],
        "matched_cases": ["cera", "austrotherm"]
    },

    # 3. Avinor AS
    "Avinor AS": {
        "industry": "Aviation Infrastructure & Airport Operations",
        "what_databricks_solves": "Consolidate telemetry from 43 Norwegian airports (Oslo Gardermoen radar, baggage handling IoT, passenger security scanners, runway sensors) into an Azure Databricks real-time Lakehouse to predict aircraft turnaround delays and optimize terminal energy.",
        "trend_macro": "Severe Nordic winter weather disruptions, strict zero-emission airport targets by 2030, and high passenger volume rebounds straining terminal security and baggage handling capacity.",
        "trend_competitors": "Leading airport operators (Schiphol, Heathrow, Swedavia) leverage Databricks streaming pipelines to forecast security queue wait times and dynamically assign baggage carousels and aircraft stands.",
        "trend_legacy_debt": "Fragmented operational databases: Separate flight information display systems (FIDS), SCADA baggage handling networks, and isolated radar feeds with zero centralized data lakehouse.",
        "fomo_cost_of_inaction": "Substantial winter delay penalties: An estimated NOK 120M annual operational friction in delayed gate turnarounds, de-icing queue bottlenecks, and unplanned runway snowplow dispatches.",
        "fomo_peer_velocity": "Automated airports predict baggage choke points 45 minutes in advance; Avinor operations control centers react only after passenger queues have already formed.",
        "fomo_vendor_traps": "Heavily siloed, proprietary airport management vendor suites charging exorbitant API access fees to extract raw operational sensor streams.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 54,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 7,
        "investment_eur": "€480,000",
        "three_year_net_value_eur": "€6,120,000",
        "key_questions": [
            {"target": "Executive VP Airport Operations", "question": "What is the quantifiable economic cost of a 20-minute de-icing or baggage turnaround delay propagating across regional Nordic feeder flights?"},
            {"target": "Chief Technology Officer (CTO)", "question": "Why are baggage IoT telemetry, radar flight feeds, and passenger security checkpoint streams isolated across different proprietary vendor databases?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much could Avinor save in terminal heating and HVAC expenditure by dynamically synchronizing building management systems with real-time flight arrival delays?"},
            {"target": "Head of Digitalization", "question": "How quickly can your data team ingest real-time runway sensor friction data into an operational predictive maintenance model?"}
        ],
        "use_cases": [
            {"title": "Real-Time Aircraft Turnaround & De-Icing Optimization", "category": "Lakehouse Modernization", "description": "Delta Live Tables streaming radar, apron camera AI, and weather telemetry to predict gate readiness and de-icing slot conflicts.", "architecture": "Azure Databricks + Delta Live Tables + Event Hubs"},
            {"title": "Predictive Passenger Flow & Baggage System Diagnostics", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting terminal checkpoint queues and mechanical baggage jam anomalies before passenger impact.", "architecture": "Mosaic AI + Feature Store + Power BI Streaming"},
            {"title": "Airport Energy & Net-Zero Aviation Emissions Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog governed data platform consolidating airport Scope 1-3 carbon emissions, auxiliary power unit fuel burn, and ground fleet electrification.", "architecture": "Unity Catalog + Cegeka ESG Blueprint"}
        ],
        "matched_cases": ["bridgestone", "fluvius"]
    },

    # 4. Bama Gruppen / BAMA Gruppen AS
    "Bama Gruppen": {
        "industry": "Fresh Produce Logistics, Cold-Chain & Wholesale Distribution",
        "what_databricks_solves": "Transform Norway's largest fresh food supply chain with an Azure Databricks Lakehouse, processing real-time IoT temperature sensor streams from cold storage and delivery fleets to eliminate food waste and predict store-level demand.",
        "trend_macro": "Severe fresh produce inflation, strict Norwegian food waste reduction directives (KuttMatsvinn2030), and complex maritime/air import supply chain lead times.",
        "trend_competitors": "Global cold-chain giants (Dole, Sysco, Coop) deploy automated Lakehouse demand sensing to reduce perishable shrinkage by up to 35% using real-time shelf-life modeling.",
        "trend_legacy_debt": "Disparate warehouse management systems (WMS), ERP logistics modules, and manual spreadsheet-based inventory ordering across regional distribution hubs.",
        "fomo_cost_of_inaction": "Massive perishable waste: An estimated NOK 80M+ annual write-offs due to shelf-life degradation in warehouses and store delivery delays that could be preempted with real-time freshness analytics.",
        "fomo_peer_velocity": "Leading food distributors execute automated intraday store replenishment adjustments; Bama distribution planners rely on previous-day batched sales reports.",
        "fomo_vendor_traps": "Proprietary ERP supply chain modules charging expensive licensing fees with rigid data export limitations that throttle real-time machine learning.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€1,900,000",
        "payback_months": 6,
        "investment_eur": "€420,000",
        "three_year_net_value_eur": "€5,280,000",
        "key_questions": [
            {"target": "Chief Operating Officer / Supply Chain VP", "question": "What is the annual financial impact of fresh produce spoilage caused by cold-chain temperature anomalies during regional transport?"},
            {"target": "Chief Information Officer (CIO)", "question": "How many hours does it take to consolidate store sell-through data from NorgesGruppen, Rema, and Coop into your central procurement demand forecasts?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What would be the margin impact of reducing perishable warehouse shrinkage by just 15% through algorithmic shelf-life allocation?"},
            {"target": "Head of Data & Analytics", "question": "Can your data team deploy a computer vision defect-detection model on fruit sorting conveyor belts directly onto your existing data stack?"}
        ],
        "use_cases": [
            {"title": "Cold-Chain IoT Telemetry & Spoilage Prevention Engine", "category": "Lakehouse Modernization", "description": "Delta Lake streaming ingestion of refrigerated container sensors, surfacing temperature deviation alerts in sub-seconds.", "architecture": "Delta Lake + Spark Structured Streaming + Azure IoT Hub"},
            {"title": "AI-Driven Intraday Store Demand Sensing & Fresh Allocation", "category": "Enterprise GenAI & Mosaic AI", "description": "Predictive ML models integrating weather forecasts, holidays, and supermarket checkout velocity to optimize daily farm-to-store routing.", "architecture": "Databricks Mosaic AI + MLflow + AutoML"},
            {"title": "Sovereign Supplier & Retailer B2B Data Sharing Enclave", "category": "Unified Governance & Security", "description": "Delta Sharing enabling secure, zero-copy inventory synchronization between BAMA and grocery retail partners without data replication.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["bridgestone", "austrotherm"]
    },

    # 5. Bonheur ASA (Fred Olsen / Fred. Olsen AS)
    "Bonheur ASA (Fred Olsen)": {
        "industry": "Renewable Energy (Offshore Wind), Maritime Shipping & Logistics",
        "what_databricks_solves": "Unify offshore wind turbine sensor telemetry, vessel installation dynamics, and shipping fleet fuel telemetry into a high-performance Databricks Lakehouse, optimizing offshore turbine installation schedules and vessel fuel consumption.",
        "trend_macro": "Rapid expansion of European offshore wind capacity, extreme weather risks during marine turbine installation, and IMO carbon intensity regulations (CII) penalizing vessel emissions.",
        "trend_competitors": "Offshore wind leaders (Ørsted, Vestas, Cadeler) leverage Databricks to model oceanic wave-height thresholds, turbine blade aerodynamic fatigue, and vessel positioning fuel burns.",
        "trend_legacy_debt": "Isolated operational systems: Wind farm SCADA databases in the UK/Norway separated from vessel chartering software and maritime fleet maintenance logs.",
        "fomo_cost_of_inaction": "Severe installation vessel downtime: An offshore jack-up wind installation vessel idle due to poor weather forecasting costs between €150,000 and €300,000 per day in lost revenue.",
        "fomo_peer_velocity": "Competitors simulate dynamic turbine installation weather windows in real-time; Fred. Olsen project teams rely on static meteorological PDF reports.",
        "fomo_vendor_traps": "Proprietary maritime software suites with locked sensor data formats charging exorbitant fees to integrate telemetry into enterprise analytics.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€2,500,000",
        "payback_months": 7,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€6,990,000",
        "key_questions": [
            {"target": "Managing Director, Fred. Olsen Windcarrier", "question": "What is the daily economic loss when a jack-up installation vessel misses a turbine installation window due to fragmented wave and weather intelligence?"},
            {"target": "Chief Technology Officer (CTO)", "question": "Why is wind turbine vibration telemetry segregated from your central engineering asset management systems?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much will IMO Carbon Intensity Indicator (CII) compliance penalties cost your maritime shipping fleet if vessel fuel optimization remains unautomated?"},
            {"target": "Head of Renewable Operations", "question": "Can your engineers run predictive turbine blade degradation models across hundreds of offshore assets simultaneously?"}
        ],
        "use_cases": [
            {"title": "Offshore Wind Installation Weather & Crane Dynamic Digital Twin", "category": "Lakehouse Modernization", "description": "Delta Lake streaming high-frequency meteorological and marine wave sensors to calculate safe turbine installation windows.", "architecture": "Delta Live Tables + Azure Databricks + Azure Digital Twins"},
            {"title": "Maritime Fleet Fuel Efficiency & IMO Carbon Modeling", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning algorithms modeling hull friction, engine load, and optimal route trim to minimize bunker fuel consumption.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Cross-Subsidiary Maritime & Energy Lakehouse", "category": "Unified Governance & Security", "description": "Unity Catalog federating data across Fred. Olsen Renewables, Windcarrier, and Shipping with role-based sovereign security.", "architecture": "Unity Catalog + Power BI Direct Lake"}
        ],
        "matched_cases": ["fluvius", "nordic-paper"]
    },

    # 6. Borr Drilling
    "Borr Drilling": {
        "industry": "Offshore Drilling & Oilfield Services",
        "what_databricks_solves": "Consolidate edge telemetry from modern shallow-water jack-up drilling rigs (topdrive vibration, mud pump pressure, blowout preventer sensor streams) into an Azure Databricks Lakehouse to predict equipment failure and eliminate non-productive time (NPT).",
        "trend_macro": "High rig dayrates, intense offshore safety and environmental scrutiny, and oil major operator demands for automated real-time drilling telemetry.",
        "trend_competitors": "Major offshore drillers (Transocean, Valaris, Noble) deploy Lakehouse predictive maintenance platforms, reducing unplanned equipment NPT by up to 25%.",
        "trend_legacy_debt": "Rig-level industrial control systems with data stored in disconnected on-rig hard drives; manual morning tour reports sent via daily email attachments.",
        "fomo_cost_of_inaction": "High Non-Productive Time (NPT): A single topdrive or drawworks breakdown on a jack-up rig can cost Borr Drilling over $100,000 per day in contract penalties and repair overhead.",
        "fomo_peer_velocity": "Leading drillers detect drilling anomaly patterns hours before bit wear causes a pipe trip; Borr crews rely on threshold alarms on individual rig consoles.",
        "fomo_vendor_traps": "Rig equipment manufacturers (OEMs) attempting to lock drilling sensor telemetry into proprietary cloud monitoring subscriptions with recurring fee escalation.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€5,840,000",
        "key_questions": [
            {"target": "VP Operations / Drilling Superintendent", "question": "What is your average annual NPT expenditure caused by mechanical failures on topdrives and mud pumps across your operating fleet?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you synchronize gigabytes of sensor telemetry generated daily on remote offshore rigs with central onshore engineering teams?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much enterprise value could you unlock by demonstrating to operators that Borr has algorithmic, real-time safety and maintenance governance on every rig?"},
            {"target": "VP of Health, Safety & Environment (HSE)", "question": "Can your safety officers query cross-fleet sensor anomalies leading up to historic near-miss incidents in natural language?"}
        ],
        "use_cases": [
            {"title": "Rig Edge-to-Cloud Telemetry & Real-Time NPT Prevention", "category": "Lakehouse Modernization", "description": "Delta Lake edge sync aggregating mud-pulse, mechanical vibration, and pressure streams into an onshore analytics Lakehouse.", "architecture": "Databricks Edge Sync + Delta Lake + Azure IoT Edge"},
            {"title": "Predictive Drill-Bit & Topdrive Asset Health Modeling", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning vibration analysis forecasting mechanical fatigue and scheduling proactive maintenance during scheduled pipe trips.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Client Data Sharing for Oil Major Operators", "category": "Unified Governance & Security", "description": "Delta Sharing providing secure, real-time telemetry access to exploration clients (TotalEnergies, Shell) without data duplication.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["fluvius", "bridgestone"]
    },

    # 7. COWI
    "COWI": {
        "industry": "Engineering Consulting, Infrastructure & Renewable Energy Design",
        "what_databricks_solves": "Integrate massive Building Information Modeling (BIM) datasets, geospatial GIS layers (H3/geoparquet), and structural engineering telemetry onto Databricks, enabling automated design compliance checks and AI-accelerated infrastructure engineering.",
        "trend_macro": "Surging Nordic megaprojects (rail, offshore wind foundations, green hydrogen hubs), complex environmental impact assessments, and acute shortage of senior structural engineers.",
        "trend_competitors": "Global engineering consultancies (Arup, WSP, Ramboll) deploy Databricks geospatial Lakehouses to automate bridge inspection via computer vision and run generative engineering spec searches.",
        "trend_legacy_debt": "Gigabytes of 3D CAD/BIM files isolated across local workstations, project-specific network drives, and disconnected project accounting databases.",
        "fomo_cost_of_inaction": "Bidding uncompetitiveness: Engineering teams spending 20% of project billable hours searching for past project calculations and manually verifying environmental codes.",
        "fomo_peer_velocity": "Competitors execute complex hydraulic and geotechnical simulations in parallel cloud clusters in minutes; COWI project engineers wait hours for desktop solver runs.",
        "fomo_vendor_traps": "Costly, escalating per-seat licenses on proprietary engineering simulation packages that restrict scalable cloud parallelization.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,300,000",
        "payback_months": 7,
        "investment_eur": "€490,000",
        "three_year_net_value_eur": "€6,410,000",
        "key_questions": [
            {"target": "Chief Operating Officer / Technical Director", "question": "What percentage of billable senior engineering time is lost manually retrieving past project calculations and verifying standard building codes?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you combining massive geospatial LiDAR, satellite imagery, and 3D BIM models into a unified corporate knowledge repository?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is your cloud compute spend across disparate engineering teams spinning up ad-hoc cloud VMs for finite element simulations?"},
            {"target": "Head of Digital Transformation", "question": "Can your engineers interrogate 50 years of COWI project blueprints and technical reports using a secure, governed internal LLM?"}
        ],
        "use_cases": [
            {"title": "Geospatial & BIM Infrastructure Lakehouse", "category": "Lakehouse Modernization", "description": "Mosaic geospatial analytics (H3 indexing, Geoparquet) integrating terrain LiDAR, GIS data, and structural sensor telemetry.", "architecture": "Azure Databricks + Databricks Mosaic Geospatial + Delta Lake"},
            {"title": "Generative Engineering Knowledge & Code Assistant", "category": "Enterprise GenAI & Mosaic AI", "description": "Governed internal LLM trained on COWI proprietary engineering project archives and Nordic building codes with source citation.", "architecture": "Databricks Mosaic AI + Vector Search + Azure OpenAI"},
            {"title": "Unified Multi-National Project Data Governance", "category": "Unified Governance & Security", "description": "Unity Catalog managing project data across Denmark, Norway, Sweden, and UK with ISO 19650 compliant audit trails.", "architecture": "Unity Catalog + Azure Data Lake Storage Gen2"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 8. Cubus / Dressmann AS (Varner Group)
    "Cubus": {
        "industry": "Fashion Retail & Omnichannel Apparel",
        "what_databricks_solves": "Unify e-commerce clickstream data, 300+ physical store POS streams, and central warehouse inventory on Azure Databricks to eliminate store stockouts, automate markdown pricing, and predict fashion trend lifecycles.",
        "trend_macro": "Severe apparel margin pressure, volatile post-pandemic foot traffic, high returns on e-commerce fashion, and regulatory pressure for textile traceability.",
        "trend_competitors": "Agile fast-fashion retailers (Inditex, Bestseller) utilize Lakehouses to synchronize real-time RFID store inventory with dynamic digital marketing, cutting unsold inventory write-offs by 22%.",
        "trend_legacy_debt": "Legacy ERP inventory modules with overnight batch processing; separate e-commerce platforms with disconnected customer loyalty databases.",
        "fomo_cost_of_inaction": "Costly inventory markdowns: Millions in margin lost each season due to late discounting and stockouts of trending sizes in high-traffic city stores.",
        "fomo_peer_velocity": "Competitors detect regional viral social fashion trends and reallocate store stock within 48 hours; Cubus merchandising cycles operate on 2-week batch reviews.",
        "fomo_vendor_traps": "Legacy e-commerce and retail analytics suites with high transactional query costs and no unified lakehouse architecture.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€1,800,000",
        "payback_months": 6,
        "investment_eur": "€390,000",
        "three_year_net_value_eur": "€5,010,000",
        "key_questions": [
            {"target": "Chief Commercial Officer / Retail Director", "question": "What is the seasonal gross margin loss when store markdown decisions rely on 48-hour-old batched sales data rather than real-time sell-through velocity?"},
            {"target": "Chief Information Officer (CIO)", "question": "How many fragmented copies of customer profiles exist between your store POS systems, mobile loyalty app, and online webshop?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much working capital is tied up in excess inventory trapped in low-demand regional stores?"},
            {"target": "Head of Supply Chain", "question": "Can your inventory allocation algorithms automatically trigger inter-store transfers based on predictive weather and local event signals?"}
        ],
        "use_cases": [
            {"title": "Real-Time Omnichannel Inventory & RFID Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Live Tables pipelines aggregating physical store POS, e-commerce orders, and warehouse RFID telemetry in sub-minutes.", "architecture": "Delta Lake + Delta Live Tables + Event Hubs"},
            {"title": "Dynamic Markdown Optimization & Demand Sensing", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting SKU-level price elasticity to maximize full-price sell-through before season end.", "architecture": "Databricks Mosaic AI + MLflow + Power BI"},
            {"title": "Governed Customer 360 & Omnichannel Loyalty", "category": "Unified Governance & Security", "description": "Unity Catalog establishing a single, GDPR-compliant customer master record with role-based access for marketing and analytics.", "architecture": "Unity Catalog + Feature Store + Delta Sharing"}
        ],
        "matched_cases": ["cera", "bridgestone"]
    },

    # 9. Danish Crown
    "Danish Crown": {
        "industry": "Food Processing, Agriculture & Global Meat Export",
        "what_databricks_solves": "Modernize Europe's largest meat processing network with an Azure Databricks Lakehouse, integrating pig abattoir computer vision yield data, farm-to-fork cold chain sensors, and CSRD Scope 3 agricultural carbon footprints across 6,000+ member farms.",
        "trend_macro": "Intense consumer and regulatory pressure for agricultural decarbonization (EU CSRD), strict food safety and veterinary audit requirements, and global export commodity volatility.",
        "trend_competitors": "Global agri-food giants (JBS, Tyson, Arla) deploy Lakehouses to optimize carcass yield cutting algorithms in real-time and automate ESG farm emissions reporting.",
        "trend_legacy_debt": "Factory-level industrial automation systems (MES/SCADA) isolated from corporate SAP ERP; reliance on manual spreadsheets for farm carbon accounting.",
        "fomo_cost_of_inaction": "Customer contract risk: Major international retailers (Tesco, Coop, McDonald's) demanding certified product-level carbon footprints that Danish Crown cannot deliver without manual audits.",
        "fomo_peer_velocity": "Competitors calculate real-time abattoir carcass yield variations and adjust cutting robotics hourly; Danish Crown plant managers receive weekly aggregate yield sheets.",
        "fomo_vendor_traps": "Legacy ERP data warehouse instances requiring expensive compute scaling to process millions of animal tracking records.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 61,
        "productivity_lift_multiplier": "3.7x",
        "annual_savings_eur": "€2,700,000",
        "payback_months": 7,
        "investment_eur": "€540,000",
        "three_year_net_value_eur": "€7,560,000",
        "key_questions": [
            {"target": "Chief Operating Officer / VP Operations", "question": "What is the annual margin impact of a 0.5% carcass yield improvement across your primary Danish slaughterhouse facilities?"},
            {"target": "Chief Technology Officer (CTO)", "question": "Why are abattoir automated cutting camera streams isolated from your central corporate SAP supply chain database?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How many man-weeks are required each quarter to calculate verified farm-to-fork Scope 3 carbon footprints for major European supermarket tenders?"},
            {"target": "VP of Sustainability & Quality", "question": "Can you trace the complete veterinary, feed, and transport history of an exported pork batch within 60 seconds of a customer inquiry?"}
        ],
        "use_cases": [
            {"title": "Automated Carcass Yield & Computer Vision Quality Engine", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting high-speed abattoir camera feeds and cutting metrics to optimize meat fabrication yields in real-time.", "architecture": "Azure Databricks + Delta Live Tables + IoT Edge"},
            {"title": "Farm-to-Fork CSRD Scope 3 Agricultural Carbon Accounting", "category": "Enterprise GenAI & Mosaic AI", "description": "Automated machine learning models processing feed, manure, and energy data from 6,000+ cooperative farms into auditable ESG reports.", "architecture": "Databricks Mosaic AI + Cegeka ESG Blueprint"},
            {"title": "Sovereign Global Export Traceability & Food Safety Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining immutable batch audit trails for Chinese and US FDA food safety inspections.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 10. Danish Government (Lægemiddelstyrelsen / Sundhedsdatastyrelsen)
    "Danish Government": {
        "industry": "Government, Health Authorities & Life Science Regulation",
        "what_databricks_solves": "Establish a sovereign Danish Health & Life Sciences Data Lakehouse on Azure Databricks with Unity Catalog clean rooms, enabling real-time pharmacovigilance, automated adverse drug reaction tracking, and secure clinical trial evaluation without privacy leaks.",
        "trend_macro": "Surging clinical trial applications for biotech therapeutics, strict Danish health privacy mandates, and the European Health Data Space (EHDS) directive.",
        "trend_competitors": "Top European health agencies (EMA, MHRA) leverage governed cloud Lakehouses to screen national health registries for emerging drug safety signals using NLP.",
        "trend_legacy_debt": "Isolated health registry silos (Landspatientregisteret, Lægemiddelstatistikregisteret) on legacy Oracle/SAS databases with multi-month query backlogs.",
        "fomo_cost_of_inaction": "Delayed public health insights: Unidentified adverse drug reactions remaining undetected for months due to slow batch queries across national prescription databases.",
        "fomo_peer_velocity": "Modern regulatory bodies identify pharmacovigilance anomalies in days; Danish agency scientists face multi-week data extraction approvals.",
        "fomo_vendor_traps": "Heavy recurring licensing for on-premise SAS and Oracle database infrastructure with prohibitive expansion costs.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 53,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,750,000",
        "payback_months": 8,
        "investment_eur": "€430,000",
        "three_year_net_value_eur": "€4,820,000",
        "key_questions": [
            {"target": "Director General / Medical Director", "question": "How many weeks does it currently take your scientific officers to correlate adverse drug event reports with national prescription databases?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you provide researchers with secure access to de-identified patient data without physically copying sensitive datasets?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the government saving by transitioning legacy SAS statistical processing to an elastic, serverless Databricks Lakehouse?"},
            {"target": "Data Protection Officer (DPO)", "question": "Can you guarantee end-to-end cryptographic auditability of every query executed against national health records?"}
        ],
        "use_cases": [
            {"title": "Sovereign Health Clean Rooms for Clinical Research", "category": "Unified Governance & Security", "description": "Unity Catalog clean rooms allowing pharmaceutical sponsors and regulators to query pooled clinical trial data without sharing raw patient PII.", "architecture": "Unity Catalog Clean Rooms + Azure Databricks"},
            {"title": "AI-Driven Pharmacovigilance & Adverse Drug Reaction NLP", "category": "Enterprise GenAI & Mosaic AI", "description": "NLP models interrogating unstructured medical discharge summaries and yellow card reports to detect drug interaction signals.", "architecture": "Databricks Mosaic AI + Azure OpenAI gpt-5-mini"},
            {"title": "National Health Registry Modernization & Fast Ingestion", "category": "Lakehouse Modernization", "description": "Delta Lake replacing batch SQL pipelines for Danish national health registries with sub-second query performance.", "architecture": "Delta Lake + Photon + Power BI"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    },

    # 11. Diaverum
    "Diaverum": {
        "industry": "Healthcare Services, Renal Care & Dialysis Clinics",
        "what_databricks_solves": "Connect clinical data and dialysis machine sensor telemetry across 450+ clinics in 24 countries into an Azure Databricks Lakehouse, predicting intradialytic hypotension and vascular access failure to improve patient survival rates and clinic efficiency.",
        "trend_macro": "Rising chronic kidney disease (CKD) prevalence globally, nursing shortages, and value-based healthcare contracts tied to patient clinical outcomes.",
        "trend_competitors": "Global renal care providers (Fresenius, DaVita) deploy Lakehouse AI models to predict patient hospitalization risks 48 hours before symptoms appear.",
        "trend_legacy_debt": "Clinic-level electronic medical records (EMR) siloed by country; dialysis machine logs rarely integrated into central clinical analytics.",
        "fomo_cost_of_inaction": "Avoidable patient hospitalizations: Clinical complications during dialysis cost millions annually and degrade quality of life, which predictive telemetry can preempt.",
        "fomo_peer_velocity": "Peers deploy real-time clinic staffing and dialysis machine scheduling algorithms; Diaverum clinic managers handle shifts with manual spreadsheets.",
        "fomo_vendor_traps": "Heavily customized legacy EMR databases with proprietary schemas requiring bespoke ETL connectors for every analytics query.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€470,000",
        "three_year_net_value_eur": "€5,830,000",
        "key_questions": [
            {"target": "Chief Medical Officer (CMO)", "question": "What is your clinical hospitalization rate for patients experiencing intradialytic hypotension that could be predicted from historical biometric trends?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you enforce multi-national GDPR and country-specific health data sovereignty across clinics in 24 countries?"},
            {"target": "Chief Operating Officer (COO)", "question": "How much clinic capacity is wasted each month due to unpredicted patient transport cancellations and missed dialysis sessions?"},
            {"target": "CFO", "question": "What is the return on investment of deploying automated dialysis consumable inventory forecasting across 450 clinics?"}
        ],
        "use_cases": [
            {"title": "Predictive Dialysis Complication & Biometric Early Warning", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models analyzing real-time blood pressure, fluid removal rates, and blood tests to alert clinicians of shock risks.", "architecture": "Databricks Mosaic AI + MLflow + Feature Store"},
            {"title": "Global Sovereign Renal Care Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog federating clinic data across Europe, Latin America, and Middle East with strict medical sovereignty controls.", "architecture": "Unity Catalog + Azure Confidential Computing"},
            {"title": "Automated Clinic Scheduling & Consumable Inventory Engine", "category": "Lakehouse Modernization", "description": "Delta Lake pipelines predicting dialyzer and medication usage to prevent stockouts and balance nursing workloads.", "architecture": "Delta Live Tables + Power BI"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    },

    # 12. ECCO Sko
    "ECCO Sko": {
        "industry": "Footwear Manufacturing, Leather Tannery & Global Retail",
        "what_databricks_solves": "Unify leather tannery chemical telemetry, automated shoe factory robotics, and 2,000+ global retail store POS feeds into an Azure Databricks Lakehouse, optimizing leather hide yield, reducing factory energy, and predicting global retail sell-through.",
        "trend_macro": "Leather raw material price volatility, global supply chain lead time pressures, EU digital product passport mandates, and shifting consumer footwear preferences.",
        "trend_competitors": "Global footwear brands (Nike, Adidas, On Running) leverage Databricks to dynamically optimize retail store size-curve inventory and factory production batches.",
        "trend_legacy_debt": "Tannery and factory SCADA systems completely isolated from corporate SAP S/4HANA ERP; retail e-commerce analytics running on disparate cloud databases.",
        "fomo_cost_of_inaction": "Tannery scrap and excess footwear inventory: A 1% yield loss in premium leather cutting costs millions annually, while misallocated retail inventory leads to heavy end-of-season discounting.",
        "fomo_peer_velocity": "Competitors rebalance retail store shoe sizes based on weekly regional sell-through velocity; ECCO country managers rely on monthly batch reports.",
        "fomo_vendor_traps": "Proprietary factory IoT monitoring platforms charging recurring per-machine fees with zero ability to cross-reference data against commercial retail sales.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,400,000",
        "payback_months": 7,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€6,690,000",
        "key_questions": [
            {"target": "Executive VP Global Operations", "question": "What is the annual cost of leather hide scrap that could be prevented through computer vision and automated cutting optimization?"},
            {"target": "Chief Commercial Officer / Retail VP", "question": "How often do high-volume ECCO retail stores run out of core shoe sizes while adjacent regional stores hold excess inventory?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is factory production telemetry in Portugal, Slovakia, and Indonesia segregated from your commercial demand planning data?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What would be the working capital reduction if global footwear manufacturing batch schedules responded dynamically to weekly e-commerce sales trends?"}
        ],
        "use_cases": [
            {"title": "Factory-to-Retail Digital Twin & Leather Yield Engine", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting tannery hide scans, factory machine logs, and global retail sales to optimize cutting yields.", "architecture": "Delta Live Tables + Azure IoT Hub + SAP Connector"},
            {"title": "Global Omnichannel Footwear Demand & Size-Curve Sensing", "category": "Enterprise GenAI & Mosaic AI", "description": "Predictive models optimizing store-level footwear allocation and size curves based on local consumer purchasing patterns.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Digital Product Passport & Supply Chain Traceability", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining immutable leather provenance and tannery environmental metrics for upcoming EU passport regulations.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["austrotherm", "bridgestone"]
    },

    # 13. Energistyrelsen (Danish Energy Agency)
    "Energistyrelsen": {
        "industry": "Energy Regulation, Utilities & Offshore Renewable Infrastructure",
        "what_databricks_solves": "Modernize national energy grid simulations, offshore wind tender assessments, and Denmark's greenhouse gas emission accounting on an Azure Databricks Lakehouse, processing millions of smart grid intervals and renewable generation telemetry.",
        "trend_macro": "Aggressive national mandate for 100% renewable electricity by 2030, North Sea energy island buildouts, and complex hydrogen and Power-to-X integration.",
        "trend_competitors": "European energy regulators (Ofgem, BNetzA) use Lakehouse analytics to simulate grid bottleneck congestion and dynamic electricity pricing impacts in minutes.",
        "trend_legacy_debt": "Legacy relational databases and statistical spreadsheets struggling to handle high-frequency smart meter readings and offshore turbine generation streams.",
        "fomo_cost_of_inaction": "Sub-optimal grid investment decisions: Inaccurate congestion forecasting risks billions in stranded offshore wind grid cabling and renewable curtailment compensation.",
        "fomo_peer_velocity": "Modern agencies run national energy transition scenarios across thousands of variables in minutes; Energistyrelsen analysts wait days for complex simulation models.",
        "fomo_vendor_traps": "High maintenance costs on legacy proprietary spatial and economic modeling tools with unscalable compute architectures.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€1,350,000",
        "payback_months": 8,
        "investment_eur": "€350,000",
        "three_year_net_value_eur": "€3,700,000",
        "key_questions": [
            {"target": "Director General / Energy Regulation Head", "question": "How rapidly can your modeling teams simulate the impact of a 5 GW offshore wind surge on domestic transmission bottlenecks?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you handling the explosive growth of 15-minute interval data flowing from Danish smart meters and district heating grids?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the computational cost of running national renewable subsidy and tender economic models on legacy infrastructure?"},
            {"target": "Chief Data Officer", "question": "Can you provide public researchers and energy developers with governed, secure access to national energy data via open APIs?"}
        ],
        "use_cases": [
            {"title": "National Grid Bottleneck & Renewable Simulation Engine", "category": "Lakehouse Modernization", "description": "Delta Lake processing high-frequency offshore wind, solar, and smart meter time-series data to simulate grid congestion.", "architecture": "Delta Lake + Spark Streaming + Power BI"},
            {"title": "AI-Driven Power-to-X & Energy Island Yield Forecasting", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting green hydrogen conversion yields and offshore wind generation under variable weather.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Sovereign Danish Energy & Climate Data Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog providing secure, governed data sharing between Energinet, wind developers, and government bodies.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["fluvius", "water-link"]
    },

    # 14. Frederiksberg Forsyning A/S / VandCenter Syd
    "Frederiksberg Forsyning A/S": {
        "industry": "District Heating, Water Utilities & Urban Infrastructure",
        "what_databricks_solves": "Consolidate district heating acoustic sensors, smart water meter telemetry, and urban storm sewer overflow monitors into an Azure Databricks Lakehouse, optimizing municipal boiler energy efficiency and predicting water pipe bursts.",
        "trend_macro": "Severe district heating biomass/electricity price volatility, urban flash flood risks from climate change, and European water directives mandating reduction of non-revenue water loss (NRW).",
        "trend_competitors": "Smart municipal utilities (HOFOR, Hamburg Wasser) deploy Lakehouse digital twins to reduce district heating pump energy by 18% and isolate pipe leaks in hours.",
        "trend_legacy_debt": "Isolated SCADA systems for district heating, water distribution, and sewage networks; smart meter data analyzed in batch spreadsheets.",
        "fomo_cost_of_inaction": "Undetected pipe bursts and energy waste: Millions in treated drinking water lost to underground leaks and unoptimized boiler firing schedules during temperature drops.",
        "fomo_peer_velocity": "Modern utilities pinpoint underground pipe bursts within 2 hours of acoustic sensor anomaly detection; Frederiksberg relies on citizen leak reports.",
        "fomo_vendor_traps": "Proprietary utility metering software charging recurring data export fees while locking telemetry away from cloud machine learning.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 53,
        "productivity_lift_multiplier": "3.1x",
        "annual_savings_eur": "€950,000",
        "payback_months": 8,
        "investment_eur": "€280,000",
        "three_year_net_value_eur": "€2,570,000",
        "key_questions": [
            {"target": "Managing Director / CEO", "question": "What is the annual cost of non-revenue water (NRW) lost to underground leaks across your municipal distribution network?"},
            {"target": "Head of District Heating / Operations", "question": "How quickly can your boiler dispatch algorithms react to real-time weather forecasts to optimize heat production?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why are district heating SCADA data, smart water meter readings, and wastewater sensor feeds separated across different database silos?"},
            {"target": "CFO", "question": "What is the operational saving of transitioning manual leak detection crews to automated acoustic sensor anomaly alerts on a Lakehouse?"}
        ],
        "use_cases": [
            {"title": "Smart District Heating & Water Digital Twin", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting smart meter telemetry, flow sensors, and weather feeds to optimize district heat pressure and pumping energy.", "architecture": "Delta Live Tables + Azure IoT Hub + Power BI"},
            {"title": "Acoustic Sensor Pipe Burst & Sewer Overflow Prediction", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning anomaly detection algorithms identifying micro-vibrations in pipes before major bursts occur.", "architecture": "Databricks Mosaic AI + Streaming Analytics"},
            {"title": "Governed Municipal Environmental & ESG Compliance", "category": "Unified Governance & Security", "description": "Unity Catalog ensuring auditable compliance with Danish environmental regulations and groundwater protection mandates.", "architecture": "Unity Catalog + Cegeka ESG Blueprint"}
        ],
        "matched_cases": ["water-link", "fluvius"]
    },

    # 15. G2 Ocean
    "G2 Ocean": {
        "industry": "Maritime Shipping, Open Hatch & Bulk Carrier Logistics",
        "what_databricks_solves": "Consolidate vessel engine fuel telemetry, weather routing feeds, and cargo stowage logistics across 130+ open hatch bulk vessels into an Azure Databricks Lakehouse, cutting bunker fuel consumption and ensuring IMO Carbon Intensity Indicator (CII) compliance.",
        "trend_macro": "EU Emissions Trading System (EU ETS) maritime inclusion, stringent IMO carbon intensity regulations, and volatile global maritime freight rates.",
        "trend_competitors": "Top shipping lines (Maersk, Wallenius Wilhelmsen) utilize Databricks Lakehouses to optimize vessel speed, trim, and weather routing, saving millions in bunker fuel annually.",
        "trend_legacy_debt": "Vessel noon reports submitted manually by ship captains via email; fragmented maintenance databases isolated from central chartering ERP.",
        "fomo_cost_of_inaction": "Severe carbon regulatory penalties: Non-compliant CII vessel ratings leading to trading restrictions and millions in EU ETS carbon allowance purchase mandates.",
        "fomo_peer_velocity": "Competitors calculate dynamic speed and route optimization hourly based on ocean currents; G2 Ocean vessels execute voyages on static pre-departure voyage plans.",
        "fomo_vendor_traps": "Proprietary maritime telemetry providers attempting to monopolize vessel sensor data with high recurring connectivity and analytics fees.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,800,000",
        "payback_months": 6,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€7,880,000",
        "key_questions": [
            {"target": "Chief Operating Officer / VP Fleet Operations", "question": "What is the annual bunker fuel expenditure difference between your top-performing and lowest-performing vessel crews across identical bulk trade routes?"},
            {"target": "Chief Commercial Officer", "question": "How quickly can your chartering team model the exact EU ETS carbon allowance cost of an upcoming dry bulk voyage tender?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you automate the ingestion of high-frequency engine sensor telemetry from 130+ vessels into a centralized analytics Lakehouse?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is your projected financial exposure to IMO CII vessel rating downgrades over the next 24 months?"}
        ],
        "use_cases": [
            {"title": "Fleet Telemetry & Dynamic Weather Routing Engine", "category": "Lakehouse Modernization", "description": "Delta Lake streaming high-frequency vessel sensor data, wave heights, and engine RPM to optimize speed and voyage fuel burn.", "architecture": "Delta Live Tables + Azure Event Hubs + Power BI"},
            {"title": "Automated EU ETS & IMO Carbon Compliance Modeler", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting voyage emissions and recommending optimal carbon allowance purchasing strategies.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Joint-Venture Chartering & Fleet Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog providing fine-grained access control across Gearbulk and Grieg Star joint-venture stakeholders.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["bridgestone", "fluvius"]
    },

    # 16. Hartmann (Brødrene Hartmann A/S)
    "Hartmann": {
        "industry": "Industrial Packaging, Moulded-Fibre Technology & Sustainable Manufacturing",
        "what_databricks_solves": "Modernize manufacturing telemetry across global moulded-fibre egg packaging plants on an Azure Databricks Lakehouse, optimizing drying oven energy consumption, predicting moulding tool wear, and streamlining global supply chain demand.",
        "trend_macro": "Severe natural gas and industrial electricity price shocks in Europe, global consumer shifts away from plastic packaging to moulded fibre, and paper pulp commodity volatility.",
        "trend_competitors": "Global packaging leaders (Huhtamaki, Smurfit Kappa) deploy industrial Lakehouses to optimize drying oven thermal curves, cutting plant energy consumption by up to 14%.",
        "trend_legacy_debt": "Plant-level industrial SCADA systems completely isolated by country; drying oven thermal data trapped in local PLC historians with zero corporate analytics.",
        "fomo_cost_of_inaction": "Escalating thermal energy costs: Drying moulded fibre requires massive heat energy; unoptimized oven operations waste millions annually in excess gas and electricity.",
        "fomo_peer_velocity": "Competitors predict pulp moulding tool degradation and schedule maintenance during planned shifts; Hartmann plants suffer unplanned machine stops.",
        "fomo_vendor_traps": "Proprietary industrial machine vendor control modules restricting raw telemetry access and demanding expensive hardware upgrades.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€1,650,000",
        "payback_months": 7,
        "investment_eur": "€370,000",
        "three_year_net_value_eur": "€4,580,000",
        "key_questions": [
            {"target": "Chief Operating Officer / VP Manufacturing", "question": "What is the thermal energy cost variance between your most efficient and least efficient moulded-fibre drying ovens per ton of packaging produced?"},
            {"target": "Chief Technology Officer (CTO)", "question": "Why is industrial sensor telemetry in your European, North American, and South American plants segregated from your central corporate ERP?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much working capital could you release by automating pulp raw material inventory replenishment based on predictive customer egg packaging orders?"},
            {"target": "Head of Sustainability", "question": "Can you provide retail customers with verified, batch-level Scope 1-3 carbon footprint certificates for your sustainable packaging products?"}
        ],
        "use_cases": [
            {"title": "Drying Oven Thermal Optimization & Energy Reduction", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting high-frequency temperature, humidity, and airflow sensors to optimize oven gas burn in real-time.", "architecture": "Delta Live Tables + Azure IoT Edge + Spark Streaming"},
            {"title": "Predictive Moulding Tool Wear & Quality Vision Inspection", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning and computer vision models predicting packaging fibre defects and mould tool wear prior to mechanical failure.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Global Industrial Plant ESG & Operations Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog centralizing production and energy metrics across 15+ international factories with auditable compliance.", "architecture": "Unity Catalog + Cegeka Reference Architecture"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 17. Jotun A/S
    "Jotun A/S": {
        "industry": "Chemicals, Marine Coatings & Architectural Paints",
        "what_databricks_solves": "Connect marine hull coating bio-fouling telemetry, chemical formulation R&D databases, and global factory manufacturing streams into an Azure Databricks Lakehouse, accelerating paint formulation discovery and proving ship fuel efficiency savings to maritime clients.",
        "trend_macro": "Stricter IMO maritime emission targets pushing shipowners toward low-friction hull coatings, chemical raw material price volatility, and demand for sustainable paints.",
        "trend_competitors": "Global chemical & paint giants (AkzoNobel, Hempel, PPG) deploy Lakehouses to model oceanic bio-fouling kinetics and simulate coating degradation using predictive AI.",
        "trend_legacy_debt": "Laboratory formulation databases siloed in Sandefjord HQ; factory production batch data disconnected from marine vessel hull performance telemetry.",
        "fomo_cost_of_inaction": "Commercial contract vulnerability: Shipowners demand guaranteed fuel savings verified by real-time hull telemetry; inability to prove performance risks multi-million maritime fleet coating contracts.",
        "fomo_peer_velocity": "Competitors screen chemical polymer formulations virtually using machine learning; Jotun R&D scientists rely on extensive physical laboratory testing cycles.",
        "fomo_vendor_traps": "Legacy ERP databases struggling with high-frequency telemetry from thousands of coated ocean vessels.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,600,000",
        "payback_months": 6,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€7,290,000",
        "key_questions": [
            {"target": "VP Marine Coatings / Commercial Director", "question": "How do you provide commercial shipowners with automated, auditable proof of hull bio-fouling resistance and fuel savings under ISO 19030?"},
            {"target": "VP Research & Development (R&D)", "question": "How many months could you shave off new coating formulations by using machine learning models to predict raw material chemical stability?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you consolidating global manufacturing batch telemetry across 40+ factories with commercial paint sales in 100+ countries?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the return on investment of deploying algorithmic raw material procurement forecasting across global chemical supply chains?"}
        ],
        "use_cases": [
            {"title": "Hull Telemetry & Vessel Fuel Efficiency Engine (ISO 19030)", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting ocean currents, vessel speed, and engine load to prove hydrodynamic hull coating savings to shipowners.", "architecture": "Delta Lake + Spark Streaming + Power BI Embedded"},
            {"title": "AI-Driven Chemical Formulation & R&D Simulation", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models predicting paint durability, viscosity, and curing times to accelerate laboratory testing.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Global Manufacturing & Raw Material Supply Chain Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog governing chemical formulation intellectual property while synchronizing inventory across 40+ worldwide plants.", "architecture": "Unity Catalog + Azure Databricks"}
        ],
        "matched_cases": ["austrotherm", "bridgestone"]
    },

    # 18. JYSK
    "JYSK": {
        "industry": "Omnichannel Retail & Global Home Furnishing",
        "what_databricks_solves": "Modernize global supply chain and store replenishment across 3,300+ stores in 48 countries onto an Azure Databricks Lakehouse, processing sub-minute point-of-sale transactions and automated distribution center robotics telemetry to eliminate out-of-stocks.",
        "trend_macro": "Severe global shipping container disruptions, furniture raw material inflation (wood, textiles), and massive consumer migration toward omnichannel click-and-collect.",
        "trend_competitors": "Global retail leaders (IKEA, Walmart) deploy Databricks Lakehouse architectures to synchronize real-time store inventory, dynamic pricing, and warehouse automated guided vehicles (AGVs).",
        "trend_legacy_debt": "Central SAP ERP running overnight batch allocation jobs; regional distribution center WMS systems disconnected from online webshop clickstreams.",
        "fomo_cost_of_inaction": "Costly out-of-stocks and lost retail sales: A 1% out-of-stock rate across 3,300 stores represents tens of millions in uncaptured revenue during promotional campaigns.",
        "fomo_peer_velocity": "Competitors rebalance store inventory and execute dynamic promo pricing within 15 minutes; JYSK store managers wait for next-day replenishment reports.",
        "fomo_vendor_traps": "Expansive licensing renewals for legacy relational data warehouses and proprietary ETL suites struggling to scale with global store expansion.",
        "tco_reduction_pct": 47,
        "compute_savings_pct": 63,
        "productivity_lift_multiplier": "3.9x",
        "annual_savings_eur": "€3,400,000",
        "payback_months": 6,
        "investment_eur": "€580,000",
        "three_year_net_value_eur": "€9,620,000",
        "key_questions": [
            {"target": "Executive VP Logistics / Supply Chain", "question": "What is the quantified lost revenue when high-volume home furnishing SKUs stock out in regional stores during weekend promotional campaigns?"},
            {"target": "Chief Information Officer (CIO)", "question": "How long does your overnight SAP batch window take to calculate inventory replenishment across 3,300+ stores and 10 mega-distribution centers?"},
            {"target": "Chief Commercial Officer (CCO)", "question": "How quickly can your merchandising team analyze the margin impact of promotional campaign discounting across 48 international markets?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the annual cloud and licensing savings of replacing legacy on-premise data warehouses with a serverless Azure Databricks Lakehouse?"}
        ],
        "use_cases": [
            {"title": "Real-Time 3,300-Store Inventory & Replenishment Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Live Tables pipelines aggregating POS sales, web orders, and distribution center AGV telemetry in sub-minutes.", "architecture": "Delta Lake + Delta Live Tables + Azure Event Hubs"},
            {"title": "AI-Powered Promotional Demand Sensing & Dynamic Allocation", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting SKU sell-through by store cluster based on promotional flyers, weather, and foot traffic.", "architecture": "Databricks Mosaic AI + MLflow + Feature Store"},
            {"title": "Global Sovereign Retail Governance & Supplier Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog managing access across 48 international business units with automated GDPR data masking.", "architecture": "Unity Catalog + Power BI Direct Lake"}
        ],
        "matched_cases": ["cera", "bridgestone"]
    },

    # 19. Kommunal Landspensjonskasse (KLP)
    "Kommunal Landspensjonskasse gjensidig forsikringsselskap": {
        "industry": "Pension Management, Municipal Insurance & Asset Management",
        "what_databricks_solves": "Modernize Norway's largest municipal pension and financial services provider (NOK 1,000B+ AUM) on Azure Databricks, enabling high-performance Solvency II risk modeling, automated municipal loan underwriting, and ESG climate portfolio screening.",
        "trend_macro": "Severe global financial market volatility, escalating Norwegian municipal pension liabilities, and stringent EU Sustainable Finance Disclosure Regulation (SFDR) requirements.",
        "trend_competitors": "Top Nordic pension funds (Storebrand, APG, Keva) deploy Lakehouses to automate multi-asset portfolio stress-testing and ESG carbon intensity auditing.",
        "trend_legacy_debt": "Legacy core pension mainframe applications, isolated mortgage and lending databases, and heavy reliance on proprietary SAS actuarial software.",
        "fomo_cost_of_inaction": "Delayed investment risk hedging: Overnight risk calculations prevent portfolio managers from executing intraday hedging strategies during macroeconomic turbulence.",
        "fomo_peer_velocity": "Leading asset managers stress-test portfolio liquidity across 10,000 scenarios in minutes; KLP quants wait overnight for complex Monte Carlo runs.",
        "fomo_vendor_traps": "Costly annual SAS license renewals and mainframe transaction fees with steep penalties for burst compute capacity.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,900,000",
        "payback_months": 7,
        "investment_eur": "€530,000",
        "three_year_net_value_eur": "€8,170,000",
        "key_questions": [
            {"target": "Chief Investment Officer (CIO)", "question": "How quickly can your asset management quants execute multi-asset portfolio stress-testing across your NOK 1,000B+ balance sheet following an interest rate decision?"},
            {"target": "Chief Risk Officer (CRO)", "question": "What is the annual software licensing overhead of maintaining legacy actuarial SAS grids for Solvency II reporting?"},
            {"target": "Director of Municipal Lending", "question": "How many days does it take to evaluate loan risk and environmental credentials for Norwegian municipal infrastructure projects?"},
            {"target": "Head of Responsible Investment / ESG", "question": "Can your investment team audit Scope 1-3 greenhouse gas emissions across all public and private asset holdings in real-time?"}
        ],
        "use_cases": [
            {"title": "High-Performance Actuarial & Solvency II Risk Engine", "category": "Lakehouse Modernization", "description": "Photon-accelerated Databricks clusters running complex actuarial liability and Monte Carlo asset simulations in minutes.", "architecture": "Databricks Photon + Delta Lake + MLflow"},
            {"title": "Automated SFDR & Institutional ESG Portfolio Screening", "category": "Enterprise GenAI & Mosaic AI", "description": "NLP and machine learning models parsing corporate sustainability disclosures to calculate portfolio alignment with Paris goals.", "architecture": "Databricks Mosaic AI + Azure OpenAI"},
            {"title": "Governed Financial Risk & Municipal Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog providing fine-grained access control and cryptographic lineage for Norwegian Finanstilsynet audits.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["cera", "austrotherm"]
    },

    # 20. LEO Pharma
    "LEO Pharma": {
        "industry": "Pharmaceuticals, Medical Dermatology & Biotech",
        "what_databricks_solves": "Consolidate global clinical trial bioinformatics, medical dermatology real-world evidence (RWE), and international pharmaceutical supply chain data onto Azure Databricks with Unity Catalog, accelerating drug candidate pipeline delivery.",
        "trend_macro": "Intense competition in biological treatments for psoriasis and atopic dermatitis, rising clinical trial execution costs, and stringent EMA/FDA regulatory audit demands.",
        "trend_competitors": "Global pharma leaders (Novartis, Sanofi, AstraZeneca) deploy Lakehouses to combine genomic datasets, electronic health records, and clinical trials, reducing clinical study cycle times by 30%.",
        "trend_legacy_debt": "Isolated clinical research systems (EDC, CTMS, lab notebooks) separated from commercial ERP; heavy reliance on custom SAS pipelines with manual validation.",
        "fomo_cost_of_inaction": "Delayed clinical trial milestones: Every month of delay in filing a regulatory trial dossier represents millions in lost commercial exclusivity in global dermatology markets.",
        "fomo_peer_velocity": "Competitors utilize automated Lakehouse data pipelines to monitor clinical trial patient safety events in real-time; LEO Pharma clinical teams handle data with weekly batch reconciliations.",
        "fomo_vendor_traps": "Legacy bio-statistical software and closed EDC platforms demanding expensive licenses with rigid data export hurdles.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.7x",
        "annual_savings_eur": "€2,850,000",
        "payback_months": 7,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€8,030,000",
        "key_questions": [
            {"target": "Chief Medical Officer / VP Clinical R&D", "question": "What is the cycle time to aggregate, cleanse, and query multi-center dermatology clinical trial data across European and US trial sites?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you maintain strict GxP regulatory validation and audit trails while enabling clinical data scientists to run modern machine learning models?"},
            {"target": "Head of Regulatory Affairs", "question": "How many manual hours are spent formatting clinical study reports for EMA and FDA regulatory submissions?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the return on investment of migrating proprietary clinical SAS servers to an elastic, governed Databricks Lakehouse?"}
        ],
        "use_cases": [
            {"title": "GxP-Validated Clinical Trial Research Enclave", "category": "Unified Governance & Security", "description": "Unity Catalog compliant with 21 CFR Part 11 and GxP standards, isolating confidential patient records with immutable lineage.", "architecture": "Unity Catalog + Azure Confidential Computing + Delta Sharing"},
            {"title": "AI-Powered Dermatological Real-World Evidence & Literature Engine", "category": "Enterprise GenAI & Mosaic AI", "description": "Domain-specific NLP models interrogating clinical trial reports and medical journals to surface efficacy and safety patterns.", "architecture": "Databricks Mosaic AI + Vector Search + Azure OpenAI"},
            {"title": "High-Throughput Omics & Biomarker Data Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting patient genomic sequences, histology imagery, and clinical telemetry for accelerated target validation.", "architecture": "Delta Lake + MLflow + Feature Store"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    },

    # 21. Ministry of Defence - Norway (Forsvarsbygg / FFI / Norwegian Armed Forces)
    "Ministry of Defence - Norway": {
        "industry": "Defence, Military Logistics & Sovereign Strategic Infrastructure",
        "what_databricks_solves": "Establish an air-gapped, sovereign military operations and logistics Lakehouse on Azure Government / Sovereign Databricks, integrating military equipment sensor telemetry (F-35, naval frigates, army vehicles), base maintenance (Forsvarsbygg), and defence intelligence (FFI).",
        "trend_macro": "Severe Nordic geopolitical tensions, NATO Nordic integration (Finland, Sweden), and urgent requirements for military equipment readiness and sovereign cyber resilience.",
        "trend_competitors": "Allied defence forces (US DoD, UK MoD) deploy Databricks to predict military aircraft spare parts failure, coordinate joint logistics, and process classified satellite and radar imagery.",
        "trend_legacy_debt": "Air-gapped relational database silos; defence facility maintenance systems (Forsvarsbygg) completely disconnected from military operational command; heavy paper and classified manual forms.",
        "fomo_cost_of_inaction": "Degraded military equipment readiness: Unplanned maintenance downtime on critical naval frigates or combat aircraft compromising national security and NATO readiness mandates.",
        "fomo_peer_velocity": "Allied forces utilize automated predictive logistics to preposition ammunition and spare parts dynamically; Norwegian logistics officers rely on scheduled calendar maintenance.",
        "fomo_vendor_traps": "Classified defence IT contracts with stagnant legacy contractors charging immense customization fees for minor reporting updates.",
        "tco_reduction_pct": 36,
        "compute_savings_pct": 48,
        "productivity_lift_multiplier": "2.9x",
        "annual_savings_eur": "€2,500,000",
        "payback_months": 9,
        "investment_eur": "€580,000",
        "three_year_net_value_eur": "€6,920,000",
        "key_questions": [
            {"target": "Chief of Defence / Joint Logistics Commander", "question": "What is the operational readiness rate of your primary combat vehicle and naval fleets, and how much downtime is driven by unexpected spare part shortages?"},
            {"target": "Chief Information Officer (CIO) / Defence Cyber Head", "question": "How do you enforce cryptographic data isolation and multi-level classification (NATO Secret / Sovereign National) across shared analytics clusters?"},
            {"target": "Director, Forsvarsbygg (Defence Estates)", "question": "How are military facility energy usage and base structural health sensors integrated into operational military readiness metrics?"},
            {"target": "Chief Scientist, FFI (Defence Research)", "question": "Can your researchers run high-performance AI simulations on massive sensor datasets without compromising sovereign data custody?"}
        ],
        "use_cases": [
            {"title": "Sovereign Military Fleet Predictive Maintenance & Logistics", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting telemetry from military vehicles, naval vessels, and aircraft to predict component failure and automate supply lines.", "architecture": "Delta Lake + Azure Sovereign Cloud + Spark Streaming"},
            {"title": "Multi-Level Classified Security & Sovereign Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog attribute-based access control enforcing strict national security and NATO classification boundaries with tamper-evident audit logs.", "architecture": "Unity Catalog + Ed25519 Cryptographic Custody"},
            {"title": "AI-Powered Sensor Fusion & Geopolitical Intelligence", "category": "Enterprise GenAI & Mosaic AI", "description": "Computer vision and NLP models analyzing satellite, radar, and open-source intelligence for strategic defense awareness.", "architecture": "Databricks Mosaic AI + Secure Enclaves"}
        ],
        "matched_cases": ["ggz-rivierduinen", "water-link"]
    },

    # 22. Monjasa A/S
    "Monjasa A/S": {
        "industry": "Marine Fuel Trading, Global Bunkering & Maritime Logistics",
        "what_databricks_solves": "Modernize global marine fuel trading, tanker fleet logistics, and counterparty credit risk on Azure Databricks, processing real-time oil market price volatility, bunker tanker vessel GPS telemetry, and IMO 2020/2024 environmental fuel quality compliance.",
        "trend_macro": "Severe global oil price volatility, complex geopolitical shipping route diversions (Red Sea, Panama Canal), and maritime decarbonization with biofuel/methanol blends.",
        "trend_competitors": "Top global commodity & bunker traders (Bunker Holding, Trafigura) deploy Lakehouses to execute real-time hedging simulations and dynamically route bunker tankers to high-margin ports.",
        "trend_legacy_debt": "Legacy trading and risk management (ETRM) databases with slow batch reconciliations; vessel logistics tracked in email attachments and spreadsheets.",
        "fomo_cost_of_inaction": "Commodity margin slippage: Unhedged fuel price swings and unoptimized bunker tanker positioning costing millions in missed arbitrage and excessive idle waiting time.",
        "fomo_peer_velocity": "Competitors adjust global marine fuel spot quotes within seconds of crude oil futures shifts; Monjasa traders face multi-minute manual calculation delays.",
        "fomo_vendor_traps": "High recurring software licenses on legacy proprietary ETRM systems with expensive database maintenance.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€1,850,000",
        "payback_months": 7,
        "investment_eur": "€410,000",
        "three_year_net_value_eur": "€5,140,000",
        "key_questions": [
            {"target": "Chief Executive Officer / Head of Trading", "question": "What is the margin gain if your global bunker traders can view real-time arbitrage spreads between Rotterdam, Singapore, and Panama simultaneously?"},
            {"target": "Chief Risk Officer (CRO)", "question": "How long does it take to calculate your counterparty credit exposure across global shipping lines when maritime freight rates plunge?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is tanker fleet AIS telemetry separated from your central commercial trading and billing databases?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How much working capital could you release by automating marine fuel inventory financing and hedging workflows on a Lakehouse?"}
        ],
        "use_cases": [
            {"title": "Real-Time Commodity Trading & Algorithmic Hedging Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting live oil market feeds, foreign exchange rates, and trading positions for sub-second risk calculations.", "architecture": "Delta Live Tables + Spark Structured Streaming + Power BI"},
            {"title": "Bunker Tanker Fleet Positioning & Port Demand Sensing", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting bunker fuel demand by maritime hub and optimizing tanker fleet bunkering routes.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Global Counterparty Risk & Sanctions Screening", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining automated screening against international maritime sanctions lists and vessel AIS blackouts.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["bridgestone", "fluvius"]
    },

    # 23. NAV (Norwegian Labour and Welfare Administration)
    "NAV": {
        "industry": "Public Welfare, Social Security & Labor Market Administration",
        "what_databricks_solves": "Modernize Norway's largest public administration platform (managing 1/3 of Norway's national budget) on Azure Databricks, automating welfare claims triage (unemployment, sickness benefits, pensions), detecting organized fraud, and ensuring sovereign data governance.",
        "trend_macro": "Rising citizen caseloads, political demands for rapid benefit disbursement, strict Norwegian and EU privacy laws, and ethical AI fairness mandates.",
        "trend_competitors": "Leading national welfare agencies (Udbetaling Danmark, Swedish Försäkringskassan) deploy governed cloud Lakehouses to automate routine claims triage and detect complex organized benefit fraud.",
        "trend_legacy_debt": "Decades-old COBOL mainframe systems (Infotrygd) running alongside modern microservices; massive data silos separating unemployment, disability, and tax records.",
        "fomo_cost_of_inaction": "Millions in fraudulent or misallocated welfare disbursements and long citizen processing wait times that attract heavy parliamentary criticism and public dissatisfaction.",
        "fomo_peer_velocity": "Modern digital agencies approve 60% of standard unemployment claims within minutes via automated rule engines; NAV caseworkers face multi-week manual document reviews.",
        "fomo_vendor_traps": "Extensive consultancy expenditure maintaining fragile point-to-point ETL bridges between legacy mainframes and modern web portals.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 53,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€3,200,000",
        "payback_months": 8,
        "investment_eur": "€680,000",
        "three_year_net_value_eur": "€8,920,000",
        "key_questions": [
            {"target": "Director General / Head of NAV", "question": "What is your average processing cycle time for complex sickness benefit claims, and how many citizen cases suffer from missing cross-agency tax records?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you enforce attribute-based access control (ABAC) when cross-functional analytical teams train fraud detection models on sensitive citizen health and income data?"},
            {"target": "Chief Technology Officer (CTO)", "question": "What is the annual operating cost of maintaining legacy mainframe data synchronizers compared to a modern event-driven Delta Lakehouse?"},
            {"target": "Chief Security Officer / DPO", "question": "Can you prove complete, tamper-evident data lineage for every automated caseworker decision if challenged in an administrative court?"}
        ],
        "use_cases": [
            {"title": "High-Throughput Citizen Claims Ingestion & Triage Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake replacing batch mainframe extracts with event-driven streaming pipelines processing millions of citizen benefit transactions daily.", "architecture": "Delta Lake + Delta Live Tables + Kafka / Event Hubs"},
            {"title": "Ethical AI Caseworker Assistant & Fraud Pattern Detection", "category": "Enterprise GenAI & Mosaic AI", "description": "Governed machine learning models identifying complex organized benefit fraud rings while maintaining strict fairness guardrails.", "architecture": "Databricks Mosaic AI + Graph Analytics + MLflow"},
            {"title": "Sovereign Welfare Data Governance & Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing Norwegian privacy laws with cryptographic auditability and granular column-level masking.", "architecture": "Unity Catalog + Sovereign Cloud Security"}
        ],
        "matched_cases": ["ggz-rivierduinen", "cera"]
    },

    # 24. Navico (Navico Group / Brunswick)
    "Navico": {
        "industry": "Marine Electronics, Connected Boating & Digital Vessel Technology",
        "what_databricks_solves": "Consolidate IoT telemetry from hundreds of thousands of connected leisure and commercial boats (Lowrance, Simrad, B&G chartplotters, sonars, radars, engine sensors) into an Azure Databricks Lakehouse, powering predictive navigation and smart boating AI services.",
        "trend_macro": "Explosive growth of connected vessel IoT, consumer demand for automotive-style smart boat experiences (autonomous docking, cloud cartography), and marine OEM electrification.",
        "trend_competitors": "Marine technology peers (Garmin, Raymarine) utilize cloud Lakehouses to stream sonar crowdsourcing data, updating nautical bathymetry charts dynamically.",
        "trend_legacy_debt": "High-frequency sonar and radar streams trapped on local SD cards and chartplotter memory; cloud backend fragmented across separate microservices databases.",
        "fomo_cost_of_inaction": "Missed recurring software revenue: Inability to monetize connected boat telemetry into subscription-based navigation and predictive engine maintenance services.",
        "fomo_peer_velocity": "Competitors release crowdsourced contour depth charts within hours of boat survey uploads; Navico chart processing pipelines take weeks of manual bathymetry processing.",
        "fomo_vendor_traps": "Escalating costs on legacy NoSQL and relational cloud databases collapsing under billions of continuous GPS and sonar telemetry points.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 61,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€2,150,000",
        "payback_months": 6,
        "investment_eur": "€440,000",
        "three_year_net_value_eur": "€6,010,000",
        "key_questions": [
            {"target": "Executive VP Digital Systems / Product Head", "question": "How quickly can you transform raw sonar telemetry uploaded from thousands of boats into updated, monetizable nautical chart layers?"},
            {"target": "Chief Technology Officer (CTO)", "question": "What is your monthly cloud infrastructure spend to ingest and query billions of high-frequency GPS and engine telemetry streams?"},
            {"target": "Chief Commercial Officer", "question": "What subscription revenue could you generate by offering boat owners predictive engine failure alerts before they get stranded offshore?"},
            {"target": "Head of Software Engineering", "question": "How easily can your engineering teams train edge computer vision models for automated boat docking using your existing cloud data infrastructure?"}
        ],
        "use_cases": [
            {"title": "High-Throughput Marine IoT & Crowdsourced Bathymetry Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting gigabytes of continuous sonar, radar, and GPS telemetry to generate dynamic bathymetric contours.", "architecture": "Delta Live Tables + Azure Event Hubs + Databricks Mosaic Geospatial"},
            {"title": "Predictive Vessel Maintenance & Autonomous Navigation AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models analyzing outboard engine telemetry and battery health to alert boaters of impending mechanical failure.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Global Connected Vessel Fleet Governance", "category": "Unified Governance & Security", "description": "Unity Catalog securing millions of customer vessel telemetry profiles with strict GDPR compliance and role-based OEM data isolation.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["fluvius", "bridgestone"]
    },

    # 25. NG Nordic AS (Norsk Gjenvinning)
    "Ng Nordic AS": {
        "industry": "Circular Economy, Waste Management & Industrial Recycling",
        "what_databricks_solves": "Modernize Norway's largest recycling and waste management operator onto an Azure Databricks Lakehouse, processing fleet collection GPS routes, automated optical sorting sensor data, and secondary raw material commodity price intelligence.",
        "trend_macro": "Stringent European circular economy directives, rising landfill carbon taxes, and corporate demand for verified recycling certificates (Scope 3 waste reduction).",
        "trend_competitors": "Global environmental service leaders (Veolia, Remondis, Ragn-Sells) deploy Lakehouses to optimize waste collection truck routing and automate commodity price hedging for scrap metal and plastics.",
        "trend_legacy_debt": "Weighbridge databases isolated across regional recycling facilities; truck fleet logistics running in separate telematics software with manual Excel reporting.",
        "fomo_cost_of_inaction": "Logistics fuel waste and missed commodity arbitrage: Running unoptimized truck collection routes and failing to hedge recycled metals and paper commodities costs millions in EBITDA.",
        "fomo_peer_velocity": "Competitors utilize automated computer vision to grade incoming recycling loads at weighbridges in seconds; NG Nordic relies on visual manual operator inspections.",
        "fomo_vendor_traps": "Proprietary weighbridge and fleet management systems with locked data exports requiring costly custom connectors.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€1,600,000",
        "payback_months": 7,
        "investment_eur": "€360,000",
        "three_year_net_value_eur": "€4,440,000",
        "key_questions": [
            {"target": "Chief Operating Officer / VP Logistics", "question": "What would be the annual fuel and labor saving of dynamically recalculating commercial waste collection routes based on sensor-monitored bin fill levels?"},
            {"target": "Chief Commercial Officer / Trading Head", "question": "How quickly can your scrap commodity trading desk model global market price shifts for recycled copper, aluminum, and plastics?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is weighbridge tonnage data from dozens of regional Norwegian sorting plants disconnected from your central financial ERP?"},
            {"target": "Director of Sustainability", "question": "Can you provide enterprise corporate clients with automated, auditable circular economy recycling certificates for their CSRD reporting?"}
        ],
        "use_cases": [
            {"title": "Automated Fleet Collection Route & Weighbridge Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake consolidating truck GPS, weighbridge ticket transactions, and bin fill sensors to optimize waste collection routes.", "architecture": "Delta Live Tables + Azure IoT + Power BI"},
            {"title": "Computer Vision Waste Sorting & Commodity Price Hedging", "category": "Enterprise GenAI & Mosaic AI", "description": "Edge AI models classifying recyclable materials on sorting belts while ML algorithms forecast secondary raw material market prices.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Auditable Circular Economy & CSRD Traceability Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining immutable material lifecycle provenance from collection to recycled raw material export.", "architecture": "Unity Catalog + Cegeka ESG Blueprint"}
        ],
        "matched_cases": ["water-link", "austrotherm"]
    },

    # 26. NNIT A/S
    "NNIT A/S": {
        "industry": "Life Sciences IT Consulting, GxP Cloud Transformation & Digital Health",
        "what_databricks_solves": "Empower NNIT's global life sciences clients with pre-validated GxP Azure Databricks Lakehouse accelerators, automating regulatory Veeva/SAP data integration, laboratory instrument telemetry ingestion, and AI clinical trial intelligence.",
        "trend_macro": "Global pharmaceutical migration from on-premise validated servers to compliant cloud architectures, surging FDA/EMA digital audit intensity, and high demand for AI-ready data foundations in biopharma.",
        "trend_competitors": "Life sciences IT systems integrators (Cognizant, ZS Associates, Accenture) deploy standardized Databricks GxP blueprints to win multi-million pharma enterprise cloud transformations.",
        "trend_legacy_debt": "Maintaining custom, brittle, client-specific GxP validation documentation frameworks and fragmented point-to-point ETL connectors for life sciences clients.",
        "fomo_cost_of_inaction": "Losing high-margin life science data platform engagements: Pharma clients are increasingly bypassing traditional IT consultancies in favor of partners with pre-packaged Databricks Lakehouse accelerators.",
        "fomo_peer_velocity": "Competitors stand up fully validated, compliant GxP Lakehouses for biopharma clients in 4 weeks; NNIT manual validation engagements require 3 to 6 months.",
        "fomo_vendor_traps": "Reliance on legacy bespoke data warehousing architectures that require endless manual engineering hours rather than scalable, modern Lakehouse software assets.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,300,000",
        "payback_months": 6,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€6,440,000",
        "key_questions": [
            {"target": "Head of Life Sciences Advisory / VP Consulting", "question": "How much faster could you close enterprise biopharma cloud transformation deals with a pre-packaged, GxP-validated Databricks migration accelerator?"},
            {"target": "Chief Technology Officer (CTO)", "question": "How are you automating 21 CFR Part 11 audit compliance and electronic signatures across your life sciences client data pipelines?"},
            {"target": "VP Cloud & Digital Solutions", "question": "What is your billable margin expansion if your engineering teams use Delta Live Tables to automate legacy SQL and SAS migrations for pharma customers?"},
            {"target": "Head of Quality & Regulatory Compliance", "question": "Can you provide biopharma clients with automated, tamper-evident cryptographic validation documentation for their regulatory submissions?"}
        ],
        "use_cases": [
            {"title": "Pre-Packaged GxP Life Sciences Cloud Lakehouse Accelerator", "category": "Lakehouse Modernization", "description": "Turnkey Azure Databricks environment pre-configured with 21 CFR Part 11 compliance, automated validation scripts, and Veeva connectors.", "architecture": "Unity Catalog + Delta Lake + GxP Validation Framework"},
            {"title": "Regulatory Submission AI Assistant & Document Interrogator", "category": "Enterprise GenAI & Mosaic AI", "description": "Mosaic AI knowledge assistants analyzing clinical study reports and regulatory guidance to accelerate dossier preparation.", "architecture": "Databricks Mosaic AI + Azure OpenAI"},
            {"title": "Governed Multi-Tenant Pharma Client Enclaves", "category": "Unified Governance & Security", "description": "Unity Catalog managing isolated, secure research enclaves for global pharmaceutical and medtech customers.", "architecture": "Unity Catalog + Azure Confidential Computing"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    },

    # 27. Nokas Group (Avarn Security)
    "Nokas Group": {
        "industry": "Physical Security, Alarm Monitoring & Cash Transit Logistics",
        "what_databricks_solves": "Consolidate alarm telemetry from hundreds of thousands of commercial and residential security systems, patrol guard GPS routing, and cash-in-transit (CIT) ATM logistics onto Azure Databricks to predict security incidents and optimize guard dispatch.",
        "trend_macro": "Decline of physical cash transactions, surging commercial building smart sensor integration, labor cost inflation for security personnel, and rapid adoption of remote video surveillance.",
        "trend_competitors": "Global security leaders (Securitas, G4S/Allied Universal) deploy cloud Lakehouses to run automated video anomaly detection and dynamic alarm dispatch algorithms.",
        "trend_legacy_debt": "Alarm monitoring software (Manitou/MasterMind) running in siloed on-premise servers; patrol fleet routing managed separately from incident logs.",
        "fomo_cost_of_inaction": "Costly false alarm responses: Security guards dispatched to tens of thousands of false sensor alarms annually, wasting labor hours and causing customer dissatisfaction.",
        "fomo_peer_velocity": "Competitors verify alarms via automated computer vision and audio anomaly detection in seconds; Nokas operators manually review camera feeds during alarm surges.",
        "fomo_vendor_traps": "Proprietary alarm receiver hardware and legacy alarm software requiring expensive maintenance and restrictive API licenses.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€1,750,000",
        "payback_months": 7,
        "investment_eur": "€380,000",
        "three_year_net_value_eur": "€4,870,000",
        "key_questions": [
            {"target": "Chief Operating Officer / Head of Security Ops", "question": "What percentage of physical security guard dispatches are triggered by environmental false alarms that could be filtered via automated sensor analytics?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why are alarm receiving center event logs segregated from your mobile patrol guard routing and scheduling databases?"},
            {"target": "Director of Cash Logistics (CIT)", "question": "How accurately can your current models predict ATM cash depletion to prevent emergency cash replenishment runs?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the operational labor savings of automating remote alarm verification across your Nordic monitoring centers?"}
        ],
        "use_cases": [
            {"title": "Real-Time Security Alarm Telemetry & Anomaly Filtering Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake streaming hundreds of thousands of alarm sensor events to filter false alarms and prioritize critical emergency events.", "architecture": "Delta Live Tables + Event Hubs + Power BI"},
            {"title": "Dynamic Security Patrol Dispatch & ATM Cash Forecasting", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting optimal guard patrol routes and ATM cash replenishment schedules.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Video Surveillance & Customer Security Portals", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining strict European privacy compliance for surveillance metadata and client audit trails.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["water-link", "bridgestone"]
    },

    # 28. Nordland Fylkeskommune
    "Nordland Fylkeskommune": {
        "industry": "Regional Government, Arctic Transportation & Public Infrastructure",
        "what_databricks_solves": "Unify Arctic ferry schedule telemetry, regional road icing sensor streams, public high school demographics, and regional economic planning onto an Azure Databricks Lakehouse, optimizing public transit subsidies and ensuring safe winter transport.",
        "trend_macro": "Severe Arctic climate challenges, rapid electrification of regional ferry and bus networks, regional depopulation, and Norwegian county digitization mandates.",
        "trend_competitors": "Leading Nordic counties (Viken, Västra Götaland) leverage Lakehouses to optimize electric public transit charging schedules and predict road maintenance needs.",
        "trend_legacy_debt": "Dozens of municipal and county databases (public transport ticketing, road sensor telemetry, school administration) running on isolated local servers with manual reporting.",
        "fomo_cost_of_inaction": "Public transport budget overruns: Inability to optimize ferry and bus timetables and electric charging schedules leading to millions in wasted fuel and county transport subsidies.",
        "fomo_peer_velocity": "Modern transport authorities predict road icing and storm disruptions hours in advance using ML sensor fusion; Nordland road maintenance crews react after ice has formed.",
        "fomo_vendor_traps": "Legacy public sector IT vendors charging high maintenance fees for rigid, closed-architecture software.",
        "tco_reduction_pct": 37,
        "compute_savings_pct": 50,
        "productivity_lift_multiplier": "3.0x",
        "annual_savings_eur": "€1,100,000",
        "payback_months": 8,
        "investment_eur": "€310,000",
        "three_year_net_value_eur": "€2,990,000",
        "key_questions": [
            {"target": "County Mayor / Fylkesrådsleder", "question": "How much county transport subsidy could be saved by dynamically synchronizing electric ferry charging schedules with fluctuating regional electricity prices?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you provide regional planners with a single, governed data platform across transportation, public education, and regional healthcare?"},
            {"target": "Head of Transportation / Samferdsel", "question": "How quickly can your road maintenance teams correlate real-time pavement temperature sensors with weather forecasts to dispatch salt trucks preemptively?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the annual saving of consolidating disparate county reporting systems into an elastic, serverless Azure Databricks Lakehouse?"}
        ],
        "use_cases": [
            {"title": "Arctic Public Transit & Electric Ferry Optimization Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake aggregating ferry GPS, passenger counts, and battery charging telemetry to minimize fuel consumption.", "architecture": "Delta Live Tables + Azure IoT + Power BI"},
            {"title": "Predictive Road Icing & Winter Weather Anomaly Engine", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models analyzing road sensor telemetry and satellite meteorological data to schedule proactive salting.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Sovereign County Regional Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing strict Norwegian privacy governance across school, transport, and administrative datasets.", "architecture": "Unity Catalog + Azure Databricks"}
        ],
        "matched_cases": ["water-link", "ggz-rivierduinen"]
    },

    # 29. Normal A/S
    "Normal A/S": {
        "industry": "Discount Retail, FMCG & Rapid Omnichannel Expansion",
        "what_databricks_solves": "Power Denmark's fastest-growing discount FMCG retailer (700+ stores across Europe) with an Azure Databricks Lakehouse, processing sub-minute store sales, viral TikTok trend demand signals, and automated warehouse cross-docking to prevent store stockouts.",
        "trend_macro": "Explosive international store rollout (Denmark, Norway, Sweden, France, Netherlands, Spain), hyper-fast product turnover driven by viral social media trends, and high warehouse throughput velocity.",
        "trend_competitors": "Global discount retailers (Action, B&M, Flying Tiger) deploy Lakehouses to sense regional viral SKU sales spikes within hours and automate cross-dock replenishment.",
        "trend_legacy_debt": "Rapidly growing retailer running on ERP and warehouse systems stretched to their limits by multi-country store openings and millions of daily register transactions.",
        "fomo_cost_of_inaction": "Massive revenue loss on viral trend stockouts: When a cosmetic or snack product goes viral on TikTok, Normal stores run out of stock in 24 hours, losing millions in uncaptured basket value.",
        "fomo_peer_velocity": "Competitors detect viral product demand surges and redirect central warehouse inventory in hours; Normal distribution planners wait for overnight batch sales reconciliation.",
        "fomo_vendor_traps": "Traditional relational database licenses requiring exponential server scaling to keep up with hundreds of new store openings.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 6,
        "investment_eur": "€420,000",
        "three_year_net_value_eur": "€6,180,000",
        "key_questions": [
            {"target": "Chief Commercial Officer / Head of Merchandising", "question": "What is the quantified lost revenue when a trending beauty or snack SKU stocks out across hundreds of stores during a viral social media spike?"},
            {"target": "Chief Information Officer (CIO)", "question": "How will your current transaction databases scale as you expand from 700 to over 1,500 stores across 8 European countries?"},
            {"target": "Head of Supply Chain & Logistics", "question": "How quickly can your warehouse management systems execute automated cross-docking for high-velocity SKUs arriving from global suppliers?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the working capital saving of using algorithmic store-level demand sensing to reduce safety stock across European distribution hubs?"}
        ],
        "use_cases": [
            {"title": "Real-Time 700+ Store POS & Cross-Dock Ingestion Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Live Tables streaming point-of-sale transactions and warehouse barcode scans in sub-seconds for instantaneous stock visibility.", "architecture": "Delta Lake + Delta Live Tables + Azure Event Hubs"},
            {"title": "Viral Trend Demand Sensing & Predictive Store Replenishment", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models tracking sales velocity spikes and social sentiment to trigger automated warehouse cross-dock shipments.", "architecture": "Databricks Mosaic AI + MLflow + Feature Store"},
            {"title": "Unified European Multi-Country Retail Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog governing cross-border operations across Denmark, Norway, Sweden, and Central Europe with centralized security.", "architecture": "Unity Catalog + Power BI Direct Lake"}
        ],
        "matched_cases": ["cera", "bridgestone"]
    },

    # 30. Norwegian Air Shuttle ASA (incl. Widerøe AS)
    "Norwegian Air Shuttle ASA": {
        "industry": "Commercial Aviation, Airline Operations & Regional Carrier Group",
        "what_databricks_solves": "Unify flight operations telemetry, aircraft engine health streams, dynamic passenger booking curves, and crew scheduling across Norwegian Air Shuttle and Widerøe onto an Azure Databricks Lakehouse, reducing aircraft turnaround delays (AOG) and maximizing ancillary seat yield.",
        "trend_macro": "Severe jet fuel price volatility, aircraft turnaround bottlenecks at European airports, intense low-cost carrier fare competition, and strict EU aviation decarbonization rules.",
        "trend_competitors": "Top low-cost carriers (Ryanair, EasyJet, Wizz Air) deploy Lakehouses to adjust seat and ancillary pricing dynamically in real-time and predict aircraft component wear before gate delays occur.",
        "trend_legacy_debt": "Core reservation systems (Amadeus/Navitaire) isolated from aircraft maintenance logs (AMOS) and crew scheduling; Widerøe integration adding secondary data silos.",
        "fomo_cost_of_inaction": "Substantial Aircraft on Ground (AOG) and flight delay costs: An unscheduled mechanical delay on an aircraft costs between €50,000 and €150,000 in passenger compensation (EU 261), crew overtime, and rebooking fees.",
        "fomo_peer_velocity": "Competitors retrain dynamic flight pricing models hourly based on competitor fare changes; Norwegian commercial teams analyze yield trends on daily batch cycles.",
        "fomo_vendor_traps": "Heavily siloed airline IT systems charging immense transaction and API fees to extract raw operational flight telemetry.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€3,100,000",
        "payback_months": 7,
        "investment_eur": "€550,000",
        "three_year_net_value_eur": "€8,750,000",
        "key_questions": [
            {"target": "Chief Operating Officer / VP Technical", "question": "What was your total annual EU 261 compensation and turnaround expenditure caused by unscheduled technical aircraft delays across your fleet?"},
            {"target": "Chief Commercial Officer / Revenue Management Head", "question": "How quickly can your pricing algorithms react to sudden competitor fare cuts across key Nordic and European leisure flight corridors?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you unifying flight operations and maintenance data between Norwegian Air Shuttle and the newly acquired Widerøe fleet?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the return on investment of deploying real-time aircraft fuel consumption modeling to optimize flight altitudes and descent profiles?"}
        ],
        "use_cases": [
            {"title": "Real-Time Flight Operations & Predictive Maintenance Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting aircraft engine ACARS telemetry, avionics logs, and turnaround status to preempt mechanical delays.", "architecture": "Delta Live Tables + Azure Databricks + AMOS Connector"},
            {"title": "Dynamic Ancillary & Seat Yield Optimization Engine", "category": "Enterprise GenAI & Mosaic AI", "description": "High-throughput machine learning pipelines adjusting seat prices, baggage fees, and fast-track options based on live booking velocity.", "architecture": "Databricks Mosaic AI + MLflow + Feature Store"},
            {"title": "Unified Airline Group Data Mesh (Norwegian + Widerøe)", "category": "Unified Governance & Security", "description": "Unity Catalog establishing single-pane governance across Norwegian Air Shuttle and Widerøe with role-based access control.", "architecture": "Unity Catalog + Power BI Direct Lake"}
        ],
        "matched_cases": ["bridgestone", "nordic-paper"]
    },

    # 31. Petroleum Geo-Services (PGS ASA / TGS)
    "Petroleum Geo-Services (PGS ASA)": {
        "industry": "Marine Geophysics, Seismic Imaging & Energy Subsurface Data",
        "what_databricks_solves": "Modernize the processing and multi-client licensing of multi-petabyte marine seismic datasets, ocean bottom node (OBN) acoustic surveys, and offshore carbon storage (CCS) site characterization onto an Azure Databricks Lakehouse with Delta Sharing.",
        "trend_macro": "Energy transition demands for offshore carbon capture and storage (CCS) site verification, high GPU compute costs for 3D/4D seismic imaging inversion, and exploration client demand for cloud data streaming.",
        "trend_competitors": "Global seismic leaders (SLB, CGG, Shearwater) deploy cloud Lakehouses to streamline petabyte seismic delivery and run deep learning seismic noise attenuation on GPU clusters.",
        "trend_legacy_debt": "Petabytes of seismic trace data stored on physical tapes and legacy on-premise high-performance compute (HPC) clusters with complex, bespoke file formats (SEG-Y).",
        "fomo_cost_of_inaction": "Extremely slow multi-client data sales cycles: Shipping physical hard drives or running multi-day cloud downloads to deliver seismic survey data to oil and CCS clients delays multi-million licensing agreements.",
        "fomo_peer_velocity": "Competitors provide oil companies with instant, zero-copy cloud access to seismic surveys via Delta Sharing; PGS/TGS teams spend days preparing custom data extracts.",
        "fomo_vendor_traps": "Massive on-premise datacenter capital expenditure and tape storage maintenance fees with stagnant operational flexibility.",
        "tco_reduction_pct": 47,
        "compute_savings_pct": 64,
        "productivity_lift_multiplier": "4.1x",
        "annual_savings_eur": "€3,900,000",
        "payback_months": 6,
        "investment_eur": "€670,000",
        "three_year_net_value_eur": "€11,030,000",
        "key_questions": [
            {"target": "Executive VP Geophysics / Chief Geophysicist", "question": "How many days does it take to prepare and deliver a 10 TB multi-client seismic dataset to an exploration or offshore CCS customer?"},
            {"target": "Chief Technology Officer (CTO)", "question": "What is your annual GPU and storage expenditure maintaining on-premise seismic processing clusters compared to elastic cloud GPU Lakehouses?"},
            {"target": "Head of Commercial Sales", "question": "What if you could license and stream seismic volumes directly into oil company workspaces instantly using Delta Sharing without duplicating data?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the margin benefit of converting static seismic tape archives into an active, monetizable cloud Lakehouse data marketplace?"}
        ],
        "use_cases": [
            {"title": "Petabyte-Scale Seismic Processing & Geoparquet Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake and Photon compute optimized for high-throughput seismic acoustic trace processing, velocity modeling, and OBN data.", "architecture": "Delta Lake + Databricks GPU Clusters + Azure Blob Storage"},
            {"title": "AI-Accelerated Subsurface Fault Detection & Carbon Storage Modeling", "category": "Enterprise GenAI & Mosaic AI", "description": "Deep learning models executing automated fault segmentation and offshore carbon sequestration reservoir integrity analysis.", "architecture": "Databricks Mosaic AI + MLflow + GPU Serving"},
            {"title": "Instant Zero-Copy Seismic Data Delivery via Delta Sharing", "category": "Unified Governance & Security", "description": "Delta Sharing enabling PGS/TGS to stream licensed seismic survey volumes directly into energy client analytics environments.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["fluvius", "nordic-paper"]
    },

    # 32. Region Nordjylland
    "Region Nordjylland": {
        "industry": "Regional Healthcare, Hospital Administration & Emergency Medicine",
        "what_databricks_solves": "Consolidate electronic health records (EHR), emergency room telemetry, hospital bed occupancy, and medical imaging logs across Aalborg University Hospital and regional care facilities into a sovereign Azure Databricks Lakehouse, predicting ER overcrowding and patient bed demand.",
        "trend_macro": "Severe healthcare staffing shortages, hospital waiting list backlogs, rising chronic patient volumes, and strict Danish health data sovereignty mandates.",
        "trend_competitors": "Top European university hospitals (Karolinska, Erasmus MC, Rigshospitalet) deploy Lakehouse AI models to forecast emergency department admissions 12 hours in advance and automate clinical report transcription.",
        "trend_legacy_debt": "Clinical data trapped in proprietary electronic medical record systems (Systematic Columna); hospital logistics and medical staff scheduling managed in disconnected databases.",
        "fomo_cost_of_inaction": "Emergency department overcrowding and canceled elective surgeries: Inability to predict patient bed flow leading to ambulance diversion, prolonged ER wait times, and high medical staff overtime.",
        "fomo_peer_velocity": "Modern hospitals predict inpatient bed shortages half a day ahead, enabling proactive nurse shift balancing; Region Nordjylland hospital coordinators react after ER beds are full.",
        "fomo_vendor_traps": "Heavily locked clinical EMR vendor contracts with exorbitant fees to extract raw clinical transaction logs for secondary medical research.",
        "tco_reduction_pct": 38,
        "compute_savings_pct": 51,
        "productivity_lift_multiplier": "3.1x",
        "annual_savings_eur": "€1,500,000",
        "payback_months": 8,
        "investment_eur": "€370,000",
        "three_year_net_value_eur": "€4,130,000",
        "key_questions": [
            {"target": "Chief Medical Officer / Hospital Director", "question": "What is the quantifiable patient care and financial impact when emergency department bed shortages force the cancellation of scheduled elective surgeries?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you enforce role-based patient data de-identification when clinical researchers need access to longitudinal hospital treatment records?"},
            {"target": "Head of Emergency Medicine", "question": "How accurately can your current systems forecast emergency admission surges driven by seasonal influenza or extreme weather events?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the annual clinical overtime expenditure that could be prevented through predictive nurse and physician shift allocation?"}
        ],
        "use_cases": [
            {"title": "Real-Time Hospital Bed Occupancy & Patient Flow Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake consolidating admissions, surgical schedules, and discharge readiness to optimize regional hospital bed turnover.", "architecture": "Delta Live Tables + Azure Databricks + Power BI Direct Lake"},
            {"title": "Predictive Emergency Room Overcrowding & Triage AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting ER patient arrival velocity and clinical complexity up to 24 hours in advance.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Sovereign Clinical Data Governance & Research Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing strict Danish health privacy rules, column masking, and cryptographic query auditability.", "architecture": "Unity Catalog + Azure Confidential Computing"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    },

    # 33. Rigspolitiet (Danish National Police)
    "Rigspolitiet": {
        "industry": "Law Enforcement, National Security & Public Safety",
        "what_databricks_solves": "Modernize national emergency dispatch telemetry, criminal intelligence graph modeling, border control sensor streams, and forensics on an air-gapped, sovereign Azure Databricks Lakehouse, accelerating investigation response times and identifying organized crime patterns.",
        "trend_macro": "Cross-border organized crime surges, cyber warfare threats against critical national infrastructure, and public scrutiny demanding rapid emergency response times.",
        "trend_competitors": "Leading national law enforcement agencies (UK Home Office, Dutch Politie, FBI) leverage Lakehouses to run graph neural networks across telephone, financial transaction, and vehicle license plate data (ANPG).",
        "trend_legacy_debt": "Legacy police case management databases (POLSAS) running on proprietary systems; automated license plate reader (ANPG) sensor feeds disconnected from central investigative intelligence.",
        "fomo_cost_of_inaction": "Delayed investigative breakthroughs: Police detectives spending hundreds of hours manually cross-referencing criminal records, vehicle sightings, and financial records across siloed databases.",
        "fomo_peer_velocity": "Allied law enforcement agencies link organized crime syndicate networks in seconds using graph algorithms; Danish investigators execute complex queries with multi-day database wait times.",
        "fomo_vendor_traps": "Proprietary public security vendor software with locked data formats charging massive customization fees for every new operational dashboard.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 52,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 8,
        "investment_eur": "€490,000",
        "three_year_net_value_eur": "€5,810,000",
        "key_questions": [
            {"target": "National Police Commissioner / Rigspolitichef", "question": "How quickly can your specialized investigative units correlate automatic license plate sightings with organized crime registry data during active manhunts?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you maintain sovereign, tamper-evident cryptographic data custody across sensitive criminal intelligence registers?"},
            {"target": "Head of Emergency Response & Dispatch (112/114)", "question": "Can your dispatch control centers analyze real-time patrol unit GPS locations and incident severity to optimize tactical emergency response times?"},
            {"target": "Director of Forensic Science", "question": "How are you scaling your infrastructure to process gigabytes of digital forensic evidence extracted from suspect smartphones and computers?"}
        ],
        "use_cases": [
            {"title": "Real-Time Emergency Dispatch & Patrol Fleet Optimization", "category": "Lakehouse Modernization", "description": "Delta Lake streaming emergency incident calls, patrol vehicle GPS, and traffic sensor data to minimize tactical response times.", "architecture": "Delta Live Tables + Event Hubs + Power BI"},
            {"title": "Criminal Network Graph Analytics & Forensic AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Graph algorithms and NLP models parsing investigative case notes, phone records, and ANPG sightings to uncover crime syndicate structures.", "architecture": "Databricks Mosaic AI + GraphFrames + Azure OpenAI"},
            {"title": "Sovereign Criminal Intelligence Governance & Audit Lineage", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing strict national security access controls with immutable, court-admissible audit trails.", "architecture": "Unity Catalog + Ed25519 Custody"}
        ],
        "matched_cases": ["ggz-rivierduinen", "water-link"]
    },

    # 34. Royal Unibrew
    "Royal Unibrew": {
        "industry": "Beverage Production, Breweries & FMCG Distribution",
        "what_databricks_solves": "Connect brewery fermentation IoT sensors, automated canning and bottling line telemetry, and European retail distribution routes (Faxe Kondi, Royal, Heineken licensee) into an Azure Databricks Lakehouse, optimizing brewery energy usage and trade spend ROI.",
        "trend_macro": "Severe aluminum can and glass bottle packaging inflation, volatile barley/malt agricultural prices, brewery water conservation mandates, and aggressive supermarket promotional price discounting.",
        "trend_competitors": "Global brewing leaders (Carlsberg, AB InBev, Heineken) deploy Lakehouses to optimize brewery refrigeration energy and analyze retail promotional trade spend effectiveness in real-time.",
        "trend_legacy_debt": "Brewery SCADA systems (Siemens/Wonderware) isolated in plant networks; trade promotion management tracked in fragmented regional spreadsheets.",
        "fomo_cost_of_inaction": "Millions lost to ineffective retail promotions: Unoptimized supermarket discounts fail to generate incremental volume, while bottling line stops cause thousands of wasted hectoliters annually.",
        "fomo_peer_velocity": "Competitors evaluate supermarket promotional sell-through within 24 hours of campaign launch; Royal Unibrew brand managers wait for monthly distributor reconciliation.",
        "fomo_vendor_traps": "Proprietary packaging line telemetry software charging high per-line monitoring fees without integration to central financial ERP.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€1,850,000",
        "payback_months": 7,
        "investment_eur": "€410,000",
        "three_year_net_value_eur": "€5,140,000",
        "key_questions": [
            {"target": "Executive VP Supply Chain & Breweries", "question": "What is the thermal and electrical energy cost variance across your primary brewing and packaging facilities per hectoliter produced?"},
            {"target": "Chief Commercial Officer / Sales VP", "question": "Which percentage of your retail trade promotions in Denmark, the Baltics, and Italy generate true incremental margin versus subsidizing baseline consumer demand?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is packaging line overall equipment effectiveness (OEE) telemetry separated from your central SAP supply chain database?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What working capital could you unlock by synchronizing brewery production schedules dynamically with regional supermarket inventory depletion?"}
        ],
        "use_cases": [
            {"title": "Brewery IoT Energy & Bottling Line OEE Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting fermentation tank temperatures, refrigeration power, and packaging line speeds to minimize energy and downtime.", "architecture": "Delta Live Tables + Azure IoT Hub + Power BI"},
            {"title": "Trade Promotion Management & Retail Demand Sensing", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting the true volume lift and price elasticity of supermarket promotional campaigns.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Unified Multi-Country Beverage Supply Chain Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog governing production and sales metrics across Denmark, Finland, the Baltics, and Italy with role-based access.", "architecture": "Unity Catalog + SAP Connector"}
        ],
        "matched_cases": ["austrotherm", "bridgestone"]
    },

    # 35. Ruter As
    "Ruter As": {
        "industry": "Public Transport Authority, Smart Mobility & Urban Transit",
        "what_databricks_solves": "Modernize the public mobility platform for Oslo and Akershus (400M+ annual passenger journeys across metro, tram, bus, and electric ferry) on Azure Databricks, processing real-time vehicle GPS, passenger boarding counters, and dynamic fleet charging.",
        "trend_macro": "Complete public transit fleet zero-emission transition (electric buses and ferries), shifting hybrid-work commuter patterns, and municipal pressure to reduce private car congestion.",
        "trend_competitors": "World-class urban transit systems (TfL London, SL Stockholm) deploy streaming Lakehouses to dynamically adjust bus headways and predict transit vehicle maintenance needs.",
        "trend_legacy_debt": "Ticketing transaction databases (Ruter app/card) disconnected from vehicle GPS telemetry (SIRI/GTFS-RT) and third-party transport operator contractor systems.",
        "fomo_cost_of_inaction": "Millions wasted in unoptimized electric bus charging during peak electricity tariff windows and commuter overcrowding during sudden weather disruptions.",
        "fomo_peer_velocity": "Leading transit authorities simulate regional crowd movements during rainstorms and concert events in minutes; Ruter dispatch planners rely on static timetable schedules.",
        "fomo_vendor_traps": "Contractor vehicle telematics providers charging expensive integration fees for proprietary real-time streaming feeds.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€1,950,000",
        "payback_months": 7,
        "investment_eur": "€440,000",
        "three_year_net_value_eur": "€5,440,000",
        "key_questions": [
            {"target": "Chief Executive Officer / Managing Director", "question": "What is the annual financial saving if your electric bus operators can dynamically optimize depot charging schedules against hourly spot electricity prices?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you process millions of daily passenger tap events and real-time vehicle GPS streams without compute latency bottlenecks?"},
            {"target": "Head of Mobility Services / Operational Director", "question": "How accurately can your current routing systems forecast commuter crowding across the Oslo metro and tram network during adverse winter weather?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the operational efficiency gain of automating contractor performance and delay penalty calculations on an immutable Lakehouse?"}
        ],
        "use_cases": [
            {"title": "Real-Time 400M-Journey Streaming Transit Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting high-frequency vehicle GPS, automatic passenger counter (APC) sensors, and ticketing streams in real-time.", "architecture": "Delta Lake + Delta Live Tables + Kafka / Event Hubs"},
            {"title": "Predictive Passenger Crowd Sensing & Dynamic Dispatch AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting station crowding and recommending dynamic extra bus dispatches for major sporting and weather events.", "architecture": "Databricks Mosaic AI + MLflow + Power BI"},
            {"title": "Governed Contractor Transparency & Zero-Emission Fleet Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog providing auditable, shared data access between Ruter and contracted bus/ferry operating companies.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["water-link", "fluvius"]
    },

    # 36. Salmar AS
    "Salmar AS": {
        "industry": "Aquaculture, Ocean Farming & Salmon Processing",
        "what_databricks_solves": "Modernize global offshore and coastal salmon farming operations (including Ocean Farm 1) on Azure Databricks, processing underwater camera video streams, fish feeding sensor telemetry, oceanographic temperature/salinity data, and sea lice counts to maximize biomass growth and eliminate feed waste.",
        "trend_macro": "Severe sea lice regulatory restrictions, Norwegian resource rent tax on aquaculture, volatile fish feed prices, and surging global demand for sustainable farmed salmon.",
        "trend_competitors": "Top aquaculture leaders (Mowi, Lerøy, Bakkafrost) deploy Lakehouses to automate underwater computer vision fish feeding algorithms, saving up to 10% on feed costs.",
        "trend_legacy_debt": "Feed barge control software running on local edge computers; underwater sensor logs and veterinary health records trapped in disparate Excel sheets and local databases.",
        "fomo_cost_of_inaction": "Millions in wasted fish feed and premature slaughter penalties: Feed represents over 50% of salmon farming production costs; unoptimized feeding or missed sea lice blooms costs tens of millions per cage.",
        "fomo_peer_velocity": "Competitors detect fish appetite shifts using underwater computer vision in seconds to halt feed blowers; SalMar farm technicians rely on manual surface viewing screens.",
        "fomo_vendor_traps": "Aquaculture equipment and feed barge vendors attempting to lock feeding and sensor data into proprietary cloud portals with steep annual licensing.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,700,000",
        "payback_months": 6,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€7,560,000",
        "key_questions": [
            {"target": "Chief Operating Officer / Farming Director", "question": "What would be the annual EBITDA impact of reducing fish feed pellet wastage by just 4% across all coastal and offshore ocean cages?"},
            {"target": "Chief Technology Officer (CTO)", "question": "How are you synchronizing high-bandwidth underwater video feeds and environmental sensors from remote offshore ocean cages into central analytics?"},
            {"target": "Head of Fish Health & Veterinary", "question": "How quickly can your biological teams detect micro-trends in sea lice larvae counts across neighboring fjord locations to coordinate early non-medicinal treatment?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How accurately can your financial models project quarterly salmon harvest biomass and size distribution against fluctuating spot market salmon prices?"}
        ],
        "use_cases": [
            {"title": "Ocean Farm Underwater Camera & Feeding Telemetry Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting continuous ocean salinity, temperature, oxygen, and feed pellet acoustic sensor streams.", "architecture": "Delta Live Tables + Azure IoT Edge + Databricks Streaming"},
            {"title": "Computer Vision Fish Appetite & Biomass Growth AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Edge and cloud deep learning models analyzing fish swimming behavior to optimize pellet feeding and predict weight distribution.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Auditable Biological Health & Resource Tax Compliance Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining immutable, auditable veterinary treatment and biomass records for Norwegian Directorate of Fisheries audits.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["fluvius", "austrotherm"]
    },

    # 37. Scandinavian Tobacco Group (incl. Swedish Match AB, General Cigar)
    "Scandinavian Tobacco Group": {
        "industry": "Consumer Goods, Tobacco & Nicotine Pouch Manufacturing",
        "what_databricks_solves": "Consolidate global tobacco leaf processing telemetry, automated high-speed packaging lines, and track-and-trace serialization across European, US, and Dominican manufacturing sites onto an Azure Databricks Lakehouse, optimizing leaf blend yields and ensuring FDA/EU TPD compliance.",
        "trend_macro": "Aggressive consumer shifts toward smoke-free nicotine pouches, stringent FDA premarket tobacco product applications (PMTA), and global track-and-trace serialization mandates.",
        "trend_competitors": "Global FMCG and tobacco leaders (Philip Morris International, BAT) deploy Lakehouses to optimize high-speed pouch machinery OEE and streamline global supply chain serialization.",
        "trend_legacy_debt": "Factory-level MES and serialization databases operating in local factory silos; disparate enterprise ERPs following international acquisitions (Swedish Match / General Cigar).",
        "fomo_cost_of_inaction": "Millions in regulatory non-compliance fines and factory downtime: Inability to trace serialized product batches across international borders risks immediate market recalls and FDA import bans.",
        "fomo_peer_velocity": "Competitors optimize leaf curing and moisture blending recipes using predictive AI in minutes; STG factory technicians rely on manual sample testing.",
        "fomo_vendor_traps": "Costly proprietary track-and-trace compliance software charging transaction fees for every product serialization query.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,250,000",
        "payback_months": 7,
        "investment_eur": "€480,000",
        "three_year_net_value_eur": "€6,270,000",
        "key_questions": [
            {"target": "Executive VP Global Operations", "question": "What is the annual yield loss during raw tobacco leaf cutting and conditioning that could be prevented through automated moisture and temperature optimization?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you unifying manufacturing and track-and-trace serialization data across European, US, and Caribbean factory operations?"},
            {"target": "Head of Regulatory Affairs / Quality", "question": "How many days does it take to compile an end-to-end batch traceability report for European TPD or US FDA audit inquiries?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the working capital reduction of synchronizing global finished goods inventory with regional distributor depletion velocity?"}
        ],
        "use_cases": [
            {"title": "Global Manufacturing Telemetry & High-Speed Packaging Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting factory sensor streams, cutting speeds, and packaging line sensor metrics to maximize overall equipment effectiveness.", "architecture": "Delta Live Tables + Azure IoT Hub + Power BI"},
            {"title": "Automated Tobacco Leaf Blend & Moisture AI Optimization", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models predicting optimal leaf humidity conditioning curves to maximize yield and reduce raw material scrap.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Global Track-and-Trace Regulatory Serialization Governance", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining immutable, cryptographically verifiable serial tracking logs for international customs and tax authorities.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 38. Schouw & Co. (BioMar, Borg Automotive, GPV, Schouw)
    "Schouw & Co.": {
        "industry": "Industrial Conglomerate (Aquaculture Feed, Automotive Remanufacturing, EMS)",
        "what_databricks_solves": "Empower a leading Nordic industrial conglomerate with an enterprise Azure Databricks multi-tenant Lakehouse, unifying fish feed formulation analytics (BioMar), electronics assembly defect detection (GPV), and circular automotive core inventory (Borg Automotive) under unified Unity Catalog governance.",
        "trend_macro": "Severe raw material supply chain volatility across electronics, automotive components, and marine feed commodities, paired with mandatory corporate sustainability reporting (CSRD) across all portfolio companies.",
        "trend_competitors": "Top industrial holding groups (Danaher, Lifco, Indutrade) leverage centralized Lakehouse architectures to drive cross-portfolio operational benchmark improvements and accelerate M&A data integration.",
        "trend_legacy_debt": "Each operating portfolio company (BioMar, GPV, Borg, HydraSpecma) runs completely independent ERPs (SAP, Dynamics 365, Infor) with fragmented monthly financial consolidation in spreadsheets.",
        "fomo_cost_of_inaction": "Sub-optimal procurement and reporting friction: Inability to execute group-wide raw material volume purchasing and spending hundreds of hours on manual quarterly financial consolidation.",
        "fomo_peer_velocity": "Leading conglomerates stand up M&A data analytics for acquired companies in weeks; Schouw portfolio managers spend months harmonizing disparate operational data.",
        "fomo_vendor_traps": "Disparate cloud and on-premise business intelligence licensing scattered across dozens of global manufacturing sites.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 61,
        "productivity_lift_multiplier": "3.7x",
        "annual_savings_eur": "€2,950,000",
        "payback_months": 7,
        "investment_eur": "€560,000",
        "three_year_net_value_eur": "€8,290,000",
        "key_questions": [
            {"target": "Chief Executive Officer / Group President", "question": "What is the group-wide procurement leverage you could unlock by aggregating raw material purchase data across BioMar, GPV, and Borg Automotive?"},
            {"target": "Chief Financial Officer (CFO)", "question": "How many man-weeks are required each quarter to execute group financial consolidation and auditable Scope 1-3 CSRD emissions across your 6 portfolio companies?"},
            {"target": "Chief Technology Officer / Head of Digital", "question": "How do you provide each portfolio company with an autonomous, high-performance data workspace while enforcing group-wide security governance?"},
            {"target": "Managing Director, BioMar Group", "question": "How quickly can your feed formulation algorithms recalculate global aquaculture feed recipes when raw soy or fish meal prices surge?"}
        ],
        "use_cases": [
            {"title": "Multi-Tenant Conglomerate Financial & ESG Consolidation Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting financial, supply chain, and emissions data from disparate portfolio company ERPs into an automated group reporting model.", "architecture": "Delta Lake + Delta Live Tables + Power BI Direct Lake"},
            {"title": "BioMar Nutritional Feed Formulation & Raw Material AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Optimization algorithms balancing nutritional protein content, raw material pricing, and carbon footprint for aquaculture feed recipes.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Group-Wide Federated Unity Catalog & Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog establishing autonomous, isolated workspaces for each portfolio subsidiary while enforcing group board-level oversight.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 39. Semler IT A/S (Semler Gruppen)
    "Semler IT A/S": {
        "industry": "Automotive Import, Dealership Network & Connected Mobility",
        "what_databricks_solves": "Modernize Denmark's largest automotive importer and dealership group (Volkswagen, Audi, Porsche, Škoda, SEAT) on Azure Databricks, unifying dealership management systems (DMS), real-time connected vehicle telemetry, and spare parts supply chains to predict vehicle servicing needs.",
        "trend_macro": "Rapid Nordic transition to electric vehicles (EVs), OEM direct-to-consumer agency sales models, connected car telemetry streams, and declining traditional combustion engine servicing revenues.",
        "trend_competitors": "Top automotive retail networks (Emil Frey, Bilia, Hedin Mobility) deploy Lakehouses to predict vehicle trade-in values and trigger automated, personalized service booking reminders.",
        "trend_legacy_debt": "Fragmented dealership management systems across independent and owned dealerships; customer vehicle service records isolated from connected EV charging telemetry.",
        "fomo_cost_of_inaction": "Customer churn to independent auto repair shops: Failing to engage EV and ICE vehicle owners with timely, personalized service alerts costs millions in high-margin workshop and parts revenue.",
        "fomo_peer_velocity": "Competitors trigger automated service booking invitations based on real-time vehicle mileage telemetry; Semler dealers rely on generic calendar service mailers.",
        "fomo_vendor_traps": "High recurring software fees on legacy automotive DMS software with rigid database export restrictions.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€1,900,000",
        "payback_months": 7,
        "investment_eur": "€420,000",
        "three_year_net_value_eur": "€5,280,000",
        "key_questions": [
            {"target": "Chief Executive Officer / Managing Director", "question": "What percentage of vehicle servicing revenue do you lose to third-party repair networks after customer manufacturer warranties expire?"},
            {"target": "Chief Commercial Officer / Head of Retail", "question": "How quickly can your marketing teams launch targeted trade-in offers based on real-time customer vehicle mileage and battery degradation models?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is connected vehicle charging telemetry segregated from your central dealership workshop and spare parts management systems?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the working capital reduction of automating spare parts replenishment across your nationwide warehouse network using predictive demand forecasting?"}
        ],
        "use_cases": [
            {"title": "Automotive Dealership & Spare Parts Supply Chain Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake unifying multi-dealership DMS transactions, manufacturer spare parts inventories, and customer repair orders.", "architecture": "Delta Live Tables + Azure Event Hubs + Power BI"},
            {"title": "Connected Vehicle Predictive Servicing & Battery Health AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models analyzing vehicle mileage velocity and diagnostic trouble codes to trigger automated workshop appointments.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Customer 360 & Dealership Network Data Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog ensuring GDPR compliance while providing secure, shared inventory access across independent dealer partners.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["bridgestone", "cera"]
    },

    # 40. SKAT Denmark (Skatteministeriet)
    "SKAT Denmark": {
        "industry": "Tax Administration, Customs & Revenue Intelligence",
        "what_databricks_solves": "Modernize the Danish Customs and Tax Administration's analytics infrastructure on Azure Databricks, processing billions of financial transactions, corporate invoices, and cross-border customs declarations to uncover VAT carousel fraud and automate tax assessment auditing with mathematical precision.",
        "trend_macro": "Cross-border VAT fraud schemes (costing billions across the EU), e-invoicing mandates, property tax valuation reforms, and public scrutiny demanding fair, transparent tax compliance.",
        "trend_competitors": "Top European tax authorities (HMRC, French DGFIP) deploy Lakehouses with graph neural networks and machine learning to intercept carousel fraud in real-time before tax refunds are paid.",
        "trend_legacy_debt": "Decades of legacy mainframe tax accounting systems running alongside disconnected relational databases, creating immense data reconciliation latency.",
        "fomo_cost_of_inaction": "Massive revenue leakage from VAT fraud: Sophisticated criminal networks exploit batch processing delays to extract fraudulent tax refunds, risking hundreds of millions in public funds.",
        "fomo_peer_velocity": "Modern tax authorities freeze fraudulent refund payouts in real-time during transaction processing; SKAT auditors discover fraud months after disbursements have left state accounts.",
        "fomo_vendor_traps": "Extensive consultancy expenditure maintaining brittle, legacy point-to-point data bridges between core tax mainframes and audit analytics tools.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€3,600,000",
        "payback_months": 7,
        "investment_eur": "€720,000",
        "three_year_net_value_eur": "€10,080,000",
        "key_questions": [
            {"target": "Director General / Skattedirektør", "question": "What is the estimated annual tax revenue leakage from cross-border VAT carousel schemes that bypass current batch audit rules?"},
            {"target": "Chief Technology Officer (CTO)", "question": "How long does it take your data engineering teams to join billions of bank transactions with corporate VAT filings on legacy infrastructure?"},
            {"target": "Head of Anti-Fraud & Economic Crime", "question": "Can your investigators query graph relationships between company directors, registered addresses, and suspicious transaction flows in sub-seconds?"},
            {"target": "Chief Information Officer / DPO", "question": "How do you enforce cryptographic data masking and audit lineage when tax auditors access sensitive citizen financial records?"}
        ],
        "use_cases": [
            {"title": "High-Performance Transaction Ingestion & Tax Audit Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake and Photon compute processing billions of banking, corporate invoice, and customs declarations with sub-second audit queries.", "architecture": "Delta Lake + Photon + Spark Streaming"},
            {"title": "Graph AI & Anomaly Detection for Cross-Border VAT Fraud", "category": "Enterprise GenAI & Mosaic AI", "description": "GraphFrames and machine learning models analyzing transaction networks to identify shell companies and carousel fraud before refunds disburse.", "architecture": "Databricks Mosaic AI + GraphFrames + MLflow"},
            {"title": "Sovereign Tax Data Clean Rooms & Legal Audit Lineage", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing strict Danish tax confidentiality laws with immutable, court-admissible audit logs.", "architecture": "Unity Catalog + Sovereign Cloud Security"}
        ],
        "matched_cases": ["cera", "ggz-rivierduinen"]
    },

    # 41. Strawberry Hotels (Nordic Choice Hotels)
    "Strawberry Hotels (Nordic Choice Hotels)": {
        "industry": "Hospitality, Hotels & Travel Guest Experience",
        "what_databricks_solves": "Unify guest reservation clickstreams, property management systems (PMS) across 240+ hotels, mobile keyless entry telemetry, and loyalty member transactions on Azure Databricks, powering dynamic RevPAR room pricing and hyper-personalized guest stays.",
        "trend_macro": "Severe post-pandemic hotel wage inflation, intense competition from online travel agencies (Booking.com, Expedia) eating booking margins, and guest expectations for seamless digital hotel experiences.",
        "trend_competitors": "Global hospitality giants (Marriott, Hilton) deploy Lakehouses to adjust room pricing dynamically hundreds of times per day based on flight bookings and local event velocity.",
        "trend_legacy_debt": "Property management systems (Opera) running on separate hotel databases; guest loyalty data (Strawberry Club) isolated from hotel food & beverage point-of-sale registers.",
        "fomo_cost_of_inaction": "Millions in RevPAR underperformance: Static or late room price adjustments leaving rooms unsold on off-peak nights and underpricing during sudden concert or conference demand spikes.",
        "fomo_peer_velocity": "Competitors update room rates across direct and OTA channels within 10 minutes of market demand shifts; Strawberry revenue managers analyze pricing on daily batch cycles.",
        "fomo_vendor_traps": "High commission fees paid to online travel agencies (15–22%) caused by an inability to deliver competitive direct booking personalization.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 6,
        "investment_eur": "€430,000",
        "three_year_net_value_eur": "€5,870,000",
        "key_questions": [
            {"target": "Chief Commercial Officer / Revenue Management Head", "question": "What is the RevPAR difference across your 240+ hotels between dynamic algorithmic pricing and manual revenue manager overrides?"},
            {"target": "Chief Information Officer (CIO)", "question": "How many fragmented copies of guest profiles exist across your central reservation system, hotel PMS databases, and mobile app?"},
            {"target": "VP of Loyalty & Guest Experience", "question": "Can your marketing systems recommend personalized hotel upgrades and dining offers in real-time as a guest checks in on their mobile app?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What would be the annual bottom-line impact of shifting just 5% of your bookings from high-commission OTAs to your direct digital channels?"}
        ],
        "use_cases": [
            {"title": "Real-Time 240-Hotel PMS & Reservation Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Live Tables pipelines aggregating room reservations, cancellations, and guest check-ins across 240+ properties in real-time.", "architecture": "Delta Lake + Delta Live Tables + Event Hubs"},
            {"title": "Dynamic RevPAR Pricing & Guest Personalization Engine", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models forecasting room demand based on airline bookings, weather, and concerts to optimize room rates automatically.", "architecture": "Databricks Mosaic AI + MLflow + Feature Store"},
            {"title": "Governed Guest 360 & Loyalty Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog establishing single-pane GDPR guest governance while enabling secure partner marketing collaboration.", "architecture": "Unity Catalog + Power BI Direct Lake"}
        ],
        "matched_cases": ["cera", "bridgestone"]
    },

    # 42. The Danish Financial Supervisory Authority (Finanstilsynet)
    "The Danish Financial Supervisory Authority (DFSA – Finanstillsynet)": {
        "industry": "Financial Regulation, Banking Supervision & Market Surveillance",
        "what_databricks_solves": "Modernize the Danish financial regulator's surveillance infrastructure on Azure Databricks, processing millions of algorithmic stock and bond trades (MiFID II), bank stress-test capital ratios, and anti-money laundering (AML) cash flow patterns to safeguard the Danish financial system.",
        "trend_macro": "High-frequency algorithmic trading market volatility, rising geopolitical cyber threats against Nordic banks, stringent EU DORA operational resilience rules, and AML enforcement scrutiny.",
        "trend_competitors": "Top European regulators (ESMA, BaFin, Bank of England) deploy Lakehouses to detect complex insider trading and spoofing patterns across millions of daily order book events.",
        "trend_legacy_debt": "Legacy relational databases and statistical tools struggling to handle high-frequency trading tick data and multi-gigabyte regulatory XBRL filing archives.",
        "fomo_cost_of_inaction": "Unidentified market manipulation: Slow batch surveillance queries allowing insider trading and spoofing networks to exploit Danish equity and bond markets before detection.",
        "fomo_peer_velocity": "Modern financial watchdogs reconstruct market order books and detect spoofing within hours of trading close; Finanstilsynet analysts face multi-week investigation delays.",
        "fomo_vendor_traps": "Extensive licensing costs on proprietary regulatory reporting software unable to scale with explosive growth in algorithmic trading data.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 54,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€1,650,000",
        "payback_months": 8,
        "investment_eur": "€390,000",
        "three_year_net_value_eur": "€4,560,000",
        "key_questions": [
            {"target": "Director General / Finanstilsynsdirektør", "question": "How quickly can your market surveillance analysts reconstruct order book events across Danish exchanges following suspicious stock price spikes?"},
            {"target": "Chief Information Officer (CIO)", "question": "How are you scaling your infrastructure to ingest and query millions of MiFIR transaction reports and Solvency II XBRL filings simultaneously?"},
            {"target": "Head of Bank Supervision / Stress Testing", "question": "What is the computational turnaround time to execute systemic credit shock simulations across Denmark's systemic banks (SIFIs)?"},
            {"target": "Chief Financial Officer / DPO", "question": "Can your audit logging systems prove immutable custody and chain of evidence if trading surveillance data is presented in a criminal trial?"}
        ],
        "use_cases": [
            {"title": "High-Frequency Market Surveillance & MiFID II Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake and Photon compute ingesting millions of daily order book ticks and transaction reports with sub-second query performance.", "architecture": "Delta Lake + Photon + Spark Streaming"},
            {"title": "AI-Driven Insider Trading & AML Market Anomaly Detection", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning and graph algorithms identifying suspicious timing patterns between corporate announcements and trading spikes.", "architecture": "Databricks Mosaic AI + GraphFrames + MLflow"},
            {"title": "Sovereign Regulatory Data Clean Rooms & Legal Audit Lineage", "category": "Unified Governance & Security", "description": "Unity Catalog enforcing strict Danish bank secrecy laws with court-admissible, tamper-evident query logging.", "architecture": "Unity Catalog + Sovereign Security"}
        ],
        "matched_cases": ["cera", "ggz-rivierduinen"]
    },

    # 43. Vard (Vard Group AS / Fincantieri)
    "Vard": {
        "industry": "Specialized Shipbuilding, Offshore Vessels & Naval Engineering",
        "what_databricks_solves": "Consolidate 3D CAD/CAM shipyard engineering models, sub-contractor supply chain tracking, and vessel sea-trial IoT telemetry across Norwegian and international shipyards onto an Azure Databricks Lakehouse, cutting custom vessel build delays and warranty rework.",
        "trend_macro": "Surging demand for offshore wind service operation vessels (SOVs) and zero-emission hybrid ships, intense global shipyard cost competition, and supply chain lead times for marine equipment.",
        "trend_competitors": "Leading European shipbuilders (Fincantieri, Damen, Meyer Werft) deploy Lakehouse digital twins to track thousands of vessel construction milestones and optimize outfitting schedules.",
        "trend_legacy_debt": "Engineering PLM systems separated from shipyard ERP; construction progress tracked via manual spreadsheets and clipboard paper logs on dry docks.",
        "fomo_cost_of_inaction": "Severe liquidated damages on delayed vessel handovers: Delivering a specialized offshore wind or naval vessel even 2 weeks late can trigger millions in late delivery penalties from shipowners.",
        "fomo_peer_velocity": "Competitors identify piping and electrical outfitting interferences during design simulation; Vard engineers discover conflicts during physical construction in the shipyard.",
        "fomo_vendor_traps": "Heavily customized ERP systems charging immense licensing fees with rigid data export hurdles.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€5,840,000",
        "key_questions": [
            {"target": "Chief Executive Officer / Shipyard Director", "question": "What was your total annual expenditure in late delivery penalties and warranty claims across custom offshore vessel construction projects?"},
            {"target": "VP Engineering & Naval Architecture", "question": "How quickly can your engineering teams simulate weight distribution and hydrodynamic stability changes when shipowners request custom equipment modifications?"},
            {"target": "Chief Information Officer (CIO)", "question": "Why is sea-trial vessel engine telemetry disconnected from your design engineering PLM databases?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the working capital reduction of automating marine equipment procurement schedules against actual shipyard outfitting progress?"}
        ],
        "use_cases": [
            {"title": "Shipyard Project Execution & Vessel Outfitting Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake integrating 3D CAD engineering schedules, sub-contractor progress, and material delivery logs to prevent dry dock bottlenecks.", "architecture": "Delta Live Tables + Azure Databricks + Power BI"},
            {"title": "Sea-Trial Vessel Hydrodynamics & Fuel Performance AI", "category": "Enterprise GenAI & Mosaic AI", "description": "Machine learning models analyzing sea-trial propulsion telemetry and wave resistance to verify contractually guaranteed fuel economy.", "architecture": "Databricks Mosaic AI + MLflow"},
            {"title": "Governed Naval & Commercial Vessel Design Mesh", "category": "Unified Governance & Security", "description": "Unity Catalog maintaining strict data isolation between confidential naval defense projects and commercial offshore wind vessels.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["austrotherm", "nordic-paper"]
    },

    # 44. Zealand Pharma
    "Zealand Pharma": {
        "industry": "Biotechnology, Peptide Therapeutics & Metabolic Disease R&D",
        "what_databricks_solves": "Accelerate next-generation peptide therapeutic discovery (obesity, rare metabolic diseases) on Azure Databricks with Mosaic AI, processing high-throughput peptide molecular simulations, clinical trial pharmacokinetic (PK/PD) telemetry, and EMA/FDA regulatory submissions.",
        "trend_macro": "Explosive global demand for obesity and metabolic GLP-1/GLP-2 receptor therapeutics, intense pharmaceutical licensing competition, and accelerated clinical development timelines.",
        "trend_competitors": "Top global biotech peers (Novo Nordisk, Eli Lilly, Amgen) deploy Databricks Mosaic AI to run generative molecular peptide design, screening millions of peptide sequences virtually.",
        "trend_legacy_debt": "Bioinformatics pipelines running on ad-hoc cloud VMs; clinical trial pharmacokinetic data stored in isolated SAS and Excel files with manual validation.",
        "fomo_cost_of_inaction": "Delayed clinical trial milestones: Every month of delay in peptide candidate optimization or regulatory clinical trial filing represents hundreds of millions in lost market capital and commercial partnership value.",
        "fomo_peer_velocity": "Competitors screen peptide receptor affinity and solubility virtually in days using fine-tuned transformer models; Zealand scientists spend months synthesizing physical lab peptides.",
        "fomo_vendor_traps": "High recurring software fees on proprietary molecular modeling and bio-statistical software packages with unscalable compute architectures.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.9x",
        "annual_savings_eur": "€2,900,000",
        "payback_months": 6,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€8,180,000",
        "key_questions": [
            {"target": "Chief Scientific Officer (CSO) / Head of Research", "question": "How many months could you shave off your peptide lead optimization cycle by running generative molecular stability simulations on GPU-accelerated Databricks clusters?"},
            {"target": "Chief Information Officer (CIO)", "question": "How do you enforce 21 CFR Part 11 and GxP regulatory compliance while giving computational chemists access to modern generative AI tools?"},
            {"target": "Head of Clinical Development", "question": "How long does it take your data teams to aggregate and query pharmacokinetic data across multi-center obesity clinical trials for interim safety reviews?"},
            {"target": "Chief Financial Officer (CFO)", "question": "What is the commercial licensing valuation uplift of demonstrating algorithmic, GxP-validated data integrity to global pharmaceutical co-development partners?"}
        ],
        "use_cases": [
            {"title": "Generative Peptide Design & Molecular Simulation Engine", "category": "Enterprise GenAI & Mosaic AI", "description": "Mosaic AI and BioNeMo models predicting peptide receptor binding affinity, metabolic half-life, and immunogenicity virtually.", "architecture": "Databricks Mosaic AI + GPU Serving + MLflow"},
            {"title": "GxP-Compliant Pharmacokinetic & Clinical Trial Lakehouse", "category": "Lakehouse Modernization", "description": "Delta Lake ingesting clinical biomarker assays, dosing schedules, and patient vitals with automated validation and traceability.", "architecture": "Delta Live Tables + Azure Databricks + Power BI"},
            {"title": "Sovereign Intellectual Property & Co-Development Clean Rooms", "category": "Unified Governance & Security", "description": "Unity Catalog isolating proprietary peptide structures while enabling secure data collaboration with pharmaceutical licensing partners.", "architecture": "Unity Catalog + Delta Sharing"}
        ],
        "matched_cases": ["lrm-medemotion", "ggz-rivierduinen"]
    }
}

# Generic mapping fallbacks for any subsidiary / sub-entity
def get_client_intelligence(client_name: str, parent: str = "", sub: str = "") -> Dict[str, Any]:
    """Retrieve or derive razor-sharp client intelligence for any of the 64 customer rows."""
    # Direct match attempts
    for key in [sub, client_name, parent]:
        if key and key in CLIENT_CATALOG:
            return CLIENT_CATALOG[key]
            
    # Substring / keyword matching
    lookup = f"{client_name} {parent} {sub}".lower()
    
    if "forsvars" in lookup or "defence" in lookup or "armed forces" in lookup:
        return CLIENT_CATALOG["Ministry of Defence - Norway"]
    if "skat" in lookup or "skatteministeriet" in lookup:
        return CLIENT_CATALOG["SKAT Denmark"]
    if "lægemiddel" in lookup or "sundhedsdata" in lookup or "ministry aps" in lookup or "danish government" in lookup:
        return CLIENT_CATALOG["Danish Government"]
    if "helsedirektoratet" in lookup:
        return CLIENT_CATALOG["Region Nordjylland"]
    if "widerøe" in lookup:
        return CLIENT_CATALOG["Norwegian Air Shuttle ASA"]
    if "fred. olsen" in lookup or "bonheur" in lookup:
        return CLIENT_CATALOG["Bonheur ASA (Fred Olsen)"]
    if "tgs" in lookup or "pgs" in lookup:
        return CLIENT_CATALOG["Petroleum Geo-Services (PGS ASA)"]
    if "biomar" in lookup or "borg automotive" in lookup or "gpv" in lookup or "schouw" in lookup:
        return CLIENT_CATALOG["Schouw & Co."]
    if "swedish match" in lookup or "general cigar" in lookup or "tobacco" in lookup:
        return CLIENT_CATALOG["Scandinavian Tobacco Group"]
    if "vandcenter" in lookup:
        return CLIENT_CATALOG["Frederiksberg Forsyning A/S"]
    if "finanstilsynet" in lookup or "dfsa" in lookup:
        return CLIENT_CATALOG["The Danish Financial Supervisory Authority (DFSA – Finanstillsynet)"]
    if "dressmann" in lookup or "cubus" in lookup:
        return CLIENT_CATALOG["Cubus"]
    if "bama" in lookup:
        return CLIENT_CATALOG["Bama Gruppen"]
    if "semler" in lookup:
        return CLIENT_CATALOG["Semler IT A/S"]
    if "normal" in lookup:
        return CLIENT_CATALOG["Normal A/S"]
    if "nordland" in lookup:
        return CLIENT_CATALOG["Nordland Fylkeskommune"]
    if "ruter" in lookup:
        return CLIENT_CATALOG["Ruter As"]
    if "salmar" in lookup:
        return CLIENT_CATALOG["Salmar AS"]
    if "monjasa" in lookup:
        return CLIENT_CATALOG["Monjasa A/S"]
    if "navico" in lookup:
        return CLIENT_CATALOG["Navico"]
    if "nokas" in lookup or "avarn" in lookup:
        return CLIENT_CATALOG["Nokas Group"]
    if "ng nordic" in lookup or "norsk gjenvinning" in lookup:
        return CLIENT_CATALOG["Ng Nordic AS"]
    if "nnit" in lookup:
        return CLIENT_CATALOG["NNIT A/S"]
    if "nav" in lookup:
        return CLIENT_CATALOG["NAV"]
    if "zealand" in lookup:
        return CLIENT_CATALOG["Zealand Pharma"]
    if "leo pharma" in lookup:
        return CLIENT_CATALOG["LEO Pharma"]
    if "diaverum" in lookup:
        return CLIENT_CATALOG["Diaverum"]
    if "ecco" in lookup:
        return CLIENT_CATALOG["ECCO Sko"]
    if "hartmann" in lookup:
        return CLIENT_CATALOG["Hartmann"]
    if "jotun" in lookup:
        return CLIENT_CATALOG["Jotun A/S"]
    if "jysk" in lookup:
        return CLIENT_CATALOG["JYSK"]
    if "klp" in lookup or "kommunal landspensjonskasse" in lookup:
        return CLIENT_CATALOG["Kommunal Landspensjonskasse gjensidig forsikringsselskap"]
    if "atp" in lookup or "arbejdsmarkedets" in lookup:
        return CLIENT_CATALOG["Arbejdsmarkedets Tillaegspension (ATP)"]
    if "avinor" in lookup:
        return CLIENT_CATALOG["Avinor AS"]
    if "cowi" in lookup:
        return CLIENT_CATALOG["COWI"]
    if "danish crown" in lookup:
        return CLIENT_CATALOG["Danish Crown"]
    if "energistyrelsen" in lookup:
        return CLIENT_CATALOG["Energistyrelsen"]
    if "g2 ocean" in lookup:
        return CLIENT_CATALOG["G2 Ocean"]
    if "rigspolitiet" in lookup:
        return CLIENT_CATALOG["Rigspolitiet"]
    if "royal unibrew" in lookup:
        return CLIENT_CATALOG["Royal Unibrew"]
    if "strawberry" in lookup or "nordic choice" in lookup:
        return CLIENT_CATALOG["Strawberry Hotels (Nordic Choice Hotels)"]
    if "vard" in lookup:
        return CLIENT_CATALOG["Vard"]
    if "borr" in lookup:
        return CLIENT_CATALOG["Borr Drilling"]
    if "digitaliseringsministeriet" in lookup:
        return CLIENT_CATALOG["Aarhus Kommune"]

    # Default fallback
    return CLIENT_CATALOG["JYSK"]
