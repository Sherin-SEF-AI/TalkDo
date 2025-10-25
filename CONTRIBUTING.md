# Contributing to CLI Task Manager

Thank you for your interest in contributing to the CLI Task Manager! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating, you agree to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/cli-task-manager/cli-task-manager.git
cd cli-task-manager

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=cli_task_manager --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Code Formatting

```bash
# Format code with black
black cli_task_manager tests

# Sort imports with isort
isort cli_task_manager tests

# Check code style with flake8
flake8 cli_task_manager tests

# Type checking with mypy
mypy cli_task_manager
```

## Contributing Guidelines

### Types of Contributions

We welcome several types of contributions:

- **Bug fixes**: Fix issues in the codebase
- **New features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Tests**: Add or improve test coverage
- **Performance**: Optimize existing code
- **Refactoring**: Improve code structure without changing functionality

### Before You Start

1. Check existing issues and pull requests to avoid duplicates
2. For large changes, open an issue first to discuss the approach
3. Ensure your changes align with the project's goals and architecture

### Commit Message Format

Use clear, descriptive commit messages:

```
type(scope): brief description

Detailed description of the changes made.

- Bullet point for specific changes
- Another bullet point if needed

Fixes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(parser): add support for relative time expressions`
- `fix(database): resolve connection leak in long-running queries`
- `docs(readme): add installation instructions for Windows`

## Pull Request Process

### Before Submitting

1. **Test your changes**: Run the full test suite
2. **Format your code**: Use black and isort
3. **Check types**: Run mypy to catch type errors
4. **Update documentation**: Add or update relevant docs
5. **Add tests**: Include tests for new functionality
6. **Update changelog**: Add entry to CHANGELOG.md

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] No merge conflicts

## Related Issues
Fixes #123
Closes #456
```

### Review Process

1. **Automated checks**: CI/CD pipeline runs tests and checks
2. **Code review**: At least one maintainer reviews the code
3. **Testing**: Changes are tested in different environments
4. **Approval**: Maintainer approves and merges the PR

## Issue Reporting

### Bug Reports

When reporting bugs, include:

1. **Clear title**: Brief description of the issue
2. **Steps to reproduce**: Detailed steps to reproduce the bug
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**: OS, Python version, package version
6. **Error messages**: Full error messages and stack traces
7. **Screenshots**: If applicable

### Feature Requests

For feature requests, include:

1. **Clear title**: Brief description of the feature
2. **Use case**: Why this feature would be useful
3. **Proposed solution**: How you think it should work
4. **Alternatives**: Other approaches you've considered
5. **Additional context**: Any other relevant information

## Coding Standards

### Python Style

- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write docstrings for all public functions and classes
- Use meaningful variable and function names
- Keep functions small and focused

### Code Organization

- Group related functionality in modules
- Use clear module and package names
- Separate concerns (parsing, database, CLI, etc.)
- Follow the existing project structure

### Error Handling

- Use specific exception types
- Provide clear error messages
- Log errors appropriately
- Handle edge cases gracefully

### Performance

- Consider performance implications
- Use appropriate data structures
- Avoid unnecessary computations
- Profile code when needed

## Testing

### Test Coverage

- Aim for 80%+ test coverage
- Test all public functions and methods
- Include edge cases and error conditions
- Test both success and failure scenarios

### Test Types

- **Unit tests**: Test individual functions and methods
- **Integration tests**: Test component interactions
- **Performance tests**: Test with large datasets
- **End-to-end tests**: Test complete workflows

### Test Structure

```python
class TestFeature:
    """Test the Feature class."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.feature = Feature()
    
    def test_success_case(self):
        """Test successful operation."""
        result = self.feature.do_something()
        assert result == expected_value
    
    def test_error_case(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            self.feature.do_something_invalid()
```

## Documentation

### Code Documentation

- Write clear docstrings for all public functions
- Include parameter and return type information
- Provide usage examples in docstrings
- Document complex algorithms and logic

### User Documentation

- Keep README.md up to date
- Add examples for new features
- Update installation instructions
- Document configuration options

### API Documentation

- Document all public APIs
- Include type information
- Provide usage examples
- Keep documentation in sync with code

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Update documentation
5. Create release notes
6. Tag the release
7. Publish to PyPI

## Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Email**: For security issues or private matters

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to the CLI Task Manager! 🎉
