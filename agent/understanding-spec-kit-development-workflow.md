# TIL: GitHub Spec Kit — Spec-Driven Development

GitHub Spec Kit is an open-source toolkit for **Spec-Driven Development (SDD)**. Instead of asking AI to generate code directly, it provides a structured workflow to define requirements, plan implementation, and validate results.

Just as developers follow software development methodologies like TDD, AI agents can also follow structured development workflows.

GitHub Spec Kit translates Spec-Driven Development into actionable instructions, specifications, and tasks that AI agents can follow.

Instead of simply asking AI to write code, we define how AI should approach software development.

**GitHub:** https://github.com/github/spec-kit

## Core Workflow

1. **Constitution — `/speckit.constitution`**
   Establish project-wide principles, coding standards, testing requirements, and architectural constraints.

2. **Specify — `/speckit.specify`**
   Define what to build and why, including user stories, functional requirements, and acceptance criteria.

3. **Clarify — `/speckit.clarify`**
   Identify ambiguities, resolve unclear requirements, and clarify edge cases.

4. **Test Design — Custom Step**
   Define test scenarios, expected outcomes, and validation criteria before technical planning.

5. **Plan — `/speckit.plan`**
   Define how to build the feature, including technology choices, architecture, data models, and interfaces.

6. **Tasks — `/speckit.tasks`**
   Break the implementation plan into actionable tasks with execution order and dependencies.

7. **Analyze — `/speckit.analyze`**
   Check consistency across specifications, plans, and tasks. Identify gaps, conflicts, and violations of project principles.

8. **Implement — `/speckit.implement`**
   Execute tasks, write code, run tests, and fix issues. Follow a test-first approach when applying TDD.

9. **Converge — `/speckit.converge`**
    Verify that the implementation satisfies the original specifications and identify any remaining gaps.


