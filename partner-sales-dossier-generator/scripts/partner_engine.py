"""
Partner Resolution & Co-Branding Engine
Cegeka Partner Sales Dossier Skill
"""

import os
import json
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List

@dataclass
class PartnerConfig:
    id: str
    display_name: str
    co_brand_text: str
    accent_color: str
    secondary_color: str
    badge_text: str
    logo_svg: str
    primary_tech_stack: str
    workload_categories: List[str]
    funding_program: str
    funding_tier: str
    funding_customer_copay: str
    funding_countdown_days: int
    funding_prerequisites: List[str]
    partner_provides: str
    when_to_involve: str

# SVG Logo Definitions
LOGOS = {
    "databricks": """<svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
        <path d="M1.5 8.25L12 2.25L22.5 8.25L12 14.25L1.5 8.25Z" fill="#FF3621"/>
        <path d="M1.5 12L12 18L22.5 12L12 6L1.5 12Z" fill="#FF3621" fill-opacity="0.7"/>
        <path d="M1.5 15.75L12 21.75L22.5 15.75L12 9.75L1.5 15.75Z" fill="#FF3621" fill-opacity="0.4"/>
    </svg>""",
    "microsoft": """<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none">
        <rect x="1" y="1" width="10" height="10" fill="#F25022"/>
        <rect x="13" y="1" width="10" height="10" fill="#7FBA00"/>
        <rect x="1" y="13" width="10" height="10" fill="#00A4EF"/>
        <rect x="13" y="13" width="10" height="10" fill="#FFB900"/>
    </svg>""",
    "joint": """<div class="flex items-center space-x-1.5">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M1.5 8.25L12 2.25L22.5 8.25L12 14.25L1.5 8.25Z" fill="#FF3621"/><path d="M1.5 12L12 18L22.5 12L12 6L1.5 12Z" fill="#FF3621" fill-opacity="0.7"/></svg>
        <span class="text-slate-300 text-xs">✕</span>
        <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none"><rect x="1" y="1" width="10" height="10" fill="#F25022"/><rect x="13" y="1" width="10" height="10" fill="#7FBA00"/><rect x="1" y="13" width="10" height="10" fill="#00A4EF"/><rect x="13" y="13" width="10" height="10" fill="#FFB900"/></svg>
    </div>""",
    "snowflake": """<svg class="w-5 h-5" viewBox="0 0 24 24" fill="#29B5E8">
        <path d="M12 2L13.5 6.5L18 5L15.5 9L20 10.5L16 12L20 13.5L15.5 15L18 19L13.5 17.5L12 22L10.5 17.5L6 19L8.5 15L4 13.5L8 12L4 10.5L8.5 9L6 5L10.5 6.5L12 2Z"/>
    </svg>""",
    "aws": """<svg class="w-5 h-5" viewBox="0 0 24 24" fill="#FF9900">
        <path d="M12 3C7.03 3 3 7.03 3 12C3 16.97 7.03 21 12 21C16.97 21 21 16.97 21 12C21 7.03 16.97 3 12 3ZM16.5 15.5C14.5 17 10.5 17.5 7.5 15.5C7.2 15.3 7.4 14.8 7.8 15C10.5 16.5 13.8 16.2 16.1 14.8C16.5 14.6 16.8 15.1 16.5 15.5Z"/>
    </svg>""",
    "gcp": """<svg class="w-5 h-5" viewBox="0 0 24 24" fill="#4285F4">
        <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4C9.11 4 6.6 5.64 5.35 8.04C2.34 8.36 0 10.91 0 14C0 17.31 2.69 20 6 20H19C21.76 20 24 17.76 24 15C24 12.36 21.95 10.22 19.35 10.04Z"/>
    </svg>"""
}

def load_partner_registry() -> Dict[str, Any]:
    ref_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reference", "partner_ecosystem.json")
    if os.path.isfile(ref_path):
        with open(ref_path, "r", encoding="utf-8") as f:
            return json.load(f).get("partners", {})
    return {}

