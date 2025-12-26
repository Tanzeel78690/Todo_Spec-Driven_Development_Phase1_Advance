# Research: Core Todo Application Features

**Purpose**: To resolve any pending decisions from the initial planning phase and document the rationale for key technical choices.

## 1. Testing Framework

### Decision
We will use `pytest` as the testing framework for this project.

### Rationale
- **Industry Standard**: `pytest` is the de-facto standard for testing in the Python ecosystem. It is widely used and well-documented.
- **Simplicity and Readability**: `pytest` allows for writing simple, readable tests using plain `assert` statements, which aligns with the project's "Clarity & Simplicity" principle.
- **Rich Feature Set**: It has a powerful fixture system for managing test state and a vast ecosystem of plugins for extensibility, should the project require it in the future.
- **Test Discovery**: `pytest` has robust and customizable test discovery mechanisms.

### Alternatives Considered
- **`unittest`**: This is Python's built-in testing library. It was rejected because its class-based structure and `self.assert...` methods are more verbose than `pytest`'s functional approach.
- **`nose2`**: While a capable test runner, it is less common than `pytest` and has a smaller community and plugin ecosystem.
