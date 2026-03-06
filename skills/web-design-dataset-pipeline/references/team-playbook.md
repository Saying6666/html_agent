# Team Playbook

Use this playbook when the user wants subagents or a team-style pipeline.

## Recommended Roles

### 1. Planner

Inputs:

- daily target or single-task request
- allowed categories and styles
- rejection history or QA feedback if available

Outputs:

- shortlisted concepts with scores
- locked task brief
- shared prompt package
- builder prompts for Gemini and GPT
- acceptance notes and risks

### 2. Builder Gemini

Inputs:

- planner brief
- `prompts/builder-gemini.md`

Outputs:

- Gemini HTML candidate
- implementation notes for layout and content risks

### 3. Builder GPT

Inputs:

- planner brief
- `prompts/builder-gpt.md`

Outputs:

- GPT HTML candidate
- implementation notes for semantics and interaction risks

### 4. Judge QA Packager

Inputs:

- both candidate HTML files
- validator output
- preview and video capture status

Outputs:

- pass or fail report
- winner selection rationale
- packaging result
- rejection-risk summary

## Handoff Contract

Pass data in this shape:

```yaml
taskid: fdu_001
category: SaaS landing page
style: Dark Mode
concept: AI observability platform
brand_name: AI Observability Platform
audience: DevOps teams at mid-market SaaS companies
sections:
  - Navbar
  - Hero
  - Metrics
  - Features
  - Pricing
  - Testimonials
  - FAQ
  - Footer
interactions:
  - button hover + active
  - card hover lift
  - navbar scroll blur
  - scroll reveal
  - counter animation
  - FAQ accordion
acceptance_notes:
  - return one complete src/index.html file only
  - keep CSS and JS inline
  - use remote assets only
  - include enough content for a full-page screenshot
risks:
  - avoid local assets
  - ensure at least 5 interaction patterns
  - avoid placeholder copy
winner_policy: validator-first then heuristic score
preview_mode: single
```

## Suggested Team Sequence

1. Planner proposes 3 candidate concepts.
2. Planner locks one concept and writes the prompt package.
3. Builder Gemini generates candidate A.
4. Builder GPT generates candidate B.
5. Judge QA runs validation for both candidates.
6. Judge QA triggers repair loops if needed.
7. Judge QA records the winner and writes `src/index.html`.
8. Judge QA captures assets, runs final validation, and builds the zip.

## Review Questions

Planner should ask:

- Is this category and style combination different enough from adjacent tasks?
- Are the prompts concrete enough that both models can execute them well?

Builders should ask:

- Does the page still work when opened directly from disk?
- Are all required interactions visible without external JS frameworks?
- Is the page long and content-rich enough for a full screenshot?

Judge QA should ask:

- Did both candidates pass the validator?
- Which candidate feels more complete and premium?
- Is every required artifact present?
- Does the video likely meet the 24 fps requirement?
