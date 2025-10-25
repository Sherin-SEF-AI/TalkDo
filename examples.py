#!/usr/bin/env python3
"""
Examples and demonstrations for the CLI Task Manager.

This script demonstrates the capabilities of the CLI Task Manager
with various natural language examples.
"""

import sys
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from cli_task_manager.core.parser import NaturalLanguageParser
from cli_task_manager.core.config import Config
from cli_task_manager.core.database import DatabaseManager
from cli_task_manager.models.task import Task, TaskPriority, TaskStatus


def demonstrate_parser():
    """Demonstrate the natural language parser."""
    print("🔍 Natural Language Parser Examples")
    print("=" * 50)
    
    parser = NaturalLanguageParser()
    
    examples = [
        "buy milk",
        "call mom tomorrow at 3pm",
        "urgent: fix production bug",
        "review pull requests every Monday",
        "high priority: deploy feature X by Friday 5pm with tags deployment, urgent",
        "weekly team meeting every Monday at 10am",
        "submit report by end of day",
        "buy groceries with tags shopping, personal",
        "remind me to water plants every 3 days",
        "deploy after tests pass in project mobile-app",
        "monthly report on the 15th",
        "meeting with client next Tuesday at 2pm #work #urgent",
        "low priority: organize desk when possible",
        "call dentist in 2 weeks",
        "urgent: fix critical bug asap",
        "every weekday: daily standup at 9am",
        "last day of each month: send invoices",
        "yearly: renew domain registration",
        "remind me at 2pm to call boss",
        "someday: learn Spanish"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i:2d}. Input: '{example}'")
        result = parser.parse(example)
        
        print(f"    Title: {result.title}")
        print(f"    Priority: {result.priority.value}")
        if result.due_date:
            print(f"    Due Date: {result.due_date.strftime('%Y-%m-%d %H:%M')}")
        if result.tags:
            print(f"    Tags: {', '.join(result.tags)}")
        if result.project:
            print(f"    Project: {result.project}")
        if result.is_recurring:
            print(f"    Recurring: {result.recurrence_pattern.type if result.recurrence_pattern else 'Yes'}")
        if result.reminders:
            print(f"    Reminders: {len(result.reminders)}")
        print(f"    Confidence: {result.confidence:.1%}")
        
        if result.warnings:
            print(f"    Warnings: {'; '.join(result.warnings)}")
        if result.errors:
            print(f"    Errors: {'; '.join(result.errors)}")


def demonstrate_database():
    """Demonstrate database operations."""
    print("\n🗄️  Database Operations Examples")
    print("=" * 50)
    
    # Create temporary database
    db_path = Path("/tmp/task_manager_demo.db")
    if db_path.exists():
        db_path.unlink()
    
    db = DatabaseManager(db_path)
    
    # Create some example tasks
    tasks = [
        Task(title="Buy groceries", priority=TaskPriority.MEDIUM, tags=["shopping", "personal"]),
        Task(title="Fix critical bug", priority=TaskPriority.URGENT, tags=["work", "urgent"]),
        Task(title="Call dentist", priority=TaskPriority.HIGH, tags=["health", "appointment"]),
        Task(title="Review code", priority=TaskPriority.MEDIUM, tags=["work", "development"]),
        Task(title="Exercise", priority=TaskPriority.LOW, tags=["health", "fitness"])
    ]
    
    print("Creating example tasks...")
    created_tasks = []
    for task in tasks:
        created_task = db.create_task(task)
        created_tasks.append(created_task)
        print(f"  ✅ Created: {created_task.title}")
    
    # List all tasks
    print(f"\nListing all tasks ({len(created_tasks)} total):")
    all_tasks = db.list_tasks()
    for task in all_tasks:
        status_icon = "✅" if task.status == TaskStatus.COMPLETED else "⏳"
        priority_value = task.priority.value if hasattr(task.priority, 'value') else str(task.priority)
        priority_icon = {"low": "🔵", "medium": "⚪", "high": "🟡", "urgent": "🔴"}[priority_value]
        print(f"  {status_icon} {priority_icon} {task.title}")
    
    # Complete a task
    print(f"\nCompleting task: {created_tasks[0].title}")
    created_tasks[0].complete()
    db.update_task(created_tasks[0])
    print("  ✅ Task completed")
    
    # Search tasks
    print(f"\nSearching for 'work' tasks:")
    work_tasks = db.search_tasks("work")
    for task in work_tasks:
        print(f"  • {task.title} (tags: {', '.join(task.tags)})")
    
    # Get statistics
    stats = db.get_statistics()
    print(f"\nDatabase Statistics:")
    print(f"  Total Tasks: {stats['total_tasks']}")
    print(f"  Completed: {stats['completed_tasks']}")
    print(f"  Pending: {stats['pending_tasks']}")
    print(f"  Completion Rate: {(stats['completed_tasks']/stats['total_tasks']*100):.1f}%")
    
    # Cleanup
    db_path.unlink()
    print(f"\n🧹 Cleaned up temporary database")


