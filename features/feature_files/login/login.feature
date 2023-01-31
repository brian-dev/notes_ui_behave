Feature: Login Scenarios

  Background: Navigate to login URL
    Given the user is on the "login" page

  @logout
  Scenario: User is directed to the Products URL after login
      When the user logs in as the "standard_user"
      Then the user is directed to the "products" url

  Scenario Outline: Error is raised with invalid credentials
      When the user logs in as the "<user type>"
      Then the user is is given a "<error type>" error
    Examples:
      |user type        |error type        |
      |locked_user      | locked_out       |
      |empty_user       | empty_login      |
      |password_only    | empty_username   |
      |username_only    | empty_password   |
      |invalid_user     | invalid_username |
      |invalid_password | invalid_password |

    Scenario Outline: User can clear error
      When the user logs in as the "<user type>"
      Then the user can clear the "<error type>" error
    Examples:
      |user type        |error type        |
      |locked_user      | locked_out       |
      |empty_user       | empty_login      |
      |password_only    | empty_username   |
      |username_only    | empty_password   |
      |invalid_user     | invalid_username |
      |invalid_password | invalid_password |