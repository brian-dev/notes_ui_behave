Feature: All Products Scenarios

  Background: Navigate to login URL
    Given the user is on the "login" page

  Scenario Outline: All product titles are listed on the page
      When the user logs in as the "standard_user"
      Then all "<product>" titles are listed on the page
    Examples:
    |product              |
    |backpack             |
    |bike_light           |
    |bolt_shirt           |
    |fleece_jacket        |
    |onesie               |
    |all_the_things_shirt |


  Scenario Outline: All product descriptions are listed on the page
      When the user logs in as the "standard_user"
      Then all "<product>" descriptions are listed on the page
    Examples:
    |product              |
    |backpack             |
    |bike_light           |
    |bolt_shirt           |
    |fleece_jacket        |
    |onesie               |
    |all_the_things_shirt |


  Scenario Outline: All product prices are listed on the page
      When the user logs in as the "standard_user"
      Then all "<product>" prices are listed on the page
    Examples:
    |product              |
    |backpack             |
    |bike_light           |
    |bolt_shirt           |
    |fleece_jacket        |
    |onesie               |
    |all_the_things_shirt |

  Scenario Outline: All product add to cart buttons are listed on the page
      When the user logs in as the "standard_user"
      Then all "<product>" add to cart buttons are listed on the page
    Examples:
    |product              |
    |backpack             |
    |bike_light           |
    |bolt_shirt           |
    |fleece_jacket        |
    |onesie               |
    |all_the_things_shirt |
    