#!/usr/bin/env python3
"""
Test runner for the CLI Task Manager.

This script runs the complete test suite with coverage reporting
and various test configurations.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description, capture_output=False):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        else:
            subprocess.run(command, shell=True, check=True)
            print(f"✅ {description} completed")
            return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if capture_output and e.stderr:
            print(f"Error output: {e.stderr}")
        return False


def check_environment():
    """Check if the environment is set up correctly."""
    print("🔍 Checking environment...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml not found. Are you in the project root?")
        return False
    
    print("✅ Project structure looks good")
    return True


def install_dependencies():
    """Install test dependencies."""
    print("📦 Installing test dependencies...")
    
    # Install in development mode
    if not run_command("pip install -e .[dev]", "Installing development dependencies"):
        print("❌ Failed to install dependencies")
        return False
    
    return True


def run_unit_tests():
    """Run unit tests."""
    print("\n🧪 Running unit tests...")
    
    # Run tests with coverage
    command = "pytest tests/ -v --cov=cli_task_manager --cov-report=term-missing --cov-report=html"
    
    if not run_command(command, "Running unit tests with coverage"):
        print("❌ Unit tests failed")
        return False
    
    return True


def run_integration_tests():
    """Run integration tests."""
    print("\n🔗 Running integration tests...")
    
    # Run integration tests
    command = "pytest tests/ -v -m integration"
    
    if not run_command(command, "Running integration tests"):
        print("❌ Integration tests failed")
        return False
    
    return True


def run_performance_tests():
    """Run performance tests."""
    print("\n⚡ Running performance tests...")
    
    # Run performance tests
    command = "pytest tests/ -v -m performance"
    
    if not run_command(command, "Running performance tests"):
        print("❌ Performance tests failed")
        return False
    
    return True


def run_linting():
    """Run code linting."""
    print("\n🔍 Running code linting...")
    
    # Run flake8
    if not run_command("flake8 cli_task_manager tests", "Running flake8"):
        print("❌ Flake8 failed")
        return False
    
    # Run mypy
    if not run_command("mypy cli_task_manager", "Running mypy"):
        print("❌ MyPy failed")
        return False
    
    return True


def run_formatting():
    """Check code formatting."""
    print("\n🎨 Checking code formatting...")
    
    # Check black formatting
    if not run_command("black --check cli_task_manager tests", "Checking black formatting"):
        print("❌ Code formatting issues found")
        print("Run 'black cli_task_manager tests' to fix")
        return False
    
    # Check isort
    if not run_command("isort --check-only cli_task_manager tests", "Checking import sorting"):
        print("❌ Import sorting issues found")
        print("Run 'isort cli_task_manager tests' to fix")
        return False
    
    return True


def generate_coverage_report():
    """Generate detailed coverage report."""
    print("\n📊 Generating coverage report...")
    
    # Generate HTML coverage report
    if run_command("pytest --cov=cli_task_manager --cov-report=html", "Generating HTML coverage report"):
        print("✅ Coverage report generated in htmlcov/index.html")
        return True
    
    return False


def run_specific_tests():
    """Run specific test categories."""
    print("\n🎯 Running specific test categories...")
    
    test_categories = [
        ("models", "tests/test_models.py"),
        ("parser", "tests/test_parser.py"),
        ("database", "tests/test_database.py"),
        ("cli", "tests/test_cli.py"),
        ("daemon", "tests/test_daemon.py"),
    ]
    
    for category, test_file in test_categories:
        if Path(test_file).exists():
            print(f"\n📋 Running {category} tests...")
            if not run_command(f"pytest {test_file} -v", f"Running {category} tests"):
                print(f"❌ {category} tests failed")
                return False
        else:
            print(f"⚠️  {test_file} not found, skipping {category} tests")
    
    return True


def run_examples():
    """Run example scripts to verify functionality."""
    print("\n📚 Running example scripts...")
    
    # Run examples script
    if Path("examples.py").exists():
        if not run_command("python examples.py", "Running examples script"):
            print("❌ Examples script failed")
            return False
    
    return True


def main():
    """Main test runner function."""
    print("🚀 CLI Task Manager Test Runner")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="CLI Task Manager Test Runner")
    parser.add_argument("--unit", action="store_true", help="Run unit tests only")
    parser.add_argument("--integration", action="store_true", help="Run integration tests only")
    parser.add_argument("--performance", action="store_true", help="Run performance tests only")
    parser.add_argument("--lint", action="store_true", help="Run linting only")
    parser.add_argument("--format", action="store_true", help="Check formatting only")
    parser.add_argument("--coverage", action="store_true", help="Generate coverage report only")
    parser.add_argument("--examples", action="store_true", help="Run examples only")
    parser.add_argument("--all", action="store_true", help="Run all tests and checks")
    
    args = parser.parse_args()
    
    # If no specific flags, run all tests
    if not any(vars(args).values()):
        args.all = True
    
    success = True
    
    # Run requested tests
    if args.unit or args.all:
        success &= run_unit_tests()
    
    if args.integration or args.all:
        success &= run_integration_tests()
    
    if args.performance or args.all:
        success &= run_performance_tests()
    
    if args.lint or args.all:
        success &= run_linting()
    
    if args.format or args.all:
        success &= run_formatting()
    
    if args.coverage or args.all:
        success &= generate_coverage_report()
    
    if args.examples or args.all:
        success &= run_examples()
    
    # Run specific test categories
    if args.all:
        success &= run_specific_tests()
    
    # Summary
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests and checks passed!")
        print("\nNext steps:")
        print("  • Review coverage report: htmlcov/index.html")
        print("  • Run examples: python examples.py")
        print("  • Install in development mode: pip install -e .")
        print("  • Try the CLI: task --help")
    else:
        print("❌ Some tests or checks failed")
        print("\nTroubleshooting:")
        print("  • Check error messages above")
        print("  • Run specific test categories with --unit, --integration, etc.")
        print("  • Fix formatting issues with: black cli_task_manager tests")
        print("  • Fix import sorting with: isort cli_task_manager tests")
        sys.exit(1)


if __name__ == "__main__":
    main()
