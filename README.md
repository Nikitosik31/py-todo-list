# Todo List

A simple Django-based todo list application. Tasks can be created, updated,
completed and deleted, and organized with tags.

## Features

- **Tasks** with content, creation datetime, an optional deadline and a
  done/not done status.
- **Tags** to categorize tasks. A task can have multiple tags and a tag can
  belong to multiple tasks (many-to-many relationship).
- Task list ordered from not done to done, and from newest to oldest.
- One-click **Complete / Undo** button to toggle a task's status.
- Full **CRUD** for both tasks and tags.
- Sidebar navigation available on all pages.
- Forms styled with crispy forms.

## Requirements

- Python 3.13+
- See [requirements.txt](requirements.txt) for the full list of dependencies.

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd py-todo-list

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/.

## Pages

- `/` — home page with the todo list.
- `/tags/` — list of tags.