def resolve_partner(partner_name: str, custom_props: Optional[Dict[str, Any]] = None) -> PartnerConfig:
    p_clean = partner_name.strip().lower()
    registry = load_partner_registry()
    
    # Direct alias resolution
    mapped_id = None
    if p_clean in ["databricks", "dbx"]:
        mapped_id = "databricks"
    elif p_clean in ["microsoft", "msft", "fabric", "azure"]:
        mapped_id = "microsoft"
    elif p_clean in ["joint", "azure databricks", "databricks+microsoft", "tri-partner"]:
        mapped_id = "joint"
    elif p_clean in ["snowflake", "snow"]:
        mapped_id = "snowflake"
    elif p_clean in ["aws", "amazon"]:
        mapped_id = "aws"
    elif p_clean in ["gcp", "google", "google cloud"]:
        mapped_id = "gcp"

    if mapped_id and mapped_id in registry:
        data = registry[mapped_id]
        return PartnerConfig(
            id=data["id"],
            display_name=data["display_name"],
            co_brand_text=data["co_brand_text"],
            accent_color=data["accent_color"],
            secondary_color=data["secondary_color"],
            badge_text=data["badge_text"],
            logo_svg=LOGOS.get(data["id"], LOGOS["databricks"]),
            primary_tech_stack=data["primary_tech_stack"],
            workload_categories=data["workload_categories"],
            funding_program=data["funding_program"],
            funding_tier=data["funding_tier"],
            funding_customer_copay=data["funding_customer_copay"],
            funding_countdown_days=data["funding_countdown_days"],
            funding_prerequisites=data["funding_prerequisites"],
            partner_provides=data["partner_provides"],
            when_to_involve=data["when_to_involve"]
        )

    # Dynamic / Custom Partner Support
    p_display = partner_name.strip().title() if partner_name else "Strategic Partner"
    custom_props = custom_props or {}
    
    return PartnerConfig(
        id=re_slug(p_display),
        display_name=p_display,
        co_brand_text=f"CEGEKA & {p_display.upper()} STRATEGIC ALLIANCE",
        accent_color=custom_props.get("accent_color", "#00828A"),
        secondary_color="#051C2C",
        badge_text=f"{p_display.upper()} ALLIANCE",
        logo_svg=f"""<div class="px-2 py-0.5 rounded bg-brand-teal/20 text-brand-teal font-mono text-xs font-bold">{p_display[:3].upper()}</div>""",
        primary_tech_stack=custom_props.get("primary_tech_stack", f"{p_display} Enterprise Cloud Data & AI Platform"),
        workload_categories=[
            f"{p_display} Unified Governance & Security",
            f"{p_display} Modern Cloud Analytics",
            f"{p_display} Enterprise AI & Machine Learning"
        ],
        funding_program=custom_props.get("funding_program", f"{p_display} Partner Migration & PoV Co-Investment Program"),
        funding_tier=custom_props.get("funding_tier", "Enterprise Partner Tier ($25,000 - $50,000 Co-Funded)"),
        funding_customer_copay="75% Subsidized / 25% Customer Co-Pay",
        funding_countdown_days=120,
        funding_prerequisites=[
            f"{p_display} Technical Assessment & Sizing Scan",
            f"Partner Opportunity Registration in {p_display} Partner Portal",
            "Signed Customer Statement of Work (SOW)",
            "120-Day Execution Delivery Milestone Clock"
        ],
        partner_provides=f"{p_display} trial capacity credits, dedicated partner Solution Architect bench, and joint executive alignment.",
        when_to_involve=f"Introduce {p_display} Partner Lead at Day 10 for co-selling alignment; schedule joint technical architecture review at Day 22; engage {p_display} executive sponsor at Day 50."
    )

def re_slug(text: str) -> str:
    import re
    return re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()


def adapt_intel_for_partner(intel: Dict[str, Any], partner: PartnerConfig) -> Dict[str, Any]:
    """
    Recursively adapts client intelligence, use cases, and executive thesis
    to match the specific target cloud/data partner's ecosystem and terminology.
    """
    import copy
    adapted = copy.deepcopy(intel)
    
    subs = []
    if partner.id == "microsoft":
        subs = [
            ("Azure Databricks", "Azure & Microsoft Fabric"),
            ("Databricks Mosaic AI", "Azure OpenAI & Copilot Studio"),
            ("Mosaic AI", "Azure OpenAI Service"),
            ("Databricks Lakehouse", "Microsoft Fabric Lakehouse"),
            ("Databricks", "Microsoft"),
            ("Lakehouse", "Fabric OneLake Lakehouse"),
            ("Unity Catalog", "Microsoft Fabric OneLake & Purview"),
            ("Delta Live Tables", "Fabric Data Pipelines"),
            ("DBU", "ACR / Fabric Capacity Units"),
        ]
    elif partner.id == "snowflake":
        subs = [
            ("Azure Databricks", "Snowflake on Azure"),
            ("Databricks Mosaic AI", "Snowflake Cortex AI"),
            ("Mosaic AI", "Snowflake Cortex AI & Streamlit"),
            ("Databricks Lakehouse", "Snowflake Data Cloud"),
            ("Databricks", "Snowflake"),
            ("Lakehouse", "Snowflake Data Cloud"),
            ("Unity Catalog", "Snowflake Horizon Governance"),
            ("Delta Live Tables", "Dynamic Tables & Snowpark"),
            ("Delta Lake", "Snowflake Managed / Iceberg Tables"),
            ("DBU", "Snowflake Credits"),
        ]
    elif partner.id == "joint":
        subs = [
            ("Databricks Lakehouse", "Azure Databricks Lakehouse & Microsoft Fabric"),
            ("Databricks", "Azure Databricks & Microsoft"),
        ]
    elif partner.id not in ["databricks"]:
        subs = [
            ("Databricks", partner.display_name),
            ("Lakehouse", f"{partner.display_name} Data Platform"),
        ]

    def _replace_terms(val: Any) -> Any:
        if isinstance(val, str):
            res = val
            for src, tgt in subs:
                res = res.replace(src, tgt)
            return res
        elif isinstance(val, list):
            return [_replace_terms(x) for x in val]
        elif isinstance(val, dict):
            return {k: _replace_terms(v) for k, v in val.items()}
        return val

    adapted = _replace_terms(adapted)
    if "what_databricks_solves" in adapted:
        adapted["what_partner_solves"] = adapted["what_databricks_solves"]
    return adapted

