# Project Context — 2026-06-07T17:35:00Z

## Current Task
Style synchronization of four sub-pages to match the Lark Style Design System, while keeping the client-side JavaScript logic 100% intact.

## Target Directories
1. `/quan-ly-team/` - Completed and verified.
2. `/theo-doi-san-pham-edit/` - Completed and verified.
3. `/phan-cong-edit-video/` - Original file is clean but needs visual styling (Be Vietnam Pro, Lark navbar, footer, container custom, button, table) without changing script content.
4. `/bang-tinh-luong-thuong/` - Has several bugs (mobile menu class mismatch, days off validation cap, clipboard secure context check, out-of-sync inputs) that need fixing.

## Critical Constraints
- Do not write code directly in the workspace.
- Spawn a specialized Worker subagent to perform all code changes.
- Ensure that the final gate check includes unit/E2E verification and a Forensic Audit.