def demonstrate_configuration():
    """Demonstrate configuration system."""
    print("\n⚙️  Configuration Examples")
    print("=" * 50)
    
    # Create default config
    config = Config()
    
    print("Default Configuration:")
    print(f"  Database Path: {config.get_database_path()}")
    print(f"  Backup Directory: {config.get_backup_directory()}")
    print(f"  Log Directory: {config.get_log_directory()}")
    
    print(f"\nGeneral Settings:")
    print(f"  Default Priority: {config.general.default_priority}")
    print(f"  Default View: {config.general.default_view}")
    print(f"  Timezone: {config.general.timezone}")
    
    print(f"\nNotification Settings:")
    print(f"  Enabled: {config.notifications.enabled}")
    print(f"  Desktop: {config.notifications.desktop_notifications}")
    print(f"  Sound: {config.notifications.sound_notifications}")
    print(f"  Advance Warnings: {config.notifications.advance_warnings}")
    
    print(f"\nDisplay Settings:")
    print(f"  Theme: {config.display.theme}")
    print(f"  Show Icons: {config.display.show_icons}")
    print(f"  Compact Mode: {config.display.compact_mode}")
    
    print(f"\nParser Settings:")
    print(f"  Confidence Threshold: {config.parser.confidence_threshold}")
    print(f"  Auto Tag: {config.parser.auto_tag_enabled}")
    print(f"  Smart Scheduling: {config.parser.smart_scheduling}")


def demonstrate_features():
    """Demonstrate key features."""
    print("\n✨ Key Features Demonstration")
    print("=" * 50)
    
    print("🎯 Natural Language Processing:")
    print("  • Understands dates: 'tomorrow', 'next Tuesday', 'in 2 days'")
    print("  • Detects priorities: 'urgent', 'high priority', 'low priority'")
    print("  • Extracts tags: 'with tags work, urgent' or '#work #urgent'")
    print("  • Identifies projects: 'in project mobile-app'")
    print("  • Handles recurrence: 'every Monday', 'daily', 'monthly'")
    print("  • Creates reminders: 'remind me at 3pm'")
    
    print("\n📊 Task Management:")
    print("  • Create, read, update, delete tasks")
    print("  • Filter by status, priority, project, tags")
    print("  • Search full-text in titles and descriptions")
    print("  • Track completion rates and statistics")
    print("  • Handle task dependencies")
    
    print("\n🔄 Recurring Tasks:")
    print("  • Daily, weekly, monthly, yearly patterns")
    print("  • Specific days: 'every Monday', 'every weekday'")
    print("  • Custom intervals: 'every 3 days', 'every 2 weeks'")
    print("  • Skip weekends option")
    print("  • Automatic next occurrence creation")
    
    print("\n🔔 Notifications:")
    print("  • Desktop notifications (cross-platform)")
    print("  • Sound notifications")
    print("  • Email notifications (configurable)")
    print("  • Advance warnings: 1 hour, 1 day before due")
    print("  • Snooze functionality")
    print("  • Background daemon service")
    
    print("\n📈 Organization:")
    print("  • Projects for grouping related tasks")
    print("  • Hierarchical tags: 'work/meetings', 'personal/health'")
    print("  • Categories for broader grouping")
    print("  • Smart lists: Today, This Week, Overdue")
    print("  • Custom filters and saved searches")
    
    print("\n📊 Statistics & Reports:")
    print("  • Task completion rates")
    print("  • Productivity trends")
    print("  • Project progress tracking")
    print("  • Time-based analytics")
    print("  • Export to JSON, CSV, Markdown")
    
    print("\n🔧 Configuration:")
    print("  • YAML-based configuration")
    print("  • Customizable themes and colors")
    print("  • Notification preferences")
    print("  • Parser settings")
    print("  • Backup and restore")


def main():
    """Main demonstration function."""
    print("🚀 CLI Task Manager - Feature Demonstrations")
    print("=" * 60)
    
    try:
        demonstrate_parser()
        demonstrate_database()
        demonstrate_configuration()
        demonstrate_features()
        
        print("\n🎉 All demonstrations completed successfully!")
        print("\nTo get started with the CLI Task Manager:")
        print("  1. Install: pip install -e .")
        print("  2. Add a task: task add 'buy milk tomorrow'")
        print("  3. List tasks: task list")
        print("  4. Get help: task --help")
        
    except Exception as e:
        print(f"\n❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
