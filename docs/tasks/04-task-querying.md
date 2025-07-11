### Task 4: Implement Task Querying (US-005, US-006, US-007)

- [ ] 4.1. Write failing e2e tests for `todo list`, `todo list --status done`, and `todo show <task-id>`.
- [ ] 4.2. For each query, follow the outside-in TDD flow:
    - [ ] 4.2.1. Write a failing application-layer test for the query handler.
    - [ ] 4.2.2. Implement the query and handler.
    - [ ] 4.2.3. Ensure the repository supports the required query methods.
    - [ ] 4.2.4. Make the e2e test pass.
- [ ] 4.3. Verify by running `pytest tests/test_infrastructure/test_cli.py`.
