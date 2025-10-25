#!/usr/bin/env python3
"""
Installation script for the CLI Task Manager.

This script helps with the installation and setup of the CLI Task Manager.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True


def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    
    # Install in development mode
    if run_command("pip install -e .", "Installing CLI Task Manager"):
        return True
    
    # Fallback: install dependencies manually
    dependencies = [
        "typer[all]>=0.9.0",
        "rich>=13.0.0", 
        "pydantic>=2.0.0",
        "sqlalchemy>=2.0.0",
        "dateparser>=1.1.0",
        "pyyaml>=6.0",
        "croniter>=1.3.0",
        "plyer>=2.1.0",
        "click>=8.0.0",
        "tabulate>=0.9.0",
        "python-dateutil>=2.8.0",
        "schedule>=1.2.0",
        "psutil>=5.9.0"
    ]
    
    for dep in dependencies:
        if not run_command(f"pip install {dep}", f"Installing {dep}"):
            return False
    
    return True


def setup_directories():
    """Setup required directories."""
    home = Path.home()
    task_manager_dir = home / ".task-manager"
    
    directories = [
        task_manager_dir,
        task_manager_dir / "backups",
        task_manager_dir / "logs"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")
    
    return True


def test_installation():
    """Test the installation."""
    print("🧪 Testing installation...")
    
    # Test import
    try:
        import cli_task_manager
        print("✅ CLI Task Manager imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import CLI Task Manager: {e}")
        return False
    
    # Test CLI command
    if run_command("task --help", "Testing CLI command"):
        print("✅ CLI command works")
        return True
    else:
        print("❌ CLI command failed")
        return False


def main():
    """Main installation function."""
    print("🚀 CLI Task Manager Installation")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Installation failed")
        sys.exit(1)
    
    # Setup directories
    if not setup_directories():
        print("❌ Directory setup failed")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("❌ Installation test failed")
        sys.exit(1)
    
    print("\n🎉 Installation completed successfully!")
    print("\nQuick start:")
    print("  task add 'buy milk tomorrow'")
    print("  task list")
    print("  task --help")
    print("\nFor more information, visit:")
    print("  https://github.com/cli-task-manager/cli-task-manager")


if __name__ == "__main__":
    main()
