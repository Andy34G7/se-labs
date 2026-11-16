#!/usr/bin/env python3
"""
Generates clean, purely monochrome (all black, no color fills/accents) Word document (.docx).
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="000000", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = OxmlElement('w:tblBorders')
        for b_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
            border = OxmlElement(f'w:{b_name}')
            border.set(qn('w:val'), val)
            border.set(qn('w:sz'), sz)
            border.set(qn('w:space'), '0')
            border.set(qn('w:color'), color)
            borders.append(border)
        tblPr[0].append(borders)

def build_docx():
    base_dir = '/home/andey/Documents/Sem5/SE/lab3'
    doc_path = os.path.join(base_dir, 'PES2UG24CS061_SE_Lab3.docx')
    img_path = os.path.join(base_dir, 'component_diagram.png')

    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    C_BLACK = RGBColor(0, 0, 0)
    C_HEADER_FILL = "FFFFFF"

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(10.5)
    style_normal.font.color.rgb = C_BLACK
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)

    # Document Header
    p_meta = doc.add_paragraph()
    r_uni = p_meta.add_run("PES UNIVERSITY | DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\n")
    r_uni.bold = True
    r_uni.font.size = Pt(9)
    r_uni.font.color.rgb = C_BLACK
    r_course = p_meta.add_run("UE24CS341A – SOFTWARE ENGINEERING | LAB 3 REPORT")
    r_course.font.size = Pt(9)
    r_course.font.color.rgb = C_BLACK
    p_meta.paragraph_format.space_after = Pt(8)

    # Main Title
    p_title = doc.add_paragraph()
    r_title = p_title.add_run("Lab 3: Component Modelling & Architectural Pattern Selection")
    r_title.bold = True
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = C_BLACK
    p_title.paragraph_format.space_after = Pt(4)

    p_info = doc.add_paragraph()
    p_info.add_run("Student Name: ").bold = True
    p_info.add_run("Andey Hemanth          ")
    p_info.add_run("SRN: ").bold = True
    p_info.add_run("PES2UG24CS061\n")
    p_info.add_run("Assigned Scenario: ").bold = True
    p_info.add_run("Problem Statement 57: Pet Adoption and Shelter Management System")
    p_info.paragraph_format.space_after = Pt(10)

    # 1. ARCHITECTURE SELECTION
    h1 = doc.add_heading(level=1)
    r1 = h1.add_run("1. Architecture Selection & Written Justification")
    r1.font.color.rgb = C_BLACK

    p_sel = doc.add_paragraph()
    r_sel = p_sel.add_run('Architecture Selection: "I chose Layered (3-Tier) Architecture for the Pet Adoption and Shelter Management System."')
    r_sel.bold = True
    r_sel.font.size = Pt(11)
    r_sel.font.color.rgb = C_BLACK
    p_sel.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.add_run("• Architectural Choice: ").bold = True
    p.add_run("Layered (3-Tier) Architecture, partitioned into Presentation Layer (Client Tier), Business Logic Layer (Application Tier), and Data Access & Persistence Layer (Database Tier).")

    p = doc.add_paragraph()
    p.add_run("• Two Scenario-Related Reasons:").bold = True
    
    p_r1 = doc.add_paragraph(style='List Bullet')
    p_r1.add_run("Separation of Concerns & ACID Consistency: ").bold = True
    p_r1.add_run("The system distinctly separates public adopter interactions (browsing pet listings, submitting adoption questionnaires) from privileged shelter operations (vaccination logging, quarantine tracking, foster scheduling). The Layered pattern enforces strict transactional boundaries within the application tier, ensuring that an animal cannot be marked as Ready for Adoption or placed in a foster home while medically quarantined, maintaining strong relational consistency.")

    p_r2 = doc.add_paragraph(style='List Bullet')
    p_r2.add_run("Operational Simplicity & Maintainability for Shelter Scale: ").bold = True
    p_r2.add_run("Animal rescue shelters require reliable, maintainable software with low operational overhead. A microservices architecture introduces distributed failure modes, complex sagas, and substantial infrastructure costs. The Layered pattern provides modular encapsulation with clean ball-and-socket interfaces while keeping deployment and monitoring straightforward on unified infrastructure.")

    p = doc.add_paragraph()
    p.add_run("• Security Advantage (NFR-002): ").bold = True
    p.add_run("Centralized Data Access Layer strictly enforces AES-256 column-level encryption at rest for all stored applicant questionnaires (containing sensitive personal information and housing details) and medical intake logs. Furthermore, Role-Based Access Control (RBAC) at the business tier prevents unauthorized public access to confidential medical and screening data.")

    p = doc.add_paragraph()
    p.add_run("• Performance Benefit (NFR-001): ").bold = True
    p.add_run("An in-memory caching mechanism (e.g., Redis/local cache) integrated into the Pet Catalog & Search Component serves public search queries in under 200 ms during peak loads of 500 concurrent users, satisfying NFR-001 without introducing distributed network latency.")
    p.paragraph_format.space_after = Pt(10)

    # 2. COMPARATIVE EVALUATION
    h2 = doc.add_heading(level=1)
    r2 = h2.add_run("2. Architectural Style Comparative Evaluation")
    r2.font.color.rgb = C_BLACK

    table_comp = doc.add_table(rows=1, cols=4)
    table_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_comp)

    headers = ["Evaluation Dimension", "Layered (3-Tier)", "Microservices", "Client-Server"]
    col_widths = [Inches(1.7), Inches(1.8), Inches(1.8), Inches(1.6)]

    hdr_cells = table_comp.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], C_HEADER_FILL)
        set_cell_margins(hdr_cells[i], 100, 100, 100, 100)
        hdr_cells[i].paragraphs[0].runs[0].bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK

    comp_data = [
        ("Separation of Concerns", "High: Strict horizontal layering (Presentation, Business, Data).", "High: Domain-driven service boundaries.", "Low to Moderate: Business logic easily bleeds into client or DB."),
        ("Data Consistency (ACID)", "High: Centralized ACID transaction guarantees across health/adoption.", "Low/Moderate: Requires distributed sagas / eventual consistency.", "High: Centralized relational ACID transactions."),
        ("Operational Complexity", "Low: Unified CI/CD deployment and centralized logging.", "Very High: Service meshes, distributed tracing, Kubernetes.", "Very Low: Simple two-tier architecture."),
        ("Security (NFR-002)", "High: Centralized AES-256 encryption at rest in Data Layer.", "Moderate: Requires securing all inter-service REST/gRPC endpoints.", "Moderate: Larger attack surface with direct client exposure."),
        ("Performance (NFR-001)", "High: Integrated in-memory caching yields < 200ms catalog search.", "Moderate: Network serialization hops increase latency.", "Moderate: Monolithic query contention under high concurrency.")
    ]

    for row in comp_data:
        row_cells = table_comp.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = val
            set_cell_margins(row_cells[i], 60, 60, 100, 100)
            row_cells[i].paragraphs[0].runs[0].font.size = Pt(8.5)
            row_cells[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK
            if i == 0:
                row_cells[i].paragraphs[0].runs[0].bold = True

    for row in table_comp.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 3. UML COMPONENT DIAGRAM
    h3 = doc.add_heading(level=1)
    r3 = h3.add_run("3. UML Component Diagram")
    r3.font.color.rgb = C_BLACK

    p_diag_intro = doc.add_paragraph("The UML Component Diagram below illustrates the 7 core components, their architectural layering, provided/required interfaces, and data persistence flows:")
    p_diag_intro.paragraph_format.space_after = Pt(6)

    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.6))
        
        p_caption = doc.add_paragraph("Figure 3.1: UML Component Diagram for Pet Adoption and Shelter Management System")
        p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption.runs[0].font.size = Pt(8.5)
        p_caption.runs[0].font.italic = True
        p_caption.runs[0].font.color.rgb = C_BLACK
        p_caption.paragraph_format.space_after = Pt(10)

    # 4. COMPONENT SPECIFICATIONS
    h4 = doc.add_heading(level=1)
    r4 = h4.add_run("4. Component Specifications & Responsibilities")
    r4.font.color.rgb = C_BLACK

    table_comp_spec = doc.add_table(rows=1, cols=4)
    table_comp_spec.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_comp_spec)

    spec_headers = ["Component Name", "Layer / Stereotype", "Provided / Required Interfaces", "Key Responsibilities"]
    spec_col_widths = [Inches(1.6), Inches(1.2), Inches(1.8), Inches(2.3)]

    hdr_cells2 = table_comp_spec.rows[0].cells
    for i, title in enumerate(spec_headers):
        hdr_cells2[i].text = title
        set_cell_background(hdr_cells2[i], C_HEADER_FILL)
        set_cell_margins(hdr_cells2[i], 100, 100, 100, 100)
        hdr_cells2[i].paragraphs[0].runs[0].bold = True
        hdr_cells2[i].paragraphs[0].runs[0].font.size = Pt(9)
        hdr_cells2[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK

    specs_data = [
        ("Public Web Portal", "Presentation\n<<component>>", "Provided: None\nRequired: IPetSearchService, IQuestionnaireService", "Public applicant UI for browsing pets and submitting adoption questionnaires."),
        ("Shelter Staff & Foster Portal", "Presentation\n<<component>>", "Provided: None\nRequired: IMedicalRecordService, IFosterPlacementService", "Administrative dashboard for medical intakes, quarantine hold, and foster scheduling."),
        ("Pet Catalog & Search", "Business\n<<component>>", "Provided: IPetSearchService\nRequired: IShelterDataAccess", "Maintains in-memory cached listings; fulfills NFR-001 search response (< 200 ms)."),
        ("Adoption & Questionnaire Manager", "Business\n<<component>>", "Provided: IQuestionnaireService\nRequired: IScreeningEngine, IHealthClearance, INotificationDispatch", "Handles questionnaire submission, tracking IDs, and state transitions (FR-002, SCRUM-10)."),
        ("Automated Screening Engine", "Business\n<<component>>", "Provided: IScreeningEngine\nRequired: IShelterDataAccess", "Evaluates questionnaire responses against rules within 5s; flags disqualifications (FR-003, SCRUM-11)."),
        ("Medical Intake & Vaccination", "Business\n<<component>>", "Provided: IMedicalRecordService, IHealthClearance\nRequired: IShelterDataAccess", "Logs vaccines, tracks medical history, enforces quarantine, clears adoption readiness (FR-001, SCRUM-8)."),
        ("Foster Placement & Scheduler", "Business\n<<component>>", "Provided: IFosterPlacementService\nRequired: INotificationDispatch, IShelterDataAccess", "Schedules foster timelines, prevents overlapping bookings, tracks milestones (FR-004, SCRUM-12)."),
        ("Notification Dispatcher", "Business\n<<component>>", "Provided: INotificationDispatch\nRequired: ISMTPClient", "Dispatches confirmation emails and 48-hour foster milestone reminder alerts (FR-005, SCRUM-13)."),
        ("Shelter Database & Data Access", "Data\n<<component>>", "Provided: IShelterDataAccess\nRequired: None (Direct ORM)", "Centralized ORM persistence layer enforcing AES-256 encryption at rest for PII/records (NFR-002).")
    ]

    for row in specs_data:
        row_cells = table_comp_spec.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = val
            set_cell_margins(row_cells[i], 60, 60, 100, 100)
            row_cells[i].paragraphs[0].runs[0].font.size = Pt(8)
            row_cells[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK
            if i == 0:
                row_cells[i].paragraphs[0].runs[0].bold = True

    for row in table_comp_spec.rows:
        for idx, width in enumerate(spec_col_widths):
            row.cells[idx].width = width

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 5. INTERFACE SPECIFICATIONS
    h5 = doc.add_heading(level=1)
    r5 = h5.add_run("5. Interface Specifications & Protocols")
    r5.font.color.rgb = C_BLACK

    table_if_spec = doc.add_table(rows=1, cols=4)
    table_if_spec.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_if_spec)

    if_headers = ["Interface Name", "Provider (Ball) / Consumer (Socket)", "Protocol / Mechanism", "Key Operations & Signatures"]
    if_col_widths = [Inches(1.6), Inches(1.8), Inches(1.5), Inches(2.0)]

    hdr_cells3 = table_if_spec.rows[0].cells
    for i, title in enumerate(if_headers):
        hdr_cells3[i].text = title
        set_cell_background(hdr_cells3[i], C_HEADER_FILL)
        set_cell_margins(hdr_cells3[i], 100, 100, 100, 100)
        hdr_cells3[i].paragraphs[0].runs[0].bold = True
        hdr_cells3[i].paragraphs[0].runs[0].font.size = Pt(9)
        hdr_cells3[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK

    if_data = [
        ("IPetSearchService", "Provider: Pet Catalog\nConsumer: Public Web Portal", "REST / JSON over HTTPS", "searchPets(filterCriteria)\ngetPetProfile(petId)\ngetAvailableBreeds()"),
        ("IQuestionnaireService", "Provider: Adoption Manager\nConsumer: Public Web Portal", "HTTPS POST / REST", "submitQuestionnaire(data)\ngetApplicationStatus(appId)\nupdateApplicationStatus(appId, status)"),
        ("IScreeningEngine", "Provider: Screening Engine\nConsumer: Adoption Manager", "Synchronous RPC / Call", "evaluateQuestionnaire(data)\nvalidateHousingRules(housing, breed)\nflagDisqualification(appId, reason)"),
        ("IMedicalRecordService", "Provider: Medical Intake\nConsumer: Staff Portal", "REST (RBAC Auth)", "logVaccination(animalId, vaccine)\ngetMedicalHistory(animalId)\nupdateAdoptionReadiness(animalId, flag)"),
        ("IHealthClearance", "Provider: Medical Intake\nConsumer: Adoption Manager", "Synchronous Call", "verifyAdoptionReadiness(animalId)\ngetQuarantineStatus(animalId)"),
        ("IFosterPlacementService", "Provider: Foster Placement\nConsumer: Staff Portal", "REST / JSON over HTTPS", "scheduleFosterTimeline(placement)\nvalidateNoOverlap(animalId, dates)\ngetUpcomingMilestones(caretakerId)"),
        ("INotificationDispatch", "Provider: Notification Dispatcher\nConsumer: Foster / Adoption", "Async Queue / Event", "enqueueMilestoneReminder(alert)\nsendApplicationConfirmation(email, appId)"),
        ("IShelterDataAccess", "Provider: Shelter DB Component\nConsumer: Business Components", "JDBC / JPA with AES-256", "saveEncryptedEntity(entity)\nfindById(id, entityClass)\nexecuteOptimizedQuery(query)")
    ]

    for row in if_data:
        row_cells = table_if_spec.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = val
            set_cell_margins(row_cells[i], 60, 60, 100, 100)
            row_cells[i].paragraphs[0].runs[0].font.size = Pt(8)
            row_cells[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK
            if i == 0:
                row_cells[i].paragraphs[0].runs[0].bold = True

    for row in table_if_spec.rows:
        for idx, width in enumerate(if_col_widths):
            row.cells[idx].width = width

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 6. TRACEABILITY MATRIX
    h6 = doc.add_heading(level=1)
    r6 = h6.add_run("6. Requirements & Backlog Traceability Matrix")
    r6.font.color.rgb = C_BLACK

    table_trace = doc.add_table(rows=1, cols=5)
    table_trace.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_trace)

    trace_headers = ["Req ID", "Jira Story", "Implementing Component", "Interface", "Verification"]
    trace_col_widths = [Inches(0.9), Inches(1.0), Inches(1.8), Inches(1.6), Inches(1.6)]

    hdr_cells4 = table_trace.rows[0].cells
    for i, title in enumerate(trace_headers):
        hdr_cells4[i].text = title
        set_cell_background(hdr_cells4[i], C_HEADER_FILL)
        set_cell_margins(hdr_cells4[i], 100, 100, 100, 100)
        hdr_cells4[i].paragraphs[0].runs[0].bold = True
        hdr_cells4[i].paragraphs[0].runs[0].font.size = Pt(9)
        hdr_cells4[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK

    trace_data = [
        ("FR-001", "SCRUM-8, 9", "Medical Intake Component", "IMedicalRecordService, IHealthClearance", "Intake logs & quarantine checks prevent adopting sick animals."),
        ("FR-002", "SCRUM-10", "Adoption Manager Component", "IQuestionnaireService", "Questionnaire submission with unique tracking ID."),
        ("FR-003", "SCRUM-11", "Automated Screening Engine", "IScreeningEngine", "Rule evaluation flags disqualifications in < 5 seconds."),
        ("FR-004", "SCRUM-12", "Foster Placement Component", "IFosterPlacementService", "Blocks overlapping foster timelines for same animal."),
        ("FR-005", "SCRUM-13", "Notification Dispatcher", "INotificationDispatch, ISMTPClient", "Automated emails sent 48h prior to milestones."),
        ("NFR-001", "SCRUM-10", "Pet Catalog & Search", "IPetSearchService", "In-memory cache delivers search in < 200 ms @ 500 users."),
        ("NFR-002", "SCRUM-8, 10", "Shelter Database Component", "IShelterDataAccess", "AES-256 column-level encryption at rest for PII & medical logs.")
    ]

    for row in trace_data:
        row_cells = table_trace.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = val
            set_cell_margins(row_cells[i], 60, 60, 100, 100)
            row_cells[i].paragraphs[0].runs[0].font.size = Pt(8)
            row_cells[i].paragraphs[0].runs[0].font.color.rgb = C_BLACK
            if i == 0:
                row_cells[i].paragraphs[0].runs[0].bold = True

    for row in table_trace.rows:
        for idx, width in enumerate(trace_col_widths):
            row.cells[idx].width = width

    doc.save(doc_path)
    print(f"Generated all-black DOCX report: {doc_path}")

if __name__ == '__main__':
    build_docx()
