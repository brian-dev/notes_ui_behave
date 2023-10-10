Feature: Home Page Scenarios

  Background: Create a new user for testing
    Given the user is on the home page

Scenario Outline: UI Elements are present and displayed
      Then the <name> is visible on page <locator>
    Examples:
      |name                  | locator                       |
      |Home Page Title       | home_title_class_loc          |
      |Practice Breadcrumb   | practice_breadcrumb_css_loc   |
      |Home Breadcrumb       | home_breadcrumb_css_loc       |
      |Login Button          | login_btn_css_loc             |
      |Create Account Button | create_acct_btn_css_loc       |
      |Google Account Link   | google_acct_btn_css_loc       |
      |Forgot Password Link  | forgot_pass_btn_css_loc       |

  Scenario: User is directed to login view when login button is clicked
    When the user clicks on the login button
    Then the user is directed to the "login" url

  Scenario: User is directed to create account view when login button is clicked
    When the user clicks on the create_account button
    Then the user is directed to the "register" url