# Lab 2: Agile Backlog Creation and Sprint Simulation in Jira

- **Name**: Angelo Arakal
- **SRN**: PES2UG24CS062

## Problem Statement 58: Digital Art Commission and Watermarking Portal

## Product Backlog: Epics and User Stories

### Epic 1: Creative Brief and Milestone Draft Management
- **Jira Key**: `DAC-6`
- **Requirement Source**: FR-2, FR-3
- **Description**: Client buyers create commission briefs and digital artists upload milestone work-in-progress drafts.

#### Story 1.1: Submit Creative Commission Brief
- **Jira Key**: `DAC-9`
- **Role**: As a client buyer,
- **Action**: I want to submit a creative brief with description text and reference images,
- **Benefit**: So that the artist understands project requirements before starting work.
- **Acceptance Criteria**: The system validates description text and attached reference images before saving the brief.
- **Priority**: High
- **Story Points**: 5

#### Story 1.2: Upload WIP Progress Draft
- **Jira Key**: `DAC-10`
- **Role**: As a digital artist,
- **Action**: I want to upload a work-in-progress draft image and tag it to a commission milestone,
- **Benefit**: So that the client tracks milestone progress accurately.
- **Acceptance Criteria**: The system stores uploaded drafts and links them to the selected milestone record.
- **Priority**: High
- **Story Points**: 3

### Epic 2: Dynamic Watermarking and Draft Review
- **Jira Key**: `DAC-7`
- **Requirement Source**: FR-1, FR-4
- **Description**: The platform watermarks draft illustrations automatically and client buyers review milestone progress.

#### Story 2.1: Dynamic Diagonal Watermark Processing
- **Jira Key**: `DAC-11`
- **Role**: As the commission platform,
- **Action**: I want to apply a diagonal overlay watermark to all draft illustrations automatically,
- **Benefit**: So that artist intellectual property remains protected before payment.
- **Acceptance Criteria**: The client portal displays only watermarked previews before milestone payment confirmation.
- **Priority**: High
- **Story Points**: 5

#### Story 2.2: Client WIP Review and Revision Feedback
- **Jira Key**: `DAC-12`
- **Role**: As a client buyer,
- **Action**: I want to review watermarked drafts and submit approval or written revision feedback,
- **Benefit**: So that the artist can refine illustrations based on my comments.
- **Acceptance Criteria**: The system records the approval status or captures required feedback text before updating the milestone.
- **Priority**: High
- **Story Points**: 3

### Epic 3: Milestone Payment and Secure Asset Delivery
- **Jira Key**: `DAC-8`
- **Requirement Source**: FR-5, NFR-1, NFR-2
- **Description**: The platform processes milestone payments and delivers unwatermarked high-resolution assets via secure expiring URLs.

#### Story 3.1: Milestone Payment Processing
- **Jira Key**: `DAC-13`
- **Role**: As a client buyer,
- **Action**: I want to complete payment for an approved milestone using the payment gateway,
- **Benefit**: So that the system unlocks the final creative assets.
- **Acceptance Criteria**: The system receives gateway webhooks and marks milestones as paid within five seconds.
- **Priority**: High
- **Story Points**: 5

#### Story 3.2: Expiring Signed Asset Download URL
- **Jira Key**: `DAC-14`
- **Role**: As a client buyer,
- **Action**: I want to download unwatermarked high-resolution source files via expiring signed links,
- **Benefit**: So that I receive paid creative assets securely.
- **Acceptance Criteria**: The system generates a signed download URL that expires after sixty minutes.
- **Priority**: Medium
- **Story Points**: 3

## Product Backlog Summary Table

| Jira Key | Epic Key | Epic Name | User Story Summary | Lab 1 Req | Priority | Story Points | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DAC-9** | DAC-6 | Brief & Draft Management | Story 1.1: Submit Creative Commission Brief | FR-2 | High | 5 | Sprint 1 |
| **DAC-10** | DAC-6 | Brief & Draft Management | Story 1.2: Upload WIP Progress Draft | FR-3 | High | 3 | Sprint 1 |
| **DAC-11** | DAC-7 | Watermarking & Review | Story 2.1: Dynamic Diagonal Watermark Processing | FR-1 | High | 5 | Sprint 1 |
| **DAC-12** | DAC-7 | Watermarking & Review | Story 2.2: Client WIP Review and Feedback | FR-4 | High | 3 | Sprint 1 |
| **DAC-13** | DAC-8 | Payment & Asset Delivery | Story 3.1: Milestone Payment Processing | FR-5 | High | 5 | Sprint 2 |
| **DAC-14** | DAC-8 | Payment & Asset Delivery | Story 3.2: Expiring Signed Asset Download URL | FR-5, NFR-1 | Medium | 3 | Sprint 2 |

## Sprint Execution and Simulation

### Sprint 1: Commission Intake, Watermarking, and Review
- **Sprint Goal**: Deliver creative briefs and watermarking.
- **Committed Story Points**: 16
- **Stories Completed**: `DAC-9`, `DAC-10`, `DAC-11`, `DAC-12`
- **Summary**: I moved all 16 story points through To Do, In Progress, and Done. I completed Sprint 1 on schedule.

### Sprint 2: Milestone Payment and Secure Delivery
- **Sprint Goal**: Deliver milestone payments and secure asset downloads.
- **Committed Story Points**: 8
- **Stories Completed**: `DAC-13`, `DAC-14`
- **Summary**: I moved all 8 story points through To Do, In Progress, and Done. I completed Sprint 2 on schedule.

## Reflection Questions

### 1. Did your estimations reflect the actual effort?
I used the Fibonacci scale during planning poker. I assigned 5 story points to tasks with external gateway integrations and image processing pipelines. I assigned 3 story points to standard draft uploads and feedback forms. These point values matched the development effort required during the sprints.

### 2. Was your backlog well-prioritized?
Yes. I scheduled brief submission, draft uploads, and watermarking in Sprint 1 because artists need an intake workflow and copyright protection before receiving payments. I placed payment gateways and secure download links in Sprint 2 to complete the post-review delivery phase.

### 3. How did your simulated sprint align with your plan?
I completed all scheduled user stories within the planned sprint timeframe. Sprint 1 delivered 16 story points for draft intake and watermarking. Sprint 2 delivered 8 story points for payment processing and asset delivery without carrying unfinished tasks forward.

### 4. What insights did the burndown chart give about your capacity?
The burndown chart confirmed that I completed 16 story points in Sprint 1 and 8 story points in Sprint 2. This shows that I handle media processing logic efficiently and complete checkout workflows quickly.

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
