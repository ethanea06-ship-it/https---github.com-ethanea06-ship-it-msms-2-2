#2.1 The core persistence engine
def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database."""
    global next_teacher_id
    new_teacher = Teacher(next_teacher_id, name, speciality)
    teacher_db.append(new_teacher)
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' added successfully.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    for student in student_db:
        instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {instruments}")

def list_teachers():
    """Prints all teachers in the database."""
    print("\n--- Teacher List ---")
    if not teacher_db:
        print("No teachers in the system.")
        return
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{term}' ---")
    results = []
    term = term.lower()  # Make search case-insensitive
    for student in student_db:
        if term in student.name.lower():
            results.append(student)
    
    if not results:
        print("No matching students found.")
    else:
        for student in results:
            instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
            print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {instruments}")

def find_teachers(term):
    """Finds teachers by name or speciality."""
    print(f"\n--- Finding Teachers matching '{term}' ---")
    results = []
    term = term.lower()  # Make search case-insensitive
    for teacher in teacher_db:
        if (term in teacher.name.lower()) or (term in teacher.speciality.lower()):
            results.append(teacher)
    
    if not results:
        print("No matching teachers found.")
    else:
        for teacher in results:
            print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")


#2.2 Refactoring and Expanding CRUD Operations
# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    teacher_id = app_data['next_teacher_id']
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    app_data['teachers'].append(new_teacher)
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")

def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    original_length = len(app_data['teachers'])
    app_data['teachers'] = [t for t in app_data['teachers'] if t['id'] != teacher_id]
    if len(app_data['teachers']) < original_length:
        print(f"Teacher {teacher_id} removed.")
    else:
        print(f"Error: Teacher with ID {teacher_id} not found.")

def add_student(name, email):
    """Adds a student dictionary to the data store."""
    student_id = app_data['next_student_id']
    new_student = {"id": student_id, "name": name, "email": email}
    app_data['students'].append(new_student)
    app_data['next_student_id'] += 1
    print(f"Core: Student '{name}' added.")

def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields."""
    for student in app_data['students']:
        if student['id'] == student_id:
            student.update(fields)
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")

def remove_student(student_id):
    """Removes a student from the data store."""
    original_length = len(app_data['students'])
    app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
    if len(app_data['students']) < original_length:
        print(f"Student {student_id} removed.")
    else:
        print(f"Error: Student with ID {student_id} not found.")