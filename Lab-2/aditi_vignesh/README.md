# Lab 2: Agile Backlog Creation and Sprint Simulation in Jira

- **Name**: Aditi Vignesh
- **SRN**: PES1UG24CS023

## Problem Statement: On-Demand Package Delivery Platform

## Product Backlog: Epics and User Stories

### Epic 1: Courier Booking and Cost Calculation
- **Jira Key**: `SL-6`
- **Requirement Source**: FR-001, FR-005
- **Description**: Senders book parcel pickups and the system calculates delivery prices based on parcel weight.

#### Story 1.1: Book Parcel Courier Pickup
- **Jira Key**: `SL-9`
- **Role**: As a sender client,
- **Action**: I want to enter pickup and destination addresses with package details,
- **Benefit**: So that I can book a delivery rider to transport my package.
- **Acceptance Criteria**: The system accepts pickup address, destination address, and weight, and then creates a booking record.
- **Priority**: High
- **Story Points**: 5

#### Story 1.2: Dynamic Cost Estimation by Weight
- **Jira Key**: `SL-10`
- **Role**: As a sender client,
- **Action**: I want to view the delivery price calculation based on package weight,
- **Benefit**: So that I know the accurate delivery cost before confirming the order.
- **Acceptance Criteria**: The system updates the total fare when package weight values change.
- **Priority**: High
- **Story Points**: 3

### Epic 2: Intelligent Rider Matching and Dispatch
- **Jira Key**: `SL-7`
- **Requirement Source**: FR-003
- **Description**: The platform identifies active riders nearby and dispatches courier pickup tasks.

#### Story 2.1: Proximity-Based Rider Matching
- **Jira Key**: `SL-11`
- **Role**: As the dispatch platform,
- **Action**: I want to search for active delivery riders within a three-kilometer radius,
- **Benefit**: So that the system assigns the nearest available rider quickly.
- **Acceptance Criteria**: The system matches the order only with active riders within three kilometers of the pickup location.
- **Priority**: High
- **Story Points**: 5

#### Story 2.2: Rider Dispatch Task Notification
- **Jira Key**: `SL-12`
- **Role**: As a delivery rider,
- **Action**: I want to receive pickup requests with route instructions on my mobile app,
- **Benefit**: So that I can accept eligible delivery tasks.
- **Acceptance Criteria**: The system delivers a push notification with pickup address and package weight to the selected rider.
- **Priority**: High
- **Story Points**: 3

### Epic 3: Live Telemetry Tracking and Destination OTP Verification
- **Jira Key**: `SL-8`
- **Requirement Source**: FR-002, FR-004
- **Description**: Senders track delivery riders in real time and delivery riders complete deliveries using recipient verification codes.

#### Story 3.1: Live GPS Telemetry Tracking
- **Jira Key**: `SL-13`
- **Role**: As a sender client,
- **Action**: I want to track the real-time GPS location of the assigned delivery rider on a live map,
- **Benefit**: So that I know the expected arrival time of my package.
- **Acceptance Criteria**: The system updates rider coordinates on the map with less than two seconds of latency.
- **Priority**: Medium
- **Story Points**: 5

#### Story 3.2: Destination OTP Verification
- **Jira Key**: `SL-14`
- **Role**: As a delivery rider,
- **Action**: I want to enter a six-digit one-time password provided by the recipient,
- **Benefit**: So that the system confirms package handover to the correct person.
- **Acceptance Criteria**: The system marks the delivery as completed only after successful code validation.
- **Priority**: Medium
- **Story Points**: 3

## Product Backlog Summary Table

| Jira Key | Epic Key | Epic Name | User Story Summary | Lab 1 Req | Priority | Story Points | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SL-9** | SL-6 | Courier Booking | Story 1.1: Book Parcel Courier Pickup | FR-001 | High | 5 | Sprint 1 |
| **SL-10** | SL-6 | Courier Booking | Story 1.2: Dynamic Cost Estimation by Weight | FR-005 | High | 3 | Sprint 1 |
| **SL-11** | SL-7 | Rider Dispatch | Story 2.1: Proximity-Based Rider Matching | FR-003 | High | 5 | Sprint 1 |
| **SL-12** | SL-7 | Rider Dispatch | Story 2.2: Rider Dispatch Task Notification | FR-003 | High | 3 | Sprint 1 |
| **SL-13** | SL-8 | Tracking & Verification | Story 3.1: Live GPS Telemetry Tracking | FR-002 | Medium | 5 | Sprint 2 |
| **SL-14** | SL-8 | Tracking & Verification | Story 3.2: Destination OTP Verification | FR-004 | Medium | 3 | Sprint 2 |

## Sprint Execution and Simulation

### Sprint 1: Booking Engine and Rider Dispatch
- **Sprint Goal**: Deliver parcel booking, weight cost calculation, and proximity rider dispatch.
- **Committed Story Points**: 16
- **Stories Completed**: `SL-9`, `SL-10`, `SL-11`, `SL-12`
- **Summary**: I moved all 16 story points through To Do, In Progress, and Done. I completed Sprint 1 on schedule.

### Sprint 2: Live Tracking and Secure Handover
- **Sprint Goal**: Deliver real-time GPS telemetry updates and destination OTP verification.
- **Committed Story Points**: 8
- **Stories Completed**: `SL-13`, `SL-14`
- **Summary**: I moved all 8 story points through To Do, In Progress, and Done. I completed Sprint 2 on schedule.

## Reflection Questions

### 1. Did your estimations reflect the actual effort?
I used the Fibonacci scale during planning poker. I assigned 5 story points to stories with algorithmic complexity, such as proximity rider matching and live map tracking. I assigned 3 story points to standard form validations and OTP verification logic. These estimates matched the work required during sprint execution.

### 2. Was your backlog well-prioritized?
Yes. I scheduled courier booking and rider dispatch in Sprint 1 because the platform needs working orders and assigned riders before anything else. I placed telemetry tracking and OTP verification in Sprint 2 to complete the post-dispatch delivery lifecycle.

### 3. How did your simulated sprint align with your plan?
I finished all planned user stories within the designated sprint timeframe. Sprint 1 completed 16 story points for the core booking engine. Sprint 2 completed 8 story points for live tracking and delivery verification without carrying incomplete items forward.

### 4. What insights did the burndown chart give about your capacity?
The burndown chart confirmed that I completed 16 story points in Sprint 1 and 8 story points in Sprint 2. This shows that I handle higher complexity during initial platform setup and maintain steady delivery speed across subsequent sprints.

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
