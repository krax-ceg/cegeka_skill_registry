"""
Raihan Chowdhury Microsoft Kunder Catalog
Dedicated Intelligence & Closing blueprints for all 40 Swedish Enterprise Accounts
Cegeka & Microsoft Strategic Alliance (vm-nor-dev)
Lead Specialist: Raihan Chowdhury (Cloud & AI Specialist, rachowdhury@microsoft.com)
Account Executive: Mårten Palm (PALMMARTEN)
Territory: SWE.SMECC.DIV.0702
"""

RAIHAN_INTEL_CATALOG = {
    "Väderstad AB": {
        "org_nr": "556052-8800",
        "tpid": "3517725",
        "industry": "Agricultural Machinery & Smart Farming Robotics",
        "what_partner_solves": "Unify IoT telemetry from tens of thousands of connected seed drills and cultivators (Tempo, Proceed, Carrier) into Microsoft Fabric OneLake and Azure IoT Operations, enabling sub-second implement diagnostics, variable seed rate agronomic models, and automated digital farm compliance while slashing on-prem SQL maintenance.",
        "what_databricks_solves": "Unify IoT telemetry from tens of thousands of connected seed drills and cultivators (Tempo, Proceed, Carrier) into Microsoft Fabric OneLake and Azure IoT Operations, enabling sub-second implement diagnostics, variable seed rate agronomic models, and automated digital farm compliance while slashing on-prem SQL maintenance.",
        "what_microsoft_solves": "Unify IoT telemetry from tens of thousands of connected seed drills and cultivators (Tempo, Proceed, Carrier) into Microsoft Fabric OneLake and Azure IoT Operations, enabling sub-second implement diagnostics, variable seed rate agronomic models, and automated digital farm compliance while slashing on-prem SQL maintenance.",
        "trend_macro": "Global sustainability mandates and EU CAP regulations requiring precision seed and fertilizer placement with verified digital field documentation.",
        "trend_competitors": "Global agricultural OEMs (John Deere, AGCO) rapidly expanding cloud farm management ecosystems with real-time implement telemetry.",
        "trend_legacy_debt": "Fragmented on-premise SQL databases and batch CAN-bus log uploads causing multi-day delays in field performance analytics.",
        "fomo_cost_of_inaction": "Risk of losing premium seed drill market share across Europe if real-time agronomic telemetry and automated variable-rate seeding are delayed.",
        "fomo_peer_velocity": "Competitor connected tractors optimize seed spacing in real time; Väderstad dealers wait for post-season machine log extraction.",
        "fomo_vendor_traps": "Escalating licensing costs for legacy on-premise relational databases with high storage friction for streaming sensor telemetry.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€5,780,000",
        "key_questions": [
            {
                "target": "VP Digital Solutions / CTO",
                "question": "How do you ingest and process telemetry across 50,000 active smart seed drills during peak spring planting without latency spikes?"
            },
            {
                "target": "Head of Agronomy & R&D",
                "question": "How quickly can agronomic yield feedback from Proceed seed drills be served back to farmers via Power BI Direct Lake?"
            },
            {
                "target": "Chief Financial Officer (CFO)",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            },
            {
                "target": "Head of Global Service",
                "question": "How many hours of field technician downtime could be eliminated through predictive implement wear alerts?"
            }
        ],
        "use_cases": [
            {
                "title": "Real-Time Implement Telemetry & Digital Twins",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming CAN-bus sensor telemetry from Tempo and Proceed seed drills via Azure IoT Operations into Fabric Real-Time Hub.",
                "architecture": "Azure IoT Operations + Fabric Real-Time Intelligence + Eventstream"
            },
            {
                "title": "Variable-Rate Agronomic Soil & Seed Lakehouse",
                "category": "Enterprise SaaS Data Fabric",
                "description": "OneLake medallion architecture merging precision soil maps, weather data, and machine planting rates for optimal crop yields.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Field Technician Diagnostic Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Mobile maintenance assistant providing machine service manuals, diagnostic codes, and hydraulic diagrams to field service teams.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Power Apps"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "Gränges AB": {
        "org_nr": "556004-0964",
        "tpid": "24610144",
        "industry": "Aluminium Engineering, Thermal Materials & Battery Foils",
        "what_partner_solves": "Consolidate global rolling mill telemetry across Sweden, US, Poland, and China into Microsoft Fabric and Azure Data Factory to deliver real-time metallurgical scrap reduction, energy optimization, and automated EU CSRD Scope 1-3 carbon tracking for automotive battery foil supply chains.",
        "what_databricks_solves": "Consolidate global rolling mill telemetry across Sweden, US, Poland, and China into Microsoft Fabric and Azure Data Factory to deliver real-time metallurgical scrap reduction, energy optimization, and automated EU CSRD Scope 1-3 carbon tracking for automotive battery foil supply chains.",
        "what_microsoft_solves": "Consolidate global rolling mill telemetry across Sweden, US, Poland, and China into Microsoft Fabric and Azure Data Factory to deliver real-time metallurgical scrap reduction, energy optimization, and automated EU CSRD Scope 1-3 carbon tracking for automotive battery foil supply chains.",
        "trend_macro": "Stringent automotive OEM decarbonization targets and EU CBAM requiring coil-level certified carbon footprints for EV battery foil.",
        "trend_competitors": "Global rolled aluminium producers (Novelis, Constellium) deploying cloud data platforms to drive energy-efficient scrap recycling.",
        "trend_legacy_debt": "Plant-level SCADA historians (Wonderware, AspenTech) locked in regional factory silos with manual monthly Excel reconciliation.",
        "fomo_cost_of_inaction": "Risk of tier-1 automotive OEM supplier disqualification if verified coil-level carbon footprints cannot be certified automatically.",
        "fomo_peer_velocity": "Competitors benchmark rolling mill scrap rates hourly; Gränges plant managers wait for end-of-month financial reports.",
        "fomo_vendor_traps": "Costly proprietary industrial historian maintenance and fragmented on-premise data warehouses.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€3,400,000",
        "payback_months": 6,
        "investment_eur": "€680,000",
        "three_year_net_value_eur": "€9,520,000",
        "key_questions": [
            {
                "target": "VP Sustainability",
                "question": "Can you provide verified Scope 1-3 carbon emissions per metric ton of rolled aluminum coil directly to automotive OEM portals?"
            },
            {
                "target": "Global Operations Director",
                "question": "What is your current scrap rate across global rolling mills, and how much could a 1.5% yield improvement save annually?"
            },
            {
                "target": "Group CIO",
                "question": "How do you enforce uniform data governance across Finspång, Shanghai, and US manufacturing facilities?"
            },
            {
                "target": "CFO",
                "question": "How will transitioning plant data pipelines to Microsoft Fabric lower overall corporate BI licensing costs?"
            }
        ],
        "use_cases": [
            {
                "title": "Global Rolling Mill Scrap & Yield Optimization",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating rolling mill speed, temperature, and strip thickness sensor feeds into OneLake to predict edge crack defects.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Automated Scope 1-3 Battery Foil Carbon Mesh",
                "category": "Unified BI & Direct Lake",
                "description": "Automated product carbon footprint (PCF) calculation per manufactured aluminium coil satisfying EU CSRD standards.",
                "architecture": "Microsoft Sustainability Manager + Power BI Direct Lake"
            },
            {
                "title": "Mill Operator AI Assistance & Recipe Advisor",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Real-time generative AI copilot recommending optimal mill rolling parameters based on alloy chemistry and ambient temperature.",
                "architecture": "Azure OpenAI + Azure AI Search + Teams Integration"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "Advokatfirman Vinge KB": {
        "org_nr": "916421-1250",
        "tpid": "1705265",
        "industry": "Corporate Legal Services & M&A Advisory",
        "what_partner_solves": "Deploy sovereign, air-gapped Azure OpenAI Service and Microsoft Copilot Studio in Sweden Central atop Microsoft Purview and Azure AI Search, automating contract due diligence, clause extraction, and knowledge retrieval across 40+ years of transactional precedent with strict client privilege confidentiality and zero external model training.",
        "what_databricks_solves": "Deploy sovereign, air-gapped Azure OpenAI Service and Microsoft Copilot Studio in Sweden Central atop Microsoft Purview and Azure AI Search, automating contract due diligence, clause extraction, and knowledge retrieval across 40+ years of transactional precedent with strict client privilege confidentiality and zero external model training.",
        "what_microsoft_solves": "Deploy sovereign, air-gapped Azure OpenAI Service and Microsoft Copilot Studio in Sweden Central atop Microsoft Purview and Azure AI Search, automating contract due diligence, clause extraction, and knowledge retrieval across 40+ years of transactional precedent with strict client privilege confidentiality and zero external model training.",
        "trend_macro": "Surge in private equity transactional complexity and regulatory scrutiny (EU FDI, AI Act, CSRD) demanding 10x faster due diligence turnarounds.",
        "trend_competitors": "Top international and Nordic law firms deploying enterprise GenAI to draft and review complex commercial contracts in minutes.",
        "trend_legacy_debt": "On-premise document management systems (iManage, NetDocuments) with basic keyword search unable to handle semantic legal reasoning.",
        "fomo_cost_of_inaction": "Losing multi-million kronor M&A legal advisory mandates to AI-augmented competitors offering 48-hour diligence turnarounds.",
        "fomo_peer_velocity": "Competitor law firms summarize 1,000-page virtual data rooms overnight using legal AI; Vinge associates spend hundreds of billable hours on manual review.",
        "fomo_vendor_traps": "Third-party legal AI point solutions requiring data exports outside Sweden or using shared public LLM endpoints.",
        "tco_reduction_pct": 36,
        "compute_savings_pct": 50,
        "productivity_lift_multiplier": "4.2x",
        "annual_savings_eur": "€1,850,000",
        "payback_months": 5,
        "investment_eur": "€340,000",
        "three_year_net_value_eur": "€5,210,000",
        "key_questions": [
            {
                "target": "Managing Partner",
                "question": "How many associate hours are spent manually reviewing boilerplate lease and employment agreements in virtual data rooms?"
            },
            {
                "target": "Head of IT / CDO",
                "question": "Can you guarantee that sensitive client diligence files never leak into external public LLM training datasets?"
            },
            {
                "target": "Head of Knowledge Management",
                "question": "How quickly can your lawyers find the specific cross-border indemnity clause drafted in 2021?"
            },
            {
                "target": "Risk & Compliance Partner",
                "question": "How do you enforce Swedish Bar Association ethical walls and role-based confidentiality across AI search queries?"
            }
        ],
        "use_cases": [
            {
                "title": "Sovereign Private M&A Due Diligence Engine",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Air-gapped semantic contract search and risk extraction running exclusively within Azure Sweden Central with zero data retention.",
                "architecture": "Azure OpenAI Service (Sweden Central) + Azure AI Search RAG"
            },
            {
                "title": "Zero-Trust Legal Knowledge Governance",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Microsoft Purview integration applying automated sensitivity labels and ethical walls between competing client matters.",
                "architecture": "Microsoft Purview Information Protection + Microsoft Fabric OneLake"
            },
            {
                "title": "Vinge Legal Drafting & Precedent Copilot",
                "category": "Unified BI & Direct Lake",
                "description": "Copilot Studio assistant integrated with Microsoft Word to suggest battle-tested clauses from 40 years of Vinge transactional archives.",
                "architecture": "Microsoft Copilot Studio + Microsoft 365 + Azure AI"
            }
        ],
        "matched_cases": [
            "cera",
            "ggz-rivierduinen"
        ]
    },
    "Motoman Robotics Europe AB": {
        "org_nr": "556211-1319",
        "tpid": "2079484",
        "industry": "Industrial Robotics, Factory Automation & Motion Control",
        "what_partner_solves": "Centralize robot fleet telemetry, edge motor vibration logs, and preventative maintenance streams into Azure IoT Operations and Microsoft Fabric Real-Time Hub, enabling automated anomaly detection before factory line stops and delivering subscription-based Robotics-as-a-Service predictive maintenance models to automotive and electronics OEMs.",
        "what_databricks_solves": "Centralize robot fleet telemetry, edge motor vibration logs, and preventative maintenance streams into Azure IoT Operations and Microsoft Fabric Real-Time Hub, enabling automated anomaly detection before factory line stops and delivering subscription-based Robotics-as-a-Service predictive maintenance models to automotive and electronics OEMs.",
        "what_microsoft_solves": "Centralize robot fleet telemetry, edge motor vibration logs, and preventative maintenance streams into Azure IoT Operations and Microsoft Fabric Real-Time Hub, enabling automated anomaly detection before factory line stops and delivering subscription-based Robotics-as-a-Service predictive maintenance models to automotive and electronics OEMs.",
        "trend_macro": "Severe factory labor shortages and high-speed EV assembly lines demanding 24/7 robotic reliability and guaranteed MTBF.",
        "trend_competitors": "ABB Robotics, Fanuc, and KUKA introducing cloud-connected robot health monitoring suites.",
        "trend_legacy_debt": "Decentralized robot controller logs stored on local teach pendants without centralized fleet analytics.",
        "fomo_cost_of_inaction": "Automotive assembly line stoppages costing up to €20,000 per minute when a welding robot suffers unpredicted servo drive failure.",
        "fomo_peer_velocity": "Leading automation OEMs predict robot joint wear 2 weeks in advance; Motoman technicians react only after alarms trigger.",
        "fomo_vendor_traps": "Fragmented third-party IoT platforms charging excessive device connection fees without unified data lake integration.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,400,000",
        "payback_months": 6,
        "investment_eur": "€490,000",
        "three_year_net_value_eur": "€6,710,000",
        "key_questions": [
            {
                "target": "VP Customer Service & Aftermarket",
                "question": "How many emergency field service callouts could be converted into scheduled maintenance with 14-day vibration warnings?"
            },
            {
                "target": "Head of Robotics Software R&D",
                "question": "How do you collect and analyze telemetry from 30,000 installed Motoman robots across European factories?"
            },
            {
                "target": "CFO",
                "question": "Can we monetize robot health telemetry into high-margin recurring SLA service contracts?"
            },
            {
                "target": "Head of IT",
                "question": "How do you integrate edge robot controllers with Azure IoT Operations securely across customer factory firewalls?"
            }
        ],
        "use_cases": [
            {
                "title": "Connected Robot Fleet Telemetry & Anomaly Hub",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming servo motor current, joint torque, and vibration logs via Azure IoT into Fabric Real-Time Hub.",
                "architecture": "Azure IoT Edge / Operations + Fabric Real-Time Hub + KQL"
            },
            {
                "title": "Robotics-as-a-Service Predictive Maintenance",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models forecasting gearbox and servo bearing wear before mechanical failure occurs.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Field Service Robot Diagnostic Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Mobile generative AI assistant guiding technicians through error code diagnostics and repair procedures.",
                "architecture": "Azure OpenAI Service + Teams Mobile + Dynamics 365 Field Service"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "Etac AB": {
        "org_nr": "556325-2138",
        "tpid": "2688748",
        "industry": "Assistive Devices, Healthcare Mobility & Ergonomic Equipment",
        "what_partner_solves": "Unify disparate ERP systems across international acquisitions into Microsoft Fabric OneLake, establishing automated Medical Device Regulation (MDR) batch traceability, global demand sensing for patient hoists and wheelchairs, and real-time supply chain inventory allocation.",
        "what_databricks_solves": "Unify disparate ERP systems across international acquisitions into Microsoft Fabric OneLake, establishing automated Medical Device Regulation (MDR) batch traceability, global demand sensing for patient hoists and wheelchairs, and real-time supply chain inventory allocation.",
        "what_microsoft_solves": "Unify disparate ERP systems across international acquisitions into Microsoft Fabric OneLake, establishing automated Medical Device Regulation (MDR) batch traceability, global demand sensing for patient hoists and wheelchairs, and real-time supply chain inventory allocation.",
        "trend_macro": "Rapidly aging European demographics driving demand for assistive technology; stringent EU MDR compliance requiring cradle-to-grave device traceability.",
        "trend_competitors": "Global assistive mobility leaders (Invacare, Sunrise Medical) optimizing international distribution networks with cloud supply chain analytics.",
        "trend_legacy_debt": "Multiple disconnected ERP systems (IFS, Dynamics NAV, Movex) from international acquisitions causing inventory blind spots.",
        "fomo_cost_of_inaction": "Severe EU MDR non-compliance audit risk resulting in product recall or shipping freezes across European healthcare systems.",
        "fomo_peer_velocity": "Competitors allocate regional warehouse stock dynamically; Etac logistics teams wait days for manual inventory consolidation.",
        "fomo_vendor_traps": "Costly custom ETL scripts connecting disparate legacy ERP databases that break during routine system upgrades.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 54,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,750,000",
        "payback_months": 7,
        "investment_eur": "€390,000",
        "three_year_net_value_eur": "€4,860,000",
        "key_questions": [
            {
                "target": "VP Quality & Regulatory",
                "question": "How long does it take your team to produce an end-to-end component traceability report during an unannounced EU MDR audit?"
            },
            {
                "target": "Supply Chain Director",
                "question": "What is your safety stock buffer across European warehouses due to lack of synchronized demand sensing?"
            },
            {
                "target": "Group CIO",
                "question": "What is your strategy to harmonize disparate ERP databases across recent acquisitions without a multi-year re-implementation?"
            },
            {
                "target": "CFO",
                "question": "How much working capital is locked in redundant wheelchair and hoist inventory across regional subsidiaries?"
            }
        ],
        "use_cases": [
            {
                "title": "EU MDR Regulatory Traceability Data Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "OneLake medallion architecture providing cryptographic batch lineage from raw steel to finished patient hoist delivery.",
                "architecture": "Microsoft Fabric OneLake + Microsoft Purview + Data Factory"
            },
            {
                "title": "Global Healthcare Mobility Demand Sensing",
                "category": "Unified BI & Direct Lake",
                "description": "Real-time demand forecasting and inventory balancing across Nordic, UK, and European distribution hubs.",
                "architecture": "Power BI Direct Lake + Azure Machine Learning + Fabric"
            },
            {
                "title": "Clinical Technical Documentation Search Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant interrogating medical device technical files, CE certificates, and user manuals.",
                "architecture": "Azure OpenAI Service + Azure AI Search + SharePoint"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "fluvius"
        ]
    },
    "OVAKO HOLDINGS AB": {
        "org_nr": "556813-5361",
        "tpid": "9744825",
        "industry": "Clean Special Steel & Decarbonized Heavy Metallurgy",
        "what_partner_solves": "Ingest high-frequency metallurgical sensor logs, electric arc furnace melt telemetry, and hydrogen electrolysis metrics into Microsoft Fabric Real-Time Intelligence, optimizing melt cycle energy efficiency, scrap alloy yield, and automated product-level Scope 1-3 carbon certificates for green steel buyers.",
        "what_databricks_solves": "Ingest high-frequency metallurgical sensor logs, electric arc furnace melt telemetry, and hydrogen electrolysis metrics into Microsoft Fabric Real-Time Intelligence, optimizing melt cycle energy efficiency, scrap alloy yield, and automated product-level Scope 1-3 carbon certificates for green steel buyers.",
        "what_microsoft_solves": "Ingest high-frequency metallurgical sensor logs, electric arc furnace melt telemetry, and hydrogen electrolysis metrics into Microsoft Fabric Real-Time Intelligence, optimizing melt cycle energy efficiency, scrap alloy yield, and automated product-level Scope 1-3 carbon certificates for green steel buyers.",
        "trend_macro": "Decarbonization mandate in European automotive and heavy machinery (Volvo, Scania, SKF) requiring certified zero-carbon specialty steel.",
        "trend_competitors": "Nordic steel innovators (SSAB, H2 Green Steel) setting global standards for digitalized, fossil-free metallurgical manufacturing.",
        "trend_legacy_debt": "Decades of proprietary mill automation systems, isolated Level 2 melt shop computers, and batch reporting causing delayed energy optimization.",
        "fomo_cost_of_inaction": "Severe electric arc furnace energy waste during peak electricity price spikes costing millions in avoidable operating expenses.",
        "fomo_peer_velocity": "Leading green mills adjust furnace heating cycles dynamically based on hourly power tariffs; Ovako operators rely on static schedules.",
        "fomo_vendor_traps": "Extensive licensing on proprietary industrial process software charging hefty fees for open data access.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 64,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€3,900,000",
        "payback_months": 6,
        "investment_eur": "€720,000",
        "three_year_net_value_eur": "€10,980,000",
        "key_questions": [
            {
                "target": "Head of Decarbonization",
                "question": "How do you calculate the exact kilowatt-hour and hydrogen consumption per finished heat of specialty steel?"
            },
            {
                "target": "Mill Production Director",
                "question": "Can your operators predict slag formation and chemical composition drift before tap time?"
            },
            {
                "target": "Chief Financial Officer (CFO)",
                "question": "How much could dynamic energy arbitrage during spot electricity price spikes reduce electric arc furnace melting costs?"
            },
            {
                "target": "CIO",
                "question": "What is your roadmap to stream Level 2 melt shop data into an enterprise cloud lakehouse securely?"
            }
        ],
        "use_cases": [
            {
                "title": "Electric Arc Furnace & Hydrogen Telemetry Mesh",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Real-time streaming of furnace electrodes, oxygen injectors, and hydrogen plant sensors into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Intelligence + Azure Eventstream + KQL"
            },
            {
                "title": "Green Steel Scope 1-3 Digital Product Passports",
                "category": "Unified BI & Direct Lake",
                "description": "Automated carbon footprint tracking per heat and finished steel bar fulfilling European CSRD requirements.",
                "architecture": "Microsoft Sustainability Manager + Power BI Direct Lake"
            },
            {
                "title": "Metallurgical Scrap & Alloy Optimization Engine",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models calculating the lowest-cost scrap blend that achieves precise metallurgical specifications.",
                "architecture": "Microsoft Fabric OneLake + Azure Machine Learning"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "Cejn AB": {
        "org_nr": "556066-4837",
        "tpid": "2994363",
        "industry": "High-Pressure Quick Connect Couplings & Precision Pneumatics",
        "what_partner_solves": "Transition fragmented on-premise manufacturing and distribution databases into Microsoft Fabric, enabling real-time leak detection telemetry analytics for thermal management quick connects (used in AI data centers and EV cooling) and global inventory forecasting.",
        "what_databricks_solves": "Transition fragmented on-premise manufacturing and distribution databases into Microsoft Fabric, enabling real-time leak detection telemetry analytics for thermal management quick connects (used in AI data centers and EV cooling) and global inventory forecasting.",
        "what_microsoft_solves": "Transition fragmented on-premise manufacturing and distribution databases into Microsoft Fabric, enabling real-time leak detection telemetry analytics for thermal management quick connects (used in AI data centers and EV cooling) and global inventory forecasting.",
        "trend_macro": "Explosive growth of liquid-cooled AI data centers and EV battery fast-charging demanding ultra-reliable quick connect couplings.",
        "trend_competitors": "Global pneumatic leaders (Parker Hannifin, Stäubli) embedding digital monitoring and automated cloud ordering into thermal management portfolios.",
        "trend_legacy_debt": "Legacy on-premise ERP with batch inventory reports and isolated SQL databases struggling with global subsidiary synchronization.",
        "fomo_cost_of_inaction": "Missing out on multi-million dollar hyperscale AI data center cooling infrastructure tenders due to lack of certified digital leak test data.",
        "fomo_peer_velocity": "Competitors share real-time thermal cooling telemetry directly with data center operators; Cejn relies on manual factory test sheets.",
        "fomo_vendor_traps": "Aging on-premise relational database maintenance agreements with high costs for storage scaling.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 52,
        "productivity_lift_multiplier": "3.1x",
        "annual_savings_eur": "€1,600,000",
        "payback_months": 7,
        "investment_eur": "€350,000",
        "three_year_net_value_eur": "€4,450,000",
        "key_questions": [
            {
                "target": "VP Thermal Management",
                "question": "How do you provide certified hydrostatic burst and leak-test data to hyperscale data center builders?"
            },
            {
                "target": "Global Sales Director",
                "question": "What is your order-to-delivery lead time for custom quick-connect assemblies across 17 global sales subsidiaries?"
            },
            {
                "target": "Group CIO",
                "question": "How do you plan to migrate legacy on-premise SQL reporting into a governed cloud fabric?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "AI Data Center Cooling Coupling Quality Analytics",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Ingesting automated pressure decay and helium leak test sensor streams into Fabric OneLake for quality validation.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Global Sales Subsidiary Inventory Mesh",
                "category": "Unified BI & Direct Lake",
                "description": "Consolidating finished coupling stock across 17 international sales offices into a single Direct Lake model.",
                "architecture": "Microsoft Fabric Lakehouse + Power BI Direct Lake"
            },
            {
                "title": "Engineering CAD & Technical Spec Assistant",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI copilot helping sales engineers match customer flow and pressure specs with the optimal coupling.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "Be Group Holding AB": {
        "org_nr": "556578-4724",
        "tpid": "11867615",
        "industry": "Steel & Metal Distribution, Processing & Supply Chain",
        "what_partner_solves": "Consolidate Nordic service center stock, dynamic raw material pricing, and transport routing from legacy ERPs into Microsoft Fabric, powering dynamic algorithmic steel pricing, deadweight inventory reduction, and automated customer carbon declarations.",
        "what_databricks_solves": "Consolidate Nordic service center stock, dynamic raw material pricing, and transport routing from legacy ERPs into Microsoft Fabric, powering dynamic algorithmic steel pricing, deadweight inventory reduction, and automated customer carbon declarations.",
        "what_microsoft_solves": "Consolidate Nordic service center stock, dynamic raw material pricing, and transport routing from legacy ERPs into Microsoft Fabric, powering dynamic algorithmic steel pricing, deadweight inventory reduction, and automated customer carbon declarations.",
        "trend_macro": "Severe volatility in global steel spot prices and rising customer demand for certified green steel tracking in construction tenders.",
        "trend_competitors": "Leading metal distributors (Klöckner & Co, Tibnor) investing heavily in digital steel trading platforms and automated e-commerce.",
        "trend_legacy_debt": "Legacy AS400 / Movex systems with rigid overnight inventory batch processing and manual pricing spreadsheets.",
        "fomo_cost_of_inaction": "Margin compression caused by slow manual repricing during rapid scrap steel price shifts, leading to inventory devaluation.",
        "fomo_peer_velocity": "Competitors update steel spot prices dynamically online; BE Group sales reps spend hours manually quoting customers.",
        "fomo_vendor_traps": "High maintenance fees on legacy ERP systems without modern API connectivity for customer digital procurement.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,800,000",
        "payback_months": 6,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€7,890,000",
        "key_questions": [
            {
                "target": "Commercial Director",
                "question": "How fast can you update spot prices across 50,000 steel articles when raw hot-rolled coil prices swing 5% in a day?"
            },
            {
                "target": "Supply Chain Director",
                "question": "How much dead capital is tied up in slow-moving structural steel beam inventory across Nordic service centers?"
            },
            {
                "target": "Chief Financial Officer (CFO)",
                "question": "Can we automate customer quote processing using Azure OpenAI to capture more transactional RFQs?"
            },
            {
                "target": "Group CIO",
                "question": "What is your roadmap to replace legacy AS400 reporting with real-time Fabric Direct Lake dashboards?"
            }
        ],
        "use_cases": [
            {
                "title": "Dynamic Algorithmic Steel Pricing Engine",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Combining global steel futures, competitor prices, and service center stock into OneLake to calculate dynamic customer margins.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Nordic Service Center Inventory Optimization",
                "category": "Unified BI & Direct Lake",
                "description": "Automated stock rebalancing and demand forecasting across Swedish, Finnish, and Baltic distribution hubs.",
                "architecture": "Power BI Direct Lake + Azure Synapse + Fabric"
            },
            {
                "title": "Intelligent RFQ & Order Document Extraction",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant extracting material specs, dimensions, and delivery dates from customer email RFQs.",
                "architecture": "Azure OpenAI Service + Azure AI Document Intelligence + Teams"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "fluvius"
        ]
    },
    "AB Fagerhult": {
        "org_nr": "556110-2977",
        "tpid": "8705499",
        "industry": "Professional Architectural & Smart Connected Commercial Lighting",
        "what_partner_solves": "Harness sensor telemetry from millions of connected smart luminaires (Organic Response IoT platform) into Microsoft Fabric and Azure Digital Twins, empowering commercial building managers to optimize occupancy, energy savings, and predictive luminaire lifecycle maintenance.",
        "what_databricks_solves": "Harness sensor telemetry from millions of connected smart luminaires (Organic Response IoT platform) into Microsoft Fabric and Azure Digital Twins, empowering commercial building managers to optimize occupancy, energy savings, and predictive luminaire lifecycle maintenance.",
        "what_microsoft_solves": "Harness sensor telemetry from millions of connected smart luminaires (Organic Response IoT platform) into Microsoft Fabric and Azure Digital Twins, empowering commercial building managers to optimize occupancy, energy savings, and predictive luminaire lifecycle maintenance.",
        "trend_macro": "EU Energy Performance of Buildings Directive (EPBD) mandating commercial building energy reduction; smart building IoT convergence.",
        "trend_competitors": "Global lighting innovators (Signify, Zumtobel) deploying enterprise cloud IoT platforms to capture recurring smart building software revenue.",
        "trend_legacy_debt": "Disconnected lighting control databases, siloed brand ERPs, and batch telemetry feeds hindering real-time analytics.",
        "fomo_cost_of_inaction": "Luminaires reduced to commoditized hardware if Fagerhult fails to provide enterprise smart building telemetry dashboards.",
        "fomo_peer_velocity": "Competitors provide commercial landlords with real-time occupancy heatmaps; Fagerhult's Organic Response data remains isolated.",
        "fomo_vendor_traps": "Proprietary cloud IoT hosting costs escalating without unified data lake integration or advanced machine learning.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,600,000",
        "payback_months": 7,
        "investment_eur": "€540,000",
        "three_year_net_value_eur": "€7,260,000",
        "key_questions": [
            {
                "target": "Head of Smart Lighting Solutions",
                "question": "How do you stream and visualize occupancy telemetry from 100,000 luminaires in real time for enterprise facility directors?"
            },
            {
                "target": "Group CIO",
                "question": "How are you unifying data architectures across Fagerhult's 12 European lighting brands?"
            },
            {
                "target": "CFO",
                "question": "What is your recurring software revenue potential from connected lighting energy analytics?"
            },
            {
                "target": "Sustainability Director",
                "question": "Can you provide automated EPBD building energy audit reports directly to commercial property owners?"
            }
        ],
        "use_cases": [
            {
                "title": "Smart Connected Lighting Telemetry Fabric",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Real-time streaming of Organic Response luminaire PIR occupancy and ambient light telemetry into Fabric Eventstream.",
                "architecture": "Azure IoT Hub + Fabric Real-Time Hub + KQL Eventhouse"
            },
            {
                "title": "Commercial Building Energy Digital Twins",
                "category": "Unified BI & Direct Lake",
                "description": "Interactive 3D building models visualizing floor-by-floor occupancy and HVAC energy savings in Power BI Direct Lake.",
                "architecture": "Azure Digital Twins + Power BI Direct Lake + Fabric"
            },
            {
                "title": "Architectural Lighting Specification Assistant",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI copilot helping lighting designers and architects query 12 brand catalogs for optimal luminaire layouts.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "fluvius",
            "austrotherm"
        ]
    },
    "Mycronic AB": {
        "org_nr": "556351-2374",
        "tpid": "955914",
        "industry": "High-Tech Photomask Pattern Generators & Surface Mount Technology",
        "what_partner_solves": "Ingest sub-micron optical telemetry, laser calibration logs, and global SMT pick-and-place machine diagnostics into Microsoft Fabric and Azure ML, delivering predictive laser wear warnings, automated yield drift correction, and 99.99% uptime for semiconductor and flat-panel display fabs globally.",
        "what_databricks_solves": "Ingest sub-micron optical telemetry, laser calibration logs, and global SMT pick-and-place machine diagnostics into Microsoft Fabric and Azure ML, delivering predictive laser wear warnings, automated yield drift correction, and 99.99% uptime for semiconductor and flat-panel display fabs globally.",
        "what_microsoft_solves": "Ingest sub-micron optical telemetry, laser calibration logs, and global SMT pick-and-place machine diagnostics into Microsoft Fabric and Azure ML, delivering predictive laser wear warnings, automated yield drift correction, and 99.99% uptime for semiconductor and flat-panel display fabs globally.",
        "trend_macro": "Global semiconductor boom and display packaging miniaturization requiring zero-defect photomask generation.",
        "trend_competitors": "Semiconductor equipment leaders (ASML, ASM Pacific) investing massive capital into predictive digital twins and AI fleet diagnostics.",
        "trend_legacy_debt": "Terabytes of proprietary optical calibration logs stored in localized machine archives without cloud fleet analytics.",
        "fomo_cost_of_inaction": "A single unplanned laser outage at an Asian display manufacturer's cleanroom halting hundreds of millions in display production.",
        "fomo_peer_velocity": "Leading semiconductor OEMs predict optical component drift 72 hours before cleanroom yield loss; Mycronic responds to alarms.",
        "fomo_vendor_traps": "Fragmented internal analytics tools requiring manual Python scripts to extract cleanroom machine performance data.",
        "tco_reduction_pct": 48,
        "compute_savings_pct": 66,
        "productivity_lift_multiplier": "3.9x",
        "annual_savings_eur": "€3,700,000",
        "payback_months": 6,
        "investment_eur": "€680,000",
        "three_year_net_value_eur": "€10,420,000",
        "key_questions": [
            {
                "target": "VP Pattern Generators",
                "question": "Can your engineering teams predict laser drift in photomask machines 72 hours before cleanroom yield degradation?"
            },
            {
                "target": "Head of Global Service",
                "question": "How do you centralize and analyze machine telemetry from cleanrooms across South Korea, Taiwan, and the US?"
            },
            {
                "target": "CISO",
                "question": "How do you ensure proprietary optical IP is strictly safeguarded when streaming telemetry to the cloud?"
            },
            {
                "target": "CFO",
                "question": "How much could converting break-fix cleanroom repairs into predictive maintenance agreements boost recurring service margin?"
            }
        ],
        "use_cases": [
            {
                "title": "Sub-Micron Precision Laser Telemetry Mesh",
                "category": "Real-Time Intelligence (KQL)",
                "description": "High-frequency streaming of optical interferometer and laser sensor telemetry into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Intelligence + Eventstream + KQL"
            },
            {
                "title": "Global Cleanroom Fleet Diagnostics & Digital Twins",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Predictive machine learning models identifying optical degradation and thermal drift across global fabs.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Semiconductor IP Protection & Sovereign Governance",
                "category": "Unified BI & Direct Lake",
                "description": "Microsoft Purview sovereign data boundaries and encryption protecting confidential photomask design algorithms.",
                "architecture": "Microsoft Purview + Azure Confidential Computing"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "HÖGANAS AB": {
        "org_nr": "556005-0120",
        "tpid": "1779563",
        "industry": "Powder Metallurgy, Sintered Metal Powders & Additive Manufacturing",
        "what_partner_solves": "Unite furnace sensor data, chemical atomization telemetry, and powder grain distribution quality control logs into Microsoft Fabric, driving automated particle size prediction, furnace energy reduction, and digital product passports.",
        "what_databricks_solves": "Unite furnace sensor data, chemical atomization telemetry, and powder grain distribution quality control logs into Microsoft Fabric, driving automated particle size prediction, furnace energy reduction, and digital product passports.",
        "what_microsoft_solves": "Unite furnace sensor data, chemical atomization telemetry, and powder grain distribution quality control logs into Microsoft Fabric, driving automated particle size prediction, furnace energy reduction, and digital product passports.",
        "trend_macro": "Electrification of automotive powertrains demanding specialized soft magnetic composites (SMC) for EV traction motors.",
        "trend_competitors": "Global powder metallurgy competitors (GKN Sinter Metals, Rio Tinto Metal Powders) scaling smart cloud manufacturing.",
        "trend_legacy_debt": "Disconnected laboratory information management systems (LIMS) and isolated atomization plant historians.",
        "fomo_cost_of_inaction": "High energy waste during batch atomization and scrap production when powder grain distribution fails EV automotive specs.",
        "fomo_peer_velocity": "Competitors predict powder particle size distribution during atomization; Höganäs waits for post-cooling lab assays.",
        "fomo_vendor_traps": "Aging on-premise industrial data historian licenses with high costs for multi-plant data integration.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,500,000",
        "payback_months": 7,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€6,990,000",
        "key_questions": [
            {
                "target": "Head of Metallurgy R&D",
                "question": "How quickly can your chemists correlate atomization temperature and gas flow with finished powder magnetic permeability?"
            },
            {
                "target": "Operations Director",
                "question": "What is your strategy to reduce furnace gas consumption through predictive temperature control models?"
            },
            {
                "target": "Group CIO",
                "question": "How do you integrate atomization telemetry with global customer ERP orders across 15 international plants?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Powder Metallurgy Atomization Analytics",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating gas nozzle pressure, melt stream temperature, and particle size laser logs into OneLake.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure Synapse"
            },
            {
                "title": "EV Soft Magnetic Composite Quality Prediction",
                "category": "Unified BI & Direct Lake",
                "description": "Machine learning models forecasting magnetic core loss and permeability in sintered components.",
                "architecture": "Azure Machine Learning + Power BI Direct Lake + Fabric"
            },
            {
                "title": "Metallurgical Material Science Knowledge Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant interrogating 50 years of Höganäs powder formulation patents and alloy specs.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "Hydroscand Group AB": {
        "org_nr": "556360-1532",
        "tpid": "7334851",
        "industry": "Hydraulic Hose Systems, Fluid Connectors & 24/7 Mobile Hose Service",
        "what_partner_solves": "Combine mobile service van inventory, GPS dispatching, and hydraulic telemetry into Microsoft Fabric Real-Time Intelligence, enabling predictive hydraulic hose failure alerts for construction/forestry OEMs, dynamic emergency van routing, and optimized central warehouse replenishment.",
        "what_databricks_solves": "Combine mobile service van inventory, GPS dispatching, and hydraulic telemetry into Microsoft Fabric Real-Time Intelligence, enabling predictive hydraulic hose failure alerts for construction/forestry OEMs, dynamic emergency van routing, and optimized central warehouse replenishment.",
        "what_microsoft_solves": "Combine mobile service van inventory, GPS dispatching, and hydraulic telemetry into Microsoft Fabric Real-Time Intelligence, enabling predictive hydraulic hose failure alerts for construction/forestry OEMs, dynamic emergency van routing, and optimized central warehouse replenishment.",
        "trend_macro": "Heavy machinery operators demanding 60-minute emergency mobile hose turnaround to prevent costly construction delays.",
        "trend_competitors": "Mobile hose service competitors (Pirtek, Dunlop Hiflex) expanding dynamic digital dispatch fleets.",
        "trend_legacy_debt": "Legacy ERP and disconnected mobile van inventory software leading to missing emergency repair parts.",
        "fomo_cost_of_inaction": "Severe customer churn to mobile repair competitors when an emergency service van arrives without the required high-pressure fitting.",
        "fomo_peer_velocity": "Competitors dispatch nearest van with guaranteed in-stock parts; Hydroscand vans carry static stock profiles.",
        "fomo_vendor_traps": "High maintenance fees on legacy dispatch tools with no integration to central ERP warehouse inventory.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€6,140,000",
        "key_questions": [
            {
                "target": "Managing Director SlangAkuten",
                "question": "What is your average response time, and how often is a technician unable to complete a job on first visit due to missing van parts?"
            },
            {
                "target": "Group Supply Chain Director",
                "question": "How do you optimize inventory across 400 mobile vans and 250 branches in real time?"
            },
            {
                "target": "Group CIO",
                "question": "How do you equip mobile technicians with offline-capable mobile diagnostic tools?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Real-Time Emergency Van Dispatch & Stock Telemetry",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Real-time streaming of mobile van GPS locations, completed job logs, and remaining high-pressure hose stock into Fabric.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            },
            {
                "title": "Predictive Hydraulic Hose Failure Analytics",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Analyzing hydraulic pressure cycles and environmental wear to recommend proactive hose replacement during scheduled fleet service.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Field Technician Mobile Hose Identification Assistant",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Computer vision copilot allowing technicians to photograph damaged fittings and identify exact replacement part numbers.",
                "architecture": "Azure OpenAI Service (GPT-4 Vision) + Power Apps Mobile"
            }
        ],
        "matched_cases": [
            "fluvius",
            "bridgestone"
        ]
    },
    "VBG AB Publ": {
        "org_nr": "556069-0751",
        "tpid": "8705179",
        "industry": "Commercial Vehicle Couplings, Truck Equipment & Bus Climate Systems",
        "what_partner_solves": "Centralize global manufacturing telemetry, drawbar stress-sensor IoT streams, and warranty claim records into Microsoft Fabric, automating predictive maintenance on safety-critical truck couplings and accelerating global R&D cycle times.",
        "what_databricks_solves": "Centralize global manufacturing telemetry, drawbar stress-sensor IoT streams, and warranty claim records into Microsoft Fabric, automating predictive maintenance on safety-critical truck couplings and accelerating global R&D cycle times.",
        "what_microsoft_solves": "Centralize global manufacturing telemetry, drawbar stress-sensor IoT streams, and warranty claim records into Microsoft Fabric, automating predictive maintenance on safety-critical truck couplings and accelerating global R&D cycle times.",
        "trend_macro": "Commercial vehicle electrification and autonomous platooning requiring sensorized drawbars and certified coupling safety data.",
        "trend_competitors": "Commercial vehicle equipment innovators (Jost Werke, SAF-Holland) introducing sensorized smart fifth wheels and drawbars.",
        "trend_legacy_debt": "Fragmented divisional ERPs (VBG, Ringfeder, Mobile Climate Control) and on-premise test bench databases.",
        "fomo_cost_of_inaction": "Safety recall liability risk and lost commercial vehicle OEM tenders if drawbar fatigue telemetry is not analyzed continuously.",
        "fomo_peer_velocity": "Leading axle and coupling OEMs provide predictive fatigue alerts to fleet operators; VBG relies on scheduled physical inspections.",
        "fomo_vendor_traps": "Isolated test bench software charging steep export fees to integrate with enterprise cloud analytics.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,300,000",
        "payback_months": 7,
        "investment_eur": "€480,000",
        "three_year_net_value_eur": "€6,420,000",
        "key_questions": [
            {
                "target": "VP Truck Equipment",
                "question": "Can your engineers stream real-time strain-gauge data from road-tested truck couplings directly into an Azure analysis model?"
            },
            {
                "target": "Head of Quality & Safety",
                "question": "How much time is lost analyzing multi-brand warranty claims across Europe and North America?"
            },
            {
                "target": "Group IT Director",
                "question": "What is your roadmap to harmonize reporting across VBG, Ringfeder, and Mobile Climate Control?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Sensorized Commercial Vehicle Coupling Telemetry",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Ingesting drawbar strain gauge and coupling angle sensor feeds into Fabric Real-Time Hub for fatigue life analysis.",
                "architecture": "Fabric Real-Time Intelligence + Azure IoT Hub + Eventstream"
            },
            {
                "title": "Divisional ERP Harmonization & OneLake Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Harmonizing operational metrics across VBG, Ringfeder, and MCC into a unified OneLake model.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Warranty Claim Analysis & Quality Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant extracting failure symptoms and vehicle mileage from international dealer warranty claims.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Dynamics 365"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "austrotherm"
        ]
    },
    "CORRAL PETROLEUM HOLDINGS AB": {
        "org_nr": "556525-4124",
        "tpid": "104432063",
        "industry": "Renewable Fuel Refining, Petrochemicals & Nordic Fuel Distribution",
        "what_partner_solves": "Consolidate refinery DCS process historians (AspenTech, OSIsoft PI), maritime crude/biofuel blending logs, and retail station pump streams into Microsoft Fabric and Azure Data Factory, enabling real-time margin optimization on bio-feedstocks, refinery flare reduction, and mandatory EU ETS carbon compliance.",
        "what_databricks_solves": "Consolidate refinery DCS process historians (AspenTech, OSIsoft PI), maritime crude/biofuel blending logs, and retail station pump streams into Microsoft Fabric and Azure Data Factory, enabling real-time margin optimization on bio-feedstocks, refinery flare reduction, and mandatory EU ETS carbon compliance.",
        "what_microsoft_solves": "Consolidate refinery DCS process historians (AspenTech, OSIsoft PI), maritime crude/biofuel blending logs, and retail station pump streams into Microsoft Fabric and Azure Data Factory, enabling real-time margin optimization on bio-feedstocks, refinery flare reduction, and mandatory EU ETS carbon compliance.",
        "trend_macro": "Sweeping energy transition transforming Sweden's largest refineries into renewable diesel (HVO) and sustainable aviation fuel (SAF) production giants.",
        "trend_competitors": "European renewable fuel leaders (Neste, St1) leveraging cloud data platforms to optimize refinery yields and trading margins.",
        "trend_legacy_debt": "Massive on-premise AspenTech / OSIsoft PI historian databases isolated from corporate enterprise ERP systems.",
        "fomo_cost_of_inaction": "Multi-million kronor refining margin leakage during crude/bio-feedstock switching and severe EU ETS non-compliance penalties.",
        "fomo_peer_velocity": "Leading refiners calculate real-time crack spreads hourly; Preem process engineers wait for end-of-month yield accounting.",
        "fomo_vendor_traps": "Costly proprietary industrial historian maintenance and fragmented on-premise data warehouses.",
        "tco_reduction_pct": 47,
        "compute_savings_pct": 65,
        "productivity_lift_multiplier": "4.1x",
        "annual_savings_eur": "€6,500,000",
        "payback_months": 5,
        "investment_eur": "€1,100,000",
        "three_year_net_value_eur": "€18,400,000",
        "key_questions": [
            {
                "target": "VP Refining Operations",
                "question": "How quickly do your process engineers correlate bio-feedstock impurities with catalytic hydrocracker catalyst deactivation?"
            },
            {
                "target": "Chief Commercial Officer",
                "question": "Can you calculate real-time refining crack spreads across fossil and renewable fuels hourly instead of end-of-month?"
            },
            {
                "target": "CIO",
                "question": "What is your strategy to integrate OT historian sensor streams with Azure Fabric without breaching NIS2 cybersecurity standards?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft ECIF co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Real-Time Refinery Process Historian & Yield Mesh",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming 100,000 refinery temperature, pressure, and flow sensors from AspenTech/PI into Fabric Real-Time Hub.",
                "architecture": "Azure IoT Edge + Fabric Real-Time Intelligence + Eventstream"
            },
            {
                "title": "Renewable Biofuel Blending & Crack Margin Optimization",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models forecasting optimal biofuel blending ratios to maximize margins and meet EU RED III mandates.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Sovereign Industrial OT Cybersecurity & NIS2 Lineage",
                "category": "Unified BI & Direct Lake",
                "description": "Microsoft Purview data governance providing cryptographic lineage for EU ETS carbon emission verification.",
                "architecture": "Microsoft Purview + Azure Sentinel + Sovereign Azure"
            }
        ],
        "matched_cases": [
            "fluvius",
            "austrotherm"
        ]
    },
    "Recipharm AB": {
        "org_nr": "556498-8425",
        "tpid": "9713231",
        "industry": "Global Pharmaceutical CDMO (Contract Development & Manufacturing)",
        "what_partner_solves": "Ingest batch production records, cleanroom environmental sensor telemetry, and sterile fill-finish quality inspection streams into Microsoft Fabric with GxP and 21 CFR Part 11 compliant audit trails in Microsoft Purview, cutting batch release cycle times from 14 days to under 48 hours.",
        "what_databricks_solves": "Ingest batch production records, cleanroom environmental sensor telemetry, and sterile fill-finish quality inspection streams into Microsoft Fabric with GxP and 21 CFR Part 11 compliant audit trails in Microsoft Purview, cutting batch release cycle times from 14 days to under 48 hours.",
        "what_microsoft_solves": "Ingest batch production records, cleanroom environmental sensor telemetry, and sterile fill-finish quality inspection streams into Microsoft Fabric with GxP and 21 CFR Part 11 compliant audit trails in Microsoft Purview, cutting batch release cycle times from 14 days to under 48 hours.",
        "trend_macro": "Global biopharma supply chain agility requirements; stringent FDA/EMA compliance demanding digital batch records.",
        "trend_competitors": "Global pharmaceutical CDMOs (Lonza, Catalent) investing heavily in paperless Pharma 4.0 cloud manufacturing suites.",
        "trend_legacy_debt": "Disparate manufacturing execution systems (MES), paper-based batch records, and isolated SCADA systems across 30 global sites.",
        "fomo_cost_of_inaction": "Quarantined pharmaceutical batches worth millions stuck in quality review; regulatory inspection warning letters.",
        "fomo_peer_velocity": "Competitors release sterile batches within 48 hours of fill-finish; Recipharm quality teams take up to 14 days of manual review.",
        "fomo_vendor_traps": "Proprietary electronic batch record systems with rigid licensing and high custom integration costs.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€3,200,000",
        "payback_months": 6,
        "investment_eur": "€620,000",
        "three_year_net_value_eur": "€8,980,000",
        "key_questions": [
            {
                "target": "Global Head of Quality",
                "question": "What is your average batch release cycle time across sterile manufacturing sites, and how much finished inventory is trapped in quarantine?"
            },
            {
                "target": "Operations Director",
                "question": "How do you detect environmental cleanroom humidity and particulate excursions before a batch is ruined?"
            },
            {
                "target": "CIO",
                "question": "How do you validate cloud analytics environments for GxP and 21 CFR Part 11 compliance with Microsoft?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "GxP-Validated Batch Release & Cleanroom Telemetry",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating cleanroom particle counters, autoclave logs, and fill-finish sensor streams into a validated OneLake environment.",
                "architecture": "Microsoft Fabric OneLake + Microsoft Purview + Data Factory"
            },
            {
                "title": "Sterile Fill-Finish Yield & Anomaly Detection",
                "category": "Unified BI & Direct Lake",
                "description": "Machine learning models detecting fill volume drift and vial seal defects before terminal sterilization.",
                "architecture": "Azure Machine Learning + Power BI Direct Lake + Fabric"
            },
            {
                "title": "Pharma Regulatory Submission & Deviation Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant drafting deviation investigation reports and summarizing batch records for QP sign-off.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Quality Portal"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "ggz-rivierduinen"
        ]
    },
    "Dellner Invest AB": {
        "org_nr": "556788-0629",
        "tpid": "17903621",
        "industry": "Railway Rolling Stock Systems, Automatic Couplers & Crash Energy Management",
        "what_partner_solves": "Ingest coupler sensor telemetry (load, vibration, wear metrics) from high-speed passenger trains into Microsoft Fabric Real-Time Intelligence, enabling condition-based predictive train overhaul scheduling, reducing costly out-of-service rolling stock delays, and optimizing rail spare parts logistics.",
        "what_databricks_solves": "Ingest coupler sensor telemetry (load, vibration, wear metrics) from high-speed passenger trains into Microsoft Fabric Real-Time Intelligence, enabling condition-based predictive train overhaul scheduling, reducing costly out-of-service rolling stock delays, and optimizing rail spare parts logistics.",
        "what_microsoft_solves": "Ingest coupler sensor telemetry (load, vibration, wear metrics) from high-speed passenger trains into Microsoft Fabric Real-Time Intelligence, enabling condition-based predictive train overhaul scheduling, reducing costly out-of-service rolling stock delays, and optimizing rail spare parts logistics.",
        "trend_macro": "High-speed rail expansion in Europe; train operators demanding availability-based maintenance contracts and zero unplanned outages.",
        "trend_competitors": "Global rail technology leaders (Voith Turbo, Wabtec) offering digital train monitoring platforms.",
        "trend_legacy_debt": "Disconnected test bench logs, manual field inspection reports, and legacy ERP databases.",
        "fomo_cost_of_inaction": "High rail operator penalty fees for unpredicted coupler failure resulting in passenger train cancellations.",
        "fomo_peer_velocity": "Competitors offer train builders real-time coupler stress dashboards; Dellner relies on periodic field service overhauls.",
        "fomo_vendor_traps": "Proprietary condition monitoring software with rigid licensing and lack of integration with train builder IoT systems.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 53,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,900,000",
        "payback_months": 7,
        "investment_eur": "€410,000",
        "three_year_net_value_eur": "€5,290,000",
        "key_questions": [
            {
                "target": "Head of Aftermarket & Service",
                "question": "How can you transition European rail operators from fixed-interval coupler overhauls to condition-based servicing?"
            },
            {
                "target": "Chief Engineer",
                "question": "How do you capture stress telemetry during high-speed train coupling impacts to optimize coupler head longevity?"
            },
            {
                "target": "CIO",
                "question": "What is your strategy to provide digital fleet dashboards to train builders like Alstom and Siemens?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Railway Coupler Real-Time Telemetry & Fatigue Hub",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Ingesting train coupler load cell, draft gear displacement, and vibration sensor feeds into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Intelligence + Azure IoT Edge + KQL"
            },
            {
                "title": "Predictive Rolling Stock Maintenance Models",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models predicting wear on coupler pivot pins and rubber draft gear springs.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Rail Engineering Specification Search Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant interrogating rail safety certifications (EN 15085, TSI) and engineering CAD files.",
                "architecture": "Azure OpenAI Service + Azure AI Search + SharePoint"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "austrotherm"
        ]
    },
    "Swedish Orphan Biovitrum": {
        "org_nr": "556038-9321",
        "tpid": "5082273",
        "industry": "Biopharmaceuticals & Rare Disease Therapeutics (Haemophilia, Immunology)",
        "what_partner_solves": "Consolidate global patient registry insights, cold-chain biologic distribution telemetry, and clinical trial outcomes into a secure Microsoft Fabric Lakehouse with Purview zero-trust governance, accelerating orphan drug market access, optimizing clinical trial supply allocation, and satisfying FDA/EMA real-world evidence demands.",
        "what_databricks_solves": "Consolidate global patient registry insights, cold-chain biologic distribution telemetry, and clinical trial outcomes into a secure Microsoft Fabric Lakehouse with Purview zero-trust governance, accelerating orphan drug market access, optimizing clinical trial supply allocation, and satisfying FDA/EMA real-world evidence demands.",
        "what_microsoft_solves": "Consolidate global patient registry insights, cold-chain biologic distribution telemetry, and clinical trial outcomes into a secure Microsoft Fabric Lakehouse with Purview zero-trust governance, accelerating orphan drug market access, optimizing clinical trial supply allocation, and satisfying FDA/EMA real-world evidence demands.",
        "trend_macro": "Increasing global regulatory pressure for real-world evidence (RWE); ultra-stringent cold chain controls for expensive biologic therapies.",
        "trend_competitors": "Global rare disease biopharmas (BioMarin, Sanofi, Takeda) accelerating orphan drug clinical trials with cloud data mesh platforms.",
        "trend_legacy_debt": "Disparate global CRO datasets, siloed clinical databases, and strict health data privacy boundaries across Europe and North America.",
        "fomo_cost_of_inaction": "Months of clinical trial recruitment delays and millions lost in patient therapy access due to fragmented clinical registry data.",
        "fomo_peer_velocity": "Competitors pool real-world patient data dynamically; Sobi clinical teams wait months for manual data harmonization across clinical sites.",
        "fomo_vendor_traps": "Proprietary clinical trial management software with exorbitant fees for custom data extraction and cross-trial analytics.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 61,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€3,600,000",
        "payback_months": 6,
        "investment_eur": "€650,000",
        "three_year_net_value_eur": "€10,150,000",
        "key_questions": [
            {
                "target": "Chief Medical Officer",
                "question": "How do you pool rare disease patient registries across 30 countries to demonstrate real-world treatment efficacy to reimbursement authorities?"
            },
            {
                "target": "Head of Supply Chain",
                "question": "Can you track cold-chain temperature telemetry in real time from factory to patient infusion for high-value biologics?"
            },
            {
                "target": "CISO / DPO",
                "question": "How do you maintain patient pseudonymization and HIPAA/GDPR compliance across cloud analytics?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Rare Disease Real-World Evidence & Registry Lakehouse",
                "category": "Enterprise SaaS Data Fabric",
                "description": "OneLake data mesh integrating de-identified patient registries, genomic markers, and clinical trial outcomes.",
                "architecture": "Microsoft Fabric OneLake + Microsoft Purview + Azure Synapse"
            },
            {
                "title": "Biologic Cold-Chain Integrity Telemetry",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming IoT temperature and GPS logger telemetry from international biologic shipments into Fabric Eventstream.",
                "architecture": "Fabric Real-Time Hub + Azure IoT Hub + Eventstream"
            },
            {
                "title": "Clinical Trial Protocol & Literature Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant analyzing rare disease clinical protocols, trial endpoints, and medical literature.",
                "architecture": "Azure OpenAI Service + Azure AI Search + SharePoint"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "cera"
        ]
    },
    "EQT Holdings AB": {
        "org_nr": "556849-4180",
        "tpid": "17826489",
        "industry": "Global Private Capital & Alternative Asset Management",
        "what_partner_solves": "Unify disparate portfolio company financial reporting, ESG carbon footprint disclosures, and pipeline deal metrics from hundreds of portfolio assets into Microsoft Fabric OneLake and Azure OpenAI, enabling near-instant cross-portfolio value creation analytics, LP institutional reporting, and AI-powered investment screening.",
        "what_databricks_solves": "Unify disparate portfolio company financial reporting, ESG carbon footprint disclosures, and pipeline deal metrics from hundreds of portfolio assets into Microsoft Fabric OneLake and Azure OpenAI, enabling near-instant cross-portfolio value creation analytics, LP institutional reporting, and AI-powered investment screening.",
        "what_microsoft_solves": "Unify disparate portfolio company financial reporting, ESG carbon footprint disclosures, and pipeline deal metrics from hundreds of portfolio assets into Microsoft Fabric OneLake and Azure OpenAI, enabling near-instant cross-portfolio value creation analytics, LP institutional reporting, and AI-powered investment screening.",
        "trend_macro": "LPs demanding institutional-grade real-time ESG metrics; private equity firms competing aggressively on digital transformation and AI value creation in portfolio companies.",
        "trend_competitors": "Global alternative asset giants (Blackstone, KKR) investing hundreds of millions in internal data science and AI platforms to supercharge deal sourcing.",
        "trend_legacy_debt": "Disparate portfolio company ERPs, monthly Excel data packs, and fragmented deal management databases.",
        "fomo_cost_of_inaction": "Missing out on proprietary deal sourcing and losing weeks in quarterly LP reporting while peers provide real-time digital LP portals.",
        "fomo_peer_velocity": "Competitors evaluate acquisition targets using AI in 24 hours; EQT investment associates spend days on manual financial data re-formatting.",
        "fomo_vendor_traps": "Third-party private equity data tools with rigid schemas and high annual recurring subscription fees.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 63,
        "productivity_lift_multiplier": "4.3x",
        "annual_savings_eur": "€4,800,000",
        "payback_months": 5,
        "investment_eur": "€750,000",
        "three_year_net_value_eur": "€13,650,000",
        "key_questions": [
            {
                "target": "Global Head of Motherbrain / Data",
                "question": "How quickly can your investment associates interrogate 10,000 historical deal memos and confidential CIMs using sovereign GenAI?"
            },
            {
                "target": "Head of Sustainability",
                "question": "How do you collect and audit Scope 1-3 carbon disclosures across 200+ portfolio companies for EU SFDR reporting?"
            },
            {
                "target": "CFO",
                "question": "Can we automate monthly portfolio EBITDA reconciliation into a unified Fabric OneLake model?"
            },
            {
                "target": "Head of Cyber & Compliance",
                "question": "How do you enforce Chinese walls between competing portfolio company financial data?"
            }
        ],
        "use_cases": [
            {
                "title": "Portfolio Company Financial & ESG OneLake Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Harmonizing monthly financial metrics and carbon accounting across hundreds of portfolio companies in OneLake.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI Direct Lake"
            },
            {
                "title": "Sovereign Deal Sourcing & Due Diligence Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Private, air-gapped generative AI assistant interrogating pitch decks, CIMs, and financial data rooms in Sweden Central.",
                "architecture": "Azure OpenAI Service (Sweden Central) + Azure AI Search RAG"
            },
            {
                "title": "Institutional LP Reporting & SFDR Article 8/9 Engine",
                "category": "Unified BI & Direct Lake",
                "description": "Automated investor reporting calculating portfolio ESG KPIs and value creation bridge metrics in real time.",
                "architecture": "Microsoft Sustainability Manager + Power BI Direct Lake + Fabric"
            }
        ],
        "matched_cases": [
            "cera",
            "austrotherm"
        ]
    },
    "BEIJER ELECTRONICS AB": {
        "org_nr": "556023-0798",
        "tpid": "2009375",
        "industry": "Industrial IoT, Robust Data Communications & HMI Panels",
        "what_partner_solves": "Connect edge device telemetry from mission-critical rail and power utility networks into Microsoft Fabric Real-Time Intelligence, enabling automated network anomaly detection, remote HMI fleet diagnostics, and subscription-based edge management software.",
        "what_databricks_solves": "Connect edge device telemetry from mission-critical rail and power utility networks into Microsoft Fabric Real-Time Intelligence, enabling automated network anomaly detection, remote HMI fleet diagnostics, and subscription-based edge management software.",
        "what_microsoft_solves": "Connect edge device telemetry from mission-critical rail and power utility networks into Microsoft Fabric Real-Time Intelligence, enabling automated network anomaly detection, remote HMI fleet diagnostics, and subscription-based edge management software.",
        "trend_macro": "Rapid modernization of power grid automation and railway signaling requiring robust industrial networking and edge data collection.",
        "trend_competitors": "Industrial networking competitors (Moxa, Advantech, Siemens) bundling hardware with cloud edge management software.",
        "trend_legacy_debt": "Isolated device firmware logs and localized HMI configurations without fleet-wide cloud visibility.",
        "fomo_cost_of_inaction": "Hardware margin compression as competitors transition customers to recurring cloud diagnostic and monitoring contracts.",
        "fomo_peer_velocity": "Competitors offer remote substation network diagnostics in real time; Beijer/Westermo customers rely on on-site technician dispatches.",
        "fomo_vendor_traps": "Fragmented IoT edge software with high licensing costs and lack of integration with enterprise cloud data lakes.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€450,000",
        "three_year_net_value_eur": "€5,850,000",
        "key_questions": [
            {
                "target": "Head of Westermo R&D",
                "question": "How do you monitor network health across 50,000 rugged switches deployed on passenger trains and power substations?"
            },
            {
                "target": "VP Business Development",
                "question": "What is your plan to offer predictive network cybersecurity monitoring as a subscription to rail operators?"
            },
            {
                "target": "Group CIO",
                "question": "How do you streamline telemetry ingestion from edge devices into Microsoft Azure without overloading cellular bandwidth?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Industrial Network & Rail Telemetry Fabric",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming Westermo switch port telemetry, jitter, and link status into Fabric Real-Time Hub.",
                "architecture": "Azure IoT Operations + Fabric Real-Time Hub + KQL Eventhouse"
            },
            {
                "title": "Edge Fleet Anomaly Detection & Predictive Maintenance",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models forecasting power supply capacitor wear and thermal stress in rugged network equipment.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Industrial Automation Field Support Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping network engineers configure Westermo WeOS network topologies.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Technical Portal"
            }
        ],
        "matched_cases": [
            "fluvius",
            "bridgestone"
        ]
    },
    "DIAB AB": {
        "org_nr": "556276-8092",
        "tpid": "4688873",
        "industry": "Composite Core Materials (Divinycell) for Wind Energy, Marine & Aerospace",
        "what_partner_solves": "Ingest foam extrusion sensor feeds, resin absorption test logs, and blade manufacturer supply chain forecasts into Microsoft Fabric, optimizing chemical density uniformity, reducing material scrap by 12%, and automating Scope 3 product carbon declarations for wind energy turbine OEMs (Vestas, Siemens Gamesa).",
        "what_databricks_solves": "Ingest foam extrusion sensor feeds, resin absorption test logs, and blade manufacturer supply chain forecasts into Microsoft Fabric, optimizing chemical density uniformity, reducing material scrap by 12%, and automating Scope 3 product carbon declarations for wind energy turbine OEMs (Vestas, Siemens Gamesa).",
        "what_microsoft_solves": "Ingest foam extrusion sensor feeds, resin absorption test logs, and blade manufacturer supply chain forecasts into Microsoft Fabric, optimizing chemical density uniformity, reducing material scrap by 12%, and automating Scope 3 product carbon declarations for wind energy turbine OEMs (Vestas, Siemens Gamesa).",
        "trend_macro": "Global offshore wind turbine scaling (15MW+ turbines) requiring structural foam with zero voids and certified low carbon intensity.",
        "trend_competitors": "Composite core materials competitors (Gurit, Armacell) deploying cloud manufacturing controls to lower PET/balsa scrap rates.",
        "trend_legacy_debt": "Disconnected factory extrusion PLC systems and laboratory shear-testing databases with delayed feedback.",
        "fomo_cost_of_inaction": "High material scrap rates eroding gross margins and failure to meet strict wind turbine OEM circularity targets.",
        "fomo_peer_velocity": "Competitors predict composite foam density drift during extrusion; DIAB relies on destructive sample cutting post-cure.",
        "fomo_vendor_traps": "Isolated laboratory testing software with no connection to central enterprise ERP systems.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 7,
        "investment_eur": "€470,000",
        "three_year_net_value_eur": "€6,130,000",
        "key_questions": [
            {
                "target": "Head of Operations",
                "question": "How much composite foam scrap is generated each month due to foam density drift during extrusion?"
            },
            {
                "target": "Global Quality Director",
                "question": "Can you provide automated batch-level structural certification data to wind turbine blade builders?"
            },
            {
                "target": "Group CIO",
                "question": "How do you synchronize production metrics across Sweden, Italy, US, and China manufacturing plants?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Composite Foam Extrusion Yield & Density Optimization",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating chemical blowing agent flow, extruder temperature, and dielectric foam density into OneLake.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Circular Material Passports for Wind OEMs",
                "category": "Unified BI & Direct Lake",
                "description": "Automated batch-level carbon and recycled content certificates meeting Vestas and Siemens Gamesa requirements.",
                "architecture": "Microsoft Sustainability Manager + Power BI Direct Lake"
            },
            {
                "title": "Global Plant Quality Telemetry Mesh",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Real-time streaming of ultrasonic quality test logs from global manufacturing plants into Fabric.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "New Wave Group AB": {
        "org_nr": "556334-8285",
        "tpid": "7079514",
        "industry": "Corporate Promo, Premium Apparel & Craft Sportswear",
        "what_partner_solves": "Unify omni-channel retail POS streams, B2B promotional distributor orders, and automated warehouse robotics telemetry into Microsoft Fabric, eliminating inventory markdowns, synchronizing international distribution hubs, and providing real-time stock availability to 10,000+ corporate resellers.",
        "what_databricks_solves": "Unify omni-channel retail POS streams, B2B promotional distributor orders, and automated warehouse robotics telemetry into Microsoft Fabric, eliminating inventory markdowns, synchronizing international distribution hubs, and providing real-time stock availability to 10,000+ corporate resellers.",
        "what_microsoft_solves": "Unify omni-channel retail POS streams, B2B promotional distributor orders, and automated warehouse robotics telemetry into Microsoft Fabric, eliminating inventory markdowns, synchronizing international distribution hubs, and providing real-time stock availability to 10,000+ corporate resellers.",
        "trend_macro": "E-commerce direct-to-consumer growth combined with volatile seasonal B2B promotional cycles; high working capital locked in warehouse apparel stock.",
        "trend_competitors": "Global activewear and promo apparel giants (VF Corp, Amer Sports) optimizing omni-channel inventory allocation using cloud demand sensing.",
        "trend_legacy_debt": "Multiple ERP instances across European subsidiaries and legacy warehouse batch management systems.",
        "fomo_cost_of_inaction": "Stockouts of core Craft athletic lines during peak marathon seasons alongside costly end-of-season promo inventory write-offs.",
        "fomo_peer_velocity": "Competitors allocate apparel stock dynamically based on weather and race registrations; New Wave Group relies on static seasonal pre-orders.",
        "fomo_vendor_traps": "Costly custom EDI scripts connecting regional warehouse management systems with high maintenance overhead.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€3,100,000",
        "payback_months": 6,
        "investment_eur": "€580,000",
        "three_year_net_value_eur": "€8,720,000",
        "key_questions": [
            {
                "target": "CEO / COO",
                "question": "How much working capital could be unlocked by reducing safety stock buffers across European central warehouses by 15%?"
            },
            {
                "target": "Head of E-commerce",
                "question": "Can corporate promotional dealers check real-time inventory and delivery dates instantly via API during bulk orders?"
            },
            {
                "target": "Group CIO",
                "question": "What is your roadmap to replace legacy batch reporting with Microsoft Fabric OneLake Direct Lake dashboards?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Omni-Channel Demand Sensing & Stock Allocation",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating retail POS feeds, B2B pre-orders, and e-commerce baskets into OneLake to forecast regional apparel demand.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "B2B Reseller Real-Time Inventory & Price Fabric",
                "category": "Unified BI & Direct Lake",
                "description": "Sub-second stock availability and tiered volume pricing served to 10,000+ corporate promotional distributors.",
                "architecture": "Fabric Real-Time Hub + Power BI Direct Lake + Azure API Management"
            },
            {
                "title": "Multilingual Product Marketing & B2B RFQ Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant drafting localized product descriptions and extracting bulk orders from customer RFQs.",
                "architecture": "Azure OpenAI Service + Azure AI Document Intelligence"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "austrotherm"
        ]
    },
    "POLYPEPTIDE LABORATORIES SWEDEN A": {
        "org_nr": "556232-2718",
        "tpid": "17082848",
        "industry": "Custom Peptide Synthesis & Biologics CDMO",
        "what_partner_solves": "Integrate high-performance liquid chromatography (HPLC) analytical runs, solid-phase peptide synthesizer telemetry, and GMP environmental records into Microsoft Fabric, predicting peptide synthesis yield degradation, automating chromatographic peak analysis, and streamlining batch record release.",
        "what_databricks_solves": "Integrate high-performance liquid chromatography (HPLC) analytical runs, solid-phase peptide synthesizer telemetry, and GMP environmental records into Microsoft Fabric, predicting peptide synthesis yield degradation, automating chromatographic peak analysis, and streamlining batch record release.",
        "what_microsoft_solves": "Integrate high-performance liquid chromatography (HPLC) analytical runs, solid-phase peptide synthesizer telemetry, and GMP environmental records into Microsoft Fabric, predicting peptide synthesis yield degradation, automating chromatographic peak analysis, and streamlining batch record release.",
        "trend_macro": "Surging global demand for GLP-1 peptide therapeutics (diabetes and weight loss); stringent GMP purity requirements exceeding 99.5%.",
        "trend_competitors": "Global peptide CDMOs (Bachem, CordenPharma) investing heavily in continuous peptide manufacturing and digital lab automation.",
        "trend_legacy_debt": "Terabytes of disconnected chromatography data systems (Empower, Chromeleon) with manual peak integration reviews.",
        "fomo_cost_of_inaction": "Delayed batch release for commercial GLP-1 peptides and yield loss during solid-phase synthesis costing hundreds of thousands per run.",
        "fomo_peer_velocity": "Competitors automate chromatographic peak integration in seconds; PolyPeptide quality analysts manually integrate curves.",
        "fomo_vendor_traps": "Proprietary chromatography data systems charging steep fees for open API access and data lake export.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.7x",
        "annual_savings_eur": "€2,400,000",
        "payback_months": 6,
        "investment_eur": "€490,000",
        "three_year_net_value_eur": "€6,710,000",
        "key_questions": [
            {
                "target": "VP Operations",
                "question": "What is your current peptide synthesis yield variance, and how do you detect incomplete amino acid coupling in real time?"
            },
            {
                "target": "Quality Director",
                "question": "How many days are spent manually reviewing chromatographic peak integration data before batch sign-off?"
            },
            {
                "target": "Head of IT",
                "question": "How do you enforce 21 CFR Part 11 electronic signature and audit trail integrity across cloud data analytics?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Automated Chromatographic Peak Analysis & Yield Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating HPLC ultraviolet absorbance spectra and mass spectrometry runs into OneLake for automated purity scoring.",
                "architecture": "Microsoft Fabric OneLake + Azure Machine Learning + Data Factory"
            },
            {
                "title": "21 CFR Part 11 Sovereign GxP Audit Lineage",
                "category": "Unified BI & Direct Lake",
                "description": "Cryptographic tamper-evident audit trails and electronic signature verification in Microsoft Purview for FDA audits.",
                "architecture": "Microsoft Purview + Azure Confidential Computing + Power BI"
            },
            {
                "title": "Peptide Synthesis Chemistry Knowledge Assistant",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant interrogating chemical reaction parameters, solvent washing protocols, and cleavage recipes.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Lab Portal"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "ggz-rivierduinen"
        ]
    },
    "Consilium AB": {
        "org_nr": "556555-4085",
        "tpid": "8265045",
        "industry": "Fire, Flame & Gas Safety Systems for Marine, Energy & Transport",
        "what_partner_solves": "Ingest live sensor telemetry and annual inspection logs from tens of thousands of vessel fire detection systems into Microsoft Fabric Real-Time Intelligence, enabling predictive sensor calibration, automated maritime safety compliance certification (IMO/SOLAS), and remote digital service contracts.",
        "what_databricks_solves": "Ingest live sensor telemetry and annual inspection logs from tens of thousands of vessel fire detection systems into Microsoft Fabric Real-Time Intelligence, enabling predictive sensor calibration, automated maritime safety compliance certification (IMO/SOLAS), and remote digital service contracts.",
        "what_microsoft_solves": "Ingest live sensor telemetry and annual inspection logs from tens of thousands of vessel fire detection systems into Microsoft Fabric Real-Time Intelligence, enabling predictive sensor calibration, automated maritime safety compliance certification (IMO/SOLAS), and remote digital service contracts.",
        "trend_macro": "International Maritime Organization (IMO) pushing for digitalized safety systems and remote maritime survey validation.",
        "trend_competitors": "Global fire and safety leaders (Honeywell Building Technologies, Johnson Controls) building cloud-connected maritime safety platforms.",
        "trend_legacy_debt": "Disconnected on-vessel voyage data recorders and localized fire panel archives without fleet-wide cloud synchronization.",
        "fomo_cost_of_inaction": "Unscheduled port detention of commercial cargo ships by maritime port authorities due to uncertified fire detector faults.",
        "fomo_peer_velocity": "Competitors offer shipowners real-time fire detection health portals; Consilium relies on physical annual technician visits.",
        "fomo_vendor_traps": "Proprietary panel firmware with high custom development costs to export operational telemetry.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€6,140,000",
        "key_questions": [
            {
                "target": "President Marine Safety",
                "question": "How can you turn annual safety inspection hardware sales into recurring digital maritime safety monitoring contracts?"
            },
            {
                "target": "Head of Global Service",
                "question": "Can shipowners monitor the sensor calibration status of 500 fire detectors across their fleet from a single cloud screen?"
            },
            {
                "target": "CIO",
                "question": "What is your architecture to securely ingest marine satellite telemetry without exorbitant airtime bandwidth fees?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Marine Safety Fleet Telemetry & Fault Hub",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Ingesting smoke obscuration, temperature, and gas sensor telemetry from connected vessels into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Intelligence + Azure IoT Hub + Eventstream"
            },
            {
                "title": "IMO/SOLAS Compliance Certification Engine",
                "category": "Unified BI & Direct Lake",
                "description": "Automated compliance reports verifying fire detector operational readiness for maritime port state control inspectors.",
                "architecture": "Microsoft Fabric OneLake + Power BI Direct Lake"
            },
            {
                "title": "Maritime Safety Regulation & Service Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping field service engineers interpret flag state safety rules and panel wiring schematics.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Service App"
            }
        ],
        "matched_cases": [
            "fluvius",
            "bridgestone"
        ]
    },
    "DACKE PMC HOLDING AB": {
        "org_nr": "556608-2516",
        "tpid": "10356829",
        "industry": "Industrial Engineering, Hydraulics & Motion Technology Holding",
        "what_partner_solves": "Harmonize monthly financial consolidation, ERP operational metrics, and factory capacity utilization across 20+ decentralized Nordic engineering subsidiaries into Microsoft Fabric OneLake, cutting group financial close time from 12 days to 3 days while retaining subsidiary autonomy.",
        "what_databricks_solves": "Harmonize monthly financial consolidation, ERP operational metrics, and factory capacity utilization across 20+ decentralized Nordic engineering subsidiaries into Microsoft Fabric OneLake, cutting group financial close time from 12 days to 3 days while retaining subsidiary autonomy.",
        "what_microsoft_solves": "Harmonize monthly financial consolidation, ERP operational metrics, and factory capacity utilization across 20+ decentralized Nordic engineering subsidiaries into Microsoft Fabric OneLake, cutting group financial close time from 12 days to 3 days while retaining subsidiary autonomy.",
        "trend_macro": "Private equity holding models requiring rapid subsidiary onboarding and unified group visibility without heavy monolithic ERPs.",
        "trend_competitors": "Decentralized industrial conglomerates (Indutrade, Lifco) leveraging agile cloud data lakes to benchmark subsidiary operating margins.",
        "trend_legacy_debt": "20+ distinct ERP systems (Visma, Monitor, Jeeves, Business Central, IFS) with manual spreadsheet consolidation each month.",
        "fomo_cost_of_inaction": "Inability to benchmark subsidiary factory capacity, margin leakage, and procurement synergies across the group.",
        "fomo_peer_velocity": "Competitors benchmark subsidiary EBITDA margins and machine utilization in real time; Dacke executives wait weeks for monthly accounts.",
        "fomo_vendor_traps": "Extensive licensing for legacy financial consolidation software with heavy manual data loading.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 51,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,800,000",
        "payback_months": 7,
        "investment_eur": "€390,000",
        "three_year_net_value_eur": "€5,010,000",
        "key_questions": [
            {
                "target": "Group CFO",
                "question": "How many business days does your finance team spend consolidating monthly P&L and balance sheets from 20 operating companies?"
            },
            {
                "target": "Head of Operational Excellence",
                "question": "Can you compare machine capacity utilization and energy intensity across all hydraulic manufacturing plants?"
            },
            {
                "target": "Group IT Director",
                "question": "How quickly can you onboard a newly acquired engineering business into your group reporting fabric?"
            },
            {
                "target": "CEO",
                "question": "What is the uncaptured volume procurement synergy potential across your 20 subsidiaries?"
            }
        ],
        "use_cases": [
            {
                "title": "Multi-Entity Financial & Operational OneLake Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating 20+ subsidiary ERPs into OneLake to deliver automated group financial consolidation in 3 days.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Cross-Subsidiary Procurement Synergy Analytics",
                "category": "Unified BI & Direct Lake",
                "description": "Analyzing raw steel, hydraulic hose, and electronic component purchases across subsidiaries to unlock bulk discounts.",
                "architecture": "Microsoft Fabric Lakehouse + Power BI Direct Lake"
            },
            {
                "title": "M&A Operational Due Diligence & Onboarding Mesh",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant extracting contract terms and financial ratios from acquired company documents during onboarding.",
                "architecture": "Azure OpenAI Service + Azure AI Document Intelligence + Purview"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "cera"
        ]
    },
    "Karo Pharma AB": {
        "org_nr": "556288-8239",
        "tpid": "37654486",
        "industry": "European Consumer Healthcare, Over-the-Counter & Prescription Dermatology",
        "what_partner_solves": "Integrate European pharmacy sell-out data, contract manufacturing delivery feeds, and promotional marketing analytics into Microsoft Fabric, establishing an automated cross-border demand sensing hub that prevents pharmacy out-of-stocks and tracks pan-European brand profitability.",
        "what_databricks_solves": "Integrate European pharmacy sell-out data, contract manufacturing delivery feeds, and promotional marketing analytics into Microsoft Fabric, establishing an automated cross-border demand sensing hub that prevents pharmacy out-of-stocks and tracks pan-European brand profitability.",
        "what_microsoft_solves": "Integrate European pharmacy sell-out data, contract manufacturing delivery feeds, and promotional marketing analytics into Microsoft Fabric, establishing an automated cross-border demand sensing hub that prevents pharmacy out-of-stocks and tracks pan-European brand profitability.",
        "trend_macro": "E-pharmacy expansion across Europe; rapid acquisition of legacy consumer health brands requiring fast commercial integration.",
        "trend_competitors": "European consumer health innovators (Perrigo, Stada) streamlining international distribution networks with cloud data platforms.",
        "trend_legacy_debt": "Disconnected distributor databases, disparate EDI feeds, and localized promotional spreadsheets.",
        "fomo_cost_of_inaction": "Lost pharmacy shelf space and distributor penalties when high-demand OTC medications face stockouts during winter peaks.",
        "fomo_peer_velocity": "Competitors predict pharmacy OTC sell-out trends weekly; Karo Pharma relies on monthly lagging wholesaler reports.",
        "fomo_vendor_traps": "Costly custom data aggregation services charging high monthly fees for distributor sell-out harmonization.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,500,000",
        "payback_months": 6,
        "investment_eur": "€510,000",
        "three_year_net_value_eur": "€7,010,000",
        "key_questions": [
            {
                "target": "Commercial Director Europe",
                "question": "What is your visibility into daily pharmacy sell-out rates across Germany, the Nordics, and the UK?"
            },
            {
                "target": "Supply Chain VP",
                "question": "How do you align contract manufacturer production schedules with volatile consumer health demand spikes?"
            },
            {
                "target": "Group CIO",
                "question": "What is your strategy to create a scalable analytics backbone that supports continuous brand acquisitions?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Pan-European Pharmacy Sell-Out Demand Sensing",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating wholesaler POS feeds and e-pharmacy orders into OneLake to forecast weekly pharmacy replenishments.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure Synapse"
            },
            {
                "title": "Cross-Border Brand Margin & Promotion ROI Fabric",
                "category": "Unified BI & Direct Lake",
                "description": "Real-time tracking of marketing campaign spend against regional OTC brand sell-out velocity in Power BI Direct Lake.",
                "architecture": "Power BI Direct Lake + Azure Machine Learning + Fabric"
            },
            {
                "title": "Regulatory Package Leaflet & Label Review Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant checking multi-country pharmaceutical packaging labels and leaflets against local health authority rules.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Regulatory Portal"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "bridgestone"
        ]
    },
    "Lagerstedt & Krantz AB": {
        "org_nr": "556040-9723",
        "tpid": "3358873",
        "industry": "Heating, Plumbing, Underfloor Climate Systems & Prefabricated Manifolds",
        "what_partner_solves": "Consolidate IoT telemetry from smart manifold controllers, BIM prefabricated pipe design models, and warehouse inventory into Microsoft Fabric, delivering dynamic HVAC energy optimization algorithms to commercial real estate builders and automating custom prefab manifold production orders.",
        "what_databricks_solves": "Consolidate IoT telemetry from smart manifold controllers, BIM prefabricated pipe design models, and warehouse inventory into Microsoft Fabric, delivering dynamic HVAC energy optimization algorithms to commercial real estate builders and automating custom prefab manifold production orders.",
        "what_microsoft_solves": "Consolidate IoT telemetry from smart manifold controllers, BIM prefabricated pipe design models, and warehouse inventory into Microsoft Fabric, delivering dynamic HVAC energy optimization algorithms to commercial real estate builders and automating custom prefab manifold production orders.",
        "trend_macro": "Nordic green building standards (Miljöbyggnad, BREEAM) demanding smart hydronic heating optimization and low embodied carbon piping.",
        "trend_competitors": "European HVAC and plumbing leaders (Uponor, Danfoss) integrating smart heating controls with cloud energy management suites.",
        "trend_legacy_debt": "Siloed BIM engineering files, disconnected manifold factory PLCs, and legacy ERP order databases.",
        "fomo_cost_of_inaction": "Missing out on large-scale prefab modular construction tenders that demand digital BIM integration and carbon documentation.",
        "fomo_peer_velocity": "Competitors generate automated prefab manufacturing orders from BIM files in minutes; LK Group engineers spend days on manual takeoffs.",
        "fomo_vendor_traps": "Isolated CAD/CAM software licenses with no connection to enterprise ERP or cloud telemetry platforms.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 54,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,700,000",
        "payback_months": 7,
        "investment_eur": "€380,000",
        "three_year_net_value_eur": "€4,720,000",
        "key_questions": [
            {
                "target": "VP Prefab Systems",
                "question": "How long does it take to convert a customer's architectural BIM model into an automated manufacturing order for custom heating manifolds?"
            },
            {
                "target": "Head of R&D",
                "question": "Can your smart underfloor heating controllers stream temperature telemetry to property managers via Azure IoT?"
            },
            {
                "target": "Group CIO",
                "question": "How do you plan to connect factory production scheduling with supplier pipe raw material delivery?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "BIM Prefab Automation & Factory Scheduling Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Extracting dimensional pipe data from customer Revit/IFC models into OneLake to automate manifold factory cutting schedules.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Smart Hydronic Heating Telemetry & Energy Analytics",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming supply/return water temperature and room occupancy data from smart manifolds into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure IoT Hub + KQL"
            },
            {
                "title": "Plumbing & HVAC Product Engineering Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping contractors select compatible pipe fittings, valves, and manifold brackets from technical manuals.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "BIOTAGE SWEDEN AB": {
        "org_nr": "556539-3138",
        "tpid": "4077111",
        "industry": "Life Science Separation, Automated Flash Purification & Flash Chromatography",
        "what_partner_solves": "Harness instrument telemetry from thousands of automated purification systems (Isolera, Extrahera) deployed across pharma labs globally into Microsoft Fabric, enabling predictive consumable replacement alerts (columns, cartridges), remote instrument diagnostics, and automated lab workflow benchmarking.",
        "what_databricks_solves": "Harness instrument telemetry from thousands of automated purification systems (Isolera, Extrahera) deployed across pharma labs globally into Microsoft Fabric, enabling predictive consumable replacement alerts (columns, cartridges), remote instrument diagnostics, and automated lab workflow benchmarking.",
        "what_microsoft_solves": "Harness instrument telemetry from thousands of automated purification systems (Isolera, Extrahera) deployed across pharma labs globally into Microsoft Fabric, enabling predictive consumable replacement alerts (columns, cartridges), remote instrument diagnostics, and automated lab workflow benchmarking.",
        "trend_macro": "Pharmaceutical medicinal chemistry moving toward automated parallel synthesis; research labs demanding connected instrumentation and remote monitoring.",
        "trend_competitors": "Global life science instrumentation leaders (Waters Corporation, Agilent Technologies) building connected laboratory cloud ecosystems.",
        "trend_legacy_debt": "Standalone instrument software without cloud telemetry connectivity; reliance on reactive field service visits.",
        "fomo_cost_of_inaction": "Losing high-margin recurring purification cartridge sales to third-party generic consumable manufacturers.",
        "fomo_peer_velocity": "Competitors alert lab directors when separation cartridges are 90% saturated; Biotage relies on manual lab technician reordering.",
        "fomo_vendor_traps": "Isolated embedded software architectures with high custom development costs to enable cloud telemetry.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,300,000",
        "payback_months": 6,
        "investment_eur": "€480,000",
        "three_year_net_value_eur": "€6,420,000",
        "key_questions": [
            {
                "target": "VP Global Service & Aftermarket",
                "question": "How much recurring revenue could you capture by automatically alerting lab managers when separation cartridges reach 90% saturation?"
            },
            {
                "target": "Head of Hardware R&D",
                "question": "What percentage of customer purification instrument issues could be diagnosed remotely via cloud telemetry?"
            },
            {
                "target": "Group CIO",
                "question": "How do you ensure customer proprietary chemical formulation runs remain air-gapped when streaming instrument health?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Connected Lab Instrument Telemetry & Consumable Sensing",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming solvent pump cycles, optical detector baseline drift, and cartridge pressure drop into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure IoT Hub + Eventstream"
            },
            {
                "title": "Remote Chromatography Diagnostics & Maintenance",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models forecasting UV lamp degradation and seal wear in automated purification instruments.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Lab Method Development & Separation Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping medicinal chemists optimize flash chromatography solvent gradients and column choices.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Scientific Portal"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "austrotherm"
        ]
    },
    "Mannheimer Swartling Advokatbyrå AB": {
        "org_nr": "556399-4499",
        "tpid": "7386242",
        "industry": "Tier-1 Nordic Business Law & Corporate Advisory",
        "what_partner_solves": "Construct a sovereign, hyper-secure legal knowledge intelligence platform on Microsoft Azure OpenAI and Microsoft Fabric with Purview ABAC encryption, enabling automated cross-matter legal research, precedent retrieval, and contract risk scoring within a zero-leakage enterprise perimeter.",
        "what_databricks_solves": "Construct a sovereign, hyper-secure legal knowledge intelligence platform on Microsoft Azure OpenAI and Microsoft Fabric with Purview ABAC encryption, enabling automated cross-matter legal research, precedent retrieval, and contract risk scoring within a zero-leakage enterprise perimeter.",
        "what_microsoft_solves": "Construct a sovereign, hyper-secure legal knowledge intelligence platform on Microsoft Azure OpenAI and Microsoft Fabric with Purview ABAC encryption, enabling automated cross-matter legal research, precedent retrieval, and contract risk scoring within a zero-leakage enterprise perimeter.",
        "trend_macro": "Exponential growth in legal complexity across EU AI Act, CSRD, and FDI sanctions; clients expecting rapid, tech-assisted legal opinions.",
        "trend_competitors": "Elite magic circle and Nordic law firms deploying internal generative AI models to compress legal research time by 50%.",
        "trend_legacy_debt": "Millions of privileged legal memos, briefs, and transactional contracts locked in siloed document management systems with basic text search.",
        "fomo_cost_of_inaction": "Risk of tier-1 institutional clients shifting recurring corporate legal work to AI-augmented competitors capable of delivering opinions in hours.",
        "fomo_peer_velocity": "Competitor law firms generate initial legal research memorandums in minutes using AI; Mannheimer associates spend hours searching archives.",
        "fomo_vendor_traps": "Third-party legal AI vendors that utilize public multi-tenant cloud APIs risking legal professional privilege.",
        "tco_reduction_pct": 37,
        "compute_savings_pct": 52,
        "productivity_lift_multiplier": "4.4x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 5,
        "investment_eur": "€380,000",
        "three_year_net_value_eur": "€5,920,000",
        "key_questions": [
            {
                "target": "Managing Partner",
                "question": "How can our senior associates synthesize 30 years of firm M&A precedent without risking client confidentiality?"
            },
            {
                "target": "Head of Legal Tech & Knowledge",
                "question": "What is your plan to integrate Microsoft Copilot Studio with our private matter repository?"
            },
            {
                "target": "DPO & Information Security Officer",
                "question": "How do you enforce cryptographic data boundaries and ethical walls between competing client matters?"
            },
            {
                "target": "Chief Operating Officer",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Sovereign Enterprise Legal Precedent & Contract Engine",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Private generative AI search interrogating 30 years of firm legal opinions and contracts running exclusively in Azure Sweden Central.",
                "architecture": "Azure OpenAI Service (Sweden Central) + Azure AI Search RAG"
            },
            {
                "title": "Ethical Walls & Cryptographic Matter Governance",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Microsoft Purview integration enforcing automated ethical walls and Bar Association confidentiality boundaries.",
                "architecture": "Microsoft Purview Information Protection + Microsoft Fabric OneLake"
            },
            {
                "title": "Transactional M&A Diligence Copilot",
                "category": "Unified BI & Direct Lake",
                "description": "Copilot Studio assistant integrated with Microsoft Word to extract indemnities, warranties, and disclosure exceptions.",
                "architecture": "Microsoft Copilot Studio + Microsoft 365 + Azure AI"
            }
        ],
        "matched_cases": [
            "cera",
            "ggz-rivierduinen"
        ]
    },
    "JLINDEBERG AB": {
        "org_nr": "556525-4298",
        "tpid": "7949165",
        "industry": "Global Fashion, Golf & Ski Performance Apparel",
        "what_partner_solves": "Unify global e-commerce clickstream data, wholesale showroom pre-orders, and supply chain logistics into Microsoft Fabric, enabling AI-driven style and size demand forecasting, minimizing end-of-season inventory write-downs, and optimizing direct-to-consumer omni-channel fulfillment.",
        "what_databricks_solves": "Unify global e-commerce clickstream data, wholesale showroom pre-orders, and supply chain logistics into Microsoft Fabric, enabling AI-driven style and size demand forecasting, minimizing end-of-season inventory write-downs, and optimizing direct-to-consumer omni-channel fulfillment.",
        "what_microsoft_solves": "Unify global e-commerce clickstream data, wholesale showroom pre-orders, and supply chain logistics into Microsoft Fabric, enabling AI-driven style and size demand forecasting, minimizing end-of-season inventory write-downs, and optimizing direct-to-consumer omni-channel fulfillment.",
        "trend_macro": "Volatile global fashion cycles and fast-moving golf/ski lifestyle trends; rapid expansion of international DTC e-commerce across US, Europe, and Asia.",
        "trend_competitors": "Global luxury sportswear brands (Bogner, Malbon, RLX) investing heavily in predictive fashion merchandising and customer personalization.",
        "trend_legacy_debt": "Fragmented e-commerce platforms (Shopify/Magento), legacy ERP databases, and manual showroom order spreadsheets.",
        "fomo_cost_of_inaction": "Heavy margin erosion from unsold seasonal inventory discounted at 40%+ and out-of-stock sizes on high-margin ski jackets.",
        "fomo_peer_velocity": "Competitors adjust production runs dynamically based on real-time e-commerce demand signals; J.Lindeberg relies on fixed seasonal orders.",
        "fomo_vendor_traps": "Disparate retail analytics point solutions charging high recurring fees without integration to central supply chain ERP.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 58,
        "productivity_lift_multiplier": "3.5x",
        "annual_savings_eur": "€2,400,000",
        "payback_months": 6,
        "investment_eur": "€470,000",
        "three_year_net_value_eur": "€6,730,000",
        "key_questions": [
            {
                "target": "CEO / Brand Director",
                "question": "How accurately can you forecast production runs for upcoming golf and ski collections based on early wholesale pre-orders?"
            },
            {
                "target": "Head of E-commerce",
                "question": "What is your cart abandonment rate, and how do you personalize product recommendations across regional online stores?"
            },
            {
                "target": "Group CIO",
                "question": "What is your timeline to unify warehouse logistics and retail POS data into Microsoft Fabric?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "AI Fashion Merchandising & Size Demand Forecasting",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating wholesale pre-orders, e-commerce clickstreams, and retail store sales into OneLake to optimize production sizing.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Omni-Channel Customer 360 & Personalization Engine",
                "category": "Unified BI & Direct Lake",
                "description": "Personalized product recommendations and inventory availability across Nordic, European, and US web stores.",
                "architecture": "Power BI Direct Lake + Azure AI Search + Fabric"
            },
            {
                "title": "Creative Marketing & Multilingual Catalog Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant generating localized product descriptions and marketing copy for international collections.",
                "architecture": "Azure OpenAI Service + Content Management System"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "austrotherm"
        ]
    },
    "VITROLIFE AB": {
        "org_nr": "556354-3452",
        "tpid": "8030841",
        "industry": "Medical Technology & Assisted Reproduction (IVF & Time-Lapse Embryo Imaging)",
        "what_partner_solves": "Securely aggregate time-lapse embryo imaging telemetry and genetic evaluation datasets into Microsoft Fabric and Azure AI within Purview medical compliance boundaries, accelerating AI-guided embryo viability scoring algorithms and streamlining global clinic software deployments.",
        "what_databricks_solves": "Securely aggregate time-lapse embryo imaging telemetry and genetic evaluation datasets into Microsoft Fabric and Azure AI within Purview medical compliance boundaries, accelerating AI-guided embryo viability scoring algorithms and streamlining global clinic software deployments.",
        "what_microsoft_solves": "Securely aggregate time-lapse embryo imaging telemetry and genetic evaluation datasets into Microsoft Fabric and Azure AI within Purview medical compliance boundaries, accelerating AI-guided embryo viability scoring algorithms and streamlining global clinic software deployments.",
        "trend_macro": "Global fertility clinic consolidation and increasing demand for automated, objective AI embryo selection tools to maximize pregnancy success rates.",
        "trend_competitors": "Global IVF technology competitors (CooperSurgical, Hamilton Thorne) investing heavily in automated laboratory data management.",
        "trend_legacy_debt": "Siloed on-premise clinic image archives, disconnected ERP systems, and strict international medical data sovereignty barriers.",
        "fomo_cost_of_inaction": "Competitors patenting and deploying cloud-native AI embryo scoring models that win preferred clinic chain tenders.",
        "fomo_peer_velocity": "Leading clinic chains demand real-time AI embryo viability reports; Vitrolife clinics wait for post-incubation manual embryologist reviews.",
        "fomo_vendor_traps": "Isolated proprietary clinic database software charging steep fees to export time-lapse imaging sequences.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 60,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,600,000",
        "payback_months": 6,
        "investment_eur": "€520,000",
        "three_year_net_value_eur": "€7,280,000",
        "key_questions": [
            {
                "target": "Chief Scientific Officer",
                "question": "How do you pool de-identified time-lapse embryo imaging feeds across hundreds of partner IVF clinics to train your diagnostic algorithms?"
            },
            {
                "target": "Head of Regulatory & Quality",
                "question": "How do you satisfy FDA SaMD (Software as a Medical Device) and EU MDR audit requirements for cloud-based AI algorithms?"
            },
            {
                "target": "Head of IT (Hanna / Sofia)",
                "question": "Are our Purview sensitivity labels ready to govern clinical trial patient records and ERP data simultaneously?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Sovereign Medical Device Data Governance (Phase 0)",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Microsoft Purview integration establishing automated sensitivity labeling and GDPR/HIPAA boundaries across IVF clinical imaging and ERP.",
                "architecture": "Microsoft Purview + Microsoft Fabric OneLake + Azure Healthcare APIs"
            },
            {
                "title": "Time-Lapse Embryo Computer Vision Viability Mesh",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Machine learning computer vision models scoring embryo division kinetics and blastocyst expansion from EmbryoScope feeds.",
                "architecture": "Azure Machine Learning + Azure Computer Vision + Fabric Lakehouse"
            },
            {
                "title": "Global IVF Clinic Telemetry & ERP Modernization",
                "category": "Unified BI & Direct Lake",
                "description": "Consolidating clinic consumable usage, incubator telemetry, and global ERP orders into Power BI Direct Lake.",
                "architecture": "Power BI Direct Lake + Azure Synapse + Fabric OneLake"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "ggz-rivierduinen"
        ]
    },
    "XANO Industri AB": {
        "org_nr": "556076-2052",
        "tpid": "8599539",
        "industry": "Industrial Machinery, Packaging Automation & Precision Plastic/Metal Systems",
        "what_partner_solves": "Centralize machinery telemetry, OEE production metrics, and ERP job-costing data across 25+ subsidiaries into Microsoft Fabric, optimizing machine tool preventive maintenance, reducing packaging line changeover scrap, and harmonizing corporate financial reporting.",
        "what_databricks_solves": "Centralize machinery telemetry, OEE production metrics, and ERP job-costing data across 25+ subsidiaries into Microsoft Fabric, optimizing machine tool preventive maintenance, reducing packaging line changeover scrap, and harmonizing corporate financial reporting.",
        "what_microsoft_solves": "Centralize machinery telemetry, OEE production metrics, and ERP job-costing data across 25+ subsidiaries into Microsoft Fabric, optimizing machine tool preventive maintenance, reducing packaging line changeover scrap, and harmonizing corporate financial reporting.",
        "trend_macro": "Smart packaging automation demand; European manufacturing reshoring driving need for high-efficiency robotic packaging lines.",
        "trend_competitors": "Global packaging and machinery innovators (Coesia, Syntegon) deploying IoT cloud packaging equipment diagnostics.",
        "trend_legacy_debt": "Decentralized PLC controllers, siloed subsidiary ERPs, and manual monthly operational consolidation.",
        "fomo_cost_of_inaction": "Unplanned packaging line downtime at customer food and pharma plants damaging OEM brand trust.",
        "fomo_peer_velocity": "Competitors offer packaging machine predictive maintenance SLAs; XANO subsidiaries rely on reactive break-fix repairs.",
        "fomo_vendor_traps": "Isolated machinery software licenses with high custom development costs to export operational metrics.",
        "tco_reduction_pct": 41,
        "compute_savings_pct": 55,
        "productivity_lift_multiplier": "3.3x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€5,840,000",
        "key_questions": [
            {
                "target": "Group Operations Director",
                "question": "What is the average Overall Equipment Effectiveness (OEE) across your 25 manufacturing plants, and where is the greatest margin leakage?"
            },
            {
                "target": "VP Packaging Machinery",
                "question": "Can your packaging machines alert operators to feed tape wear and pneumatic pressure drops before line jams occur?"
            },
            {
                "target": "Group CFO",
                "question": "How do you eliminate manual monthly reporting reconciliation across your acquired subsidiaries?"
            },
            {
                "target": "Group CIO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Packaging Machinery IoT Fleet Telemetry",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming pneumatic pressure, motor vibration, and cycle speed from connected packaging lines into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure IoT Operations + Eventstream"
            },
            {
                "title": "Multi-Plant OEE & Production Scrap Optimization",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating 25 factory production logs into OneLake to benchmark machine uptime and reduce changeover scrap.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Component CAD Design & Quote Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant extracting precision component dimensions from customer CAD drawings to accelerate quotes.",
                "architecture": "Azure OpenAI Service + Azure AI Search + ERP Portal"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "AB WILH BECKER": {
        "org_nr": "556016-1703",
        "tpid": "16739178",
        "industry": "Industrial Surface Coatings & Coil/Wood Finishes",
        "what_partner_solves": "Consolidate chemical formulation recipes, batch spectrophotometer color-matching telemetry, and raw material volatility metrics into Microsoft Fabric, enabling automated batch color drift correction, VOC emission compliance tracking, and global plant yield benchmarking.",
        "what_databricks_solves": "Consolidate chemical formulation recipes, batch spectrophotometer color-matching telemetry, and raw material volatility metrics into Microsoft Fabric, enabling automated batch color drift correction, VOC emission compliance tracking, and global plant yield benchmarking.",
        "what_microsoft_solves": "Consolidate chemical formulation recipes, batch spectrophotometer color-matching telemetry, and raw material volatility metrics into Microsoft Fabric, enabling automated batch color drift correction, VOC emission compliance tracking, and global plant yield benchmarking.",
        "trend_macro": "Stringent EU REACH chemical regulations and solvent-free/low-VOC environmental mandates from industrial manufacturers.",
        "trend_competitors": "Global coatings innovators (AkzoNobel, PPG) accelerating formulation development and color-matching using cloud AI models.",
        "trend_legacy_debt": "Proprietary laboratory formulation databases and batch manufacturing execution systems isolated from corporate ERP.",
        "fomo_cost_of_inaction": "Entire industrial coating batches discarded or reworked due to color tint drift during automated mixing.",
        "fomo_peer_velocity": "Competitors correct batch color tinting in real time using spectrophotometer algorithms; Becker technicians rely on manual sample testing.",
        "fomo_vendor_traps": "Isolated lab formulation software with expensive custom export fees and lack of cloud data integration.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 57,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 7,
        "investment_eur": "€470,000",
        "three_year_net_value_eur": "€6,130,000",
        "key_questions": [
            {
                "target": "Head of Formulation R&D",
                "question": "How many physical laboratory tinting iterations are needed before a custom industrial coating recipe matches customer specs?"
            },
            {
                "target": "Quality Director",
                "question": "Can you correlate spectrophotometer color measurements in real time during batch production to correct tint drift automatically?"
            },
            {
                "target": "Environmental Compliance Officer",
                "question": "How do you calculate and audit VOC emission certificates across global coating shipments?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Automated Chemical Formulation & Color Matching Engine",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models predicting spectrophotometer Lab color values based on pigment concentration and resin chemistry.",
                "architecture": "Microsoft Fabric OneLake + Azure Machine Learning + Data Factory"
            },
            {
                "title": "Real-Time Batch Mixing Telemetry & Scrap Reduction",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming mixing vat temperature, viscosity, and tint dosing feeds into Fabric Real-Time Hub to eliminate off-spec batches.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            },
            {
                "title": "EU REACH Chemical Compliance Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI search assistant checking formulation raw materials against restricted chemical substance lists and generating SDS sheets.",
                "architecture": "Azure OpenAI Service + Azure AI Search + SharePoint"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "AQ GROUP AB": {
        "org_nr": "556281-8418",
        "tpid": "20962316",
        "industry": "Global Industrial Component Manufacturing (Wiring Systems, Sheet Metal, Injection Molding)",
        "what_partner_solves": "Ingest real-time machine telemetry, copper/resin procurement price fluctuations, and production line OEE across 40+ international manufacturing plants into Microsoft Fabric, driving dynamic production scheduling, scrap reduction, and automated customer quality certifications.",
        "what_databricks_solves": "Ingest real-time machine telemetry, copper/resin procurement price fluctuations, and production line OEE across 40+ international manufacturing plants into Microsoft Fabric, driving dynamic production scheduling, scrap reduction, and automated customer quality certifications.",
        "what_microsoft_solves": "Ingest real-time machine telemetry, copper/resin procurement price fluctuations, and production line OEE across 40+ international manufacturing plants into Microsoft Fabric, driving dynamic production scheduling, scrap reduction, and automated customer quality certifications.",
        "trend_macro": "Shifting global supply chains in automotive, commercial vehicle, and rail; severe volatility in copper, steel, and polymer raw material prices.",
        "trend_competitors": "Global contract electronics and components manufacturers (Sanmina, Kimball) investing in smart factory IoT platforms.",
        "trend_legacy_debt": "40 distinct factory floor systems, local MES databases, and disparate ERPs with heavy manual reporting.",
        "fomo_cost_of_inaction": "Uncoordinated raw material procurement across 16 countries causing millions in lost volume purchasing power.",
        "fomo_peer_velocity": "Competitors optimize global plant capacity dynamically; AQ Group relies on decentralized subsidiary scheduling.",
        "fomo_vendor_traps": "Dozens of localized legacy ERP maintenance contracts without central cloud data synchronization.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 62,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€3,500,000",
        "payback_months": 6,
        "investment_eur": "€620,000",
        "three_year_net_value_eur": "€9,880,000",
        "key_questions": [
            {
                "target": "CEO / COO",
                "question": "Can you benchmark manufacturing productivity and component scrap rates across your 40 global factories in real time?"
            },
            {
                "target": "Head of Global Procurement",
                "question": "How do you synchronize bulk copper and sheet metal purchasing across European and Asian production hubs?"
            },
            {
                "target": "Group CIO",
                "question": "What is your strategy to create a unified data platform across 16 countries without disrupting 24/7 manufacturing plants?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Global 40-Plant Manufacturing OEE & Scrap Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating machine uptime, stamping speed, and injection moulding scrap rates across 40 factories into OneLake.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "Raw Material Procurement & Hedging Analytics",
                "category": "Unified BI & Direct Lake",
                "description": "Analyzing global copper, aluminium, and polymer purchasing volumes against spot commodity exchanges to optimize bulk buys.",
                "architecture": "Power BI Direct Lake + Azure Synapse + Fabric"
            },
            {
                "title": "Automotive Quality Control (PPAP/APQP) Document Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant extracting test dimensions and generating certified PPAP documentation for automotive OEMs.",
                "architecture": "Azure OpenAI Service + Azure AI Document Intelligence + SharePoint"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "bridgestone"
        ]
    },
    "aPak AB": {
        "org_nr": "556059-4307",
        "tpid": "21111834",
        "industry": "Industrial Packaging Solutions & Automated Packaging Logistics",
        "what_partner_solves": "Unify customer CAD packaging designs, corrugated raw paper procurement pricing, and just-in-time warehouse dispatch data into Microsoft Fabric, delivering automated carton optimization algorithms, eliminating freight air shipping waste, and calculating Scope 3 packaging carbon footprints.",
        "what_databricks_solves": "Unify customer CAD packaging designs, corrugated raw paper procurement pricing, and just-in-time warehouse dispatch data into Microsoft Fabric, delivering automated carton optimization algorithms, eliminating freight air shipping waste, and calculating Scope 3 packaging carbon footprints.",
        "what_microsoft_solves": "Unify customer CAD packaging designs, corrugated raw paper procurement pricing, and just-in-time warehouse dispatch data into Microsoft Fabric, delivering automated carton optimization algorithms, eliminating freight air shipping waste, and calculating Scope 3 packaging carbon footprints.",
        "trend_macro": "E-commerce expansion demanding sustainable, right-sized corrugated packaging; EU Packaging and Packaging Waste Regulation (PPWR) deadlines.",
        "trend_competitors": "Global packaging leaders (Smurfit Westrock, DS Smith) deploying cloud carton optimization and digital customer supply chain portals.",
        "trend_legacy_debt": "Legacy ERP and on-premise warehouse management systems with delayed order-to-dispatch synchronization.",
        "fomo_cost_of_inaction": "Customers switching to packaging suppliers that provide automated carbon footprint metrics and right-sized box algorithms.",
        "fomo_peer_velocity": "Competitors calculate custom box carbon footprints instantly in online portals; aPak relies on manual spreadsheet engineering takeoffs.",
        "fomo_vendor_traps": "Isolated warehouse management software charging high fees for custom API integration to central ERP.",
        "tco_reduction_pct": 39,
        "compute_savings_pct": 52,
        "productivity_lift_multiplier": "3.1x",
        "annual_savings_eur": "€1,500,000",
        "payback_months": 7,
        "investment_eur": "€340,000",
        "three_year_net_value_eur": "€4,160,000",
        "key_questions": [
            {
                "target": "Managing Director",
                "question": "How can you help your industrial customers reduce shipping empty air by 20% using automated carton design optimization?"
            },
            {
                "target": "Supply Chain Director",
                "question": "Can you track raw corrugated board inventory in real time against customer seasonal fulfillment spikes?"
            },
            {
                "target": "Group CIO",
                "question": "How do you plan to automate customer packaging quotes and RFQs using Microsoft Azure AI?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Automated Packaging Optimization & Dimensioning Engine",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning algorithms matching customer product CAD dimensions with optimal corrugated carton die-lines to reduce air volume.",
                "architecture": "Microsoft Fabric OneLake + Azure Machine Learning + Data Factory"
            },
            {
                "title": "Just-in-Time 3PL Warehouse & Dispatch Mesh",
                "category": "Unified BI & Direct Lake",
                "description": "Real-time tracking of corrugated board inventory and dispatch logistics in Power BI Direct Lake.",
                "architecture": "Power BI Direct Lake + Azure Synapse + Fabric"
            },
            {
                "title": "Sustainable Packaging Spec & PPWR Compliance Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant calculating recyclability percentages and generating EU PPWR compliance declarations.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "austrotherm"
        ]
    },
    "CELLINK AB": {
        "org_nr": "559050-5052",
        "tpid": "36921894",
        "industry": "3D Bioprinting, Bioinks & Cellular Automation Technologies",
        "what_partner_solves": "Ingest high-resolution bioprinter sensor feeds (pneumatic nozzle pressures, bioink rheology, thermal extrusion logs) into Microsoft Fabric Real-Time Intelligence, optimizing print fidelity for live-cell tissue constructs and accelerating regenerative medicine research workflows globally.",
        "what_databricks_solves": "Ingest high-resolution bioprinter sensor feeds (pneumatic nozzle pressures, bioink rheology, thermal extrusion logs) into Microsoft Fabric Real-Time Intelligence, optimizing print fidelity for live-cell tissue constructs and accelerating regenerative medicine research workflows globally.",
        "what_microsoft_solves": "Ingest high-resolution bioprinter sensor feeds (pneumatic nozzle pressures, bioink rheology, thermal extrusion logs) into Microsoft Fabric Real-Time Intelligence, optimizing print fidelity for live-cell tissue constructs and accelerating regenerative medicine research workflows globally.",
        "trend_macro": "Global drive to replace animal testing in pharmaceutical drug discovery with 3D-bioprinted human tissue constructs (FDA Modernization Act 2.0).",
        "trend_competitors": "Global bioprinting innovators (Organovo, Aspect Biosystems) advancing cloud-connected tissue engineering platforms.",
        "trend_legacy_debt": "Localized printer log files and disconnected laboratory databases preventing global machine learning on print parameters.",
        "fomo_cost_of_inaction": "High bioink and primary cell line failure rates during hours-long tissue construct printing due to undetected nozzle shear stress.",
        "fomo_peer_velocity": "Competitors train AI models on thousands of global print runs; CELLINK research teams analyze single-printer logs in isolation.",
        "fomo_vendor_traps": "Proprietary instrument software architectures requiring high custom engineering fees to export raw telemetry.",
        "tco_reduction_pct": 43,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.8x",
        "annual_savings_eur": "€2,200,000",
        "payback_months": 6,
        "investment_eur": "€450,000",
        "three_year_net_value_eur": "€6,150,000",
        "key_questions": [
            {
                "target": "Head of Bioprinting R&D",
                "question": "How do your software algorithms adjust print pressure in real time when bioink viscosity shifts due to ambient temperature?"
            },
            {
                "target": "VP Global Sales",
                "question": "Can you offer biopharma customers guaranteed print reproducibility by analyzing cloud telemetry from 2,000 installed bioprinters?"
            },
            {
                "target": "Group CIO",
                "question": "How do you safeguard proprietary bioink formulations and customer medical IP in a sovereign cloud environment?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Live-Cell Bioprinting Telemetry & Rheology Mesh",
                "category": "Real-Time Intelligence (KQL)",
                "description": "High-frequency streaming of pneumatic pressure, nozzle temperature, and optical droplet sensors into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            },
            {
                "title": "Predictive Tissue Print Fidelity Models",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models predicting live-cell viability and scaffold collapse before completion of hours-long print runs.",
                "architecture": "Microsoft Fabric OneLake + Azure Machine Learning + Power BI"
            },
            {
                "title": "Life Science Protocol & Bioink Optimization Assistant",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping researchers match cell types with optimal bioink hydrogels, crosslinking wavelengths, and nozzle gauges.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Cloud Software"
            }
        ],
        "matched_cases": [
            "lrm-medemotion",
            "austrotherm"
        ]
    },
    "Future Ordering AB": {
        "org_nr": "559048-2831",
        "tpid": "37881112",
        "industry": "Enterprise Digital Ordering Platform for Quick Service Restaurants (QSR)",
        "what_partner_solves": "Ingest massive multi-tenant transactional clickstream events, kitchen display system (KDS) order prep latencies, and consumer basket data into Microsoft Fabric and Azure Cosmos DB, delivering sub-second personalized upselling recommendations, dynamic kitchen surge balancing, and restaurant revenue forecasting.",
        "what_databricks_solves": "Ingest massive multi-tenant transactional clickstream events, kitchen display system (KDS) order prep latencies, and consumer basket data into Microsoft Fabric and Azure Cosmos DB, delivering sub-second personalized upselling recommendations, dynamic kitchen surge balancing, and restaurant revenue forecasting.",
        "what_microsoft_solves": "Ingest massive multi-tenant transactional clickstream events, kitchen display system (KDS) order prep latencies, and consumer basket data into Microsoft Fabric and Azure Cosmos DB, delivering sub-second personalized upselling recommendations, dynamic kitchen surge balancing, and restaurant revenue forecasting.",
        "trend_macro": "QSR digital orders surpassing 60% of total revenue; restaurant chains competing on frictionless kiosk, drive-thru, and mobile app ordering speeds.",
        "trend_competitors": "Global enterprise restaurant software innovators (Olo, NCR Voyix) scaling cloud analytics to optimize kitchen throughput.",
        "trend_legacy_debt": "Multi-tenant transactional databases facing latency spikes during peak meal hours (lunch/dinner rushes) and delayed reporting.",
        "fomo_cost_of_inaction": "A 2-second delay in digital kiosk response times during lunch rush causing order drop-offs and lost restaurant throughput.",
        "fomo_peer_velocity": "Competitors calculate dynamic upselling baskets in under 50 milliseconds; Future Ordering relies on static menu item suggestions.",
        "fomo_vendor_traps": "High cloud database burst compute costs during daily lunch surges without elastic auto-scaling.",
        "tco_reduction_pct": 45,
        "compute_savings_pct": 61,
        "productivity_lift_multiplier": "3.7x",
        "annual_savings_eur": "€2,500,000",
        "payback_months": 6,
        "investment_eur": "€490,000",
        "three_year_net_value_eur": "€7,010,000",
        "key_questions": [
            {
                "target": "Chief Technology Officer (CTO)",
                "question": "How do you handle lunch rush transactional concurrency across 5,000 digital kiosks without database latency degradation?"
            },
            {
                "target": "VP Product & Growth",
                "question": "Can your upselling recommendation engine calculate personalized basket add-ons in under 50 milliseconds based on weather and store inventory?"
            },
            {
                "target": "Head of Data Engineering",
                "question": "How quickly can restaurant franchise managers see hourly sales and kitchen prep bottle-necks in Power BI Direct Lake?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "High-Concurrency Real-Time QSR Clickstream Analytics",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Streaming millions of kiosk touches, mobile basket changes, and payment confirmations into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            },
            {
                "title": "Dynamic Kitchen Surge & Prep Time Forecasting",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models forecasting order prep times and kitchen station bottlenecks to balance drive-thru and counter queues.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Azure Cosmos DB"
            },
            {
                "title": "Intelligent Multilingual Menu Localization & Nutritional Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant auto-translating menu descriptions and answering customer allergen queries across 10 European languages.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web API"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "fluvius"
        ]
    },
    "Flokk AB": {
        "org_nr": "556614-2757",
        "tpid": "47641567",
        "industry": "Ergonomic Workplace Seating & Sustainable Furniture",
        "what_partner_solves": "Integrate circular manufacturing supply chain data, recycled plastic/aluminium batch tracking, and European B2B dealer orders into Microsoft Fabric, automating EU Digital Product Passport (DPP) compliance, predicting upholstery fabric demand, and optimizing Nordic assembly plants.",
        "what_databricks_solves": "Integrate circular manufacturing supply chain data, recycled plastic/aluminium batch tracking, and European B2B dealer orders into Microsoft Fabric, automating EU Digital Product Passport (DPP) compliance, predicting upholstery fabric demand, and optimizing Nordic assembly plants.",
        "what_microsoft_solves": "Integrate circular manufacturing supply chain data, recycled plastic/aluminium batch tracking, and European B2B dealer orders into Microsoft Fabric, automating EU Digital Product Passport (DPP) compliance, predicting upholstery fabric demand, and optimizing Nordic assembly plants.",
        "trend_macro": "European Green Deal mandating Digital Product Passports by 2027; corporate buyers demanding certified recycled materials in office furniture.",
        "trend_competitors": "Global commercial furniture leaders (Steelcase, MillerKnoll) investing heavily in circular furniture supply chain analytics.",
        "trend_legacy_debt": "Legacy ERP databases and disconnected assembly plant spreadsheets across Sweden, Norway, and Poland.",
        "fomo_cost_of_inaction": "Exclusion from major European government and corporate workplace procurement tenders if product circularity cannot be verified digitally.",
        "fomo_peer_velocity": "Competitors provide verified product carbon footprints instantly in dealer configuration tools; Flokk relies on manual sustainability estimates.",
        "fomo_vendor_traps": "Isolated sustainability reporting software charging steep fees without integration to central factory ERP.",
        "tco_reduction_pct": 40,
        "compute_savings_pct": 54,
        "productivity_lift_multiplier": "3.2x",
        "annual_savings_eur": "€1,800,000",
        "payback_months": 7,
        "investment_eur": "€410,000",
        "three_year_net_value_eur": "€4,990,000",
        "key_questions": [
            {
                "target": "Head of Circular Economy",
                "question": "Can you provide verified cradle-to-grave carbon footprints and recycled content percentages for every office chair manufactured?"
            },
            {
                "target": "Operations Director",
                "question": "What is your lead time on custom textile and component assemblies across Nordic manufacturing plants?"
            },
            {
                "target": "Group CIO",
                "question": "How do you connect B2B dealer ordering portals with real-time factory scheduling in Microsoft Fabric?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Circular Economy & Digital Product Passport Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Tracking recycled ocean plastic, post-consumer aluminium, and fabric suppliers in OneLake to generate EU Digital Product Passports.",
                "architecture": "Microsoft Sustainability Manager + Microsoft Fabric OneLake + Purview"
            },
            {
                "title": "Custom Ergonomic Furniture Demand & Fabric Sizing",
                "category": "Unified BI & Direct Lake",
                "description": "Machine learning models forecasting fabric roll utilization and custom upholstery cutting schedules to eliminate textile waste.",
                "architecture": "Power BI Direct Lake + Azure Machine Learning + Fabric"
            },
            {
                "title": "B2B Dealer Product Configuration & Spec Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping interior architects select ergonomic chair configurations meeting local workplace health norms.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Web Portal"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "IPCO SWEDEN AB": {
        "org_nr": "556029-7987",
        "tpid": "50946054",
        "industry": "Solid Steel Belts & Industrial Continuous Process Systems",
        "what_partner_solves": "Collect vibration, heat distribution, and belt tension telemetry from industrial pastillation and bake oven installations globally into Microsoft Fabric Real-Time Intelligence, providing customers with predictive belt maintenance warnings and reducing unplanned plant downtime.",
        "what_databricks_solves": "Collect vibration, heat distribution, and belt tension telemetry from industrial pastillation and bake oven installations globally into Microsoft Fabric Real-Time Intelligence, providing customers with predictive belt maintenance warnings and reducing unplanned plant downtime.",
        "what_microsoft_solves": "Collect vibration, heat distribution, and belt tension telemetry from industrial pastillation and bake oven installations globally into Microsoft Fabric Real-Time Intelligence, providing customers with predictive belt maintenance warnings and reducing unplanned plant downtime.",
        "trend_macro": "Continuous chemical pastillation and industrial food baking requiring uninterrupted 24/7 belt operations; replacement costs for heavy steel belts exceed €200,000.",
        "trend_competitors": "Industrial process equipment competitors (Berndorf Band Group) developing specialized cloud belt condition monitoring tools.",
        "trend_legacy_debt": "Localized field service inspection notes, isolated vibration sensor data, and legacy on-premise ERP.",
        "fomo_cost_of_inaction": "Catastrophic steel belt failure halting chemical pastillation lines for weeks, triggering heavy customer claims.",
        "fomo_peer_velocity": "Competitors offer remote belt tracking telemetry; IPCO relies on scheduled annual physical technician visits.",
        "fomo_vendor_traps": "Isolated condition monitoring software with high subscription fees and lack of cloud data integration.",
        "tco_reduction_pct": 42,
        "compute_savings_pct": 56,
        "productivity_lift_multiplier": "3.4x",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "investment_eur": "€460,000",
        "three_year_net_value_eur": "€5,840,000",
        "key_questions": [
            {
                "target": "VP Global Service",
                "question": "How many catastrophic steel belt fractures could be prevented by continuous heat distribution and tracking telemetry?"
            },
            {
                "target": "Chief Metallurgist",
                "question": "Can your engineering teams analyze belt weld stress fatigue remotely across customer industrial plants?"
            },
            {
                "target": "Group CIO",
                "question": "What is your strategy to monetize industrial IoT telemetry into high-margin predictive maintenance contracts?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Continuous Steel Belt Telemetry & Vibration Hub",
                "category": "Real-Time Intelligence (KQL)",
                "description": "Ingesting belt tracking sensor feeds, optical edge wear cameras, and thermal scanners into Fabric Real-Time Hub.",
                "architecture": "Fabric Real-Time Hub + Azure Eventstream + KQL"
            },
            {
                "title": "Industrial Pastillation & Oven Maintenance Predictor",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Machine learning models predicting weld fatigue and drum alignment drift in chemical cooling lines.",
                "architecture": "Microsoft Fabric OneLake + Azure ML + Power BI Direct Lake"
            },
            {
                "title": "Technical Field Service & Belt Repair Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Generative AI assistant helping service engineers calculate weld repair parameters and drum crown adjustments.",
                "architecture": "Azure OpenAI Service + Azure AI Search + Mobile Service App"
            }
        ],
        "matched_cases": [
            "austrotherm",
            "fluvius"
        ]
    },
    "Cars2click": {
        "org_nr": "556810-7451",
        "tpid": "56428871",
        "industry": "B2B Cross-Border Automotive Trading & Vehicle Remarketing Platform",
        "what_partner_solves": "Ingest daily vehicle listings, regional price arbitrage spreads, cross-border VAT/import tax regulations, and currency rates into Microsoft Fabric, powering algorithmic used-car price optimization, automated cross-border margin calculations, and fast dealer inventory turnover.",
        "what_databricks_solves": "Ingest daily vehicle listings, regional price arbitrage spreads, cross-border VAT/import tax regulations, and currency rates into Microsoft Fabric, powering algorithmic used-car price optimization, automated cross-border margin calculations, and fast dealer inventory turnover.",
        "what_microsoft_solves": "Ingest daily vehicle listings, regional price arbitrage spreads, cross-border VAT/import tax regulations, and currency rates into Microsoft Fabric, powering algorithmic used-car price optimization, automated cross-border margin calculations, and fast dealer inventory turnover.",
        "trend_macro": "Volatile European used car pricing caused by EV residual value depreciation and cross-border currency swings.",
        "trend_competitors": "Global digital used car remarketing platforms (AUTO1 Group, BCA) investing tens of millions in algorithmic pricing engines.",
        "trend_legacy_debt": "Scraping multiple European dealer listing portals into fragile SQL databases with slow manual price comparison spreadsheets.",
        "fomo_cost_of_inaction": "Purchasing batches of used leasing vehicles at uncompetitive prices due to delayed insight into destination country price drops.",
        "fomo_peer_velocity": "Competitors calculate cross-border trading margins in seconds; Cars2click traders spend hours manually calculating net margins.",
        "fomo_vendor_traps": "High third-party vehicle valuation API fees without centralized data lake storage for historical price analysis.",
        "tco_reduction_pct": 44,
        "compute_savings_pct": 59,
        "productivity_lift_multiplier": "3.6x",
        "annual_savings_eur": "€2,300,000",
        "payback_months": 6,
        "investment_eur": "€470,000",
        "three_year_net_value_eur": "€6,430,000",
        "key_questions": [
            {
                "target": "CEO / Head of Trading",
                "question": "How quickly do your traders calculate the net cross-border margin on a fleet of 500 leasing cars including transport, VAT, and local registration fees?"
            },
            {
                "target": "CTO",
                "question": "How many European used car listing feeds can your data architecture ingest and normalize each morning?"
            },
            {
                "target": "Chief Data Officer",
                "question": "Can we automate vehicle condition report analysis and damage deduction using Azure OpenAI vision models?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $40k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Algorithmic European Vehicle Pricing & Arbitrage Engine",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating 500,000 European vehicle listings and auction results into OneLake to calculate geographic arbitrage spreads.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Azure ML"
            },
            {
                "title": "Real-Time Cross-Border VAT & Margin Calculation Fabric",
                "category": "Unified BI & Direct Lake",
                "description": "Automated calculation of net trader margins incorporating local European vehicle taxes, transport, and currency exchange.",
                "architecture": "Power BI Direct Lake + Azure Synapse + Fabric"
            },
            {
                "title": "Vehicle Inspection Sheet & Damage Deduction Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Computer vision and generative AI assistant analyzing vehicle inspection photos to estimate repair deductions.",
                "architecture": "Azure OpenAI Service (GPT-4 Vision) + Azure AI Search"
            }
        ],
        "matched_cases": [
            "bridgestone",
            "fluvius"
        ]
    },
    "Bravida AB": {
        "org_nr": "556891-5390",
        "tpid": "4954069",
        "industry": "Technical Installation & End-to-End Building Services (Electrical, HVAC, Plumbing)",
        "what_partner_solves": "Consolidate field service job-costing, mobile technician dispatch logs, building energy telemetry, and supplier price catalogs into Microsoft Fabric, optimizing field technician utilization across 14,000 workers, automating project margin leakage detection, and providing smart building energy analytics to property owners.",
        "what_databricks_solves": "Consolidate field service job-costing, mobile technician dispatch logs, building energy telemetry, and supplier price catalogs into Microsoft Fabric, optimizing field technician utilization across 14,000 workers, automating project margin leakage detection, and providing smart building energy analytics to property owners.",
        "what_microsoft_solves": "Consolidate field service job-costing, mobile technician dispatch logs, building energy telemetry, and supplier price catalogs into Microsoft Fabric, optimizing field technician utilization across 14,000 workers, automating project margin leakage detection, and providing smart building energy analytics to property owners.",
        "trend_macro": "Tight commercial construction margins requiring stringent labor utilization and material cost control; surging demand for smart building energy retrofits.",
        "trend_competitors": "Nordic installation giants (Caverion, Assemblin Caverion Group) investing in centralized digital service platforms to automate technician dispatch and preventive maintenance.",
        "trend_legacy_debt": "Fragmented branch ERP instances, disparate mobile technician timesheet apps, and disconnected supplier wholesale price feeds.",
        "fomo_cost_of_inaction": "Even a 1.5% margin slippage on fixed-price technical installation contracts across 14,000 employees costs Bravida over 400 million SEK annually.",
        "fomo_peer_velocity": "Competitors benchmark project margin drift daily; Bravida branch managers detect project cost overruns only at monthly billing.",
        "fomo_vendor_traps": "Extensive licensing on disparate legacy branch ERP databases with heavy manual financial consolidation.",
        "tco_reduction_pct": 46,
        "compute_savings_pct": 64,
        "productivity_lift_multiplier": "4.0x",
        "annual_savings_eur": "€5,200,000",
        "payback_months": 6,
        "investment_eur": "€890,000",
        "three_year_net_value_eur": "€14,710,000",
        "key_questions": [
            {
                "target": "CEO / COO",
                "question": "How quickly can division managers detect cost overruns on active multi-million kronor commercial installation projects before monthly billing closes?"
            },
            {
                "target": "Head of Digital Service",
                "question": "What is the billable utilization rate of your 14,000 field technicians, and how much time is lost manually reconciling material receipts?"
            },
            {
                "target": "Group CIO",
                "question": "What is your strategy to harmonize supplier pricing across Rexel, Ahlsell, and Solar into a real-time Fabric Direct Lake dashboard?"
            },
            {
                "target": "CFO",
                "question": "Can we offset initial Fabric architecture costs using $50k in Microsoft AMMP co-funding?"
            }
        ],
        "use_cases": [
            {
                "title": "Enterprise Technical Installation Job-Costing & Margin Mesh",
                "category": "Enterprise SaaS Data Fabric",
                "description": "Consolidating timesheets, wholesale supplier invoices, and project milestones into OneLake to alert project managers to margin slippage.",
                "architecture": "Microsoft Fabric OneLake + Azure Data Factory + Power BI"
            },
            {
                "title": "14,000 Field Technician Dispatch & Utilization Analytics",
                "category": "Unified BI & Direct Lake",
                "description": "Dynamic service van routing and technician scheduling optimization across Sweden, Norway, Denmark, and Finland.",
                "architecture": "Power BI Direct Lake + Azure Machine Learning + Fabric"
            },
            {
                "title": "Field Technician Troubleshooting & Safety SOP Copilot",
                "category": "Enterprise GenAI (Azure OpenAI)",
                "description": "Mobile generative AI assistant providing Swedish electrical codes, HVAC wiring schematics, and safety checklists via Teams.",
                "architecture": "Azure OpenAI Service + Teams Mobile + SharePoint"
            }
        ],
        "matched_cases": [
            "fluvius",
            "austrotherm"
        ]
    }
}

RAIHAN_CLOSING_CATALOG = {
    "Väderstad AB": {
        "target_contract_value_eur": "€4,800,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,648,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Farm IoT Telemetry Modernization & Microsoft Fabric Migration",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Agronomic Telemetry Assessment & AMMP Qualification",
                "action": "Align with VP Digital Solutions and CTO on spring planting telemetry bottlenecks. Nominate Väderstad for $50k Microsoft AMMP co-funding.",
                "deliverable": "Approved Problem Statement & AMMP Engagement Submission"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Fabric Real-Time Architecture Whiteboard",
                "action": "Joint session with Raihan Chowdhury (Microsoft Cloud & AI Specialist) and Geoff Scott (DSE Data & AI) demonstrating Fabric KQL streaming on CAN-bus data.",
                "deliverable": "Validated OneLake Reference Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Seed Drill Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart in Väderstad's Azure tenant. Stream 500 connected seed drills with sub-second KQL query response.",
                "deliverable": "Live Fabric Prototype with Power BI Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Close & 3-Year SOW",
                "action": "Present validated business case to Väderstad CFO and Executive Board. Structure 3-year enterprise rollout drawing down Azure MACC.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Quantified TCO reduction (42%), AMMP subsidy offset, and 7-month payback.",
                "objection_handler": "Demonstrate that Microsoft AMMP absorbs upfront migration costs while Fabric eliminates legacy database licensing."
            },
            "technical_champion": {
                "role": "VP Digital Solutions / CTO",
                "focus": "Sub-second streaming telemetry ingestion, OneLake unified storage, and zero-maintenance SaaS.",
                "objection_handler": "Highlight native Fabric integration with existing Azure IoT footprint and zero ETL Direct Lake reporting."
            },
            "operational_sponsor": {
                "role": "Head of Global Service & Agronomy",
                "focus": "Predictive seed drill maintenance alerts and farmer mobile telemetry dashboards.",
                "objection_handler": "Share Cegeka's Austrotherm reference case showing real-time manufacturing and field telemetry stabilization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security & Procurement",
                "focus": "MACC commitment consumption, GDPR farm data sovereignty, and Microsoft Purview compliance.",
                "objection_handler": "All data resides within Väderstad's Sweden Central Azure boundary under Purview governance."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury (Microsoft Cloud & AI Specialist) and Mårten Palm (AE) at Day 5; loop in Geoff Scott (Data & AI DSE) for Fabric sizing at Day 18; executive alignment at Day 45.",
            "what_partner_does": "Allocate $50,000 AMMP Fabric voucher; provide dedicated Azure DSE engineering hours; support MACC contract drawdown alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury (Microsoft Cloud & AI Specialist) and Mårten Palm (AE) at Day 5; loop in Geoff Scott (Data & AI DSE) for Fabric sizing at Day 18; executive alignment at Day 45.",
            "what_databricks_does": "Allocate $50,000 AMMP Fabric voucher; provide dedicated Azure DSE engineering hours; support MACC contract drawdown alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery session with Väderstad's VP Digital Solutions focusing on spring planting machine telemetry and share Cegeka Austrotherm IoT benchmark.",
        "deal_blocker_mitigation": "Blocker: Legacy embedded SQL telemetry inertia. Mitigation: Position Fabric as a non-disruptive cloud streaming layer running alongside existing machine systems."
    },
    "Gränges AB": {
        "target_contract_value_eur": "€6,200,000",
        "win_probability_pct": 74,
        "expected_value_eur": "€4,588,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Smart Mill Analytics & CSRD Carbon Mesh on Microsoft Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Rolling Mill Telemetry & Carbon Audit",
                "action": "Brief Gränges VP Sustainability and Global Operations Director on automotive PCF requirements. Submit Microsoft ECIF discovery funding request.",
                "deliverable": "Manufacturing Pain-Point Dossier & Approved ECIF Allocation"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-Plant Architecture Design",
                "action": "Joint architectural blueprint session with Raihan Chowdhury (Microsoft Specialist) and Claudio Pierpaoli (Infra DSE) for hybrid plant connectivity.",
                "deliverable": "Enterprise Fabric Blueprint & Global Governance Framework"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "Finspång Plant PoV & Carbon Proof",
                "action": "Deploy Cegeka 4-Week Accelerator at Finspång rolling mill. Ingest real-time historian streams and automate coil carbon calculation.",
                "deliverable": "Working Fabric Solution with Direct Lake Dashboards"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Global Enterprise Agreement Close",
                "action": "Present validated energy and scrap savings to Executive Committee. Execute 3-year contract covering Swedish, US, and European plants.",
                "deliverable": "Signed 3-Year Master Services Agreement & Scope of Work"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Quantified mill scrap reduction (€3.4M/yr), energy savings, and 6-month payback.",
                "objection_handler": "Demonstrate clear ROI where a 1% scrap reduction in Finspång pays for the entire software investment in 4 months."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "Unifying disparate plant data lakes, single-pane governance with Purview, and Power BI integration.",
                "objection_handler": "Position Fabric OneLake as a logical data mesh overlay that connects existing plant historians without rip-and-replace."
            },
            "operational_sponsor": {
                "role": "Global Operations Director",
                "focus": "Real-time rolling mill defect alerts and cross-plant OEE benchmarking.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing reference case demonstrating real-time plant optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Zero-trust manufacturing OT/IT segmentation and secure cross-border cloud telemetry.",
                "objection_handler": "Highlight Azure ExpressRoute connectivity and Microsoft Purview sensitivity labeling."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50k ECIF funding; involve Claudio Pierpaoli (Infra DSE) for hybrid OT gateway review at Day 20.",
            "what_partner_does": "Provide $50k in ECIF partner subsidies; assign Azure manufacturing specialist architects; provide MACC commitment drawdown credits."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50k ECIF funding; involve Claudio Pierpaoli (Infra DSE) for hybrid OT gateway review at Day 20.",
            "what_databricks_does": "Provide $50k in ECIF partner subsidies; assign Azure manufacturing specialist architects; provide MACC commitment drawdown credits."
        },
        "immediate_next_action": "Schedule an executive briefing with Gränges VP Sustainability and Global Operations Director on automated coil-level carbon passports and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Plant engineering hesitation regarding cloud OT security. Mitigation: Utilize read-only Azure IoT Edge gateways air-gapped from mill control networks."
    },
    "Advokatfirman Vinge KB": {
        "target_contract_value_eur": "€3,600,000",
        "win_probability_pct": 80,
        "expected_value_eur": "€2,880,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Sovereign Legal GenAI & Purview Governance on Microsoft Azure",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Confidential Legal AI Readiness Review",
                "action": "Brief Managing Partner and Head of Knowledge Management on sovereign Azure OpenAI in Sweden Central. Submit Microsoft AMMP assessment.",
                "deliverable": "Approved Information Governance Scope & AMMP Subsidy Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Purview Ethical Wall & Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) demonstrating air-gapped Azure AI Search with zero retention.",
                "deliverable": "Sovereign AI Security Architecture & Bar Compliance Briefing"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Virtual Data Room Diligence PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart in Vinge's tenant. Index 2,000 sanitized M&A contracts and benchmark clause extraction speed.",
                "deliverable": "Working Legal Copilot Prototype & Associate Usability Report"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Partnership Board Approval & Rollout",
                "action": "Present time-savings benchmark to Vinge Partner Committee. Finalize 3-year enterprise agreement drawing down Azure MACC.",
                "deliverable": "Signed 3-Year Enterprise Services Contract & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Managing Partner / Finance Partner",
                "focus": "Associate billable leverage (4.2x productivity), fixed-fee win rate, and 5-month payback.",
                "objection_handler": "Show that sovereign GenAI allows associates to review 10x more documents per deal without increasing headcount."
            },
            "technical_champion": {
                "role": "Chief Digital Officer / Head of IT",
                "focus": "Air-gapped Azure OpenAI (Sweden Central), Microsoft Purview data boundary, and seamless M365 integration.",
                "objection_handler": "Demonstrate that data remains strictly encrypted in tenant with zero training on client prompts."
            },
            "operational_sponsor": {
                "role": "Head of Knowledge Management",
                "focus": "Instant semantic retrieval across 40 years of Vinge precedents and automated clause drafting.",
                "objection_handler": "Share Cegeka's CERA case study demonstrating secure AI knowledge search in regulated financial services."
            },
            "procurement_infosec": {
                "role": "Head of InfoSec & Compliance",
                "focus": "Swedish Bar Association ethics guidelines, ISO 27001, and tamper-proof query logging.",
                "objection_handler": "Present Microsoft's official legal commitments regarding zero data retention and dedicated regional tenant isolation."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5; loop in Paul Boland (Security DSE) at Day 15 for compliance review; executive sign-off at Day 50.",
            "what_partner_does": "Allocate $40,000 in Microsoft ECIF AI vouchers; provide legal sector compliance verification; endorse Cegeka as premier Nordic AI partner."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5; loop in Paul Boland (Security DSE) at Day 15 for compliance review; executive sign-off at Day 50.",
            "what_databricks_does": "Allocate $40,000 in Microsoft ECIF AI vouchers; provide legal sector compliance verification; endorse Cegeka as premier Nordic AI partner."
        },
        "immediate_next_action": "Schedule a 30-minute discovery session with Vinge's Head of Knowledge Management and CDO on sovereign M&A contract diligence and share Cegeka CERA benchmark.",
        "deal_blocker_mitigation": "Blocker: Extreme sensitivity regarding legal professional privilege. Mitigation: Provide legally binding Microsoft Sweden Central sovereign deployment architecture."
    },
    "Motoman Robotics Europe AB": {
        "target_contract_value_eur": "€4,400,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,300,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "IoT Fleet Telemetry & Robotics-as-a-Service Modernization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Robot Fleet Connectivity & AMMP Sizing",
                "action": "Engage VP Customer Service and Head of Software on recurring SLA revenue opportunities. Submit Microsoft AMMP voucher.",
                "deliverable": "Fleet Connectivity Scoping Document & AMMP Allocation"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Edge-to-Fabric Real-Time Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing sub-second telemetry ingestion.",
                "deliverable": "Validated Edge-to-Cloud IoT Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Robot Fleet Diagnostic PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 100 industrial robots. Demonstrate automated bearing wear anomaly alerts.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Commercial RaaS Rollout Agreement",
                "action": "Present validated warranty reduction and SLA revenue metrics to Executive Management. Finalize 3-year enterprise rollout.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "CFO / VP Aftermarket",
                "focus": "New recurring service revenues, warranty claims reduction (€2.4M/yr), and 6-month payback.",
                "objection_handler": "Show how recurring predictive maintenance contracts increase customer lifetime value by 35%."
            },
            "technical_champion": {
                "role": "Head of Robotics Software R&D",
                "focus": "Real-time KQL queries, containerized edge deployment with Azure IoT Operations, and OneLake.",
                "objection_handler": "Fabric handles high-frequency robotic telemetry with zero cluster configuration overhead."
            },
            "operational_sponsor": {
                "role": "Head of Field Service Europe",
                "focus": "First-time fix rates, remote diagnostic triage, and technician mobile enablement.",
                "objection_handler": "Share Cegeka's Bridgestone IoT case study proving rapid field service optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "OT security standards (IEC 62443), client network isolation, and encryption in transit.",
                "objection_handler": "Azure IoT Edge provides outbound-only TLS 1.3 telemetry connections requiring zero incoming firewall ports."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for IoT Hub sizing at Day 18.",
            "what_partner_does": "Provide $50,000 AMMP ACR voucher; assign Azure IoT specialist engineers; provide executive alignment with Microsoft Europe manufacturing leads."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for IoT Hub sizing at Day 18.",
            "what_databricks_does": "Provide $50,000 AMMP ACR voucher; assign Azure IoT specialist engineers; provide executive alignment with Microsoft Europe manufacturing leads."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Motoman's VP Customer Service on predictive robot telemetry and share Cegeka Austrotherm IoT case study.",
        "deal_blocker_mitigation": "Blocker: OEM customer reluctance to connect factory robots to cloud. Mitigation: Implement outbound-only Azure IoT Operations with local data buffering."
    },
    "Etac AB": {
        "target_contract_value_eur": "€3,800,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€2,926,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "MDR Compliance & Supply Chain Mesh on Microsoft Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Regulatory Traceability & Supply Chain Scan",
                "action": "Engage VP Quality & Regulatory and CIO on EU MDR audit readiness. Submit Microsoft AMMP assessment.",
                "deliverable": "Regulatory Gap Analysis & AMMP Subsidy Confirmation"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-ERP Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Alok Ranjan Sinha (Apps DSE) demonstrating unified ERP ingestion.",
                "deliverable": "OneLake Medical Device Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week MDR Lineage & Inventory PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting two primary ERP instances. Automate batch traceability reporting in Power BI.",
                "deliverable": "Working Fabric Solution with Direct Lake Dashboards"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement & Group Rollout",
                "action": "Present validated inventory reduction and audit time savings to Executive Board. Finalize 3-year strategic enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Contract & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Working capital optimization (€1.75M/yr), inventory reduction, and 7-month payback.",
                "objection_handler": "Show how synchronizing European inventory reduces excess stock while AMMP covers onboarding fees."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake zero-copy virtualization across disparate ERPs and Purview regulatory governance.",
                "objection_handler": "Fabric integrates with IFS, Dynamics, and SAP out of the box using pre-built Data Factory connectors."
            },
            "operational_sponsor": {
                "role": "VP Quality & Regulatory",
                "focus": "Instant EU MDR audit compliance and automated technical file generation.",
                "objection_handler": "Share Cegeka's LRM medEmotion reference case demonstrating medical compliance modernization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "GDPR compliance for patient trial data and role-based access control.",
                "objection_handler": "Microsoft Purview provides row-level security and automated PII data masking."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Alok Ranjan Sinha (Apps DSE) at Day 18 for ERP connector review.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign healthcare data architecture specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Alok Ranjan Sinha (Apps DSE) at Day 18 for ERP connector review.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign healthcare data architecture specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery session with Etac's VP Quality & Regulatory on automated EU MDR batch traceability and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Concern over disrupting active ERP transactional databases. Mitigation: Ingest read-only change data capture (CDC) feeds into Fabric OneLake."
    },
    "OVAKO HOLDINGS AB": {
        "target_contract_value_eur": "€6,800,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€5,100,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Green Steel Decarbonization & Fabric Real-Time Intelligence",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Melt Shop Energy & Telemetry Assessment",
                "action": "Engage Head of Decarbonization and Mill Director on electric arc furnace power optimization. Submit Microsoft ECIF co-funding request.",
                "deliverable": "Melt Shop Optimization Scope & ECIF Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Fabric Architecture Blueprint",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL telemetry queries.",
                "deliverable": "Real-Time Metallurgy Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Hofors Melt Shop PoV",
                "action": "Deploy Cegeka 4-Week Accelerator at Hofors mill. Ingest real-time furnace telemetry and demonstrate dynamic power cost alerts.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Agreement Close",
                "action": "Present validated energy reduction and carbon accounting accuracy to Executive Committee. Execute 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Scope of Work"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Electricity cost reduction (€3.9M/yr), scrap alloy optimization, and 6-month payback.",
                "objection_handler": "Show how dynamic power optimization during Nordic peak spot tariff hours yields rapid multi-million payback."
            },
            "technical_champion": {
                "role": "Mill Production Director / Head of IT",
                "focus": "Sub-second sensor ingestion, OT cybersecurity isolation, and OneLake analytics.",
                "objection_handler": "Fabric Real-Time Hub processes millions of furnace telemetry events per second with zero server management."
            },
            "operational_sponsor": {
                "role": "Head of Decarbonization",
                "focus": "Automated hydrogen electrolysis tracking and product-level Scope 1-3 carbon passports.",
                "objection_handler": "Share Cegeka's Fluvius energy telemetry case study demonstrating industrial grid data optimization."
            },
            "procurement_infosec": {
                "role": "CISO & Head of Procurement",
                "focus": "NIS2 compliance, plant OT safety isolation, and Azure MACC drawdown.",
                "objection_handler": "Azure IoT Edge provides uni-directional data diode compatibility meeting strict industrial security standards."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; involve Geoff Scott (Data & AI DSE) for Real-Time Hub architecture at Day 18.",
            "what_partner_does": "Allocate $50,000 ECIF voucher; provide specialized heavy industry solution architects; align MACC consumption commitment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; involve Geoff Scott (Data & AI DSE) for Real-Time Hub architecture at Day 18.",
            "what_databricks_does": "Allocate $50,000 ECIF voucher; provide specialized heavy industry solution architects; align MACC consumption commitment."
        },
        "immediate_next_action": "Schedule an executive briefing with Ovako's Head of Decarbonization and Hofors Mill Director on automated green steel carbon passports and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Concern over real-time OT network latency. Mitigation: Deploy edge filtering on Azure IoT Edge gateways sending only aggregated telemetry to Fabric."
    },
    "Cejn AB": {
        "target_contract_value_eur": "€3,400,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€2,652,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Precision Manufacturing & Global Distribution on Microsoft Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Thermal Management Quality & AMMP Review",
                "action": "Engage VP Thermal Management and CIO on data center cooling qualification. Submit Microsoft AMMP voucher.",
                "deliverable": "Thermal Telemetry Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Subsidiary Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Direct Lake reporting.",
                "deliverable": "Fabric Reference Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Leak-Test Analytics PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Skövde factory test rigs. Automate customer quality certificate generation.",
                "deliverable": "Working Fabric Solution & Customer Certificate Generator"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Global Enterprise Agreement Close",
                "action": "Present validated lead-time and scrap savings to Cejn Management. Execute 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Contract & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Inventory turnover optimization (€1.6M/yr), AMMP subsidy offset, and 7-month payback.",
                "objection_handler": "Microsoft AMMP covers initial deployment fees while Fabric consolidates BI tool licenses."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "Retiring aging SQL servers, automated Data Factory pipelines, and Power BI integration.",
                "objection_handler": "Fabric eliminates ETL complexity with native OneLake shortcuts to existing data sources."
            },
            "operational_sponsor": {
                "role": "VP Thermal Management & Sales",
                "focus": "Automated leak test certification for data center customers and faster custom quote turnaround.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating automated quality telemetry."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Secure cloud boundary, IP protection for proprietary coupling patents, and Purview governance.",
                "objection_handler": "All proprietary CAD and test data is protected with Microsoft Purview encryption."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) at Day 18 for Data Factory pipeline review.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; provide dedicated Azure technical specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) at Day 18 for Data Factory pipeline review.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; provide dedicated Azure technical specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Cejn's VP Thermal Management on automated data center leak test certification and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: IT team bandwidth constraints. Mitigation: Cegeka delivers full turnkey 4-Week Jumpstart requiring less than 5 hours/week from Cejn staff."
    },
    "Be Group Holding AB": {
        "target_contract_value_eur": "€4,600,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,496,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Supply Chain Pricing Automation & Fabric Data Lake",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Steel Pricing & Inventory Assessment",
                "action": "Engage Commercial Director and Supply Chain Director on pricing volatility. Submit Microsoft ECIF discovery funding request.",
                "deliverable": "Pricing Friction Analysis & ECIF Subsidy Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Pricing Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Fabric pricing models.",
                "deliverable": "Dynamic Pricing Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Malmö Service Center PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Movex ERP. Demonstrate automated RFQ processing with Azure OpenAI.",
                "deliverable": "Working Fabric Solution & RFQ Extraction Demo"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Agreement Close",
                "action": "Present validated margin improvement and inventory turnover metrics to Executive Committee. Execute 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Services Contract & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Gross margin protection (€2.8M/yr), dead stock reduction, and 6-month payback.",
                "objection_handler": "Show how dynamic pricing protects margins against steel coil deflation while ECIF funds the initial build."
            },
            "technical_champion": {
                "role": "Group CIO / IT Director",
                "focus": "Decoupling legacy AS400 with OneLake, zero-copy Direct Lake reporting, and modern Azure security.",
                "objection_handler": "Fabric integrates with Movex and legacy ERPs without requiring risky database modifications."
            },
            "operational_sponsor": {
                "role": "Commercial Director & Sales VP",
                "focus": "Instant RFQ response times and automated customer steel certificates.",
                "objection_handler": "Share Cegeka's Bridgestone supply chain case study demonstrating real-time order processing."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Commercial price data confidentiality and Microsoft Purview sensitivity labeling.",
                "objection_handler": "Microsoft Purview enforces granular encryption ensuring competitive pricing never leaks."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning pricing review at Day 18.",
            "what_partner_does": "Allocate $50,000 ECIF voucher; assign retail/distribution data architects; provide MACC contract drawdown credits."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning pricing review at Day 18.",
            "what_databricks_does": "Allocate $50,000 ECIF voucher; assign retail/distribution data architects; provide MACC contract drawdown credits."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with BE Group's Commercial Director on algorithmic steel pricing and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Entrenched reliance on legacy Movex ERP spreadsheets. Mitigation: Build Fabric dashboards that directly feed existing sales workflows without interface disruption."
    },
    "AB Fagerhult": {
        "target_contract_value_eur": "€5,200,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,900,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Connected IoT Lighting & Building Analytics on Microsoft Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Smart Building Telemetry & AMMP Review",
                "action": "Engage Head of Smart Lighting and CIO on Organic Response cloud scaling. Submit Microsoft AMMP voucher.",
                "deliverable": "Smart Lighting Architecture Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Fabric Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL telemetry queries.",
                "deliverable": "Fabric Real-Time Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Connected Luminaire PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 1,000 Organic Response nodes. Deliver real-time occupancy heatmaps in Power BI.",
                "deliverable": "Working Fabric Telemetry Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement & Group Rollout",
                "action": "Present validated recurring software revenue model to Executive Management. Finalize 3-year strategic enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "New recurring software revenues, EPBD compliance demand, and 7-month payback.",
                "objection_handler": "Show how recurring SaaS analytics subscriptions transform one-off hardware sales into high-margin ARR."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "Unifying 12 brand data silos, OneLake single-pane governance, and serverless scalability.",
                "objection_handler": "Fabric integrates multi-brand telemetry into a single OneLake without requiring centralized ERP consolidation."
            },
            "operational_sponsor": {
                "role": "Head of Smart Lighting Solutions",
                "focus": "Scalable cloud backbone for Organic Response and turnkey facility manager dashboards.",
                "objection_handler": "Share Cegeka's Fluvius smart grid case study demonstrating massive telemetry ingestion."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "GDPR employee privacy in office occupancy tracking and Azure security compliance.",
                "objection_handler": "Organic Response sensors capture anonymous heat signatures; Purview ensures zero PII storage."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; provide Azure IoT and Digital Twin specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; provide Azure IoT and Digital Twin specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Fagerhult's Head of Smart Lighting on real-time Organic Response telemetry and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Concern over multi-brand data integration complexity. Mitigation: Deploy Fabric OneLake shortcuts allowing each brand to maintain autonomy while rolling up group analytics."
    },
    "Mycronic AB": {
        "target_contract_value_eur": "€5,800,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€4,524,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Semiconductor Equipment Telemetry & Sovereign Purview Governance",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Cleanroom Telemetry & IP Security Review",
                "action": "Engage VP Pattern Generators and CISO on predictive laser diagnostics. Submit Microsoft AMMP assessment.",
                "deliverable": "Cleanroom Diagnostics Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Sovereign Fabric Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing Purview IP encryption.",
                "deliverable": "Sovereign Telemetry Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Laser Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting test pattern generator. Benchmark predictive laser wear alerts in Fabric.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated warranty and uptime metrics to Executive Committee. Execute 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Scope of Work"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Cleanroom SLA protection (€3.7M/yr), recurring service margin growth, and 6-month payback.",
                "objection_handler": "Show how predictive laser diagnostics prevent multi-million customer compensation claims."
            },
            "technical_champion": {
                "role": "VP Pattern Generators / CTO",
                "focus": "Sub-micron optical telemetry ingestion, serverless KQL queries, and Azure ML integration.",
                "objection_handler": "Fabric Real-Time Hub processes millions of machine events per second with microsecond query speed."
            },
            "operational_sponsor": {
                "role": "Head of Global Service & Aftermarket",
                "focus": "Global fab uptime, remote diagnostic triage, and first-time fix rates.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating predictive equipment diagnostics."
            },
            "procurement_infosec": {
                "role": "Chief Information Security Officer (CISO)",
                "focus": "Safeguarding cutting-edge Swedish optical IP and strict tenant encryption.",
                "objection_handler": "Microsoft Purview and Azure Confidential Computing guarantee zero unauthorized access to optical algorithms."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for sovereign IP governance.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign Azure High-Performance Computing and IoT specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for sovereign IP governance.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign Azure High-Performance Computing and IoT specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Mycronic's VP Pattern Generators on predictive laser diagnostics and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Stringent semiconductor fab confidentiality requirements. Mitigation: Deploy sovereign Azure Confidential Computing with customer-managed encryption keys."
    },
    "HÖGANAS AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,150,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Metallurgy AI & High-Temperature Process Optimization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Metallurgical Process & AMMP Assessment",
                "action": "Engage Head of Metallurgy R&D and Operations Director on atomization scrap reduction. Submit Microsoft AMMP voucher.",
                "deliverable": "Atomization Optimization Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Metallurgy Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Azure ML integration.",
                "deliverable": "Metallurgy Data Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Atomization Quality PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart at Höganäs main plant. Predict particle size distribution with 95%+ accuracy.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated scrap reduction and gas energy savings to Executive Management. Finalize 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Atomization scrap reduction (€2.5M/yr), furnace gas savings, and 7-month payback.",
                "objection_handler": "Show how reducing atomization off-spec powder by 2% pays for the entire software rollout in 5 months."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake data unification, eliminating legacy historian licensing, and Azure ML integration.",
                "objection_handler": "Fabric integrates seamlessly with existing plant SCADA systems using lightweight Azure IoT Edge."
            },
            "operational_sponsor": {
                "role": "Operations Director",
                "focus": "Furnace energy efficiency, consistent powder quality, and operator decision support.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating energy and scrap reduction."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Proprietary alloy formulation security and Microsoft Purview data governance.",
                "objection_handler": "Microsoft Purview encrypts chemical recipes ensuring proprietary metallurgy IP never leaks."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; provide dedicated Azure manufacturing specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; provide dedicated Azure manufacturing specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Höganäs' Head of Metallurgy R&D on predictive atomization quality and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Proprietary chemical recipe confidentiality concerns. Mitigation: Deploy private, single-tenant Azure ML workspaces with customer-managed keys."
    },
    "Hydroscand Group AB": {
        "target_contract_value_eur": "€4,500,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,420,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Field Service Telemetry & Mobile Inventory Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Mobile Service & Inventory Scoping",
                "action": "Engage MD SlangAkuten and Supply Chain Director on first-time fix rates. Submit Microsoft AMMP voucher.",
                "deliverable": "Field Service Scoping Document & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Dispatch Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Alok Ranjan Sinha (Apps DSE) showing mobile app integration.",
                "deliverable": "Mobile Telemetry Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Mobile Van Inventory PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 20 mobile service vans. Benchmark dynamic replenishment alerts in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Mobile App Demo"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated first-time fix improvement and inventory reduction to Executive Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "First-time fix rate improvement (€2.2M/yr), van stock optimization, and 7-month payback.",
                "objection_handler": "Show how raising first-time fix rates by 8% unlocks thousands of additional billable mobile service hours."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "Real-time Fabric telemetry, native Power Apps mobile integration, and Azure security.",
                "objection_handler": "Fabric integrates seamlessly with mobile field apps via lightweight REST APIs with offline caching."
            },
            "operational_sponsor": {
                "role": "Managing Director SlangAkuten",
                "focus": "Sub-60 minute emergency response times and technician mobile enablement.",
                "objection_handler": "Share Cegeka's Bridgestone mobile fleet case study demonstrating real-time technician dispatching."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Mobile device management (MDM) security, driver GPS privacy, and GDPR compliance.",
                "objection_handler": "Microsoft Intune and Purview enforce strict device compliance and location data anonymization."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Alok Ranjan Sinha (Apps DSE) for Power Apps review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; provide Azure IoT and Mobile Solutions specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Alok Ranjan Sinha (Apps DSE) for Power Apps review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; provide Azure IoT and Mobile Solutions specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Hydroscand's MD SlangAkuten on mobile van first-time fix optimization and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Mobile connectivity blackspots in remote forestry/construction sites. Mitigation: Implement offline-first local caching in mobile diagnostic apps."
    },
    "VBG AB Publ": {
        "target_contract_value_eur": "€4,600,000",
        "win_probability_pct": 74,
        "expected_value_eur": "€3,404,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Heavy Vehicle IoT & Divisional Harmonization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Divisional Architecture & AMMP Scoping",
                "action": "Engage VP Truck Equipment and Group IT Director on divisional ERP harmonization. Submit Microsoft AMMP voucher.",
                "deliverable": "Harmonization Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-Division Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing unified OneLake schema.",
                "deliverable": "Enterprise OneLake Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Coupling Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting test truck telemetry. Deliver automated fatigue calculation in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated warranty and testing cycle savings to Executive Board. Finalize 3-year enterprise rollout agreement.",
                "deliverable": "Signed 3-Year Enterprise Contract & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Warranty claims reduction (€2.3M/yr), testing cycle time compression, and 7-month payback.",
                "objection_handler": "Show how predictive coupling analytics prevents expensive safety recalls while AMMP covers startup fees."
            },
            "technical_champion": {
                "role": "Group IT Director / VP IT",
                "focus": "Unifying disparate divisional ERPs with OneLake and automating Power BI Direct Lake reporting.",
                "objection_handler": "OneLake shortcuts allow each division to keep its local ERP while executive reporting is automated."
            },
            "operational_sponsor": {
                "role": "VP Truck Equipment",
                "focus": "Smart coupling telemetry, OEM digital certification, and R&D fatigue validation.",
                "objection_handler": "Share Cegeka's Bridgestone vehicle telemetry case study demonstrating fleet sensor analytics."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Protecting vehicle telemetry IP and automotive cybersecurity compliance (ISO 21434).",
                "objection_handler": "Microsoft Purview provides cryptographic tenant encryption satisfying automotive security standards."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign automotive industry solution architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign automotive industry solution architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with VBG's VP Truck Equipment on sensorized coupling telemetry and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Divisional autonomy resistance across brands. Mitigation: Deploy Fabric OneLake domains giving each division full data ownership while rolling up group KPIs."
    },
    "CORRAL PETROLEUM HOLDINGS AB": {
        "target_contract_value_eur": "€9,500,000",
        "win_probability_pct": 70,
        "expected_value_eur": "€6,650,000",
        "target_close_quarter": "Q1 2027",
        "deal_motion": "Refinery OT Historian Modernization & Green Fuel Analytics on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Refinery Telemetry & NIS2 Scoping",
                "action": "Engage VP Refining Operations and CIO on Lysekil/Gothenburg refinery historian integration. Submit Microsoft ECIF voucher.",
                "deliverable": "Refinery Telemetry Scoping Plan & ECIF Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Historian Fabric Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL historian streaming.",
                "deliverable": "Refinery Real-Time Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Hydrocracker Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Lysekil hydrocracker historian. Benchmark real-time yield prediction in Power BI.",
                "deliverable": "Working Fabric Historian Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Agreement Close",
                "action": "Present validated refining margin expansion (€6.5M/yr) to Preem Executive Committee. Execute 3-year strategic agreement.",
                "deliverable": "Signed 3-Year Strategic Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Refining crack spread optimization (€6.5M/yr), catalyst longevity, and 5-month payback.",
                "objection_handler": "Show how real-time bio-feedstock margin optimization generates millions in additional quarterly EBITDA."
            },
            "technical_champion": {
                "role": "CIO / Head of IT & OT",
                "focus": "Retiring expensive proprietary historian licensing, NIS2 cybersecurity compliance, and OneLake.",
                "objection_handler": "Azure IoT Edge gateways provide read-only, diode-isolated historian ingestion meeting strict NIS2 rules."
            },
            "operational_sponsor": {
                "role": "VP Refining Operations",
                "focus": "Catalytic reactor yield optimization, flare reduction, and real-time process monitoring.",
                "objection_handler": "Share Cegeka's Fluvius industrial energy case study demonstrating massive telemetry ingestion."
            },
            "procurement_infosec": {
                "role": "CISO & Head of Industrial Security",
                "focus": "Critical infrastructure compliance, air-gapped refinery safety, and Azure sovereign security.",
                "objection_handler": "Microsoft Azure Sweden Central provides certified sovereign infrastructure with Purview auditability."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $50,000 ECIF voucher; assign energy/refining industry principal architects; support multi-million MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $50,000 ECIF voucher; assign energy/refining industry principal architects; support multi-million MACC contract alignment."
        },
        "immediate_next_action": "Schedule an executive briefing with Preem's VP Refining Operations and CIO on real-time refinery historian analytics and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Strict refinery OT air-gap and safety regulations. Mitigation: Deploy hardware unidirectional data diodes streaming historian events into Azure IoT Edge."
    },
    "Recipharm AB": {
        "target_contract_value_eur": "€5,600,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€4,256,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Pharma 4.0 GxP Compliance & Fabric OneLake",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "GxP Compliance & Batch Release Scoping",
                "action": "Engage Global Head of Quality and CIO on paperless batch release acceleration. Submit Microsoft AMMP voucher.",
                "deliverable": "GxP Validation Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Validated OneLake Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing Purview GxP auditability.",
                "deliverable": "GxP Compliant Fabric Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Sterile Fill-Finish PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting sterile fill line. Benchmark deviation detection speed in Power BI.",
                "deliverable": "Working Fabric Solution & QP Release Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Global Enterprise Agreement Close",
                "action": "Present validated quarantine reduction (€3.2M/yr) to Recipharm Executive Committee. Finalize 3-year enterprise rollout.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Quarantine inventory reduction (€3.2M/yr), faster cash conversion, and 6-month payback.",
                "objection_handler": "Show how compressing batch release from 14 days to 48 hours unlocks tens of millions in working capital."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake multi-site data mesh, retiring legacy MES reporting tools, and Microsoft Purview compliance.",
                "objection_handler": "Microsoft provides formal GxP qualification documentation and audit rights for regulated Azure services."
            },
            "operational_sponsor": {
                "role": "Global Head of Quality & QP",
                "focus": "Automated batch deviation review, electronic signatures (21 CFR Part 11), and regulatory audit readiness.",
                "objection_handler": "Share Cegeka's LRM medEmotion case study demonstrating GxP-validated life sciences compliance."
            },
            "procurement_infosec": {
                "role": "CISO & Head of Regulatory Compliance",
                "focus": "Data integrity, immutable audit logging, and FDA/EMA data sovereignty.",
                "objection_handler": "Microsoft Purview provides immutable audit trails and cryptographic tamper-evident logging."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for GxP validation review.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign healthcare and life sciences principal architects; provide MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for GxP validation review.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign healthcare and life sciences principal architects; provide MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Recipharm's Global Head of Quality on accelerating batch release cycle times and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Stringent GxP software re-validation concerns. Mitigation: Leverage Cegeka's pre-packaged GxP qualification accelerators for Microsoft Fabric."
    },
    "Dellner Invest AB": {
        "target_contract_value_eur": "€3,800,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€2,850,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Railway Telemetry & Condition-Based Maintenance on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Rail Telemetry & Aftermarket Scoping",
                "action": "Engage Head of Aftermarket and Chief Engineer on predictive maintenance contracts. Submit Microsoft AMMP voucher.",
                "deliverable": "Condition-Based Maintenance Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Fabric Rail Telemetry Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL streaming.",
                "deliverable": "Rail Telemetry Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Passenger Coupler PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting test rig sensor data. Benchmark fatigue prediction accuracy in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated warranty and overhaul savings to Executive Management. Finalize 3-year strategic enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Overhaul cost reduction (€1.9M/yr), recurring aftermarket ARR growth, and 7-month payback.",
                "objection_handler": "Show how condition-based servicing contracts generate multi-year high-margin service revenue."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake telemetry unification, Azure IoT Edge train connectivity, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates seamlessly with train builder telemetry without requiring complex custom ETL pipelines."
            },
            "operational_sponsor": {
                "role": "Head of Aftermarket & Service",
                "focus": "Predictive maintenance alerts for rail operators and spare parts inventory optimization.",
                "objection_handler": "Share Cegeka's Bridgestone vehicle telemetry case study demonstrating fleet predictive maintenance."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Rail cybersecurity standards (TS 50701) and protecting proprietary coupler design IP.",
                "objection_handler": "Microsoft Purview and Azure IoT Edge provide certified end-to-end encryption satisfying rail safety norms."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign transportation IoT specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign transportation IoT specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Dellner's Head of Aftermarket on condition-based coupler servicing and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Complex data sharing agreements with train operators. Mitigation: Deploy Fabric OneLake multi-tenant workspaces allowing controlled data sharing between train builder and operator."
    },
    "Swedish Orphan Biovitrum": {
        "target_contract_value_eur": "€6,400,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€4,928,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Rare Disease Clinical Data Mesh & Sovereign Purview Governance",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Clinical Data Mesh & Sovereign Scoping",
                "action": "Engage Chief Medical Officer and DPO on rare disease registry harmonization. Submit Microsoft AMMP voucher.",
                "deliverable": "Clinical Data Governance Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Sovereign Healthcare Fabric Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing Purview pseudonymization.",
                "deliverable": "Sovereign Healthcare Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Patient Registry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting sanitized patient cohort. Deliver real-world efficacy dashboard in Power BI.",
                "deliverable": "Working Fabric Registry Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Agreement Close",
                "action": "Present validated clinical trial acceleration metrics to Sobi Executive Committee. Finalize 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Clinical trial cycle time compression (€3.6M/yr), faster drug reimbursement, and 6-month payback.",
                "objection_handler": "Show how accelerating rare disease market access by 3 months generates tens of millions in patient therapy revenue."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake zero-trust data mesh, retiring legacy CRO data silos, and Microsoft Purview compliance.",
                "objection_handler": "Microsoft Purview provides automated cryptographic classification and automated HIPAA/GDPR policy enforcement."
            },
            "operational_sponsor": {
                "role": "Chief Medical Officer",
                "focus": "Instant real-world evidence generation for FDA/EMA reimbursement negotiations.",
                "objection_handler": "Share Cegeka's LRM medEmotion clinical data case study demonstrating secure medical analytics."
            },
            "procurement_infosec": {
                "role": "Data Protection Officer (DPO) & CISO",
                "focus": "Patient data pseudonymization, cross-border health data sovereignty, and ISO 27001.",
                "objection_handler": "All data resides strictly within Azure Sweden Central with customer-managed cryptographic keys."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for healthcare sovereignty review.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign healthcare and life sciences principal architects; provide MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for healthcare sovereignty review.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign healthcare and life sciences principal architects; provide MACC contract alignment."
        },
        "immediate_next_action": "Schedule an executive briefing with Sobi's Chief Medical Officer and CIO on sovereign real-world evidence data mesh and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Highly stringent cross-border patient privacy regulations. Mitigation: Deploy sovereign Azure Confidential Computing with automated cryptographic patient anonymization."
    },
    "EQT Holdings AB": {
        "target_contract_value_eur": "€8,400,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€6,300,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Portfolio Value Creation Lakehouse & Confidential Deal GenAI on Azure",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Motherbrain & Portfolio Mesh Scoping",
                "action": "Engage Global Head of Motherbrain and CFO on cross-portfolio data unification. Submit Microsoft ECIF voucher.",
                "deliverable": "Portfolio Analytics Scoping Plan & ECIF Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Confidential Azure Architecture Blueprint",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing ethical walls.",
                "deliverable": "Sovereign Financial Fabric Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Deal Screening & ESG PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart indexing historical deal memos. Benchmark AI diligence accuracy in Azure OpenAI.",
                "deliverable": "Working Fabric Solution & Deal Copilot Prototype"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Partnership Agreement Close",
                "action": "Present validated investment team productivity and LP reporting savings to EQT Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Portfolio value creation tracking (€4.8M/yr), LP reporting automation, and 5-month payback.",
                "objection_handler": "Show how automating monthly portfolio financial collection saves thousands of investment team hours."
            },
            "technical_champion": {
                "role": "Global Head of Motherbrain / CDO",
                "focus": "OneLake data virtualization across portfolio companies and private Azure OpenAI in Sweden Central.",
                "objection_handler": "Fabric OneLake shortcuts enable portfolio companies to share KPIs without changing their underlying cloud stacks."
            },
            "operational_sponsor": {
                "role": "Head of Sustainability / ESG",
                "focus": "Automated SFDR Article 8/9 compliance and audited carbon reporting across portfolio companies.",
                "objection_handler": "Share Cegeka's CERA regulated financial services case study demonstrating audit-ready data mesh architecture."
            },
            "procurement_infosec": {
                "role": "Head of Cyber & Compliance",
                "focus": "SEC / Swedish FSA regulatory compliance, ethical walls between deal teams, and zero data leakage.",
                "objection_handler": "Microsoft Purview provides cryptographic ethical walls ensuring deal teams cannot see competing portfolio metrics."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Paul Boland (Security DSE) at Day 15 for financial sector sovereignty review.",
            "what_partner_does": "Allocate $50,000 ECIF voucher; assign financial services and AI principal architects; provide MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 ECIF funding; loop in Paul Boland (Security DSE) at Day 15 for financial sector sovereignty review.",
            "what_databricks_does": "Allocate $50,000 ECIF voucher; assign financial services and AI principal architects; provide MACC contract alignment."
        },
        "immediate_next_action": "Schedule an executive briefing with EQT's Global Head of Motherbrain and CFO on confidential deal diligence GenAI and share Cegeka CERA benchmark.",
        "deal_blocker_mitigation": "Blocker: Extreme sensitivity regarding material non-public information (MNPI). Mitigation: Deploy air-gapped Azure OpenAI instances with cryptographic ethical walls and zero logging."
    },
    "BEIJER ELECTRONICS AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,192,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Industrial Edge Telemetry & Connected Hardware Modernization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Edge Telemetry & SaaS Scoping",
                "action": "Engage Head of Westermo R&D and VP Business Development on edge cloud monetization. Submit Microsoft AMMP voucher.",
                "deliverable": "Connected Edge Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Edge Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL telemetry queries.",
                "deliverable": "Edge-to-Cloud Fabric Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Rugged Switch Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 100 Westermo switches. Deliver real-time network topology heatmaps in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated recurring software revenue model to Beijer Electronics Management. Finalize 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Recurring SaaS revenue growth (€2.1M/yr), hardware margin expansion, and 7-month payback.",
                "objection_handler": "Show how bundling hardware with cloud edge diagnostics transforms one-off hardware sales into recurring ARR."
            },
            "technical_champion": {
                "role": "Head of Westermo R&D / VP Engineering",
                "focus": "Lightweight containerized edge agents (Azure IoT Operations), sub-second KQL queries, and OneLake.",
                "objection_handler": "Azure IoT Operations runs seamlessly on resource-constrained embedded Linux switches."
            },
            "operational_sponsor": {
                "role": "VP Business Development & Service",
                "focus": "Turnkey remote management portal for rail and utility network operators.",
                "objection_handler": "Share Cegeka's Fluvius utility telemetry case study demonstrating massive IoT scalability."
            },
            "procurement_infosec": {
                "role": "Head of Cybersecurity",
                "focus": "Critical infrastructure compliance (NIS2, IEC 62443) and encrypted telemetry in transit.",
                "objection_handler": "Azure IoT Edge provides certificate-based authentication and TLS 1.3 encryption meeting utility standards."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign Azure IoT and edge computing specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign Azure IoT and edge computing specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Beijer Electronics' Head of Westermo R&D on edge cloud diagnostics and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Embedded memory constraints on older field devices. Mitigation: Deploy edge telemetry collectors on gateway devices while supporting legacy endpoints via Modbus/SNMP."
    },
    "DIAB AB": {
        "target_contract_value_eur": "€4,100,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,075,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Composite Material Optimization & Wind OEM Supply Chain on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Extrusion Scrap & Carbon Audit",
                "action": "Engage Head of Operations and Quality Director on wind blade material certification. Submit Microsoft AMMP voucher.",
                "deliverable": "Extrusion Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Manufacturing Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Azure ML models.",
                "deliverable": "Manufacturing Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Laholm Extrusion PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Laholm plant extruders. Predict density drift with 94%+ accuracy.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated scrap reduction and customer certification savings to Executive Board. Finalize 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Raw material scrap reduction (€2.2M/yr), wind OEM tier-1 retention, and 7-month payback.",
                "objection_handler": "Show how reducing polymer resin and PET scrap by 3% fully recovers software costs in 5 months."
            },
            "technical_champion": {
                "role": "Group CIO / IT Director",
                "focus": "OneLake multi-plant data mesh, retiring legacy historians, and automated Power BI reporting.",
                "objection_handler": "Fabric integrates with factory PLCs using lightweight edge connectors without disturbing plant networks."
            },
            "operational_sponsor": {
                "role": "Head of Operations & Quality",
                "focus": "Extruder scrap minimization, automated batch certification, and operator decision support.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating real-time scrap reduction."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Proprietary chemical polymer formulation security and Microsoft Purview compliance.",
                "objection_handler": "Microsoft Purview provides robust encryption protecting structural core formulation IP."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign Azure manufacturing specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign Azure manufacturing specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with DIAB's Head of Operations on composite foam scrap reduction and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Plant operators accustomed to legacy manual quality sampling. Mitigation: Deliver intuitive Power BI mobile touchscreens directly to extrusion line operators."
    },
    "New Wave Group AB": {
        "target_contract_value_eur": "€5,400,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€4,104,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Omni-Channel Retail Demand Sensing & Inventory Modernization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Omni-Channel Inventory & AMMP Scoping",
                "action": "Engage COO and Head of E-commerce on promotional stockouts and safety stock buffers. Submit Microsoft AMMP voucher.",
                "deliverable": "Demand Sensing Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Retail Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Direct Lake reporting.",
                "deliverable": "Retail Data Architecture Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Craft Sportswear Inventory PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Craft warehouse data. Deliver dynamic reordering alerts in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated markdown reduction and working capital savings to Executive Committee. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Working capital liberation (€3.1M/yr), markdown elimination, and 6-month payback.",
                "objection_handler": "Show how reducing seasonal overstock markdowns directly protects operating margins."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake data unification across brand silos, retiring custom ETL, and Azure scalability.",
                "objection_handler": "Fabric integrates with existing ERPs via OneLake shortcuts without requiring a single database migration."
            },
            "operational_sponsor": {
                "role": "COO / Head of Supply Chain",
                "focus": "European warehouse inventory rebalancing and automated dealer order processing.",
                "objection_handler": "Share Cegeka's Bridgestone supply chain case study demonstrating real-time logistics optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "GDPR compliance for consumer e-commerce data and secure B2B API gateways.",
                "objection_handler": "Microsoft Purview provides automated PII classification and encryption across all retail feeds."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Sensing ML review at Day 18.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign retail/consumer goods principal architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Sensing ML review at Day 18.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign retail/consumer goods principal architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with New Wave Group's COO on reducing warehouse safety stock buffers and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Disparate brand ERPs with incompatible product numbering schemas. Mitigation: Build a unified master product hierarchy in Fabric OneLake."
    },
    "POLYPEPTIDE LABORATORIES SWEDEN A": {
        "target_contract_value_eur": "€4,300,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€3,311,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Peptide Biomanufacturing & Purview GxP Governance on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Chromatography Telemetry & GxP Scoping",
                "action": "Engage VP Operations and Quality Director on automated HPLC peak review. Submit Microsoft AMMP voucher.",
                "deliverable": "GxP Biomanufacturing Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Sovereign GxP Architecture Blueprint",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing Purview audit lineage.",
                "deliverable": "Sovereign Life Sciences Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Peptide Yield PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting HPLC instruments. Deliver automated chromatographic purity calculation in Power BI.",
                "deliverable": "Working Fabric Solution & GxP Release Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated batch yield improvement and QA time savings to Executive Board. Finalize 3-year enterprise agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Peptide synthesis yield optimization (€2.4M/yr), QA review time savings, and 6-month payback.",
                "objection_handler": "Show how a 1.5% improvement in peptide synthesis coupling yield saves hundreds of thousands per commercial batch."
            },
            "technical_champion": {
                "role": "Head of IT & Digital Lab",
                "focus": "OneLake chromatography data lake, retiring manual data export scripts, and Microsoft Purview compliance.",
                "objection_handler": "Microsoft Purview provides out-of-the-box regulatory lineage satisfying FDA 21 CFR Part 11 requirements."
            },
            "operational_sponsor": {
                "role": "VP Operations & Quality Director",
                "focus": "Automated batch release, instant HPLC peak integration, and audit inspection readiness.",
                "objection_handler": "Share Cegeka's LRM medEmotion life sciences case study demonstrating GxP validation compliance."
            },
            "procurement_infosec": {
                "role": "Head of Quality Compliance & CISO",
                "focus": "Protecting patented peptide synthesis sequences and sovereign Swedish cloud hosting.",
                "objection_handler": "Azure Sweden Central provides sovereign, single-tenant data boundaries with customer-managed keys."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for GxP audit review.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign healthcare and biopharma solution architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for GxP audit review.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign healthcare and biopharma solution architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with PolyPeptide's VP Operations on automated HPLC peak integration and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Strict regulatory validation overhead for chromatographic software. Mitigation: Deliver pre-validated Cegeka GxP documentation accelerators for Microsoft Fabric."
    },
    "Consilium AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€3,276,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Maritime Safety Telemetry & Compliance on Microsoft Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Marine Safety Telemetry Scoping",
                "action": "Engage President Marine Safety and Head of Service on recurring digital compliance contracts. Submit Microsoft AMMP voucher.",
                "deliverable": "Maritime IoT Scoping Document & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Marine Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL event streaming.",
                "deliverable": "Marine Real-Time Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Vessel Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 20 commercial vessels via satellite IoT. Deliver automated IMO compliance dashboard.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated recurring software revenue model to Consilium Management. Finalize 3-year strategic enterprise agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Recurring maritime SaaS revenue (€2.2M/yr), service productivity lift, and 7-month payback.",
                "objection_handler": "Show how recurring safety compliance subscriptions create high-margin, predictable annual contract value."
            },
            "technical_champion": {
                "role": "Group CIO / VP Technology",
                "focus": "OneLake data unification, lightweight satellite telemetry compression, and Azure IoT security.",
                "objection_handler": "Azure IoT Edge provides smart edge filtering to transmit only critical sensor state changes over costly satellite links."
            },
            "operational_sponsor": {
                "role": "President Marine Safety & Head of Service",
                "focus": "Automated shipowner compliance dashboards and remote technician triage.",
                "objection_handler": "Share Cegeka's Fluvius utility telemetry case study demonstrating massive real-time IoT ingestion."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Maritime cybersecurity compliance (IACS UR E26/E27) and protecting safety system integrity.",
                "objection_handler": "Azure IoT Edge and Microsoft Purview satisfy maritime classification society cybersecurity requirements."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign transportation IoT and edge computing specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign transportation IoT and edge computing specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Consilium's President Marine Safety on digital IMO safety compliance and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: High marine satellite communication data transmission costs. Mitigation: Implement intelligent edge compression sending only alert events and hourly heartbeats."
    },
    "DACKE PMC HOLDING AB": {
        "target_contract_value_eur": "€3,600,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€2,772,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Decentralized Subsidiary Data Mesh & Rapid Consolidation on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Group Financial Consolidation Scoping",
                "action": "Engage Group CFO and IT Director on financial close acceleration. Submit Microsoft AMMP voucher.",
                "deliverable": "Financial Consolidation Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-ERP Architecture Blueprint",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing OneLake shortcuts.",
                "deliverable": "Multi-Entity OneLake Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Subsidiary Consolidation PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 3 subsidiary ERPs. Demonstrate automated P&L rollup in Power BI.",
                "deliverable": "Working Fabric Solution & Group Consolidation Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated finance team productivity and procurement savings to Group Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Group Chief Financial Officer (CFO)",
                "focus": "Compressing monthly close from 12 to 3 days, procurement savings (€1.8M/yr), and 7-month payback.",
                "objection_handler": "Show how automated OneLake consolidation cuts finance overtime and captures bulk purchasing synergies."
            },
            "technical_champion": {
                "role": "Group IT Director",
                "focus": "OneLake shortcuts to diverse ERPs, zero-maintenance SaaS fabric, and Power BI Direct Lake.",
                "objection_handler": "Fabric OneLake shortcuts connect to Monitor, Visma, and Business Central without requiring database migrations."
            },
            "operational_sponsor": {
                "role": "Head of Operational Excellence",
                "focus": "Cross-subsidiary OEE benchmarking, capacity optimization, and best-practice sharing.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating multi-plant performance optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Subsidiary data isolation, role-based access control, and Microsoft Purview compliance.",
                "objection_handler": "Microsoft Purview enforces row-level security ensuring subsidiary MDs see only their own company data."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign enterprise data architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign enterprise data architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Dacke PMC's Group CFO on compressing monthly financial close to 3 days and share Cegeka CERA benchmark.",
        "deal_blocker_mitigation": "Blocker: Subsidiary managing directors resisting centralized IT mandates. Mitigation: Frame Fabric as an executive reporting overlay that leaves subsidiary ERP choices untouched."
    },
    "Karo Pharma AB": {
        "target_contract_value_eur": "€4,400,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,344,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Consumer Healthcare Demand Sensing & Brand M&A Integration on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Wholesaler Data & Supply Chain Scoping",
                "action": "Engage Commercial Director Europe and Supply Chain VP on pharmacy out-of-stocks. Submit Microsoft AMMP voucher.",
                "deliverable": "Demand Sensing Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Consumer Health Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Direct Lake reporting.",
                "deliverable": "Consumer Health Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Nordic Pharmacy PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Swedish and Danish wholesaler feeds. Deliver automated demand forecast in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated out-of-stock reduction and promotion ROI metrics to Executive Committee. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Out-of-stock elimination (€2.5M/yr), marketing ROI optimization, and 6-month payback.",
                "objection_handler": "Show how real-time pharmacy demand sensing prevents costly stockouts during peak seasonal illness surges."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake data unification, retiring disparate EDI scripts, and scalable cloud architecture for M&A.",
                "objection_handler": "Fabric OneLake allows newly acquired consumer health brands to be integrated into group reporting in weeks."
            },
            "operational_sponsor": {
                "role": "Commercial Director Europe & Supply Chain VP",
                "focus": "Wholesaler stock transparency, contract manufacturer alignment, and promotion tracking.",
                "objection_handler": "Share Cegeka's Bridgestone consumer goods supply chain case study demonstrating demand sensing."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Commercial price data security, pharmaceutical marketing compliance, and GDPR compliance.",
                "objection_handler": "Microsoft Purview provides robust data classification and role-based access control across Europe."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Forecasting review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign consumer healthcare industry solution architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Forecasting review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign consumer healthcare industry solution architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Karo Pharma's Commercial Director on pan-European pharmacy demand sensing and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Highly fragmented European wholesaler data formats. Mitigation: Deploy pre-built Cegeka healthcare wholesaler ingestion pipelines in Azure Data Factory."
    },
    "Lagerstedt & Krantz AB": {
        "target_contract_value_eur": "€3,500,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€2,695,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Smart HVAC Telemetry & Prefab BIM Automation on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "BIM Prefab & Telemetry Scoping",
                "action": "Engage VP Prefab Systems and Head of R&D on automated BIM takeoff. Submit Microsoft AMMP voucher.",
                "deliverable": "Prefab Automation Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Engineering Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Fabric ingestion.",
                "deliverable": "Engineering Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Prefab Manifold PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting BIM parser. Deliver automated manifold bill of materials in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated engineering time savings and prefab scrap reduction to LK Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Prefab manufacturing lead time reduction (€1.7M/yr), engineering productivity, and 7-month payback.",
                "objection_handler": "Show how automating BIM takeoff cuts engineering drafting hours by 60% while AMMP covers startup fees."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake engineering data mesh, Azure IoT Hub smart controller integration, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with existing CAD tools and factory PLCs using standard cloud connectors."
            },
            "operational_sponsor": {
                "role": "VP Prefab Systems & Head of R&D",
                "focus": "Turnkey prefab manifold production and smart underfloor heating energy analytics.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating automated engineering workflows."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Customer proprietary BIM building design security and Azure tenant isolation.",
                "objection_handler": "Microsoft Purview provides robust encryption protecting customer architectural designs."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for IoT Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign smart building and manufacturing specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for IoT Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign smart building and manufacturing specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with LK Group's VP Prefab Systems on automated BIM manifold manufacturing and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Complex architectural IFC/Revit file formats. Mitigation: Deploy pre-built Azure CAD extraction modules normalizing BIM models into Fabric OneLake."
    },
    "BIOTAGE SWEDEN AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,192,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Connected Lab Instrumentation & Consumable Telemetry on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Instrument Telemetry & Aftermarket Scoping",
                "action": "Engage VP Global Service and Head of R&D on consumable replenishment alerts. Submit Microsoft AMMP voucher.",
                "deliverable": "Connected Lab Instrument Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Instrument Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL streaming.",
                "deliverable": "Lab Telemetry Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Purification Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 20 Isolera systems. Benchmark predictive cartridge saturation alerts in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated consumable revenue uplift and remote service savings to Executive Board. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Recurring consumable revenue growth (€2.3M/yr), warranty cost reduction, and 6-month payback.",
                "objection_handler": "Show how automated consumable reordering increases customer cartridge retention by 25%."
            },
            "technical_champion": {
                "role": "Group CIO / VP Technology",
                "focus": "OneLake data unification, retiring standalone instrument databases, and Azure IoT security.",
                "objection_handler": "Fabric integrates with embedded instruments using lightweight Azure IoT Edge with zero on-prem server footprint."
            },
            "operational_sponsor": {
                "role": "VP Global Service & Aftermarket",
                "focus": "Remote diagnostic triage, first-time fix rate improvement, and automated customer reorders.",
                "objection_handler": "Share Cegeka's LRM medEmotion healthcare telemetry case study demonstrating connected instrumentation."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Air-gapping customer chemical molecule structures and ensuring strict ISO 27001 compliance.",
                "objection_handler": "Instruments transmit only physical hardware telemetry (pressure, voltage) without logging customer chemical names."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign healthcare and life sciences specialist architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign healthcare and life sciences specialist architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Biotage's VP Global Service on automated consumable replenishment alerts and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Pharmaceutical customer confidentiality regarding proprietary molecules. Mitigation: Transmit strictly anonymized machine hardware telemetry with zero chemical context."
    },
    "Mannheimer Swartling Advokatbyrå AB": {
        "target_contract_value_eur": "€3,900,000",
        "win_probability_pct": 81,
        "expected_value_eur": "€3,159,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Sovereign Legal Knowledge Mesh & Purview Security on Azure",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Legal Tech & Bar Compliance Scoping",
                "action": "Engage Managing Partner and Head of Knowledge Management on sovereign Azure OpenAI in Sweden Central. Submit Microsoft AMMP voucher.",
                "deliverable": "Sovereign Legal Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Purview Ethical Wall Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) showing cryptographic client isolation.",
                "deliverable": "Sovereign Security Blueprint & Bar Compliance Plan"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Precedent Research PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart indexing historical legal memos. Benchmark research speed and citation accuracy.",
                "deliverable": "Working Legal Copilot Prototype & Associate Usability Study"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Partnership Board Agreement Close",
                "action": "Present validated associate time savings to Mannheimer Swartling Management Committee. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Managing Partner / Finance Partner",
                "focus": "Associate billable leverage (4.4x productivity), client retention, and 5-month payback.",
                "objection_handler": "Show how sovereign GenAI allows lawyers to deliver faster turnaround on complex corporate mandates while maintaining top billable rates."
            },
            "technical_champion": {
                "role": "Head of Legal Tech & Knowledge Management",
                "focus": "Air-gapped Azure OpenAI (Sweden Central), Microsoft Purview data governance, and seamless M365 integration.",
                "objection_handler": "Demonstrate that data is never stored outside Sweden and models are never trained on client prompts."
            },
            "operational_sponsor": {
                "role": "Chief Operating Officer",
                "focus": "Knowledge management efficiency, associate onboarding speed, and firm-wide precedent search.",
                "objection_handler": "Share Cegeka's CERA regulated financial services case study demonstrating secure AI knowledge search."
            },
            "procurement_infosec": {
                "role": "DPO & Information Security Officer",
                "focus": "Swedish Bar Association ethics guidelines, ISO 27001, and zero data leakage.",
                "objection_handler": "Microsoft provides formal legal commitments verifying private tenant isolation and zero persistent data retention."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for sovereign security review.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign legal sector AI specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Paul Boland (Security DSE) at Day 15 for sovereign security review.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign legal sector AI specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Mannheimer Swartling's Head of Knowledge Management on sovereign M&A precedent search and share Cegeka CERA benchmark.",
        "deal_blocker_mitigation": "Blocker: Strict Swedish Bar Association rules regarding client privilege. Mitigation: Provide legally binding Microsoft Sweden Central deployment architecture with zero model training."
    },
    "JLINDEBERG AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€3,234,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Omni-Channel Fashion Demand Sensing & Merchandising Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Fashion Merchandising & Inventory Scoping",
                "action": "Engage Brand Director and Head of E-commerce on seasonal markdown reduction. Submit Microsoft AMMP voucher.",
                "deliverable": "Fashion Demand Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Omni-Channel Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Direct Lake dashboards.",
                "deliverable": "Omni-Channel Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Golf Apparel Inventory PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting e-commerce and warehouse feeds. Deliver automated size replenishment alerts in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated markdown reduction and working capital savings to J.Lindeberg Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Inventory markdown reduction (€2.4M/yr), working capital optimization, and 6-month payback.",
                "objection_handler": "Show how reducing end-of-season clearance markdowns directly protects gross margin while AMMP covers startup fees."
            },
            "technical_champion": {
                "role": "Group CIO / Head of IT",
                "focus": "OneLake data unification, retiring standalone retail reporting tools, and Azure scalability.",
                "objection_handler": "Fabric integrates with Shopify, ERP, and warehouse systems using standard pre-built Data Factory connectors."
            },
            "operational_sponsor": {
                "role": "Head of E-commerce & Merchandising",
                "focus": "Real-time stock availability, personalized recommendations, and automated product catalog copy.",
                "objection_handler": "Share Cegeka's Bridgestone consumer goods case study demonstrating real-time supply chain demand sensing."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "GDPR compliance for global consumer shopper data and PCI-DSS compliance.",
                "objection_handler": "Microsoft Purview provides automated PII classification and encryption across all retail clickstreams."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Forecasting review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign retail and fashion industry solution architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Demand Forecasting review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign retail and fashion industry solution architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with J.Lindeberg's Head of E-commerce on reducing seasonal markdown write-offs and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Rapid seasonal product catalog turnover. Mitigation: Deploy automated Azure OpenAI catalog ingestion that auto-classifies new apparel lines in Fabric."
    },
    "VITROLIFE AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 88,
        "expected_value_eur": "€3,696,000",
        "target_close_quarter": "November / Q4 2026",
        "deal_motion": "Data Governance Phase 0 & Sovereign IVF Imaging Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Data Governance Phase 0 Workshop",
                "action": "Execute joint Data Governance workshop (Purview + ERP) with Hanna and Sofia (Vitrolife) and Raihan Chowdhury (Microsoft).",
                "deliverable": "Approved Governance Workshop Findings & Phase 0 Roadmap"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Sovereign Medical Architecture Blueprint",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Paul Boland (Security DSE) finalizing Purview medical sensitivity labels.",
                "deliverable": "Purview Medical Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Embryo Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting EmbryoScope test feeds. Benchmark automated viability scoring in Fabric.",
                "deliverable": "Working Fabric Solution & Clinician Scoring Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated clinical efficiency and regulatory compliance metrics to Vitrolife Executive Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Clinical software ARR growth (€2.6M/yr), MDR compliance audit protection, and 6-month payback.",
                "objection_handler": "Show how cloud AI embryo scoring positions Vitrolife as the premium technology standard in commercial IVF clinics."
            },
            "technical_champion": {
                "role": "Head of IT (Hanna / Sofia)",
                "focus": "Purview sensitivity labeling, OneLake clinical image mesh, and automated ERP integration.",
                "objection_handler": "Microsoft Purview provides turnkey healthcare data classification satisfying global medical regulations."
            },
            "operational_sponsor": {
                "role": "Chief Scientific Officer & Clinical Director",
                "focus": "Embryo viability algorithm accuracy, embryologist workflow acceleration, and clinic adoption.",
                "objection_handler": "Share Cegeka's LRM medEmotion clinical healthcare case study demonstrating medical AI compliance."
            },
            "procurement_infosec": {
                "role": "Head of Quality & Regulatory",
                "focus": "FDA Software as a Medical Device (SaMD), EU MDR, and cross-border patient health data sovereignty.",
                "objection_handler": "Azure Sweden Central provides sovereign, air-gapped tenant isolation with customer-managed cryptographic keys."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Active partner co-sell: Coordinate workshop agenda with Raihan Chowdhury (Microsoft Specialist); loop in Paul Boland (Security DSE) for Purview review at Day 10.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; provide dedicated Azure Healthcare Solution Architects; co-deliver Phase 0 workshop."
        },
        "databricks_involvement": {
            "when_to_involve": "Active partner co-sell: Coordinate workshop agenda with Raihan Chowdhury (Microsoft Specialist); loop in Paul Boland (Security DSE) for Purview review at Day 10.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; provide dedicated Azure Healthcare Solution Architects; co-deliver Phase 0 workshop."
        },
        "immediate_next_action": "Finalize workshop date with Hanna and Sofia (Vitrolife) and Raihan (Microsoft) to deliver Data Governance Phase 0 and drive toward November close.",
        "deal_blocker_mitigation": "Blocker: Undefined roles between Cegeka, Microsoft, and Vitrolife. Mitigation: Cegeka leads governance delivery while Microsoft provides platform vouchers and architecture sponsorship."
    },
    "XANO Industri AB": {
        "target_contract_value_eur": "€4,300,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,225,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Multi-Plant OEE Telemetry & Group Harmonization on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Packaging Telemetry & Group Scoping",
                "action": "Engage Group Operations Director and VP Packaging Machinery on OEE benchmarking. Submit Microsoft AMMP voucher.",
                "deliverable": "Multi-Plant Scoping Document & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-Plant Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL telemetry queries.",
                "deliverable": "Multi-Plant IoT Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Packaging Machine PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 10 packaging machines. Deliver real-time OEE and jam alerts in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated scrap reduction and service revenue metrics to XANO Group Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Group Chief Financial Officer (CFO)",
                "focus": "OEE improvement (€2.1M/yr), scrap reduction across 25 plants, and 7-month payback.",
                "objection_handler": "Show how raising multi-plant OEE by 2% yields millions in additional production throughput without adding machines."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake shortcuts to diverse subsidiary ERPs, Azure IoT Edge plant integration, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with factory PLCs using standard OPC-UA connectors without disturbing plant automation."
            },
            "operational_sponsor": {
                "role": "Group Operations Director & VP Packaging",
                "focus": "Machine jam prevention, automated changeover schedules, and operator decision support.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating real-time OEE optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Factory network isolation, customer CAD drawing confidentiality, and ISO 27001.",
                "objection_handler": "Azure IoT Edge provides secure outbound-only TLS 1.3 telemetry requiring zero open incoming ports."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign manufacturing IoT and cloud data architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign manufacturing IoT and cloud data architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with XANO's Group Operations Director on multi-plant OEE benchmarking and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Highly diverse PLC hardware across acquired plants. Mitigation: Deploy standard Azure IoT Edge OPC-UA gateways abstracting hardware differences."
    },
    "AB WILH BECKER": {
        "target_contract_value_eur": "€4,100,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,116,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Chemical Formulation AI & Batch Scrap Reduction on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Chemical Formulation & Scrap Scoping",
                "action": "Engage Head of Formulation R&D and Quality Director on automated color matching. Submit Microsoft AMMP voucher.",
                "deliverable": "Formulation AI Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Chemical Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Azure ML models.",
                "deliverable": "Chemical Formulation Blueprint & TCO Model"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Color Matching PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting lab spectrophotometers. Benchmark predictive tint accuracy in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated batch rework reduction and VOC compliance savings to Becker Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Batch scrap and rework reduction (€2.2M/yr), formulation R&D acceleration, and 7-month payback.",
                "objection_handler": "Show how eliminating 3% of batch rework in high-volume coil coatings pays for the software rollout in 5 months."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake chemical data mesh, retiring standalone lab databases, and Azure ML integration.",
                "objection_handler": "Fabric integrates with factory mixing vats and lab spectrophotometers using lightweight standard connectors."
            },
            "operational_sponsor": {
                "role": "Head of Formulation R&D & Quality",
                "focus": "Faster customer color matching, zero off-spec batches, and automated safety data sheets (SDS).",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating chemical scrap and energy optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Proprietary paint formulation confidentiality and Microsoft Purview data governance.",
                "objection_handler": "Microsoft Purview provides robust encryption protecting chemical recipe IP from unauthorized access."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign chemical and process manufacturing specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign chemical and process manufacturing specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Becker's Head of Formulation R&D on automated spectrophotometer color matching and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Confidentiality concerns over proprietary coating chemical recipes. Mitigation: Deploy private, customer-managed single-tenant Azure ML workspaces."
    },
    "AQ GROUP AB": {
        "target_contract_value_eur": "€5,600,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€4,200,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Global 40-Plant Manufacturing Mesh & OneLake on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Global Manufacturing Telemetry Scoping",
                "action": "Engage COO and Head of Global Procurement on cross-plant OEE benchmarking. Submit Microsoft AMMP voucher.",
                "deliverable": "Global Manufacturing Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Multi-Plant Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing OneLake mesh.",
                "deliverable": "Multi-Plant Fabric Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Stamping & Moulding PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 3 manufacturing plants. Deliver real-time scrap benchmarking in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated scrap reduction and procurement savings to AQ Group Executive Board. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Raw material procurement savings (€3.5M/yr), global scrap reduction, and 6-month payback.",
                "objection_handler": "Show how pooling global copper and polymer demand across 40 plants generates immediate purchasing discounts."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake shortcuts connecting disparate plant ERPs, zero-maintenance SaaS fabric, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with diverse factory floor systems without requiring centralized ERP re-implementation."
            },
            "operational_sponsor": {
                "role": "CEO / COO & Head of Procurement",
                "focus": "Global OEE transparency, automated automotive PPAP quality packages, and production capacity rebalancing.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating multi-plant scrap optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Automotive tier-1 cybersecurity standards (TISAX) and protecting client engineering designs.",
                "objection_handler": "Microsoft Azure and Purview satisfy automotive TISAX Level 3 information security norms."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign global manufacturing solution architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign global manufacturing solution architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with AQ Group's COO on benchmarking component scrap rates across 40 plants and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Plant engineering teams operating in 16 different languages and jurisdictions. Mitigation: Deploy localized Power BI Direct Lake dashboards with automated multilingual interface."
    },
    "aPak AB": {
        "target_contract_value_eur": "€3,200,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€2,464,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Smart Packaging Logistics & Carbon Calculation Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Packaging Logistics & Carbon Scoping",
                "action": "Engage Managing Director and Supply Chain Director on PPWR carbon documentation. Submit Microsoft AMMP voucher.",
                "deliverable": "Packaging Logistics Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Packaging Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Fabric dashboards.",
                "deliverable": "Packaging Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Carton Optimization PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting CAD die-line repository. Deliver automated carton carbon calculation in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated freight savings and customer quote acceleration to aPak Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Freight cost savings (€1.5M/yr), inventory turnover optimization, and 7-month payback.",
                "objection_handler": "Show how right-sized carton algorithms reduce customer shipping costs while AMMP covers deployment fees."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake data unification, retiring standalone warehouse scripts, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with existing ERP and CAD software using standard cloud connectors."
            },
            "operational_sponsor": {
                "role": "Managing Director & Supply Chain Director",
                "focus": "Automated carton sizing, EU PPWR compliance, and rapid customer RFQ turnaround.",
                "objection_handler": "Share Cegeka's Bridgestone logistics case study demonstrating real-time supply chain optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Customer proprietary CAD packaging design security and Azure tenant compliance.",
                "objection_handler": "Microsoft Purview provides robust encryption protecting customer packaging designs."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign retail/packaging industry specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning model review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign retail/packaging industry specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with aPak's Managing Director on automated EU PPWR carbon documentation and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Complex customer packaging CAD formats. Mitigation: Deploy pre-built Azure AI Document Intelligence models extracting carton dimensions automatically."
    },
    "CELLINK AB": {
        "target_contract_value_eur": "€4,200,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,192,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Bioprinting Fleet Telemetry & Life Science AI Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Bioprinting Telemetry & R&D Scoping",
                "action": "Engage Head of Bioprinting R&D and VP Sales on printer fleet reproducibility. Submit Microsoft AMMP voucher.",
                "deliverable": "Bioprinting Telemetry Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Bioprinting Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL event streaming.",
                "deliverable": "Bioprinting Data Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week BIO X Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 10 BIO X bioprinters. Deliver real-time print fidelity scoring in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated print success rate and biopharma software ARR metrics to BICO Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Software ARR growth (€2.2M/yr), printer consumable retention, and 6-month payback.",
                "objection_handler": "Show how cloud print reproducibility software positions CELLINK as the premier partner for big pharma drug screening."
            },
            "technical_champion": {
                "role": "Group CIO / VP Technology",
                "focus": "OneLake data unification, retiring standalone instrument databases, and Azure IoT security.",
                "objection_handler": "Fabric integrates with bioprinter firmware using lightweight Azure IoT Edge agents with local buffering."
            },
            "operational_sponsor": {
                "role": "Head of Bioprinting R&D & Product",
                "focus": "Real-time print failure detection, automated crosslinking calibration, and researcher protocol sharing.",
                "objection_handler": "Share Cegeka's LRM medEmotion healthcare telemetry case study demonstrating precision medical diagnostics."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Protecting customer proprietary stem cell and cancer tissue research IP.",
                "objection_handler": "Microsoft Purview provides confidential tenant isolation ensuring academic and pharma research IP never leaks."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign life sciences and high-performance computing specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign life sciences and high-performance computing specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with CELLINK's Head of Bioprinting R&D on predictive live-cell print fidelity and share Cegeka LRM medEmotion benchmark.",
        "deal_blocker_mitigation": "Blocker: Academic and pharmaceutical customer IP confidentiality. Mitigation: Transmit strictly anonymized mechanical printer telemetry without logging cellular construct names."
    },
    "Future Ordering AB": {
        "target_contract_value_eur": "€4,500,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€3,510,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Real-Time QSR Transactional Lakehouse & AI Recommendations on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Transactional Concurrency & Kiosk Scoping",
                "action": "Engage CTO and VP Product on lunch rush concurrency and sub-50ms recommendation latency. Submit Microsoft AMMP voucher.",
                "deliverable": "High-Concurrency Architecture Scope & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time Fabric & Cosmos DB Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL event streaming.",
                "deliverable": "QSR Real-Time Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Max Burgers Kiosk PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting 100 restaurant kiosks. Benchmark personalized recommendation lift in Power BI.",
                "deliverable": "Working Fabric Prototype & Basket Recommendation Demo"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated basket size expansion (+8%) and cloud cost reduction to Executive Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Average order value (AOV) expansion (€2.5M/yr), cloud compute optimization, and 6-month payback.",
                "objection_handler": "Show how raising average basket size by 4% across millions of digital orders generates massive recurring EBITDA."
            },
            "technical_champion": {
                "role": "Chief Technology Officer (CTO)",
                "focus": "Zero database latency during lunch rush, serverless KQL streaming, and Azure Cosmos DB integration.",
                "objection_handler": "Fabric Real-Time Hub scales elastically during peak rush hours without over-provisioning baseline cluster costs."
            },
            "operational_sponsor": {
                "role": "VP Product & Restaurant Operations",
                "focus": "Sub-50ms AI recommendation latency, kitchen prep bottleneck alerts, and franchise portal.",
                "objection_handler": "Share Cegeka's Bridgestone high-throughput telemetry case study demonstrating sub-second response times."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "PCI-DSS compliance, tokenized customer payment processing, and GDPR compliance.",
                "objection_handler": "Microsoft Azure provides certified PCI-DSS Level 1 compliance and automated tokenization."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign retail technology and high-concurrency cloud architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign retail technology and high-concurrency cloud architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Future Ordering's CTO on handling lunch rush transactional concurrency and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Concern over cloud recommendation latency slowing down kiosk ordering. Mitigation: Implement edge caching and sub-50ms Cosmos DB vector lookups."
    },
    "Flokk AB": {
        "target_contract_value_eur": "€3,800,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€2,926,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Circular Manufacturing & DPP Compliance Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Circular Supply Chain & DPP Scoping",
                "action": "Engage Head of Circular Economy and Operations Director on EU Digital Product Passport readiness. Submit Microsoft AMMP voucher.",
                "deliverable": "Circular Economy Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Sustainability Architecture",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Sustainability Manager.",
                "deliverable": "Sustainability Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week HÅG Capisco Carbon PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Nässjö plant assembly data. Deliver automated chair carbon passport in Power BI.",
                "deliverable": "Working Fabric Solution & Digital Passport Demo"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated tender win-rate uplift and fabric scrap reduction to Flokk Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Public tender win rate protection (€1.8M/yr), fabric scrap reduction, and 7-month payback.",
                "objection_handler": "Show how verified digital product passports secure multi-million corporate workplace contracts."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake data unification across Sweden, Norway, and Poland plants, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with existing ERPs and CAD furniture configurators using standard cloud connectors."
            },
            "operational_sponsor": {
                "role": "Head of Circular Economy & Sustainability",
                "focus": "Automated EU DPP compliance, recycled material verification, and corporate ESG reporting.",
                "objection_handler": "Share Cegeka's Fluvius sustainability data case study demonstrating automated carbon auditing."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Supply chain partner data security and Microsoft Purview compliance.",
                "objection_handler": "Microsoft Purview enforces granular encryption protecting supplier pricing and formulation data."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Sustainability Manager review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign sustainability and manufacturing specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Sustainability Manager review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign sustainability and manufacturing specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Flokk's Head of Circular Economy on automated Digital Product Passports and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Complex multi-tier supplier data collection for recycled materials. Mitigation: Deploy automated Microsoft Purview supplier assessment questionnaires."
    },
    "IPCO SWEDEN AB": {
        "target_contract_value_eur": "€4,100,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€3,075,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Industrial Steel Belt Telemetry & Predictive Service on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Belt Telemetry & Aftermarket Scoping",
                "action": "Engage VP Global Service and Chief Metallurgist on predictive belt maintenance contracts. Submit Microsoft AMMP voucher.",
                "deliverable": "Belt Telemetry Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "Real-Time IoT Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing KQL telemetry queries.",
                "deliverable": "Industrial IoT Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Pastillator Telemetry PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting test pastillation line. Deliver automated weld fatigue alerts in Power BI.",
                "deliverable": "Working Fabric Telemetry Prototype & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated customer downtime reduction and service revenue metrics to IPCO Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Strategic Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Recurring aftermarket SLA growth (€2.1M/yr), warranty risk mitigation, and 7-month payback.",
                "objection_handler": "Show how bundling steel belts with cloud telemetry contracts protects high-margin aftermarket revenue."
            },
            "technical_champion": {
                "role": "Group CIO / IT Manager",
                "focus": "OneLake data unification, retiring standalone sensor tools, and Azure IoT Edge security.",
                "objection_handler": "Fabric integrates with industrial optical scanners and vibration sensors using standard edge protocols."
            },
            "operational_sponsor": {
                "role": "VP Global Service & Chief Metallurgist",
                "focus": "Belt fracture prevention, remote technician triage, and customer plant uptime.",
                "objection_handler": "Share Cegeka's Austrotherm manufacturing case study demonstrating heavy equipment predictive diagnostics."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Industrial chemical plant OT security standards and tenant data isolation.",
                "objection_handler": "Azure IoT Edge provides certificate-based authentication and outbound-only TLS 1.3 telemetry encryption."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign heavy industrial IoT and process engineering specialists; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Real-Time Hub review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign heavy industrial IoT and process engineering specialists; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with IPCO's VP Global Service on predictive steel belt maintenance and share Cegeka Austrotherm benchmark.",
        "deal_blocker_mitigation": "Blocker: Chemical plant customer reluctance to connect continuous process lines to cloud. Mitigation: Implement edge-based anomaly detection sending only alert flags over cellular IoT."
    },
    "Cars2click": {
        "target_contract_value_eur": "€3,900,000",
        "win_probability_pct": 77,
        "expected_value_eur": "€3,003,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Automotive Arbitrage Data Platform & Valuation AI on Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Arbitrage Telemetry & Scraping Scoping",
                "action": "Engage CEO and CTO on cross-border vehicle price normalization. Submit Microsoft AMMP voucher.",
                "deliverable": "Pricing Engine Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Arbitrage Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Azure ML models.",
                "deliverable": "Arbitrage Data Blueprint & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week EV Arbitrage PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting German and Nordic dealer listing feeds. Deliver automated arbitrage spread alerts in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Agreement Close",
                "action": "Present validated trading margin lift and vehicle inventory turnover savings to Cars2click Management. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Enterprise Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Trading gross margin expansion (€2.3M/yr), inventory turnover acceleration, and 6-month payback.",
                "objection_handler": "Show how capturing an extra €250 margin per vehicle across thousands of annual trades generates massive ROI."
            },
            "technical_champion": {
                "role": "Chief Technology Officer (CTO)",
                "focus": "High-throughput data ingestion, retiring fragile scraper scripts, and serverless Azure scalability.",
                "objection_handler": "Fabric handles millions of scraped vehicle records daily with automated schema evolution in OneLake."
            },
            "operational_sponsor": {
                "role": "CEO & Head of Automotive Trading",
                "focus": "Instant cross-border margin calculations, automated tax deductions, and trader decision support.",
                "objection_handler": "Share Cegeka's Bridgestone automotive supply chain case study demonstrating high-velocity trading analytics."
            },
            "procurement_infosec": {
                "role": "Head of IT Security",
                "focus": "Dealer commercial pricing confidentiality and European GDPR compliance.",
                "objection_handler": "Microsoft Purview provides robust data classification and tenant isolation for confidential trade data."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning valuation review at Day 18.",
            "what_partner_does": "Allocate $40,000 AMMP voucher; assign retail/automotive cloud data architects; support MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $40,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for Machine Learning valuation review at Day 18.",
            "what_databricks_does": "Allocate $40,000 AMMP voucher; assign retail/automotive cloud data architects; support MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Cars2click's CEO on algorithmic European vehicle price arbitrage and share Cegeka Bridgestone benchmark.",
        "deal_blocker_mitigation": "Blocker: Fragile third-party web scraper feeds. Mitigation: Deploy resilient Azure Data Factory web connectors with automated schema drift handling."
    },
    "Bravida AB": {
        "target_contract_value_eur": "€8,800,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€6,864,000",
        "target_close_quarter": "Q4 2026",
        "deal_motion": "Nordic Installation Margin Mesh & Field Service Fabric",
        "four_phases": [
            {
                "phase": "Phase 1 (Day 1-15)",
                "title": "Field Service & Job-Costing Scoping",
                "action": "Engage COO and Head of Digital Service on project margin leakage and technician utilization. Submit Microsoft AMMP voucher.",
                "deliverable": "Margin Leakage Scoping Plan & AMMP Approval"
            },
            {
                "phase": "Phase 2 (Day 16-30)",
                "title": "OneLake Enterprise Architecture Design",
                "action": "Joint session with Raihan Chowdhury (Microsoft Specialist) and Geoff Scott (DSE Data & AI) showing Direct Lake dashboards.",
                "deliverable": "Enterprise Data Architecture & TCO Business Case"
            },
            {
                "phase": "Phase 3 (Day 31-60)",
                "title": "4-Week Stockholm Division PoV",
                "action": "Deploy Cegeka 4-Week Jumpstart connecting Stockholm electrical branch data. Deliver real-time project margin alerts in Power BI.",
                "deliverable": "Working Fabric Solution & Direct Lake Dashboard"
            },
            {
                "phase": "Phase 4 (Day 61-90)",
                "title": "Executive Board Agreement Close",
                "action": "Present validated margin protection (€5.2M/yr) and technician productivity metrics to Bravida Executive Board. Finalize 3-year agreement.",
                "deliverable": "Signed 3-Year Master Services Agreement & Production SOW"
            }
        ],
        "stakeholders": {
            "economic_buyer": {
                "role": "Chief Financial Officer (CFO)",
                "focus": "Project margin slippage prevention (€5.2M/yr), billable technician hours lift, and 6-month payback.",
                "objection_handler": "Show how stopping just a 1% margin leak on multi-million kronor projects saves tens of millions annually."
            },
            "technical_champion": {
                "role": "Group CIO / VP IT",
                "focus": "OneLake data unification across Nordic divisions, retiring disparate branch reporting tools, and Power BI Direct Lake.",
                "objection_handler": "Fabric integrates with diverse branch ERPs using OneLake shortcuts without requiring a unified ERP replacement."
            },
            "operational_sponsor": {
                "role": "Chief Operating Officer & Head of Digital Service",
                "focus": "Technician mobile enablement, automated supplier price matching, and project manager alerts.",
                "objection_handler": "Share Cegeka's Fluvius field service and grid maintenance case study demonstrating massive technician optimization."
            },
            "procurement_infosec": {
                "role": "Head of IT Security & CISO",
                "focus": "GDPR compliance for technician location tracking, supplier commercial confidentiality, and ISO 27001.",
                "objection_handler": "Microsoft Purview provides automated data masking and granular role-based access control across all Nordic branches."
            }
        },
        "partner_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_partner_does": "Allocate $50,000 AMMP voucher; assign field service and enterprise cloud architects; support multi-million MACC contract alignment."
        },
        "databricks_involvement": {
            "when_to_involve": "Engage Raihan Chowdhury and Mårten Palm at Day 5 to secure $50,000 AMMP funding; loop in Geoff Scott (Data & AI DSE) for OneLake architecture review at Day 18.",
            "what_databricks_does": "Allocate $50,000 AMMP voucher; assign field service and enterprise cloud architects; support multi-million MACC contract alignment."
        },
        "immediate_next_action": "Schedule a 30-minute discovery call with Bravida's COO on preventing installation project margin leakage and share Cegeka Fluvius benchmark.",
        "deal_blocker_mitigation": "Blocker: Decentralized branch autonomy and diverse local estimating habits. Mitigation: Implement intuitive Power BI mobile dashboards that help branch managers immediately protect their project bonuses."
    }
}

RAIHAN_TOP_DEALS = [
    {
        "rank": 1,
        "client_name": "Bravida AB",
        "parent_company": "Bravida Holding AB",
        "target_slide_idx": 40,
        "industry": "Technical Installation & Building Services",
        "deal_value_eur": "€8,800,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€6,864,000",
        "annual_savings_eur": "€5,200,000",
        "payback_months": 6,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "Project margin leakage across 14,000 field technicians and building energy telemetry fragmentation across Nordic branches.",
        "target_champion": "Chief Operating Officer / Head of Digital Service & CFO",
        "immediate_action": "Schedule 30-min discovery call with Bravida COO on stopping project margin leakage and share Cegeka Fluvius benchmark."
    },
    {
        "rank": 2,
        "client_name": "CORRAL PETROLEUM HOLDINGS AB",
        "parent_company": "Preem AB",
        "target_slide_idx": 14,
        "industry": "Renewable Fuel Refining & Petrochemicals",
        "deal_value_eur": "€9,500,000",
        "win_probability_pct": 70,
        "expected_value_eur": "€6,650,000",
        "annual_savings_eur": "€6,500,000",
        "payback_months": 5,
        "target_close_quarter": "Q1 2027",
        "burning_platform": "Massive refinery transition to renewable HVO and SAF fuels requiring real-time OT process historian integration and EU ETS carbon compliance.",
        "target_champion": "VP Refining Operations & Head of IT/OT",
        "immediate_action": "Brief Preem VP Refining Operations and CIO on real-time refinery historian analytics and share Cegeka Fluvius benchmark."
    },
    {
        "rank": 3,
        "client_name": "EQT Holdings AB",
        "parent_company": "EQT AB",
        "target_slide_idx": 18,
        "industry": "Global Private Capital & Alternative Assets (€240B+ AUM)",
        "deal_value_eur": "€8,400,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€6,300,000",
        "annual_savings_eur": "€4,800,000",
        "payback_months": 5,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "Fragmented portfolio company reporting across hundreds of assets; urgent demand for automated ESG carbon data mesh and AI deal due diligence.",
        "target_champion": "Global Head of Motherbrain / Data & CFO",
        "immediate_action": "Executive briefing with EQT Global Head of Motherbrain and CFO on confidential deal due diligence GenAI and share Cegeka CERA benchmark."
    },
    {
        "rank": 4,
        "client_name": "VITROLIFE AB",
        "parent_company": "Vitrolife Group",
        "target_slide_idx": 30,
        "industry": "Medical Technology & Assisted Reproduction (IVF)",
        "deal_value_eur": "€4,200,000",
        "win_probability_pct": 88,
        "expected_value_eur": "€3,696,000",
        "annual_savings_eur": "€2,600,000",
        "payback_months": 6,
        "target_close_quarter": "November / Q4 2026",
        "burning_platform": "Data Governance Phase 0 (Purview + ERP) workshop agenda prepared with Microsoft; urgent need to lock in Purview compliance before 2027.",
        "target_champion": "Hanna, Sofia (Vitrolife) & Raihan Chowdhury (Microsoft)",
        "immediate_action": "Confirm workshop date with Hanna, Sofia, and Raihan (Microsoft) to deliver Data Governance Phase 0 and drive toward November close."
    },
    {
        "rank": 5,
        "client_name": "Väderstad AB",
        "parent_company": "Väderstad Group",
        "target_slide_idx": 1,
        "industry": "Agricultural Machinery & Smart Farming Robotics",
        "deal_value_eur": "€4,800,000",
        "win_probability_pct": 76,
        "expected_value_eur": "€3,648,000",
        "annual_savings_eur": "€2,100,000",
        "payback_months": 7,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "IoT sensor telemetry from tens of thousands of connected seed drills (Tempo/Proceed) overwhelming legacy SQL batch systems during spring planting.",
        "target_champion": "VP Digital Solutions & CTO",
        "immediate_action": "Schedule 30-min discovery call with VP Digital Solutions on spring planting machine telemetry and share Cegeka Austrotherm IoT benchmark."
    }
]
