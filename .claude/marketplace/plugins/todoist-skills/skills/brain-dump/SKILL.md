---
name: brain-dump
description: Take a freeform list of things and bulk-create tasks from them. Use when the user wants to quickly capture multiple tasks at once, do a brain dump, or create several tasks from a messy list of thoughts.
disable-model-invocation: true
---

The user is doing a brain dump. They will provide a freeform list of things — sentences, fragments, messy notes, anything.

Your job:
1. Parse their input ($ARGUMENTS) and identify distinct tasks
2. For each task, infer a clean title (short, actionable, starts with a verb)
3. Create each task using mcp__todoist__create_task
4. After creating all tasks, show a summary list of what was created

Keep task titles concise. Don't ask clarifying questions — just process and create. If input is empty, ask the user to type their brain dump.
