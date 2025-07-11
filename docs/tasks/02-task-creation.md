### Task 2: Implement Task Creation (US-001)

- [x] 2.1. Write a failing end-to-end test in `tests/test_infrastructure/test_cli.py` for the `todo add` command.
- [x] 2.2. Run the test to confirm it fails because the command doesn't exist.
- [x] 2.3. Implement the basic CLI structure in `src/todo_app/infrastructure/cli/main.py` using `rich` and `typer`.
- [x] 2.4. Write a failing test for the `AddTaskCommandHandler` in `tests/test_application/test_commands.py`.
- [x] 2.5. Implement the `AddTaskCommand` and its handler in `src/todo_app/application/commands.py`.
- [x] 2.6. Write a failing test for the `InMemoryTaskRepository` in `tests/test_infrastructure/test_persistence.py`.
- [x] 2.7. Implement the `InMemoryTaskRepository` in `src/todo_app/infrastructure/persistence/in_memory.py`.
- [x] 2.8. Wire everything together and make the end-to-end test pass.
- [ ] 2.9. Verify by running `pytest tests/test_infrastructure/test_cli.py`.
