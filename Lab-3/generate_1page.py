#!/usr/bin/env python3
"""
Generates a dedicated, strictly 1-page Architecture Selection & Written Justification
document in pure black and white (PDF and DOCX) using first-person singular phrasing ("I chose").
"""

import os
import weasyprint
import docx
from docx.shared import Inches, Pt, RGBColor

def build_1page_pdf():
    base_dir = '/home/andey/Documents/Sem5/SE/lab3'
    pdf_out = os.path.join(base_dir, 'PES2UG24CS061_Lab3_Justification_1Page.pdf')

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 3: Architecture Selection & Written Justification</title>
<style>
    @page {
        size: A4;
        margin: 15mm 15mm 15mm 15mm;
    }
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
        font-size: 10pt;
        line-height: 1.45;
        color: #000000;
        background-color: #ffffff;
    }
    .header-box {
        border-bottom: 1.5px solid #000000;
        padding-bottom: 8px;
        margin-bottom: 12px;
    }
    h1 {
        font-size: 16pt;
        color: #000000;
        font-weight: bold;
        margin: 0 0 4px 0;
    }
    .meta-grid {
        font-size: 9pt;
        color: #000000;
    }
    .selection-box {
        border: 1px solid #000000;
        padding: 8px 12px;
        margin: 12px 0;
        font-weight: bold;
        font-size: 10.5pt;
        color: #000000;
        background-color: #ffffff;
    }
    h2 {
        font-size: 11pt;
        color: #000000;
        font-weight: bold;
        margin: 12px 0 4px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    ul {
        margin: 4px 0 8px 0;
        padding-left: 18px;
    }
    li {
        margin-bottom: 6px;
        color: #000000;
    }
    p {
        margin: 4px 0 8px 0;
        color: #000000;
    }
    .strong-title {
        color: #000000;
        font-weight: bold;
    }
</style>
</head>
<body>

<div class="header-box">
    <h1>Lab 3: Architecture Selection &amp; Written Justification</h1>
    <div class="meta-grid">
        <strong>Student Name:</strong> Andey Hemanth &nbsp;|&nbsp; 
        <strong>SRN:</strong> PES2UG24CS061 &nbsp;|&nbsp; 
        <strong>Assigned Scenario:</strong> Problem Statement 57: Pet Adoption and Shelter Management System
    </div>
</div>

<div class="selection-box">
    Architecture Selection: "I chose Layered (3-Tier) Architecture for the Pet Adoption and Shelter Management System."
</div>

<h2>1. Architectural Choice</h2>
<p>
    The system is structured using a <strong>Layered (3-Tier) Architecture</strong> comprising:
    (1) <em>Presentation Layer (Client Tier)</em> for applicant and staff web portals;
    (2) <em>Business Logic Layer (Application Tier)</em> encapsulating domain modules (Pet Catalog, Adoption Manager, Automated Screening, Medical Intake, Foster Scheduler, and Notification Dispatcher); and
    (3) <em>Data Access &amp; Persistence Layer (Database Tier)</em> managing centralized relational persistence and encryption.
</p>

<h2>2. Scenario-Related Reasons</h2>
<ul>
    <li>
        <span class="strong-title">Strict Separation of Concerns &amp; ACID Consistency:</span>
        The shelter domain requires a rigid operational divide between public adopter interactions (catalog search, questionnaire submission) and privileged administrative operations (medical intake logging, quarantine tracking, and foster timeline management). An animal undergoing medical quarantine or an active foster placement cannot be marked as <em>Ready for Adoption</em>. The Layered pattern enforces strict transactional boundaries within the application tier, guaranteeing relational ACID consistency across medical clearance and adoption workflows without the failure modes of distributed microservices.
    </li>
    <li>
        <span class="strong-title">Operational Simplicity &amp; Low Maintenance Overhead for Shelter Scale:</span>
        Animal shelter operations require dependable software with manageable infrastructure costs. A microservices architecture introduces excessive complexity (service meshes, distributed tracing, network latency, and distributed sagas) disproportionate to a shelter's organizational scale. The Layered architecture provides clean modularity via explicit ball-and-socket component interfaces while keeping deployment, monitoring, and database management unified and cost-effective.
    </li>
</ul>

<h2>3. Security Advantage (NFR-002)</h2>
<p>
    <strong>Centralized AES-256 Encryption at Rest:</strong> Adoption questionnaires contain sensitive applicant Personally Identifiable Information (PII) such as home addresses, family details, and housing histories, while medical logs contain confidential veterinary records. In this Layered Architecture, all data access is routed through the centralized <em>Shelter Database &amp; Data Access Component</em>, which transparently enforces <strong>AES-256 column-level encryption at rest</strong> prior to disk storage (satisfying NFR-002). Furthermore, Role-Based Access Control (RBAC) at the business tier prevents unauthorized public access to quarantine and screening data.
</p>

<h2>4. Performance Benefit (NFR-001)</h2>
<p>
    <strong>Sub-200ms Catalog Search via Layer-Integrated In-Memory Caching:</strong> To satisfy Non-Functional Requirement <strong>NFR-001</strong> (returning catalog search results in &lt; 200 ms under 500 concurrent users), the <em>Pet Catalog &amp; Search Component</em> integrates an in-memory caching engine (e.g., Redis). Public read-heavy catalog queries are resolved directly from cache memory in under 20 ms without database disk I/O, while write operations (medical clearances, new intakes) invalidate cache keys atomically through internal service events.
</p>

</body>
</html>
"""
    html_obj = weasyprint.HTML(string=html_content, base_url=base_dir)
    html_obj.write_pdf(pdf_out)
    print(f"Generated all-black 1-page PDF: {pdf_out}")

def build_1page_docx():
    base_dir = '/home/andey/Documents/Sem5/SE/lab3'
    doc_path = os.path.join(base_dir, 'PES2UG24CS061_Lab3_Justification_1Page.docx')
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    C_BLACK = RGBColor(0, 0, 0)

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(10)
    style_normal.font.color.rgb = C_BLACK
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)

    p_title = doc.add_paragraph()
    r_title = p_title.add_run("Lab 3: Architecture Selection & Written Justification")
    r_title.bold = True
    r_title.font.size = Pt(15)
    r_title.font.color.rgb = C_BLACK
    p_title.paragraph_format.space_after = Pt(2)

    p_info = doc.add_paragraph()
    p_info.add_run("Student Name: ").bold = True
    p_info.add_run("Andey Hemanth   |   ")
    p_info.add_run("SRN: ").bold = True
    p_info.add_run("PES2UG24CS061   |   ")
    p_info.add_run("Scenario: ").bold = True
    p_info.add_run("Problem Statement 57 (Pet Adoption & Shelter Management)")
    p_info.paragraph_format.space_after = Pt(6)

    # Selection Callout
    p_sel = doc.add_paragraph()
    r_sel = p_sel.add_run('Architecture Selection: "I chose Layered (3-Tier) Architecture for the Pet Adoption and Shelter Management System."')
    r_sel.bold = True
    r_sel.font.size = Pt(10.5)
    r_sel.font.color.rgb = C_BLACK
    p_sel.paragraph_format.space_after = Pt(6)

    # 1. Choice
    p = doc.add_paragraph()
    p.add_run("1. Architectural Choice: ").bold = True
    p.add_run("The system adopts a Layered (3-Tier) Architecture, organized into Presentation Layer (Client Tier), Business Logic Layer (Application Tier), and Data Access & Persistence Layer (Database Tier).")

    # 2. Reasons
    p = doc.add_paragraph()
    p.add_run("2. Two Scenario-Related Reasons:").bold = True

    p_r1 = doc.add_paragraph(style='List Bullet')
    p_r1.add_run("Strict Separation of Concerns & ACID Consistency: ").bold = True
    p_r1.add_run("The shelter requires an operational divide between public adopter interactions (catalog search, questionnaire submission) and privileged shelter operations (vaccination logging, quarantine tracking, foster scheduling). The Layered pattern enforces strict transactional boundaries within the application tier, ensuring that an animal cannot be marked as Ready for Adoption or assigned to foster care while medically quarantined.")

    p_r2 = doc.add_paragraph(style='List Bullet')
    p_r2.add_run("Operational Simplicity & Maintainability for Shelter Scale: ").bold = True
    p_r2.add_run("Animal rescue shelters require reliable software with low infrastructure overhead. A microservices pattern introduces distributed failure modes, complex saga transactions, and heavy operational costs. The Layered pattern provides modular encapsulation via explicit component interfaces while keeping deployment and monitoring centralized.")

    # 3. Security
    p = doc.add_paragraph()
    p.add_run("3. Security Advantage (NFR-002): ").bold = True
    p.add_run("Centralized Data Access Layer strictly enforces AES-256 column-level encryption at rest for all stored applicant questionnaires (containing sensitive PII and housing data) and medical logs. Additionally, Role-Based Access Control (RBAC) at the business tier prevents unauthorized public access to confidential quarantine records.")

    # 4. Performance
    p = doc.add_paragraph()
    p.add_run("4. Performance Benefit (NFR-001): ").bold = True
    p.add_run("An in-memory caching engine integrated into the Pet Catalog & Search Component serves public search queries in under 200 ms during peak loads of 500 concurrent users, satisfying NFR-001 without introducing distributed network latency.")

    doc.save(doc_path)
    print(f"Generated all-black 1-page DOCX: {doc_path}")

if __name__ == '__main__':
    build_1page_pdf()
    build_1page_docx()
