from behave import given, when, then
from pages.note_page import NotePage
from factories.note_factory import NoteFactory, NoteData

note_page = NotePage()
note_factory = NoteFactory()
created_notes = []

@given('I have a valid note payload')
def step_valid_note_payload(context):
    context.note_data = note_factory.create_valid_note()

@given('I have an invalid note payload')
def step_invalid_note_payload(context):
    context.note_data = note_factory.create_invalid_note()

@given('there are no notes in the system')
def step_clear_notes(context):
    note_page.clear_notes()

@given('there are notes in the system')
def step_create_notes(context):
    note_page.clear_notes()
    for i in range(3):
        note_data = note_factory.create_valid_note()
        response = note_page.create_note(note_data.__dict__)
        created_notes.append(response.json())

@given('I have created a note')
def step_create_single_note(context):
    note_page.clear_notes()
    context.note_data = note_factory.create_valid_note()
    response = note_page.create_note(context.note_data.__dict__)
    context.created_note = response.json()

@given('I have an invalid note ID')
def step_invalid_note_id(context):
    context.note_id = 9999  # Non-existent ID

@when('I send a POST request to create the note')
def step_send_create_request(context):
    context.response = note_page.create_note(context.note_data.__dict__)

@when('I send a GET request to list all notes')
def step_send_get_all_request(context):
    context.response = note_page.get_all_notes()

@when('I send a GET request to get the note by ID')
def step_send_get_by_id_request(context):
    if hasattr(context, 'created_note'):
        context.note_id = context.created_note['id']
    context.response = note_page.get_note_by_id(context.note_id)

@when('I send a PUT request to update the note')
def step_send_update_request(context):
    updated_data = note_factory.create_valid_note()
    context.updated_data = updated_data
    if hasattr(context, 'created_note'):
        context.note_id = context.created_note['id']
    context.response = note_page.update_note(context.note_id, updated_data.__dict__)

@when('I send a DELETE request to delete the note')
def step_send_delete_request(context):
    if hasattr(context, 'created_note'):
        context.note_id = context.created_note['id']
    context.response = note_page.delete_note(context.note_id)

@then('the response status code should be {status_code:d}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain the correct title and content')
def step_check_note_content(context):
    response_data = context.response.json()
    assert response_data['title'] == context.note_data.title
    assert response_data['content'] == context.note_data.content

@then('the response should be an empty list')
def step_check_empty_list(context):
    assert context.response.json() == []

@then('the response should contain the created notes')
def step_check_notes_list(context):
    notes = context.response.json()
    assert len(notes) == 3

@then('the response should contain the correct note data')
def step_check_specific_note(context):
    response_data = context.response.json()
    assert response_data['id'] == context.note_id
    assert 'title' in response_data
    assert 'content' in response_data

@then('the response should contain the updated data')
def step_check_updated_note(context):
    response_data = context.response.json()
    assert response_data['title'] == context.updated_data.title
    assert response_data['content'] == context.updated_data.content

@then('the note should be successfully deleted')
def step_check_note_deleted(context):
    # Verify the note no longer exists
    check_response = note_page.get_note_by_id(context.note_id)
    assert check_response.status_code == 404
