### Task 1: Project Scaffolding & Core Domain Modeling

- [x] 1.1. Create the directory structure as outlined in `docs/prd.md`.
- [x] 1.2. Initialize the project with `uv` and add `pytest`, `ruff`, `rich`, and `pydantic`.
- [x] 1.3. Write a failing test in `tests/test_domain/test_entities.py` for the `Task` entity's creation and status management.
- [x] 1.4. Implement the `Task` entity in `src/todo_app/domain/entities.py` to make the test pass.
- [x] 1.5. Write failing tests for `TaskId` and other value objects.
- [x] 1.6. Implement the value objects in `src/todo_app/domain/value_objects.py`.
- [ ] 1.7. Verify by running `pytest tests/test_domain/`.
