Feature: Login Scenarios

  Background: Navigate to login URL
    Given the user is on the "login" page

  Scenario: User is directed to the Products URL after login
      When the user logs in as the "standard_user"
      Then the user is directed to the "products" url