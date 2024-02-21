**1. Create a Django Project:**

```bash
django-admin startproject smartnotes .
```

* This command creates a new Django project named `smartnotes` in the current directory ('.').

**2. Start the Development Server:**

```bash
python3 manage.py runserver
```

* This command starts the Django development server, allowing you to test your application locally.

**3. Create a Django App:**

```bash
python3 manage.py startapp home
```

* This command creates a new Django app named `home` within the `smartnotes` project. Apps encapsulate smaller, reusable components of your web application.

**4. Migrate the Database:**

```bash
python3 manage.py migrate
```

* This command applies any pending database schema changes based on your models. Ensure you've already configured your database settings in `settings.py`.

**5. Create a Superuser:**

```bash
python3 manage.py createsuperuser
```

* This command creates a superuser account with administrative privileges, allowing you to manage users, create content, and access sensitive areas of your site.

**6. Create Migration Files (if necessary):**

```bash
python3 manage.py makemigrations
```

* This command generates migration files (if needed) to track future changes in your models and database schema. This step isn't always necessary if you haven't made any model modifications.

**7. Open the Django Shell and Explore the Database**

```bash
python3 manage.py shell
```

This command opens an interactive Django shell, providing a Python environment where you can directly interact with your application's models and database.

**Exploring the Database:**

While in the shell, you can leverage the Django ORM (Object-Relational Mapper) to query and manipulate data. Here's an example:

```python
from notes.models import Note  # Corrected import name

# Fetch a specific note using its primary key (pk)
note = Note.objects.get(pk=1)

# Print the note's title and content
print(f"Title: {note.title}")
print(f"Text: {note.text}")

# Display all notes
all_notes = Notes.objects.all()
print("\nAll notes:")
for note in all_notes:
    print(f"- {note.title}")

# Create a new note
new_note = Notes.objects.create(title="Test shell", text="Test content")
print(f"\nCreated new note: {new_note.title}")

# Filter notes based on title
filtered_notes = Notes.objects.filter(title__startswith="Test")
print("\nNotes with title starting with 'Test':")
for note in filtered_notes:
    print(f"- {note.title}")

# Filter notes by excluding
filtered_notes = Notes.objects.exclude(text__icontains="Nose")
print("\nNotes without 'Nose' in content:")
for note in filtered_notes:
    print(f"- {note.title}")

# Combine filters
Notes.objects.filter(title__icontains='Test').exclude(text_icontains='Nose')
```

**Manage user**
```python
from django.contrib.auth.models import User
# Get the first user
user = User.objects.get(pk=1)
# Count user's notes
user.notes.count()
```