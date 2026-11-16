#!/usr/bin/env python3
"""
Generates clean, purely monochrome (100% black & white) UML 2.5 Component Diagram
for Lab 3: Problem Statement 57 (Pet Adoption and Shelter Management System).
"""

import os

def create_component_diagram():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Component-Diagram-Lab3" id="lab3-comp-diag">
    <mxGraphModel dx="1200" dy="950" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="920" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ==================== 1. LAYER BOUNDARIES (Black Dashed Outlines) ==================== -->
        <mxCell id="box_pres" value="&lt;b&gt;Presentation Layer (Client Tier)&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=4;verticalAlign=top;align=left;spacingLeft=15;spacingTop=10;fontStyle=1;fontSize=12;dashed=1;strokeWidth=1.5;fillColor=none;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1120" height="130" as="geometry" />
        </mxCell>

        <mxCell id="box_biz" value="&lt;b&gt;Business Logic Layer (Application Tier - Layered Architecture Pattern)&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=4;verticalAlign=top;align=left;spacingLeft=15;spacingTop=10;fontStyle=1;fontSize=12;dashed=1;strokeWidth=1.5;fillColor=none;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="40" y="200" width="1120" height="430" as="geometry" />
        </mxCell>

        <mxCell id="box_data" value="&lt;b&gt;Data Access &amp;amp; Persistence Layer (Database Tier)&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=4;verticalAlign=top;align=left;spacingLeft=15;spacingTop=10;fontStyle=1;fontSize=12;dashed=1;strokeWidth=1.5;fillColor=none;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="40" y="660" width="1120" height="140" as="geometry" />
        </mxCell>

        <!-- ==================== 2. PRESENTATION COMPONENTS ==================== -->
        <mxCell id="c_ui_applicant" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Public Web Portal&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Adoption Applicant UI]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="70" y="80" width="240" height="65" as="geometry" />
        </mxCell>

        <mxCell id="c_ui_staff" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Shelter Staff &amp;amp; Foster Portal&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Shelter Operations &amp;amp; Intake UI]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="610" y="80" width="280" height="65" as="geometry" />
        </mxCell>

        <mxCell id="c_ext_email" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;External Mail Gateway&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[SMTP / Cloud Email Service]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="930" y="80" width="200" height="65" as="geometry" />
        </mxCell>

        <!-- ==================== 3. BUSINESS LOGIC COMPONENTS ==================== -->
        <!-- Left Column: Pet Catalog -->
        <mxCell id="c_catalog" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Pet Catalog &amp;amp; Search&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[In-Memory Cache &amp;amp; Filter]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="70" y="250" width="240" height="75" as="geometry" />
        </mxCell>

        <!-- Middle Column: Adoption Manager & Screening -->
        <mxCell id="c_adoption" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Adoption &amp;amp; Questionnaire Manager&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Application Workflow &amp;amp; State]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=10.5;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="340" y="250" width="260" height="75" as="geometry" />
        </mxCell>

        <mxCell id="c_screening" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Automated Screening Engine&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Rules Engine &amp;amp; Policy Checker]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="340" y="440" width="260" height="75" as="geometry" />
        </mxCell>

        <!-- Right Column: Medical Intake & Foster Scheduler -->
        <mxCell id="c_medical" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Medical Intake &amp;amp; Vaccination&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Health History &amp;amp; Quarantine]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=10.5;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="630" y="250" width="260" height="75" as="geometry" />
        </mxCell>

        <mxCell id="c_foster" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Foster Placement &amp;amp; Scheduler&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Placement Timeline &amp;amp; Validation]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="630" y="440" width="260" height="75" as="geometry" />
        </mxCell>

        <!-- Far Right: Notification Dispatcher -->
        <mxCell id="c_notification" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Notification Dispatcher&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Milestone Alert Engine]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="930" y="340" width="190" height="75" as="geometry" />
        </mxCell>

        <!-- ==================== 4. DATA ACCESS LAYER COMPONENT ==================== -->
        <mxCell id="c_db_access" value="&amp;laquo;component&amp;raquo;&lt;br&gt;&lt;b&gt;Shelter Database &amp;amp; Data Access Component&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px;&quot;&gt;[Central Repository | ORM Mapping | AES-256 Encrypted Storage Engine]&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=6;strokeWidth=1.5;fontSize=11;align=center;verticalAlign=middle;fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="250" y="695" width="670" height="75" as="geometry" />
        </mxCell>

        <!-- ==================== 5. CONNECTORS & INTERFACES ==================== -->
        <!-- UI -> Catalog (IPetSearchService) -->
        <mxCell id="e1" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IPetSearchService&lt;/b&gt;&lt;br&gt;(REST / JSON, &amp;lt; 200ms)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.35;exitY=1;entryX=0.35;entryY=0;" edge="1" parent="1" source="c_ui_applicant" target="c_catalog">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- UI -> Adoption (IQuestionnaireService) -->
        <mxCell id="e2" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IQuestionnaireService&lt;/b&gt;&lt;br&gt;(HTTPS POST / REST)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.8;exitY=1;entryX=0.2;entryY=0;" edge="1" parent="1" source="c_ui_applicant" target="c_adoption">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Staff -> Medical (IMedicalRecordService) -->
        <mxCell id="e3" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IMedicalRecordService&lt;/b&gt;&lt;br&gt;(REST / RBAC Auth)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.25;exitY=1;entryX=0.25;entryY=0;" edge="1" parent="1" source="c_ui_staff" target="c_medical">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Staff -> Foster (IFosterPlacementService) -->
        <mxCell id="e4" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IFosterPlacementService&lt;/b&gt;&lt;br&gt;(REST / Timelines)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.8;exitY=1;entryX=0.8;entryY=0;" edge="1" parent="1" source="c_ui_staff" target="c_foster">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="834" y="180" />
              <mxPoint x="905" y="180" />
              <mxPoint x="905" y="410" />
              <mxPoint x="838" y="410" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Adoption -> Screening (IScreeningEngine) -->
        <mxCell id="e5" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IScreeningEngine&lt;/b&gt;&lt;br&gt;(Rules Evaluation &amp;lt; 5s)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="c_adoption" target="c_screening">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Adoption -> Medical (IHealthClearance) -->
        <mxCell id="e6" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IHealthClearance&lt;/b&gt;&lt;br&gt;(Quarantine Check)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="c_adoption" target="c_medical">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Foster -> Notification (INotificationDispatch) -->
        <mxCell id="e7" value="&amp;laquo;use&amp;raquo; &lt;b&gt;INotificationDispatch&lt;/b&gt;&lt;br&gt;(48h Milestone Alert)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=1;exitY=0.5;entryX=0.2;entryY=1;" edge="1" parent="1" source="c_foster" target="c_notification">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Notification -> External SMTP (ISMTPClient) -->
        <mxCell id="e9" value="&amp;laquo;use&amp;raquo; &lt;b&gt;ISMTPClient&lt;/b&gt;&lt;br&gt;(SMTP / TLS)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.5;exitY=0;entryX=0.5;entryY=1;" edge="1" parent="1" source="c_notification" target="c_ext_email">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Data Access Connections (IShelterDataAccess) -->
        <mxCell id="e10" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IShelterDataAccess&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.5;exitY=1;entryX=0.08;entryY=0;" edge="1" parent="1" source="c_catalog" target="c_db_access">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="190" y="650" />
              <mxPoint x="303" y="650" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="e11" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IShelterDataAccess&lt;/b&gt;&lt;br&gt;(AES-256 Questionnaires)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.5;exitY=1;entryX=0.4;entryY=0;" edge="1" parent="1" source="c_screening" target="c_db_access">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e12" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IShelterDataAccess&lt;/b&gt;&lt;br&gt;(AES-256 Medical Records)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.3;exitY=1;entryX=0.68;entryY=0;" edge="1" parent="1" source="c_medical" target="c_db_access">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="708" y="380" />
              <mxPoint x="615" y="380" />
              <mxPoint x="615" y="650" />
              <mxPoint x="705" y="650" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="e13" value="&amp;laquo;use&amp;raquo; &lt;b&gt;IShelterDataAccess&lt;/b&gt;&lt;br&gt;(Timelines &amp;amp; Schedules)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;fontColor=#000000;strokeColor=#000000;strokeWidth=1.5;labelBackgroundColor=#ffffff;labelBorderColor=#000000;exitX=0.5;exitY=1;entryX=0.88;entryY=0;" edge="1" parent="1" source="c_foster" target="c_db_access">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''
    return xml

if __name__ == '__main__':
    xml_out = create_component_diagram()
    out_dir = '/home/andey/Documents/Sem5/SE/lab3'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'component_diagram.drawio')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(xml_out)
    print(f"Written updated monochrome draw.io diagram to {out_path}")
