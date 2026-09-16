package main

// SOWData mirrors schema/sow-data.schema.json. Every field is optional;
// zero values render as placeholders in the PDF.
type SOWData struct {
	Meta struct {
		Ref     string `json:"ref"`
		Version string `json:"version"`
		Date    string `json:"date"`
	} `json:"meta"`

	DocControl struct {
		ClientLegalName string `json:"client_legal_name"`
		CegekaEntity    string `json:"cegeka_entity"`
		MsaDate         string `json:"msa_date"`
		EffectiveDate   string `json:"effective_date"`
		SowOwnerCegeka  string `json:"sow_owner_cegeka"`
		SowOwnerClient  string `json:"sow_owner_client"`
	} `json:"doc_control"`

	ExecSummary struct {
		Narrative          string `json:"narrative"`
		WhatWeDeliver      string `json:"what_we_deliver"`
		HowSuccessMeasured string `json:"how_success_measured"`
		CommercialHeadline string `json:"commercial_headline"`
	} `json:"exec_summary"`

	ContextScope struct {
		BusinessContext string `json:"business_context"`
		Objectives      []struct {
			Text string `json:"text"`
			Type string `json:"type"`
		} `json:"objectives"`
		Workstreams []struct {
			Workstream string `json:"workstream"`
			InScope    string `json:"in_scope"`
			OutOfScope string `json:"out_of_scope"`
		} `json:"workstreams"`
		Assumptions               []string `json:"assumptions"`
		Prerequisites             []string `json:"prerequisites"`
		DataProvided              string   `json:"data_provided"`
		ReferenceCaseStudyAllowed bool     `json:"reference_case_study_allowed"`
		Dependencies              []string `json:"dependencies"`
	} `json:"context_scope"`

	SuccessMetrics []struct {
		Metric      string `json:"metric"`
		Definition  string `json:"definition"`
		Target      string `json:"target"`
		Window      string `json:"window"`
		ValidatedBy string `json:"validated_by"`
	} `json:"success_metrics"`

	Deliverables []struct {
		ID                 string `json:"id"`
		Name               string `json:"name"`
		Priority           string `json:"priority"`
		Format             string `json:"format"`
		Milestone          string `json:"milestone"`
		TargetDate         string `json:"target_date"`
		AcceptanceCriteria string `json:"acceptance_criteria"`
		AcceptanceProcess  string `json:"acceptance_process"`
	} `json:"deliverables"`

	Acceptance struct {
		ReviewWindowBusinessDays int    `json:"review_window_business_days"`
		ReworkRoundsIncluded     string `json:"rework_rounds_included"`
		CheckpointTiming         string `json:"checkpoint_timing"`
		CheckpointDescription    string `json:"checkpoint_description"`
	} `json:"acceptance"`

	Approach struct {
		ProjectType string `json:"project_type"`
		Phases      []struct {
			Phase        string `json:"phase"`
			FeeTreatment string `json:"fee_treatment"`
			GateDecision string `json:"gate_decision"`
		} `json:"phases"`
		TechnicalDescription string `json:"technical_description"`
		GovernanceCadence    string `json:"governance_cadence"`
	} `json:"approach"`

	Roles struct {
		CegekaTeam             string   `json:"cegeka_team"`
		ClientTeam             string   `json:"client_team"`
		ClientObligations      []string `json:"client_obligations"`
		DelayGraceBusinessDays string   `json:"delay_grace_business_days"`
	} `json:"roles"`

	Timeline []struct {
		Milestone  string `json:"milestone"`
		TargetDate string `json:"target_date"`
		Dependency string `json:"dependency"`
	} `json:"timeline"`

	CommercialModel string `json:"commercial_model"`

	Commercial struct {
		TotalFee          string `json:"total_fee"`
		MilestonePayments []struct {
			Milestone   string `json:"milestone"`
			Deliverable string `json:"deliverable"`
			TargetDate  string `json:"target_date"`
			Amount      string `json:"amount"`
			Trigger     string `json:"trigger"`
		} `json:"milestone_payments"`
		PaymentTerms      string `json:"payment_terms"`
		ExpensesPolicy    string `json:"expenses_policy"`
		PassThroughPolicy string `json:"pass_through_policy"`
		CofundingProgram  string `json:"cofunding_program"`
		InvoicingAddress  string `json:"invoicing_address"`
		InvoicingEmail    string `json:"invoicing_email"`
		PoNumber          string `json:"po_number"`
	} `json:"commercial"`

	Term struct {
		EndCondition          string `json:"end_condition"`
		TerminationNoticeDays string `json:"termination_notice_days"`
		TransitionAssistance  string `json:"transition_assistance"`
	} `json:"term"`

	IP struct {
		ModelArtifactsOwnership string `json:"model_artifacts_ownership"`
	} `json:"ip"`

	DataProtection struct {
		ProcessorRole   string   `json:"processor_role"`
		Subprocessors   []string `json:"subprocessors"`
		RetentionPolicy string   `json:"retention_policy"`
	} `json:"data_protection"`

	Regulatory struct {
		AIRiskClassification string `json:"ai_risk_classification"`
		HumanOversight       string `json:"human_oversight"`
		BiasFairnessTesting  string `json:"bias_fairness_testing"`
	} `json:"regulatory"`

	Liability struct {
		Cap string `json:"cap"`
	} `json:"liability"`

	Contacts struct {
		ClientDayToDay string `json:"client_day_to_day"`
		CegekaDayToDay string `json:"cegeka_day_to_day"`
	} `json:"contacts"`

	OpenItems []struct {
		Section          string `json:"section"`
		Question         string `json:"question"`
		WhyItMatters     string `json:"why_it_matters"`
		RiskIfUnresolved string `json:"risk_if_unresolved"`
		SuggestedOwner   string `json:"suggested_owner"`
	} `json:"open_items"`
}
