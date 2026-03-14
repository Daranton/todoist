---
name: triage
description: List all tasks and help prioritize or clean up interactively. Use when the user wants to review, clean up, or prioritize their task list.
disable-model-invocation: true
---

Help the user triage their task list.

Steps:
1. Fetch all tasks using mcp__todoist__list_tasks
2. Display them grouped by a quick assessment:
   - **Do now** — urgent or blocked on you
   - **Do later** — important but not urgent
   - **Maybe/unclear** — vague or possibly outdated
3. For each "maybe/unclear" task, briefly ask if it should be kept, deleted, or reworded
4. Act on the user's responses: delete stale tasks, complete done ones, or update titles if needed
5. End with a clean summary of what remains

Be direct. Don't pad responses. If the list is empty, say so.
