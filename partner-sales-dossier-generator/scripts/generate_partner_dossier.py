#!/usr/bin/env python3
"""
Multi-Partner Strategic Sales Dossier & Closing Plan Compiler
Cegeka Autonomous Sales Intelligence Environment (vm-nor-dev)

Author: Principal Python Engineer & Tier-1 Management Consulting Design Director
Supports:
  - Strategic Partners: Databricks, Microsoft, Joint (Azure Databricks), Snowflake, AWS, GCP, or Custom
  - Modes: sales-dossier (8-part sequence) | closing-plan (4-phase roadmap & stakeholder matrix)
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any, Optional

# Add script dir to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from partner_engine import resolve_partner, PartnerConfig, adapt_intel_for_partner
from client_intelligence_catalog import get_client_intelligence, CLIENT_CATALOG
from client_closing_strategy_catalog import get_client_closing_strategy, CLOSING_CATALOG

# ==============================================================================
# TOP 5 HIGH-YIELD OPPORTUNITIES
# ==============================================================================

TOP_PRIORITY_DEALS = [
    {
        "rank": 1,
        "client_name": "JYSK",
        "parent_company": "JYSK",
        "target_slide_idx": 25,
        "industry": "Omnichannel Retail & Global Supply Chain",
        "deal_value_eur": "€9,620,000",
        "win_probability_pct": 82,
        "expected_value_eur": "€7,888,400",
        "annual_savings_eur": "€3,400,000",
        "payback_months": 6,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "Overstretched overnight SAP batch window failing 3,300 stores; weekend promotional out-of-stocks.",
        "target_champion": "Executive VP Logistics / Supply Chain & CIO",
        "immediate_action": "Schedule 30-min discovery call with JYSK CDO on promotional stockouts and share Cegeka real-time reference story."
    },
    {
        "rank": 2,
        "client_name": "Arbejdsmarkedets Tillaegspension (ATP)",
        "parent_company": "Arbejdsmarkedets Tillaegspension (ATP)",
        "target_slide_idx": 2,
        "industry": "Pension Management & Welfare Administration",
        "deal_value_eur": "€10,750,000",
        "win_probability_pct": 68,
        "expected_value_eur": "€7,310,000",
        "annual_savings_eur": "€3,800,000",
        "payback_months": 7,
        "target_close_quarter": "Q1 2027",
        "burning_platform": "€100B+ pension reserve exposed to overnight market risk; high legacy SAS licensing costs and welfare fraud leakage.",
        "target_champion": "Chief Risk Officer (CRO) & Director of Udbetaling Danmark",
        "immediate_action": "Send briefing paper to ATP CRO contrasting legacy SAS batch runtimes against modern serverless compute clusters."
    },
    {
        "rank": 3,
        "client_name": "Norwegian Air Shuttle ASA",
        "parent_company": "Norwegian Air Shuttle ASA",
        "target_slide_idx": 37,
        "industry": "Commercial Aviation & Fleet Logistics",
        "deal_value_eur": "€8,750,000",
        "win_probability_pct": 78,
        "expected_value_eur": "€6,825,000",
        "annual_savings_eur": "€3,100,000",
        "payback_months": 7,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "Post-acquisition Widerøe fleet integration; costly Aircraft on Ground (AOG) turnaround delays.",
        "target_champion": "Chief Operating Officer / VP Flight Operations & CCO",
        "immediate_action": "Request 30-min meeting with Norwegian VP Technical Operations on predictive APU telemetry and fleet reliability."
    },
    {
        "rank": 4,
        "client_name": "Salmar AS",
        "parent_company": "Salmar AS",
        "target_slide_idx": 48,
        "industry": "Industrial Aquaculture & Ocean Salmon Farming",
        "deal_value_eur": "€7,560,000",
        "win_probability_pct": 75,
        "expected_value_eur": "€5,670,000",
        "annual_savings_eur": "€2,700,000",
        "payback_months": 6,
        "target_close_quarter": "Q4 2026",
        "burning_platform": "Fish feed represents 50%+ of opex; urgent Directorate of Fisheries sea lice and environmental compliance.",
        "target_champion": "Chief Operating Officer / Farming Director & CFO",
        "immediate_action": "Reach out to SalMar Farming Director with executive briefing on underwater camera telemetry and feed cost reduction."
    },
    {
        "rank": 5,
        "client_name": "Danish Crown",
        "parent_company": "Danish Crown",
        "target_slide_idx": 11,
        "industry": "Agri-Food, Cold-Chain & Global Meat Export",
        "deal_value_eur": "€7,560,000",
        "win_probability_pct": 74,
        "expected_value_eur": "€5,594,400",
        "annual_savings_eur": "€2,700,000",
        "payback_months": 7,
        "target_close_quarter": "Q1 2027",
        "burning_platform": "Mandatory EU CSRD Scope 3 farm emissions deadline for European supermarket contracts; abattoir yield variance.",
        "target_champion": "Chief Operating Officer / VP Operations & VP Sustainability",
        "immediate_action": "Contact Danish Crown VP Operations to present benchmark on automated carcass yield optimization and CSRD compliance."
    }
]

# ==============================================================================
# HTML TEMPLATE WITH DYNAMIC PARTNER BRANDING & WORKLOADS
# ==============================================================================

HTML_UNIFIED_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ partner.display_name }} Executive Sales Dossier | Cegeka Strategic Alliance</title>
    
    <!-- Fonts: Newsreader Editorial Serif + Inter Sans + JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS Play CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        partner: {
                            accent: '{{ partner.accent_color }}',
                            secondary: '{{ partner.secondary_color }}'
                        },
                        brand: {
                            navy: '#051C2C',      /* McKinsey Midnight Navy */
                            slate: '#1E293B',     /* Bain Slate Blue */
                            teal: '#00828A',      /* Cegeka Signature Cyan/Teal */
                            cegeka: '#0C2340',    /* Cegeka Deep Blue */
                            bgslate: '#F8FAFC',   /* Crisp Light Canvas */
                            border: '#E2E8F0',    /* Hairline Divider Gray */
                            accent: '#F1F5F9'
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'Georgia', 'serif'],
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <style>
        body {
            background-color: #0B1521;
            color: #051C2C;
            font-feature-settings: "cv02", "cv03", "cv04", "cv11";
            -webkit-font-smoothing: antialiased;
        }

        .executive-slide {
            background: #FFFFFF;
            width: 100%;
            max-width: 1680px;
            min-height: 940px;
            margin: 0 auto;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 1px solid #CBD5E1;
        }

        .consulting-quadrant {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 6px;
            transition: all 0.15s ease;
        }
        .consulting-quadrant:hover {
            border-color: #94A3B8;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        #toast {
            visibility: hidden;
            opacity: 0;
            transition: opacity 0.25s ease, visibility 0.25s;
        }
        #toast.show {
            visibility: visible;
            opacity: 1;
        }

        @media print {
            body {
                background: #FFFFFF !important;
                color: #000000 !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            .no-print {
                display: none !important;
            }
            .slide-page {
                display: block !important;
                page-break-after: always !important;
                page-break-inside: avoid !important;
                height: 100vh !important;
                width: 100vw !important;
                margin: 0 !important;
                padding: 10mm 12mm !important;
                box-sizing: border-box !important;
            }
            .executive-slide {
                max-width: 100% !important;
                min-height: 100% !important;
                box-shadow: none !important;
                border: none !important;
                border-radius: 0 !important;
            }
            @page {
                size: A4 landscape;
                margin: 0;
            }
        }
    </style>
</head>
<body class="p-3 sm:p-6 flex flex-col items-center">

    <!-- TOP SLIDE DECK CONTROL BAR -->
    <header class="no-print w-full max-w-[1680px] bg-white/95 backdrop-blur-md rounded-lg shadow-md border border-slate-200 px-5 py-3 mb-4 flex flex-col md:flex-row items-center justify-between gap-3">
        
        <!-- Co-Branding -->
        <div class="flex items-center space-x-3">
            <span class="font-bold text-lg tracking-tight text-brand-cegeka">cegeka</span>
            <span class="text-xs px-2 py-0.5 rounded font-mono font-semibold bg-brand-teal/10 text-brand-teal border border-brand-teal/20">{{ partner.badge_text }}</span>
            <span class="text-slate-300 font-light">✕</span>
            <div class="flex items-center space-x-1.5">
                {{ partner.logo_svg|safe }}
                <span class="font-bold text-base tracking-tight text-brand-navy">{{ partner.display_name }}</span>
            </div>
            
            <button onclick="goToSlide(0)" class="ml-2 text-xs font-semibold px-2.5 py-1 bg-brand-navy/5 hover:bg-brand-navy/10 text-brand-navy rounded border border-brand-navy/20 flex items-center gap-1 transition">
                <i data-lucide="layout-dashboard" class="w-3.5 h-3.5 text-brand-teal"></i>
                <span>Top 5 Landing Page</span>
            </button>
        </div>

        <!-- Navigation Controls -->
        <div class="flex items-center space-x-2">
            <button onclick="prevSlide()" class="px-3 py-1.5 rounded bg-slate-100 hover:bg-slate-200 text-brand-navy font-semibold text-xs flex items-center gap-1 transition">
                <i data-lucide="chevron-left" class="w-4 h-4"></i> Prev
            </button>

            <span id="slideIndicator" class="px-3 py-1 bg-brand-navy text-white text-xs font-mono font-bold rounded">
                Landing Page (Top 5)
            </span>

            <button onclick="nextSlide()" class="px-3 py-1.5 rounded bg-slate-100 hover:bg-slate-200 text-brand-navy font-semibold text-xs flex items-center gap-1 transition">
                Next <i data-lucide="chevron-right" class="w-4 h-4"></i>
            </button>

            <select id="slideDropdown" onchange="goToSlide(parseInt(this.value, 10))" 
                    class="text-xs font-medium bg-slate-50 border border-slate-300 rounded py-1.5 px-2 focus:outline-none cursor-pointer max-w-[240px]">
                <option value="0">★ Landing Page: Top 5 Priority Opportunities</option>
                {% for c in clients %}
                <option value="{{ loop.index }}">{{ loop.index }}. {{ c.name }}</option>
                {% endfor %}
            </select>

            <div class="relative w-44">
                <input type="text" id="quickFilter" onkeyup="filterSlideDropdown()" placeholder="Quick find client..."
                       class="w-full text-xs pl-7 pr-2 py-1.5 rounded border border-slate-300 bg-slate-50 focus:bg-white focus:outline-none">
                <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 absolute left-2 top-1/2 -translate-y-1/2"></i>
            </div>

            <button onclick="window.print()" class="px-3 py-1.5 rounded bg-brand-navy hover:bg-slate-800 text-white font-semibold text-xs flex items-center gap-1.5 shadow-xs transition">
                <i data-lucide="printer" class="w-3.5 h-3.5"></i> Export A4 Deck
            </button>
        </div>

    </header>

    <!-- ALL SLIDES CONTAINER -->
    <div id="deckContainer" class="w-full max-w-[1680px]">

        <!-- SLIDE 0: LANDING PAGE -->
        <div id="slide-0" class="slide-page">
            <div class="executive-slide p-6 flex flex-col justify-between">
                
                <div>
                    <!-- Header -->
                    <div class="flex items-start justify-between pb-3 border-b border-brand-border">
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-[11px] font-mono uppercase tracking-wider font-bold px-2.5 py-0.5 rounded bg-brand-navy text-white">
                                    Strategic Portfolio Strategy
                                </span>
                                <span class="text-[11px] font-semibold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 flex items-center gap-1">
                                    <i data-lucide="trending-up" class="w-3 h-3 text-emerald-600"></i> Revenue Optimization Matrix
                                </span>
                                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">
                                    EV = Win Likelihood (P) × 3-Yr Deal Value (V)
                                </span>
                            </div>
                            <h1 class="text-3xl font-serif font-bold text-brand-navy tracking-tight">
                                Top 5 High-Yield {{ partner.display_name }} Opportunities
                            </h1>
                            <p class="text-xs text-slate-500 mt-0.5">
                                Executive account prioritization ranked by risk-adjusted expected revenue for {{ partner.display_name }} adoption across 64 Nordic enterprise accounts.
                            </p>
                        </div>

                        <div class="text-right">
                            <div class="text-[11px] font-mono text-slate-400">
                                Lead Account Executive: <strong class="text-slate-700">Thomas Dinsen</strong>
                            </div>
                            <div class="text-xs font-mono font-bold text-brand-navy mt-0.5">
                                Executive Landing Page (Deck Overview)
                            </div>
                            <div class="text-[10px] text-slate-400 font-mono mt-0.5">
                                {{ partner.co_brand_text }}
                            </div>
                        </div>
                    </div>

                    <!-- Macro KPI Banner -->
                    <div class="grid grid-cols-2 lg:grid-cols-5 gap-3 my-4">
                        <div class="p-3 bg-brand-navy text-white rounded-lg text-center">
                            <span class="text-[9px] font-mono uppercase tracking-wider text-slate-300 block">Total Top 5 Pipeline</span>
                            <span class="text-xl font-bold font-mono text-white mt-0.5 block">€44,240,000</span>
                            <span class="text-[9px] text-slate-300">Combined 3-Yr Addressable</span>
                        </div>
                        <div class="p-3 bg-brand-navy text-white rounded-lg text-center border-b-2 border-b-emerald-400">
                            <span class="text-[9px] font-mono uppercase tracking-wider text-emerald-300 block">Risk-Adjusted EV</span>
                            <span class="text-xl font-bold font-mono text-emerald-400 mt-0.5 block">€33,287,800</span>
                            <span class="text-[9px] text-emerald-200 font-medium">Weighted Revenue Potential</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-lg border border-slate-200 text-center">
                            <span class="text-[9px] font-mono uppercase tracking-wider text-slate-500 block">Avg Win Likelihood</span>
                            <span class="text-xl font-bold font-mono text-brand-navy mt-0.5 block">75.4%</span>
                            <span class="text-[9px] text-emerald-600 font-semibold">High Strategic Readiness</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-lg border border-slate-200 text-center">
                            <span class="text-[9px] font-mono uppercase tracking-wider text-slate-500 block">Co-Funding Subsidies</span>
                            <span class="text-xl font-bold font-mono text-brand-teal mt-0.5 block">{{ partner.funding_tier.split('(')[0] }}</span>
                            <span class="text-[9px] text-slate-500">{{ partner.funding_program.split('(')[0] }}</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-lg border border-slate-200 text-center">
                            <span class="text-[9px] font-mono uppercase tracking-wider text-slate-500 block">Total Accounts Mapped</span>
                            <span class="text-xl font-bold font-mono text-partner-accent mt-0.5 block">64 Clients</span>
                            <span class="text-[9px] text-slate-500">100% Portfolio Coverage</span>
                        </div>
                    </div>

                    <!-- Top 5 Ranked Cards -->
                    <div class="space-y-2.5">
                        {% for deal in top_deals %}
                        <div class="p-3.5 bg-white rounded-lg border border-slate-200 hover:border-brand-navy/60 hover:shadow-md transition flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
                            
                            <div class="flex items-center space-x-3.5 min-w-[280px]">
                                <div class="w-8 h-8 rounded-full bg-brand-navy text-white flex items-center justify-center font-bold font-mono text-sm shrink-0">
                                    #{{ deal.rank }}
                                </div>
                                <div>
                                    <div class="flex items-center gap-2">
                                        <h3 class="text-base font-bold text-brand-navy">{{ deal.client_name }}</h3>
                                        <span class="text-[9px] font-mono uppercase px-1.5 py-0.2 rounded bg-slate-100 text-slate-700 border border-slate-200">
                                            {{ deal.industry }}
                                        </span>
                                    </div>
                                    <p class="text-[11px] text-slate-500 mt-0.5">
                                        Target Close: <strong class="text-brand-navy">{{ deal.target_close_quarter }}</strong> &nbsp;|&nbsp; Champion: <strong class="text-slate-700">{{ deal.target_champion }}</strong>
                                    </p>
                                </div>
                            </div>

                            <div class="grid grid-cols-3 gap-3 min-w-[340px] text-center bg-slate-50 p-2.5 rounded-md border border-slate-200/70">
                                <div>
                                    <span class="text-[9px] font-mono uppercase text-slate-400 block">Deal Value</span>
                                    <span class="text-xs font-bold font-mono text-brand-navy block">{{ deal.deal_value_eur }}</span>
                                </div>
                                <div>
                                    <span class="text-[9px] font-mono uppercase text-slate-400 block">Likelihood (P)</span>
                                    <div class="flex items-center justify-center gap-1.5 mt-0.5">
                                        <div class="w-12 bg-slate-200 rounded-full h-1.5 overflow-hidden">
                                            <div class="bg-emerald-600 h-1.5 rounded-full" style="width: {{ deal.win_probability_pct }}%"></div>
                                        </div>
                                        <span class="text-xs font-bold font-mono text-emerald-700">{{ deal.win_probability_pct }}%</span>
                                    </div>
                                </div>
                                <div class="border-l border-slate-200 pl-2">
                                    <span class="text-[9px] font-mono uppercase text-emerald-700 font-bold block">Expected Value (EV)</span>
                                    <span class="text-xs font-bold font-mono text-emerald-600 block">{{ deal.expected_value_eur }}</span>
                                </div>
                            </div>

                            <div class="flex-1 text-[11px] leading-tight text-slate-700 max-w-xl">
                                <p><strong class="text-amber-800">Burning Platform:</strong> {{ deal.burning_platform }}</p>
                                {% if mode == 'closing-plan' %}
                                <p class="mt-1 text-slate-600"><strong class="text-brand-teal">Opening Move:</strong> {{ deal.immediate_action }}</p>
                                {% else %}
                                <p class="mt-1 text-slate-600"><strong class="text-brand-navy">{{ partner.display_name }} Solution:</strong> {{ partner.primary_tech_stack }}</p>
                                {% endif %}
                            </div>

                            <div class="shrink-0 flex flex-col items-end gap-1">
                                <button onclick="goToSlide({{ deal.target_slide_idx }})" class="px-3.5 py-1.5 rounded bg-brand-navy hover:bg-slate-800 text-white font-semibold text-xs flex items-center gap-1.5 shadow-xs transition">
                                    <span>View Slide {{ deal.target_slide_idx }}</span>
                                    <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-brand-teal"></i>
                                </button>
                                <span class="text-[9px] font-mono text-emerald-700 font-semibold">{{ partner.funding_tier.split('(')[0] }}</span>
                            </div>

                        </div>
                        {% endfor %}
                    </div>
                </div>

                <!-- Footer -->
                <div class="mt-4 pt-3 border-t border-brand-border flex items-center justify-between text-[11px] text-slate-500 font-mono">
                    <div class="flex items-center space-x-4">
                        <span>Portfolio Strategy: <strong class="text-brand-navy">64 Enterprise Accounts</strong></span>
                        <span>Partner Program: <strong class="text-emerald-700">{{ partner.funding_program }}</strong></span>
                    </div>
                    <div>
                        <button onclick="goToSlide(1)" class="text-xs font-semibold text-brand-navy hover:text-brand-teal flex items-center gap-1">
                            <span>Browse All 64 Client Slides</span>
                            <i data-lucide="chevron-right" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

            </div>
        </div>

        <!-- SLIDES 1 to 64: DEDICATED SLIDES -->
        {% for c in clients %}
        <div id="slide-{{ loop.index }}" class="slide-page hidden">
            
            <div class="executive-slide p-6 flex flex-col justify-between">
                
                <div>
                    <!-- Header -->
                    <div class="flex items-start justify-between pb-3 border-b border-brand-border">
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-[11px] font-mono uppercase tracking-wider font-bold px-2.5 py-0.5 rounded bg-brand-navy text-white">
                                    {{ c.industry }}
                                </span>
                                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">
                                    {{ c.country }}
                                </span>
                                <span class="text-[11px] font-semibold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 flex items-center gap-1">
                                    <i data-lucide="check-circle" class="w-3 h-3 text-emerald-600"></i> {{ partner.display_name }} Co-Funding Ready
                                </span>
                            </div>
                            <div class="flex items-baseline gap-3">
                                <h1 class="text-3xl font-serif font-bold text-brand-navy tracking-tight">
                                    {{ c.name }}
                                </h1>
                                {% if c.parent_company and c.parent_company != c.name %}
                                <span class="text-sm font-medium text-slate-500">
                                    (Parent: <strong class="text-slate-700">{{ c.parent_company }}</strong>)
                                </span>
                                {% endif %}
                            </div>
                        </div>

                        <!-- Right Metric Strip -->
                        <div class="text-right">
                            <div class="text-[11px] font-mono text-slate-400">
                                Account Executive: <strong class="text-slate-700">{{ c.account_executive }}</strong>
                            </div>
                            <div class="text-xs font-mono font-bold text-brand-navy mt-0.5">
                                {% if mode == 'closing-plan' %}Closing Plan Slide {{ loop.index }} of {{ clients|length }}{% else %}Sales Dossier Slide {{ loop.index }} of {{ clients|length }}{% endif %}
                            </div>
                            <div class="text-[10px] text-slate-400 font-mono mt-0.5">
                                {{ partner.co_brand_text }}
                            </div>
                        </div>
                    </div>

                    <!-- Thesis Callout Banner -->
                    <div class="mt-3.5 mb-4 p-3.5 rounded-md bg-brand-navy text-white flex items-center justify-between border-l-4 border-l-partner-accent shadow-xs">
                        <div class="flex items-start space-x-3">
                            <div class="p-1.5 bg-white/10 rounded mt-0.5">
                                <i data-lucide="crosshair" class="w-4 h-4 text-partner-accent"></i>
                            </div>
                            <div>
                                <span class="text-[10px] font-mono uppercase tracking-widest text-slate-300 font-bold block">
                                    {% if mode == 'closing-plan' %}Strategic Closing Thesis & Deal Motion for {{ c.name }}{% else %}What {{ partner.display_name }} Solves for {{ c.name }} (Core Executive Thesis){% endif %}
                                </span>
                                <p class="text-xs font-medium text-slate-100 leading-snug mt-0.5">
                                    {{ c.intel.what_partner_solves or c.intel.what_databricks_solves }}
                                </p>
                            </div>
                        </div>
                        <div class="hidden lg:flex items-center space-x-3 pl-4 border-l border-white/20 shrink-0 text-right">
                            <div>
                                <span class="text-[10px] font-mono uppercase text-slate-300">Est. 3-Yr Net Value</span>
                                <span class="text-base font-mono font-bold text-emerald-400 block">{{ c.intel.three_year_net_value_eur }}</span>
                            </div>
                        </div>
                    </div>

                    {% if mode == 'closing-plan' %}
                    <!-- CLOSING PLAN MODE: 4 TACTICAL CLOSING QUADRANTS -->
                    <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
                        
                        <!-- Quadrant 1: 4-Phase Roadmap -->
                        <div class="consulting-quadrant p-3.5 flex flex-col justify-between border-t-2 border-t-brand-navy">
                            <div>
                                <div class="flex items-center justify-between pb-1 mb-2 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-navy flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-brand-navy text-white inline-flex items-center justify-center text-[9px]">1</span>
                                        Step-by-Step Approach Roadmap
                                    </span>
                                    <span class="text-[9px] font-mono text-slate-400">90-Day Close</span>
                                </div>
                                <div class="space-y-2">
                                    {% for ph in c.closing.four_phases %}
                                    <div class="p-2 rounded bg-slate-50 border border-slate-200/80 text-[10px] leading-tight">
                                        <strong class="text-brand-navy font-mono text-[9px] block">{{ ph.phase }}</strong>
                                        <p class="font-bold text-slate-800 text-[10px]">{{ ph.title }}</p>
                                        <p class="text-slate-600 mt-0.5 leading-snug">{{ ph.action }}</p>
                                        <p class="text-brand-teal font-medium mt-1 text-[9px]">✓ Deliverable: {{ ph.deliverable }}</p>
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>

                        <!-- Quadrant 2: Stakeholder Matrix -->
                        <div class="consulting-quadrant p-3.5 flex flex-col justify-between border-t-2 border-t-emerald-600">
                            <div>
                                <div class="flex items-center justify-between pb-1 mb-2 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-emerald-800 flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-emerald-700 text-white inline-flex items-center justify-center text-[9px]">2</span>
                                        Stakeholder Engagement Matrix
                                    </span>
                                    <span class="text-[9px] font-mono text-slate-400">4 Personas</span>
                                </div>
                                <div class="space-y-2 text-[10px]">
                                    <div class="p-2 rounded bg-slate-50 border border-slate-200/80">
                                        <span class="font-bold text-brand-navy block text-[10px]">Economic Buyer (CFO / Finance)</span>
                                        <p class="text-slate-600 mt-0.5">{{ c.closing.stakeholders.economic_buyer.focus }}</p>
                                        <p class="text-slate-500 italic mt-0.5">Handler: {{ c.closing.stakeholders.economic_buyer.objection_handler }}</p>
                                    </div>
                                    <div class="p-2 rounded bg-slate-50 border border-slate-200/80">
                                        <span class="font-bold text-brand-navy block text-[10px]">Technical Champion (CTO / Architecture)</span>
                                        <p class="text-slate-600 mt-0.5">{{ c.closing.stakeholders.technical_champion.focus }}</p>
                                        <p class="text-slate-500 italic mt-0.5">Handler: {{ c.closing.stakeholders.technical_champion.objection_handler }}</p>
                                    </div>
                                    <div class="p-2 rounded bg-slate-50 border border-slate-200/80">
                                        <span class="font-bold text-brand-navy block text-[10px]">Operational Sponsor (CDO / Ops)</span>
                                        <p class="text-slate-600 mt-0.5">{{ c.closing.stakeholders.operational_sponsor.focus }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Quadrant 3: Partner Co-Selling -->
                        <div class="consulting-quadrant p-3.5 flex flex-col justify-between border-t-2 border-t-partner-accent">
                            <div class="space-y-3 text-[10px]">
                                <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-navy flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-brand-navy text-white inline-flex items-center justify-center text-[9px]">3</span>
                                        {{ partner.display_name }} Co-Selling
                                    </span>
                                    <span class="text-[9px] font-mono text-slate-400">Joint Touchpoints</span>
                                </div>
                                <div class="p-2.5 rounded bg-slate-50 border border-slate-200/80">
                                    <span class="text-[10px] font-bold text-brand-navy uppercase font-mono block mb-1">When to Bring in {{ partner.display_name }}</span>
                                    <p class="text-slate-700 leading-snug">{{ partner.when_to_involve }}</p>
                                </div>
                                <div class="p-2.5 rounded bg-slate-50 border border-slate-200/80">
                                    <span class="text-[10px] font-bold text-brand-teal uppercase font-mono block mb-1">What {{ partner.display_name }} Provides Us</span>
                                    <p class="text-slate-700 leading-snug">{{ partner.partner_provides }}</p>
                                </div>
                            </div>
                        </div>

                        <!-- Quadrant 4: Execution & Next Move -->
                        <div class="consulting-quadrant p-3.5 flex flex-col justify-between border-t-2 border-t-brand-teal">
                            <div class="space-y-2.5 text-[10px]">
                                <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-teal flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-brand-teal text-white inline-flex items-center justify-center text-[9px]">4</span>
                                        Execution Action Plan
                                    </span>
                                    <span class="text-[9px] font-mono text-emerald-700 font-bold">This Week</span>
                                </div>
                                <div class="p-2.5 bg-emerald-50/70 rounded border border-emerald-300/80">
                                    <div class="flex items-center justify-between mb-1">
                                        <span class="text-[10px] font-bold text-emerald-950 uppercase font-mono flex items-center gap-1">
                                            <i data-lucide="play" class="w-3 h-3 text-emerald-700"></i> Opening Move (This Week)
                                        </span>
                                        <button onclick="copyAction('{{ c.closing.immediate_next_action|replace("'", "\\\\'") }}')" class="text-emerald-800 hover:text-emerald-950 p-0.5">
                                            <i data-lucide="copy" class="w-3 h-3"></i>
                                        </button>
                                    </div>
                                    <p class="text-emerald-950 font-medium text-[10px] leading-snug">{{ c.closing.immediate_next_action }}</p>
                                </div>
                                <div class="p-2 rounded bg-slate-50 border border-slate-200">
                                    <span class="text-[9px] font-bold text-amber-800 uppercase font-mono block mb-0.5">Deal Blocker & Countermeasure</span>
                                    <p class="text-slate-700 leading-snug">{{ c.closing.deal_blocker_mitigation }}</p>
                                </div>
                            </div>
                        </div>

                    </div>
                    {% else %}
                    <!-- SALES DOSSIER MODE: STRICT 8-PART STRATEGIC CONSULTING GRID -->
                    <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
                        
                        <!-- Col 1: Part 1 & 2 (Recon & FOMO) -->
                        <div class="consulting-quadrant p-4 flex flex-col justify-between border-t-2 border-t-brand-navy">
                            <div class="space-y-3">
                                <div>
                                    <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-slate-100">
                                        <span class="text-[10px] font-mono font-bold uppercase text-brand-navy flex items-center gap-1">
                                            <span class="w-4 h-4 rounded-full bg-brand-navy text-white inline-flex items-center justify-center text-[9px]">1</span>
                                            Trendspaning & Legacy Debt
                                        </span>
                                    </div>
                                    <p class="text-[11px] text-slate-700 leading-tight"><strong>Tailwind:</strong> {{ c.intel.trend_macro }}</p>
                                    <p class="text-[11px] text-brand-teal mt-1 leading-tight"><strong>Peer Moves:</strong> {{ c.intel.trend_competitors }}</p>
                                    <p class="text-[11px] text-slate-600 mt-1 leading-tight"><strong class="text-amber-800">Architectural Debt:</strong> {{ c.intel.trend_legacy_debt }}</p>
                                </div>
                                <div class="pt-2 border-t border-slate-100">
                                    <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-slate-100">
                                        <span class="text-[10px] font-mono font-bold uppercase text-amber-700 flex items-center gap-1">
                                            <span class="w-4 h-4 rounded-full bg-amber-600 text-white inline-flex items-center justify-center text-[9px]">2</span>
                                            FOMO: Cost of Inaction
                                        </span>
                                    </div>
                                    <div class="p-2 bg-amber-50/70 rounded border border-amber-200/60 mb-1.5">
                                        <p class="text-[11px] font-medium text-amber-950 leading-tight">{{ c.intel.fomo_cost_of_inaction }}</p>
                                    </div>
                                    <p class="text-[10px] text-slate-600 leading-tight"><strong>Velocity Gap:</strong> {{ c.intel.fomo_peer_velocity }}</p>
                                </div>
                            </div>
                        </div>

                        <!-- Col 2: Part 3 & 4 (Business Case & Questions) -->
                        <div class="consulting-quadrant p-4 flex flex-col justify-between border-t-2 border-t-emerald-600">
                            <div>
                                <div class="flex items-center justify-between pb-1 mb-2 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-emerald-800 flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-emerald-700 text-white inline-flex items-center justify-center text-[9px]">3</span>
                                        Business Case Metrics
                                    </span>
                                    <span class="text-[9px] font-mono text-slate-400">Payback: {{ c.intel.payback_months }} Mo</span>
                                </div>
                                <div class="grid grid-cols-2 gap-2 mb-2">
                                    <div class="p-2 bg-slate-50 rounded border border-slate-200 text-center">
                                        <span class="text-[9px] font-mono uppercase text-slate-400 block">3-Yr TCO Savings</span>
                                        <span class="text-base font-bold font-mono text-brand-navy">{{ c.intel.tco_reduction_pct }}%</span>
                                    </div>
                                    <div class="p-2 bg-slate-50 rounded border border-slate-200 text-center">
                                        <span class="text-[9px] font-mono uppercase text-slate-400 block">DE Productivity</span>
                                        <span class="text-base font-bold font-mono text-partner-accent">{{ c.intel.productivity_lift_multiplier }}</span>
                                    </div>
                                </div>
                                <div class="pt-2 border-t border-slate-100">
                                    <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-slate-100">
                                        <span class="text-[10px] font-mono font-bold uppercase text-brand-navy flex items-center gap-1">
                                            <span class="w-4 h-4 rounded-full bg-brand-navy text-white inline-flex items-center justify-center text-[9px]">4</span>
                                            Provocative Key Questions
                                        </span>
                                    </div>
                                    <div class="space-y-1.5">
                                        {% for q in c.intel.key_questions[:3] %}
                                        <div class="p-2 rounded bg-slate-50 border border-slate-200 text-[11px] text-slate-800 flex items-start justify-between gap-1.5">
                                            <div>
                                                <span class="text-[9px] font-mono font-bold uppercase text-slate-500 block">{{ q.target }}</span>
                                                <p class="leading-tight italic mt-0.5">"{{ q.question }}"</p>
                                            </div>
                                            <button onclick="copyAction('{{ q.question|replace("'", "\\\\'") }}')" class="p-1 text-slate-400 hover:text-brand-navy shrink-0">
                                                <i data-lucide="copy" class="w-3 h-3"></i>
                                            </button>
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Col 3: Part 5 (Partner Workloads) -->
                        <div class="consulting-quadrant p-4 flex flex-col justify-between border-t-2 border-t-partner-accent">
                            <div>
                                <div class="flex items-center justify-between pb-1 mb-2 border-b border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-navy flex items-center gap-1">
                                        <span class="w-4 h-4 rounded-full bg-brand-navy text-white inline-flex items-center justify-center text-[9px]">5</span>
                                        {{ partner.display_name }} Workloads
                                    </span>
                                </div>
                                <div class="space-y-2.5">
                                    {% for uc in c.intel.use_cases %}
                                    <div class="p-2.5 rounded bg-slate-50 border border-slate-200/80">
                                        <span class="text-[9px] font-mono font-bold uppercase px-1.5 py-0.2 rounded bg-blue-100 text-blue-800 block w-fit mb-1">{{ uc.category }}</span>
                                        <h4 class="text-xs font-bold text-brand-navy leading-tight">{{ uc.title }}</h4>
                                        <p class="text-[10px] text-slate-600 leading-tight mt-1">{{ uc.description }}</p>
                                        <div class="mt-2 pt-1 border-t border-slate-200/60 text-[9px] font-mono text-slate-500 flex items-center gap-1">
                                            <i data-lucide="cpu" class="w-2.5 h-2.5 text-brand-teal"></i>
                                            <span class="truncate">{{ uc.architecture }}</span>
                                        </div>
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>

                        <!-- Col 4: Part 6, 7 & 8 (Subsidies & Peer Benchmark) -->
                        <div class="consulting-quadrant p-4 flex flex-col justify-between border-t-2 border-t-brand-teal">
                            <div class="space-y-3">
                                <div>
                                    <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-slate-100">
                                        <span class="text-[10px] font-mono font-bold uppercase text-brand-teal flex items-center gap-1">
                                            <span class="w-4 h-4 rounded-full bg-brand-teal text-white inline-flex items-center justify-center text-[9px]">6</span>
                                            {{ partner.display_name }} Co-Funding
                                        </span>
                                        <span class="text-[9px] font-mono text-emerald-700 font-bold">{{ partner.funding_countdown_days }}-Day Clock</span>
                                    </div>
                                    <div class="p-2 bg-slate-50 rounded border border-slate-200 text-[11px]">
                                        <p class="font-bold text-brand-navy">{{ partner.funding_tier }}</p>
                                        <p class="text-[10px] text-slate-500 mt-0.5">{{ partner.funding_customer_copay }}</p>
                                    </div>
                                </div>
                                <div class="pt-1 border-t border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-navy block mb-1">7. 4-Week Accelerator</span>
                                    <p class="text-[10px] text-slate-700 leading-tight">Cegeka Zero-Risk 4-Week {{ partner.display_name }} Jumpstart (W1: LZ $\to$ W2: Convert $\to$ W3: Modeling $\to$ W4: Handover).</p>
                                </div>
                                <div class="pt-1 border-t border-slate-100">
                                    <span class="text-[10px] font-mono font-bold uppercase text-brand-navy block mb-1">8. Cegeka Peer Case</span>
                                    {% if c.intel.matched_cases %}
                                    <div class="p-2 bg-slate-50 rounded border border-slate-200 text-[10px]">
                                        <p class="font-bold text-brand-navy">{{ c.intel.matched_cases[0] }}</p>
                                        <p class="text-slate-600 mt-0.5 leading-tight">Verified production reference from Cegeka customer portfolio.</p>
                                    </div>
                                    {% endif %}
                                </div>
                            </div>
                        </div>

                    </div>
                    {% endif %}
                </div>

                <!-- Footer -->
                <div class="mt-4 pt-3 border-t border-brand-border flex items-center justify-between text-[10px] text-slate-400 font-mono">
                    <div class="flex items-center space-x-3">
                        <span class="text-brand-navy font-bold">CONFIDENTIAL</span>
                        <span>Prepared exclusively for {{ c.name }} Leadership</span>
                        <span>Lead AE: {{ c.account_executive }}</span>
                    </div>
                    <div class="flex items-center space-x-3">
                        <span>Slide {{ loop.index }} of {{ clients|length }}</span>
                        <span>{{ partner.co_brand_text }}</span>
                    </div>
                </div>

            </div>

        </div>
        {% endfor %}

    </div>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 bg-brand-navy text-white text-xs px-4 py-2.5 rounded-lg shadow-lg flex items-center space-x-2 border border-slate-700">
        <i data-lucide="check" class="w-4 h-4 text-emerald-400"></i>
        <span>Copied to clipboard</span>
    </div>

    <script>
        let currentSlide = 0;
        const totalSlides = {{ clients|length }};

        lucide.createIcons();

        function showSlide(index) {
            if (index < 0) index = 0;
            if (index > totalSlides) index = totalSlides;

            for (let i = 0; i <= totalSlides; i++) {
                const el = document.getElementById(`slide-${i}`);
                if (el) {
                    if (i === index) {
                        el.classList.remove('hidden');
                    } else {
                        el.classList.add('hidden');
                    }
                }
            }

            currentSlide = index;
            if (index === 0) {
                document.getElementById('slideIndicator').textContent = `Landing Page (Top 5)`;
            } else {
                document.getElementById('slideIndicator').textContent = `Slide ${index} / ${totalSlides}`;
            }
            document.getElementById('slideDropdown').value = index;
            lucide.createIcons();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function nextSlide() { showSlide(currentSlide + 1); }
        function prevSlide() { showSlide(currentSlide - 1); }
        function goToSlide(index) { showSlide(index); }

        window.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
            if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
            else if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        });

        function filterSlideDropdown() {
            const query = document.getElementById('quickFilter').value.toLowerCase();
            const dropdown = document.getElementById('slideDropdown');
            let firstMatch = -1;
            for (let i = 0; i < dropdown.options.length; i++) {
                const opt = dropdown.options[i];
                const matches = opt.textContent.toLowerCase().includes(query);
                opt.style.display = matches ? '' : 'none';
                if (matches && firstMatch === -1) firstMatch = i;
            }
            if (firstMatch !== -1) showSlide(firstMatch);
        }

        function copyAction(text) {
            navigator.clipboard.writeText(text).then(() => {
                const toast = document.getElementById('toast');
                toast.classList.add('show');
                setTimeout(() => toast.classList.remove('show'), 2000);
            });
        }
    </script>
</body>
</html>
"""

