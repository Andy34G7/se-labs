# Lab 2: Agile Backlog Creation and Sprint Simulation in Jira

- **Name**: Vinaayak G Dasika
- **SRN**: PES2UG24CS588
- **Section**: 5J

## Problem Statement: Warehouse Inventory and Pallet Location Tracker

## Product Backlog: Epics and User Stories

### Epic 1: Pallet Storage Validation and Load Control
- **Jira Key**: `WIPT-1`
- **Requirement Source**: FR-001, FR-004
- **Description**: The system validates structural load limits and maintains atomic rack utilization states.

#### Story 1.1: Rack Load Capacity Validation
- **Jira Key**: `WIPT-4`
- **Role**: As a warehouse operator,
- **Action**: I want the system to validate proposed pallet weight against the rack structural load limit,
- **Benefit**: So that I prevent structural rack overloading before storing pallets.
- **Acceptance Criteria**: The system permits pallet placement only when total weight is less than or equal to the rated limit.
- **Priority**: High
- **Story Points**: 5

#### Story 1.2: Live Rack Utilization Tracking
- **Jira Key**: `WIPT-5`
- **Role**: As a logistics supervisor,
- **Action**: I want the system to track live rack load percentages and send alerts at ninety percent capacity,
- **Benefit**: So that I can take preventive safety actions before reaching maximum limits.
- **Acceptance Criteria**: The system updates rack load state atomically on every move and alerts the supervisor at ninety percent load.
- **Priority**: High
- **Story Points**: 3

### Epic 2: Stock Movement Scanning and Audit Logging
- **Jira Key**: `WIPT-2`
- **Requirement Source**: FR-002
- **Description**: Warehouse operators capture barcode and RFID scans to record immutable stock movement logs.

#### Story 2.1: Barcode and RFID Movement Capture
- **Jira Key**: `WIPT-6`
- **Role**: As a warehouse operator,
- **Action**: I want to scan pallet and bin barcodes during put-away and transfer operations,
- **Benefit**: So that the system logs the SKU, quantity, coordinates, timestamp, and operator identifier.
- **Acceptance Criteria**: Every scan creates an immutable timestamped movement record in the warehouse database.
- **Priority**: High
- **Story Points**: 5

#### Story 2.2: Scan Deduplication and Audit Persistence
- **Jira Key**: `WIPT-7`
- **Role**: As a logistics supervisor,
- **Action**: I want the system to reject duplicate scans and persist transactions durably,
- **Benefit**: So that inventory audit logs contain zero duplicate or unconfirmed movements.
- **Acceptance Criteria**: The system rejects repeated scans within three seconds and guarantees zero data loss on confirmed moves.
- **Priority**: High
- **Story Points**: 3

### Epic 3: Real-Time SKU Lookup and Movement Reporting
- **Jira Key**: `WIPT-3`
- **Requirement Source**: FR-003, FR-005
- **Description**: The system provides rapid pallet location queries and exports operational movement reports.

#### Story 3.1: Real-Time Pallet Coordinate Lookup
- **Jira Key**: `WIPT-8`
- **Role**: As a warehouse operator,
- **Action**: I want to search for any SKU and view its exact zone, aisle, rack, level, and bin coordinates,
- **Benefit**: So that I can locate and pick stored pallets without manual floor searches.
- **Acceptance Criteria**: The system returns accurate coordinate data across all bins in under one hundred milliseconds.
- **Priority**: Medium
- **Story Points**: 5

#### Story 3.2: Movement History and Rack Load Reporting
- **Jira Key**: `WIPT-9`
- **Role**: As a logistics supervisor,
- **Action**: I want to generate movement history and rack load reports with date and zone filters,
- **Benefit**: So that I can audit warehouse throughput and export summaries as CSV files.
- **Acceptance Criteria**: The system exports filtered report totals that reconcile with the underlying movement log entries.
- **Priority**: Medium
- **Story Points**: 3

## Product Backlog Summary Table

