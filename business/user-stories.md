```markdown
# user-stories.md

## Epic 1 – Scope Definition & Discovery
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 1 | **As an open‑source maintainer, I want to import my repo metadata so that I can auto‑populate the initial scope template.** | • Repo URL is validated and cloned via GitHub API.<br>• README, LICENSE, and existing issue labels are fetched.<br>• A default scope document is generated with sections for goals, constraints, and deliverables.<br>• User can edit the template before finalizing. | S |
| 2 | **As a contributor, I want to propose a new feature scope in a single form so that I can quickly add it to the project backlog.** | • Form includes title, description, acceptance criteria, and estimated effort.<br>• Auto‑suggests related issues or PRs.<br>• Submits as a GitHub issue with a `scope-proposal` label.<br>• Notifies maintainers via a comment. | S |
| 3 | **As a maintainer, I want to set scope boundaries (e.g., tech stack, release cadence) so that contributors know what is in scope.** | • Boundary settings are stored in a `.scope.yml` file.<br>• UI shows current boundaries and allows edits.<br>• Changes trigger a diff preview against existing scope.<br>• Boundary changes are versioned and linked to releases. | M |

## Epic 2 – Scope Validation & Prioritization
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 4 | **As a maintainer, I want to run a scope validation check so that I can ensure new proposals align with the project’s scope boundaries.** | • Validation scans issue titles, labels, and PR descriptions.<br>• Flags any out‑of‑scope items with a severity score.<br>• Generates a report and suggests remediation steps.<br>• Can be run manually or on every PR merge. | M |
| 5 | **As a contributor, I want to see a priority ranking of scope items so that I can focus on the most valuable work.** | • Items are ranked by impact, effort, and community votes.<br>• Ranking is displayed in the scope dashboard.<br>• Users can upvote/downvote items.<br>• Rankings update in real time. | M |
| 6 | **As a maintainer, I want to lock the scope for a release so that no new features are added mid‑cycle.** | • Scope lock toggles a `locked` flag in `.scope.yml`.<br>• New proposals are rejected with a clear message.<br>• Lock status is visible on the dashboard.<br>• Lock can be overridden by an admin with a justification. | S |

## Epic 3 – Scope Tracking & Analytics
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 7 | **As a maintainer, I want to view a scope health dashboard so that I can monitor scope creep over time.** | • Dashboard shows scope size, number of open proposals, and burn‑up chart.<br>• Highlights trends and alerts when scope exceeds thresholds.<br>• Data is sourced from GitHub events and `.scope.yml`. | L |
| 8 | **As a contributor, I want to receive automated reminders when my PR is out of scope so that I can adjust it before review.** | • Bot posts a comment on PR with scope violation details.<br>• Provides a link to the relevant scope section.<br>• Option to auto‑close the PR if not corrected within 48h. | M |
| 9 | **As a maintainer, I want to export scope metrics to CSV so that I can share them with stakeholders.** | • Export includes scope size, number of proposals, acceptance rate, and burn‑up.<br>• CSV is generated on demand via a button.<br>• Includes metadata (repo, date range). | S |
| 10 | **As a contributor, I want to see my personal scope contribution history so that I can track my impact.** | • History lists all proposals I submitted, their status, and outcome.<br>• Includes timestamps and comments.<br>• Accessible via the user profile page. | S |

## Epic 4 – Collaboration & Governance
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 11 | **As a maintainer, I want to assign reviewers to scope proposals so that they receive appropriate feedback.** | • Reviewer assignment is done via a dropdown of repo collaborators.<br>• Assigned reviewers receive a GitHub notification.<br>• Review status is tracked in the scope dashboard. | S |
| 12 | **As a contributor, I want to comment on scope proposals so that I can discuss feasibility with maintainers.** | • Inline comments are supported on the proposal page.<br>• Comments are linked to the issue thread.<br>• Thread can be resolved or closed by the maintainer. | S |
```
```