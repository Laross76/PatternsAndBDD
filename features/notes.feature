Feature: Note Management API

  Scenario: Successfully create a note with valid data
    Given I have a valid note payload
    When I send a POST request to create the note
    Then the response status code should be 201
    And the response should contain the correct title and content

  Scenario: Fail to create note with invalid data
    Given I have an invalid note payload
    When I send a POST request to create the note
    Then the response status code should be 422

  Scenario: Get all notes when no notes exist
    Given there are no notes in the system
    When I send a GET request to list all notes
    Then the response status code should be 200
    And the response should be an empty list

  Scenario: Get all notes when notes exist
    Given there are notes in the system
    When I send a GET request to list all notes
    Then the response status code should be 200
    And the response should contain the created notes

  Scenario: Get note by valid ID
    Given I have created a note
    When I send a GET request to get the note by ID
    Then the response status code should be 200
    And the response should contain the correct note data

  Scenario: Get note by invalid ID
    Given I have an invalid note ID
    When I send a GET request to get the note by ID
    Then the response status code should be 404

  Scenario: Update note with valid ID
    Given I have created a note
    When I send a PUT request to update the note
    Then the response status code should be 200
    And the response should contain the updated data

  Scenario: Update note with invalid ID
    Given I have an invalid note ID
    When I send a PUT request to update the note
    Then the response status code should be 404

  Scenario: Delete note with valid ID
    Given I have created a note
    When I send a DELETE request to delete the note
    Then the response status code should be 200
    And the note should be successfully deleted

  Scenario: Delete note with invalid ID
    Given I have an invalid note ID
    When I send a DELETE request to delete the note
    Then the response status code should be 404