# ==============================================================================
# CLI DISPATCHER
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Multi-Partner Sales Dossier & Closing Plan Compiler")
    parser.add_argument("--partner", default="databricks", help="Target partner (databricks, microsoft, joint, snowflake, aws, gcp, or custom)")
    parser.add_argument("--mode", choices=["sales-dossier", "closing-plan"], default="sales-dossier", help="Execution mode (sales-dossier or closing-plan)")
    parser.add_argument("--client-list", default="", help="Path to client list file")
    parser.add_argument("--output", default="", help="Output HTML filename")
    parser.add_argument("--clients", default="", help="Comma-separated client names")
    parser.add_argument("--max-clients", type=int, default=100, help="Max clients to process")
    args = parser.parse_args()

    # Resolve Partner
    partner_cfg = resolve_partner(args.partner)

    # Determine default output file if not set
    if not args.output:
        p_slug = partner_cfg.id
        if args.mode == "closing-plan":
            args.output = f"{p_slug}_closing_plan_dossier.html"
        else:
            args.output = f"{p_slug}_sales_dossier_v2.html"

    sys.stdout.write("================================================================================\n")
    sys.stdout.write(f"  CEGEKA MULTI-PARTNER DOSSIER COMPILER (vm-nor-dev)\n")
    sys.stdout.write(f"  Partner: {partner_cfg.display_name.upper()} | Mode: {args.mode.upper()}\n")
    sys.stdout.write("================================================================================\n")

    # Locate client list
    list_path = args.client_list
    if not list_path:
        # Check standard locations
        candidates = [
            os.path.join(os.getcwd(), "client_list.txt"),
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples", "sample_client_list.txt")
        ]
        for c in candidates:
            if os.path.isfile(c):
                list_path = c
                break

    if not list_path or not os.path.isfile(list_path):
        sys.stderr.write(f"[!] Error: Could not locate client list file.\n")
        sys.exit(1)

    sys.stdout.write(f"[*] Ingesting customer accounts from: {list_path}\n")
    with open(list_path, "r", encoding="utf-8") as f:
        lines = [l.strip().split("\t") for l in f if l.strip()]

    data_lines = lines[1:] if lines and "account executive" in lines[0][0].lower() else lines
    
    clients = []
    slide_map = {}
    for idx, parts in enumerate(data_lines, 1):
        ae = parts[0].strip() if len(parts) > 0 else "Thomas Dinsen"
        parent = parts[1].strip() if len(parts) > 1 else ""
        sub = parts[2].strip() if len(parts) > 2 else ""
        name = sub if sub else parent
        
        intel = get_client_intelligence(name, parent, sub)
        intel = adapt_intel_for_partner(intel, partner_cfg)
        closing = get_client_closing_strategy(name, parent, sub, intel.get("industry", "Enterprise"))
        
        clients.append({
            "slide_number": idx,
            "name": name,
            "parent_company": parent if parent != name else "",
            "subsidiary": sub if sub != name else "",
            "account_executive": ae,
            "industry": intel.get("industry", "Enterprise"),
            "country": "Nordics (Denmark, Norway, Sweden)",
            "intel": intel,
            "closing": closing
        })
        slide_map[name.lower()] = idx

    # Apply client filter if requested
    if args.clients:
        allowed = [c.strip().lower() for c in args.clients.split(",") if c.strip()]
        clients = [c for c in clients if any(a in c["name"].lower() or a in c["parent_company"].lower() for a in allowed)]

    clients = clients[:args.max_clients]

    # Map Top 5 Deals
    enriched_top_deals = []
    for d in TOP_PRIORITY_DEALS:
        deal_copy = dict(d)
        matched_idx = None
        for s_name, s_num in slide_map.items():
            if d["client_name"].lower() in s_name or s_name in d["client_name"].lower():
                matched_idx = s_num
                break
        deal_copy["target_slide_idx"] = matched_idx if matched_idx is not None else d["target_slide_idx"]
        enriched_top_deals.append(deal_copy)

    # Compile HTML using Jinja2
    try:
        from jinja2 import Template
    except ImportError:
        sys.stderr.write("[!] Jinja2 is required.\n")
        sys.exit(1)

    template = Template(HTML_UNIFIED_TEMPLATE)
    rendered_html = template.render(
        partner=partner_cfg,
        mode=args.mode,
        clients=clients,
        top_deals=enriched_top_deals
    )

    output_path = os.path.abspath(args.output)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    file_size_kb = os.path.getsize(output_path) / 1024
    sys.stdout.write(f"[✓] Compiled {partner_cfg.display_name} {args.mode.replace('-', ' ').title()} Deck: {output_path} ({file_size_kb:.1f} KB)\n")
    sys.stdout.write(f"    - Partner: {partner_cfg.display_name} ({partner_cfg.badge_text})\n")
    sys.stdout.write(f"    - Slides: Landing Page (Top 5 Matrix) + {len(clients)} Account Slides\n")
    sys.stdout.write("================================================================================\n")

if __name__ == "__main__":
    main()
