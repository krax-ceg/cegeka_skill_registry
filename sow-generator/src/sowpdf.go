package main

import (
	"fmt"
	"strings"
)

func nonEmpty(s string) bool { return strings.TrimSpace(s) != "" }

func firstNonEmpty(a, b string) string {
	if nonEmpty(a) {
		return a
	}
	return b
}

func modelLabel(m string) string {
	switch m {
	case "fixed_fee":
		return "Fixed Fee"
	case "outcome_based":
		return "Outcome-Based"
	case "hybrid":
		return "Hybrid"
	case "time_and_materials":
		return "Time & Materials"
	default:
		return ""
	}
}

func BuildSOWPDF(d *SOWData) []byte {
	p := NewPDF()
	contentW := pageW - 2*marginX

	// ---- Cover ----
	p.y = pageH - 140
	p.SetFont("F4", 24)
	p.SetColor(colNavy)
	p.Paragraph(marginX, contentW, "Statement of Work")
	p.SetFont("F4", 16)
	p.Paragraph(marginX, contentW, "Data, AI & Knowledge Services")
	p.Gap(20)
	p.HLine(marginX, pageW-marginX, p.y, colGold, 1.5)
	p.Gap(20)

	coverRow := func(label, val string) {
		p.SetFont("F2", 10)
		p.SetColor(colNavy)
		p.Paragraph(marginX, contentW, label+":")
		p.WriteValue(marginX+14, contentW-14, val)
		p.Gap(4)
	}
	coverRow("Client", d.DocControl.ClientLegalName)
	coverRow("Cegeka Entity", d.DocControl.CegekaEntity)
	coverRow("SOW Reference", d.Meta.Ref)
	coverRow("Date", d.Meta.Date)
	coverRow("Version", firstNonEmpty(d.Meta.Version, "v1.0"))

	p.newPage()

	// ---- 1. Executive Summary ----
	p.SectionHeading("1. Executive Summary")
	p.WriteLead(marginX, contentW, d.ExecSummary.VisionStatement)
	p.Gap(6)
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.WriteValue(marginX, contentW, d.ExecSummary.Narrative)
	p.Gap(6)
	for _, kv := range [][2]string{
		{"What we will deliver", d.ExecSummary.WhatWeDeliver},
		{"How success is measured", d.ExecSummary.HowSuccessMeasured},
	} {
		p.SubHeading(kv[0])
		p.WriteValue(marginX, contentW, kv[1])
	}
	p.SubHeading("Commercial headline")
	p.WriteValueBold(marginX, contentW, d.ExecSummary.CommercialHeadline)

	// ---- 2. Document Control ----
	p.SectionHeading("2. Document Control")
	p.Table([]string{"Field", "Value"}, []float64{1, 2.5}, [][]string{
		{"Client", d.DocControl.ClientLegalName},
		{"Cegeka Entity", d.DocControl.CegekaEntity},
		{"SOW reference number", d.Meta.Ref},
		{"MSA date", d.DocControl.MsaDate},
		{"Effective date", d.DocControl.EffectiveDate},
		{"SOW owner (Cegeka)", d.DocControl.SowOwnerCegeka},
		{"SOW owner (Client)", d.DocControl.SowOwnerClient},
		{"Version", firstNonEmpty(d.Meta.Version, "v1.0")},
	})

	// ---- 3. Business Context, Objectives & Scope ----
	p.SectionHeading("3. Business Context, Objectives & Scope of Services")
	p.SubHeading("3.1 Business context")
	p.WriteValue(marginX, contentW, d.ContextScope.BusinessContext)

	p.SubHeading("3.2 Objectives")
	if len(d.ContextScope.Objectives) == 0 {
		p.WriteValueList(marginX, contentW, nil)
	} else {
		items := make([]string, len(d.ContextScope.Objectives))
		for i, o := range d.ContextScope.Objectives {
			tag := "[Tactical]"
			if strings.EqualFold(o.Type, "strategic") {
				tag = "[Strategic]"
			}
			items[i] = tag + " " + o.Text
		}
		p.WriteValueList(marginX, contentW, items)
	}

	if len(d.ContextScope.Workstreams) > 0 {
		p.SubHeading("Scope by Workstream")
		rows := make([][]string, len(d.ContextScope.Workstreams))
		for i, w := range d.ContextScope.Workstreams {
			rows[i] = []string{w.Workstream, w.InScope, w.OutOfScope}
		}
		p.Table([]string{"Workstream", "In-scope activities", "Out of scope"}, []float64{1, 1.6, 1.6}, rows, 0)
	}

	p.SubHeading("3.3 Assumptions")
	p.WriteValueList(marginX, contentW, d.ContextScope.Assumptions)

	p.SubHeading("3.4 Prerequisites")
	p.WriteValueList(marginX, contentW, d.ContextScope.Prerequisites)

	p.SubHeading("3.5 Data provided by Client")
	p.WriteValue(marginX, contentW, d.ContextScope.DataProvided)

	p.SubHeading("3.7 Dependencies")
	p.WriteValueList(marginX, contentW, d.ContextScope.Dependencies)

	// ---- 4. Success Metrics ----
	p.SectionHeading("4. Success Metrics")
	if len(d.SuccessMetrics) == 0 {
		p.WriteValueList(marginX, contentW, nil)
	} else {
		rows := make([][]string, len(d.SuccessMetrics))
		for i, m := range d.SuccessMetrics {
			rows[i] = []string{m.Metric, m.Definition, m.Target, m.Window, m.ValidatedBy, m.ConsumedBy}
		}
		p.Table([]string{"Metric", "Definition & method", "Target", "Window", "Validated by", "Consumed by"},
			[]float64{0.9, 1.5, 0.6, 0.7, 0.8, 1.1}, rows)
	}

	// ---- 5. Deliverables ----
	p.SectionHeading("5. Deliverables, Milestones & Acceptance Criteria")
	if len(d.Deliverables) == 0 {
		p.WriteValueList(marginX, contentW, nil)
	} else {
		rows := make([][]string, len(d.Deliverables))
		for i, dl := range d.Deliverables {
			pr := dl.Priority
			if pr == "" {
				pr = "[unset]"
			}
			rows[i] = []string{dl.ID, dl.Name, pr, dl.Format, dl.Milestone, dl.TargetDate, dl.AcceptanceCriteria, dl.AcceptanceProcess}
		}
		p.Table([]string{"#", "Deliverable", "Priority", "Format", "Mst.", "Date", "Acceptance criteria", "Acceptance process"},
			[]float64{0.35, 1.3, 0.6, 0.5, 0.4, 0.55, 1.4, 1.2}, rows)
	}
	p.SubHeading("5.1 Acceptance procedure")
	days := d.Acceptance.ReviewWindowBusinessDays
	if days == 0 {
		days = 3
	}
	p.WriteValue(marginX, contentW, fmt.Sprintf(
		"Client reviews against the stated acceptance criteria within a %d business day review window; silence beyond the window constitutes deemed acceptance. Rework rounds included per deliverable: %s.",
		days, firstNonEmpty(d.Acceptance.ReworkRoundsIncluded, "")))
	p.SubHeading("5.2 Progress checkpoint (value gate)")
	chk := strings.TrimSpace(d.Acceptance.CheckpointTiming + " " + d.Acceptance.CheckpointDescription)
	p.WriteValue(marginX, contentW, chk)

	// ---- 6. Approach ----
	p.SectionHeading("6. Approach, Methodology & Technical Description")
	if len(d.Approach.Phases) > 0 {
		rows := [][]string{}
		for _, ph := range d.Approach.Phases {
			if strings.EqualFold(ph.Phase, "hypercare") && d.Approach.ProjectType != "industrialization_rollout" {
				continue
			}
			rows = append(rows, []string{ph.Phase, ph.FeeTreatment, ph.GateDecision})
		}
		p.Table([]string{"Phase", "Fee treatment", "Gate decision"}, []float64{1, 1, 1.6}, rows)
	} else {
		p.WriteValueList(marginX, contentW, nil)
	}
	p.SubHeading("6.3 Technical description & reference architecture")
	p.WriteValue(marginX, contentW, d.Approach.TechnicalDescription)
	p.SubHeading("6.4 Governance & reporting cadence")
	p.WriteValue(marginX, contentW, d.Approach.GovernanceCadence)

	// ---- 7. Roles ----
	p.SectionHeading("7. Roles, Responsibilities & Governance")
	p.SubHeading("7.1 Cegeka team")
	p.WriteValue(marginX, contentW, d.Roles.CegekaTeam)
	p.SubHeading("7.2 Client team & obligations")
	p.WriteValue(marginX, contentW, d.Roles.ClientTeam)
	p.WriteValueList(marginX, contentW, d.Roles.ClientObligations)
	p.SubHeading("7.4 Delay consequence")
	grace := d.Roles.DelayGraceBusinessDays
	if nonEmpty(grace) {
		p.WriteValue(marginX, contentW, fmt.Sprintf(
			"If Client fails to meet an obligation above or a Prerequisite in Section 3.4 within %s business days of the agreed date, Cegeka may extend the timeline day-for-day without fee reduction and/or treat the delay as a Change Control trigger.", grace))
	} else {
		p.WriteValue(marginX, contentW, "")
	}

	// ---- 8. Timeline ----
	p.SectionHeading("8. Timeline")
	if len(d.Timeline) == 0 {
		p.WriteValueList(marginX, contentW, nil)
	} else {
		rows := make([][]string, len(d.Timeline))
		for i, t := range d.Timeline {
			rows[i] = []string{t.Milestone, t.TargetDate, t.Dependency}
		}
		p.Table([]string{"Milestone", "Target date", "Dependency"}, []float64{1.4, 0.7, 1.4}, rows)
	}

	// ---- 9. Change Control ----
	p.SectionHeading("9. Change Control")
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.Paragraph(marginX, contentW,
		"Either party may raise a Change Request when scope, an assumption, a prerequisite, or a dependency changes materially, or a Success Metric definition needs to change. Cegeka provides an impact assessment (scope, fee, timeline) within 5 business days. No work begins, and no scope/fee/timeline is deemed changed, until both parties sign the Change Request. Absent an approved Change Request, the original SOW scope, fee, and acceptance criteria remain binding.")

	// ---- 10. Escalation ----
	// Distinct from Section 8 (delivery Timeline) and Section 12 (Commercial /
	// milestone payments) - this is the issue-escalation path during delivery,
	// not a schedule or a payment structure. Kept structurally separate per
	// explicit client feedback.
	p.SectionHeading("10. Escalation")
	ownerRole := firstNonEmpty(d.Escalation.OwnerRole, "Project/Engagement Manager")
	responseSLA := firstNonEmpty(d.Escalation.ResponseSLABusinessDays, "5")
	slaRef := firstNonEmpty(d.Escalation.SLAReference, "Per MSA")
	p.Table([]string{"Level", "Trigger", "Escalates to", "Response SLA"}, []float64{0.4, 1.2, 1.2, 0.8}, [][]string{
		{"1", "Operational issue", ownerRole, "2 business days"},
		{"2", "Unresolved at L1, or scope/commercial dispute", "Sponsors named in Section 7", responseSLA + " business days"},
		{"3", "Unresolved at L2", "Account Executive / Client Exec Sponsor", slaRef},
	})

	// ---- 11. Commercial Model ----
	p.SectionHeading("11. Engagement Type & Commercial Model")
	models := []string{"fixed_fee", "outcome_based", "hybrid", "time_and_materials"}
	labels := []string{"Fixed Fee", "Outcome-Based", "Hybrid", "Time & Materials"}
	for i, m := range models {
		mark := "[ ]"
		if d.CommercialModel == m {
			mark = "[X]"
		}
		p.SetFont("F1", 9.5)
		p.SetColor(colSlate)
		p.Paragraph(marginX, contentW, mark+" "+labels[i])
	}

	// ---- 12. Commercial Terms ----
	p.SectionHeading("12. Commercial Terms")
	p.SubHeading("12.1 Total Fee")
	p.WriteValue(marginX, contentW, d.Commercial.TotalFee)
	if len(d.Commercial.MilestonePayments) > 0 {
		p.SubHeading("Milestone Payment Structure")
		rows := make([][]string, len(d.Commercial.MilestonePayments))
		for i, m := range d.Commercial.MilestonePayments {
			rows[i] = []string{m.Milestone, m.Deliverable, m.TargetDate, m.Amount, m.Trigger, firstNonEmpty(m.FundingSource, "Client")}
		}
		p.Table([]string{"Milestone", "Deliverable(s)", "Date", "Amount", "Trigger", "Funding source"}, []float64{0.55, 1.2, 0.55, 0.45, 1.2, 0.65}, rows)
	}
	for _, kv := range [][2]string{
		{"12.2 Payment terms", d.Commercial.PaymentTerms},
		{"12.3 Expenses", d.Commercial.ExpensesPolicy},
		{"12.4 Third-party / pass-through costs", d.Commercial.PassThroughPolicy},
	} {
		p.SubHeading(kv[0])
		p.WriteValue(marginX, contentW, kv[1])
	}
	p.SubHeading("12.6 Vendor co-funding / financing programs")
	if nonEmpty(d.Commercial.CofundingProgram) {
		p.WriteValue(marginX, contentW, d.Commercial.CofundingProgram)
	} else {
		p.SetFont("F1", 9.5)
		p.SetColor(colSlate)
		p.Paragraph(marginX, contentW, "Not applicable - no co-funding/financing program is associated with this engagement.")
	}
	p.SubHeading("12.7 Invoicing details")
	p.Table([]string{"Field", "Value"}, []float64{1, 2.5}, [][]string{
		{"Invoice (billing) address", d.Commercial.InvoicingAddress},
		{"Invoice email address", d.Commercial.InvoicingEmail},
		{"Invoicing contact name", d.Commercial.InvoicingContactName},
		{"Invoicing contact phone", d.Commercial.InvoicingContactPhone},
		{"PO number / reference", d.Commercial.PoNumber},
	})

	// ---- 13. Term ----
	p.SectionHeading("13. Term, Termination & Transition")
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.WriteValue(marginX, contentW, "Term: from Effective Date until final deliverable acceptance, or "+firstNonEmpty(d.Term.EndCondition, ""))
	p.WriteValue(marginX, contentW, "Termination for convenience notice period (days): "+firstNonEmpty(d.Term.TerminationNoticeDays, ""))
	p.WriteValue(marginX, contentW, "Transition/exit assistance: "+firstNonEmpty(d.Term.TransitionAssistance, ""))

	// ---- 14. IP ----
	p.SectionHeading("14. Intellectual Property")
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.Paragraph(marginX, contentW,
		"Each party retains ownership of its pre-existing IP. Subject to full payment, Client owns the deliverables created specifically for Client, excluding embedded Cegeka accelerators (perpetual, non-exclusive, royalty-free license granted for use as part of the deliverable). Client retains all ownership of Client Data.")
	p.SubHeading("14.4 Model artifacts")
	p.WriteValue(marginX, contentW, d.IP.ModelArtifactsOwnership)

	// ---- 15. Data Protection ----
	p.SectionHeading("15. Data Protection, Confidentiality & Security")
	p.SubHeading("Processor role")
	p.WriteValue(marginX, contentW, d.DataProtection.ProcessorRole)
	p.SubHeading("Sub-processors / third-party AI services")
	p.WriteValueList(marginX, contentW, d.DataProtection.Subprocessors)
	p.SubHeading("Data retention / deletion")
	p.WriteValue(marginX, contentW, d.DataProtection.RetentionPolicy)

	// ---- 16. Regulatory ----
	p.SectionHeading("16. Regulatory & Responsible AI Considerations")
	p.SubHeading("AI system risk classification")
	p.WriteValue(marginX, contentW, d.Regulatory.AIRiskClassification)
	p.SubHeading("Human oversight")
	p.WriteValue(marginX, contentW, d.Regulatory.HumanOversight)
	p.SubHeading("Bias / fairness testing")
	p.WriteValue(marginX, contentW, d.Regulatory.BiasFairnessTesting)

	// ---- 17. Warranties ----
	p.SectionHeading("17. Warranties, Disclaimers & Liability")
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.Paragraph(marginX, contentW,
		"17.1 Cegeka warrants Services will be performed with reasonable skill and care consistent with good industry practice. 17.2 Client acknowledges that outputs of statistical, machine learning, or generative AI models are probabilistic and may contain errors or omissions; they do not constitute professional, legal, financial, or medical advice. Cegeka does not warrant that any model or AI-based deliverable will be error-free or that a Success Metric will remain stable indefinitely under changing data/production conditions. Client is responsible for appropriate human review of AI-generated outputs before relying on them for business-critical or regulated decisions.")
	p.SubHeading("17.3 Liability cap")
	p.WriteValue(marginX, contentW, d.Liability.Cap)

	// ---- 18. Signatories & Contacts (always blank signature block) ----
	p.SectionHeading("18. Signatories & Contacts")
	p.SubHeading("Signatories")
	p.Table([]string{"", "Client", "Cegeka"}, []float64{0.8, 1, 1}, [][]string{
		{"Name", "", ""},
		{"Role", "", ""},
		{"Company", "", ""},
		{"Email", "", ""},
		{"Signature", "", ""},
		{"Date", "", ""},
	})
	p.SubHeading("Day-to-day & Invoicing Contact Persons")
	p.Table([]string{"", "Client", "Cegeka"}, []float64{0.8, 1, 1}, [][]string{
		{"Contact details", d.Contacts.ClientDayToDay, d.Contacts.CegekaDayToDay},
	})

	// Footer note on final page
	p.Gap(16)
	p.SetFont("F3", 8)
	p.SetColor(colSlate)
	p.Paragraph(marginX, contentW,
		"This document requires Legal review before being sent to a client. The signature section above is intentionally left blank.")

	return p.Bytes()
}
