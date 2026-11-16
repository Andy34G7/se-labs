# Lab 2: Agile Backlog Creation and Sprint Simulation in Jira

- **Name**: Andey Hemanth
- **SRN**: PES2UG24CS061

## Problem Statement 57: Pet Adoption and Shelter Management System

## Product Backlog: Epics and User Stories

### Epic 1: Animal Medical Intake and Status Management
- **Jira Key**: `SCRUM-5`
- **Requirement Source**: FR-001
- **Description**: Shelter staff records medical intake details and updates animal adoption availability.

#### Story 1.1: Log Vaccination and Medical Intake
- **Jira Key**: `SCRUM-8`
- **Role**: As shelter staff,
- **Action**: I want to record vaccination details and medical intake history,
- **Benefit**: So that I can maintain a complete health record for every rescued animal.
- **Acceptance Criteria**: The system links medical records to the animal profile and saves the date, medication, and dosage.
- **Priority**: High
- **Story Points**: 5

#### Story 1.2: Update Animal Availability Status
- **Jira Key**: `SCRUM-9`
- **Role**: As shelter staff,
- **Action**: I want to mark medically cleared animals as Ready for Adoption,
- **Benefit**: So that eligible animals appear immediately on the public pet catalog.
- **Acceptance Criteria**: The system updates the animal status only after a staff member verifies all mandatory vaccinations.
- **Priority**: High
- **Story Points**: 3

### Epic 2: Adopter Application and Eligibility Screening
- **Jira Key**: `SCRUM-6`
- **Requirement Source**: FR-002, FR-003
- **Description**: Adoption applicants submit questionnaires and shelter staff evaluates applicant eligibility.

#### Story 2.1: Submit Adoption Questionnaire
- **Jira Key**: `SCRUM-10`
- **Role**: As an adoption applicant,
- **Action**: I want to submit an online adoption questionnaire for an available pet,
- **Benefit**: So that shelter staff can review my application and housing profile.
- **Acceptance Criteria**: The system validates all required fields, saves the form, and generates a unique tracking identifier.
- **Priority**: High
- **Story Points**: 5

#### Story 2.2: Automated Eligibility Screening
- **Jira Key**: `SCRUM-11`
- **Role**: As shelter staff,
- **Action**: I want the system to screen submitted questionnaires automatically against shelter criteria,
- **Benefit**: So that I can identify qualified applicants quickly.
- **Acceptance Criteria**: The system flags disqualifying responses within five seconds and alerts staff to policy conflicts.
- **Priority**: High
- **Story Points**: 5

### Epic 3: Foster Placement and Milestone Tracking
- **Jira Key**: `SCRUM-7`
- **Requirement Source**: FR-004, FR-005
- **Description**: Shelter staff manages foster placement schedules and sends milestone alerts to foster caretakers.

#### Story 3.1: Schedule Foster Placement Timeline
- **Jira Key**: `SCRUM-12`
- **Role**: As shelter staff,
- **Action**: I want to schedule foster placement start dates, check-in dates, and expected return dates,
- **Benefit**: So that the shelter tracks the location and care duration of every animal.
- **Acceptance Criteria**: The system records the timeline and blocks overlapping foster assignments for the same animal.
- **Priority**: Medium
- **Story Points**: 3

#### Story 3.2: Foster Milestone Reminder Alerts
- **Jira Key**: `SCRUM-13`
- **Role**: As a foster caretaker,
- **Action**: I want to receive email alerts forty-eight hours before scheduled veterinary check-ins,
- **Benefit**: So that I bring the foster animal for medical evaluations on time.
- **Acceptance Criteria**: The system sends an email reminder forty-eight hours before each milestone date.
- **Priority**: Medium
- **Story Points**: 2

## Product Backlog Summary Table

