# Project Plan: Style Synchronization

This plan outlines the steps required to synchronize the design of 4 internal feature sub-directories with the main landing page.

## Phase 1: Exploration
- **Goal**: Identify style components from the landing page (`index.html`, `style.css`) and analyze target files in the 4 sub-directories.
- **Worker**: Explorer subagent
- **Artifact**: Analysis report and implementation details
- **Verification**: Verify that the design variables, typography (Be Vietnam Pro), color scheme (#1456F0 & White), buttons, tables, and card structures are thoroughly mapped.

## Phase 2: Implementation
- **Goal**: Apply UI Style Synchronization to the 4 pages.
- **Sub-pages to modify**:
  1. `/quan-ly-team/index.html`
  2. `/theo-doi-san-pham-edit/index.html`
  3. `/phan-cong-edit-video/index.html`
  4. `/bang-tinh-luong-thuong/index.html`
- **Worker**: Worker subagent
- **Verification**: Verify that fonts, colors, buttons, navbars, and cards look identical to the landing page style. Verify that all scripts, data tables, dynamic calculations, and routing are intact and fully functional.

## Phase 3: Review & Refinement
- **Goal**: Review code changes and test responsiveness, styling, and functionality.
- **Worker**: Reviewer / Challenger subagents
- **Verification**: Reviewer checks correctness. Challenger performs E2E checks to confirm all elements function as expected.

## Phase 4: Final Auditing & Sign-off
- **Goal**: Perform an integrity audit to ensure compliance.
- **Worker**: Forensic Auditor subagent
- **Verification**: Clean audit verdict.
