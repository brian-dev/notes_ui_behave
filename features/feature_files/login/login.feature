Feature: Login Scenarios

  Background: Navigate to login URL
    Given the user is on the login page

  @manual_logout
  Scenario: User is directed to the Products URL after login
      Given a user has been created
      When the user logs in as the "active_user" user
      Then the user is directed to the "home" url

  Scenario Outline: Error is raised with invalid credentials
      When the user logs in as the "<user type>" user
      Then the user is is given a "<error type>" error
    Examples:
      |user type        |error type            |
      |empty_email      | email_required       |
      |incomplete_email | invalid_address      |
