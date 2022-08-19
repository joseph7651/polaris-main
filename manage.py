#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# touched on 2025-05-27T15:29:02.329295Z
# touched on 2025-08-14T21:16:34.770116Z
# touched on 2025-08-14T21:16:47.630727Z
# touched on 2025-08-14T21:17:28.541027Z
# touched on 2025-08-14T21:17:47.436842Z
# touched on 2025-08-14T21:17:55.705560Z
# touched on 2025-08-14T21:18:18.398164Z
# touched on 2025-08-14T21:18:24.754112Z