| Jira Key | Epic Key | Epic Name | User Story Summary | Lab 1 Req | Priority | Story Points | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **WIPT-4** | WIPT-1 | Storage Validation | Story 1.1: Rack Load Capacity Validation | FR-001 | High | 5 | Sprint 1 |
| **WIPT-5** | WIPT-1 | Storage Validation | Story 1.2: Live Rack Utilization Tracking | FR-004 | High | 3 | Sprint 1 |
| **WIPT-6** | WIPT-2 | Movement Logging | Story 2.1: Barcode and RFID Movement Capture | FR-002 | High | 5 | Sprint 1 |
| **WIPT-7** | WIPT-2 | Movement Logging | Story 2.2: Scan Deduplication and Persistence | FR-002 | High | 3 | Sprint 1 |
| **WIPT-8** | WIPT-3 | Location & Reports | Story 3.1: Real-Time Pallet Coordinate Lookup | FR-003 | Medium | 5 | Sprint 2 |
| **WIPT-9** | WIPT-3 | Location & Reports | Story 3.2: Movement History and Load Reports | FR-005 | Medium | 3 | Sprint 2 |

## Sprint Execution and Simulation

### Sprint 1: Storage Load Validation and Movement Scanning
- **Sprint Goal**: Deliver rack capacity checks, live utilization tracking, and barcode movement logging.
- **Committed Story Points**: 16
- **Stories Completed**: `WIPT-4`, `WIPT-5`, `WIPT-6`, `WIPT-7`
- **Summary**: I moved all 16 story points through To Do, In Progress, and Done. I completed Sprint 1 on schedule.

### Sprint 2: Real-Time SKU Lookup and Supervisor Reporting
- **Sprint Goal**: Deliver fast SKU location queries and exportable movement audit reports.
- **Committed Story Points**: 8
- **Stories Completed**: `WIPT-8`, `WIPT-9`
- **Summary**: I moved all 8 story points through To Do, In Progress, and Done. I completed Sprint 2 on schedule.

## Reflection Questions

### 1. Did your estimations reflect the actual effort?
I used the Fibonacci scale during planning poker. I assigned 5 story points to tasks with atomic weight calculations and high-speed database queries. I assigned 3 story points to scan deduplication logic and CSV report exporting. These point values matched the development effort required during the sprints.

### 2. Was your backlog well-prioritized?
Yes. I scheduled rack structural load validation and scan logging in Sprint 1 because safe physical storage and accurate inventory intake are mandatory first steps. I placed coordinate lookups and reporting in Sprint 2 to build on verified movement data.

### 3. How did your simulated sprint align with your plan?
I completed all scheduled user stories within the planned sprint timeframe. Sprint 1 delivered 16 story points for safety checks and scan logging. Sprint 2 delivered 8 story points for search and reporting without carrying unfinished tasks forward.

### 4. What insights did the burndown chart give about your capacity?
The burndown chart confirmed that I completed 16 story points in Sprint 1 and 8 story points in Sprint 2. This shows that I handle critical safety and intake logic efficiently and complete secondary reporting tools quickly.

## Submission Screenshots

The following screenshots from Jira confirm the backlog setup, story points, active sprint board, and burndown metrics:

1. **Jira Backlog and Epics View**:  
   [01_jira_backlog.png](screenshots/01_jira_backlog.png)  
   Shows the active backlog with Sprint 1 user stories, Epics, High priorities, and story points.

2. **Full Backlog and Story Point Estimation**:  
   [02_story_points_backlog_full.png](screenshots/02_story_points_backlog_full.png)  
   Shows the complete backlog with all 6 user stories across Sprint 1 (16 points) and Sprint 2 (8 points).

3. **Active Sprint Board**:  
   [03_active_sprint_board.png](screenshots/03_active_sprint_board.png)  
   Shows the board during sprint execution with tasks transitioned across To Do, In Progress, and Done columns.

4. **Burndown Chart and Project Reports**:  
   [04_project_reports_metrics.png](screenshots/04_project_reports_metrics.png)  
   Shows the completion metrics, work items by status, work items by type, and resolution trends.
