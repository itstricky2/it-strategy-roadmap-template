# Contributing to the IT Strategy

This strategy is a living product. We treat it like open-source software: collaborative, transparent, and governed by a defined process.

## Governance Process

We follow a "Request for Comments" (RFC) model for strategic changes.

### 1. New Initiatives
To propose a new strategic initiative (e.g., adopting a new technology, starting a major project):

1.  **Open an Issue**: Create a GitHub Issue with the label `RFC`.
2.  **Draft the Initiative**: Create a new file in `/initiatives/` (e.g., `initiatives/002-kubernetes-adoption.md`) using the standard template.
3.  **Submit a Pull Request**: Submit a PR linking to the RFC issue.
4.  **Architecture Review Board (ARB)**: The ARB will review the PR. Discussion happens in the PR comments.
    *   **Approval**: Requires sign-off from at least 2 ARB members.
    *   **Merge**: Once approved, the PR is merged, and the Roadmap is updated.

### 2. Updating the Roadmap
Direct updates to `.mmd` files in `/roadmap/` should accompany any approved Initiative PR.

*   **Horizon 1 Updates**: Adjust dates and dependencies in `tactical_roadmap.mmd` as projects evolve.
*   **Horizon 2/3 Updates**: Update `strategic_roadmap.mmd` only when there is a fundamental shift in direction.

## Style Guide

*   **Mermaid.js**: Use standard syntax. Ensure visualizations are readable.
*   **Markdown**: Use clear, concise language. Focus on business value, not just technical details.