| Jira Key | Epic Key | Epic Name | User Story Summary | Lab 1 Req | Priority | Story Points | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SCRUM-8** | SCRUM-5 | Animal Medical Intake | Story 1.1: Log Vaccination and Intake | FR-001 | High | 5 | Sprint 1 |
| **SCRUM-9** | SCRUM-5 | Animal Medical Intake | Story 1.2: Update Animal Status | FR-001 | High | 3 | Sprint 1 |
| **SCRUM-10** | SCRUM-6 | Adopter Screening | Story 2.1: Submit Questionnaire | FR-002 | High | 5 | Sprint 1 |
| **SCRUM-11** | SCRUM-6 | Adopter Screening | Story 2.2: Automated Screening | FR-003 | High | 5 | Sprint 1 |
| **SCRUM-12** | SCRUM-7 | Foster Management | Story 3.1: Schedule Foster Timeline | FR-004 | Medium | 3 | Sprint 2 |
| **SCRUM-13** | SCRUM-7 | Foster Management | Story 3.2: Foster Reminder Alerts | FR-005 | Medium | 2 | Sprint 2 |

## Sprint Execution and Simulation

### Sprint 1: Core Adoption and Intake Workflow
- **Sprint Goal**: Deliver medical intake logging and adoption questionnaire screening.
- **Committed Story Points**: 18
- **Stories Completed**: `SCRUM-8`, `SCRUM-9`, `SCRUM-10`, `SCRUM-11`
- **Summary**: I moved all 18 story points through To Do, In Progress, and Done. I completed Sprint 1 on schedule.

### Sprint 2: Foster Placement and Alert Automation
- **Sprint Goal**: Deliver foster timeline scheduling and automated milestone email alerts.
- **Committed Story Points**: 5
- **Stories Completed**: `SCRUM-12`, `SCRUM-13`
- **Summary**: I moved all 5 story points through To Do, In Progress, and Done. I completed Sprint 2 on schedule.

## Reflection Questions

### 1. Did the estimations reflect the actual effort?
I used the Fibonacci scale during planning poker. I assigned 5 story points to tasks with data validation and background rules, such as medical intake and questionnaire screening. I assigned 2 or 3 story points to simpler tasks, such as status toggles and email reminders. These point values matched the effort required during implementation.

### 2. Was the backlog well-prioritized?
Yes. I placed medical intake and adopter screening into Sprint 1 because the shelter needs verified animal records and screened adopters before anything else. I placed foster placement schedules and milestone alerts into Sprint 2 as secondary coordination tools.

### 3. How did the simulated sprint align with your plan?
I completed all scheduled user stories within the planned sprint timeframe. Sprint 1 completed 18 story points for core intake and screening. Sprint 2 completed 5 story points for foster care without carrying unfinished tasks into future sprints.

### 4. What insights did the burndown chart give about your capacity?
The burndown chart confirmed that I completed 18 story points in Sprint 1 and 5 story points in Sprint 2. This shows that I can handle high velocity for primary features and resolve secondary coordination tasks quickly.

## Submission Screenshots

The following screenshots from Jira confirm the backlog setup, story points, active sprint board, and burndown metrics:

1. **Jira Backlog and Epics View**:  
   [01_jira_backlog.png](screenshots/01_jira_backlog.png)  
   Shows the active backlog with Sprint 1 user stories, Epics, High priorities, and story points.

2. **Full Backlog and Story Point Estimation**:  
   [02_story_points_backlog_full.png](screenshots/02_story_points_backlog_full.png)  
   Shows the complete backlog with all 6 user stories across Sprint 1 (18 points) and Sprint 2 (5 points).

3. **Active Sprint Board**:  
   [03_active_sprint_board.png](screenshots/03_active_sprint_board.png)  
   Shows the board during sprint execution with tasks transitioned across To Do, In Progress, and Done columns.

4. **Project Reports and Metrics**:  
   [04_project_reports_metrics.png](screenshots/04_project_reports_metrics.png)  
   Shows the completion metrics, work items by status, work items by type, and resolution trends.
