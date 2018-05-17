Feature: Admin can login SF system

  Scenario: Admin can login SF system
    Given I am a admin
    When I go to classical model
    Then I can go to home page

  Scenario Outline: Admin can login SF system
    Given I am a admin
    When I go to classical model
    Then I can go to home page and <tab> tab
    Examples:
      | tab                   |
      | Foundation            |

  Scenario: Admin can goto BU
    Given I am a admin
    When I go to classical model
    Then I can go to BU page
    And I can search and view "China Franchise" BU
    Then I can view the "China Franchise" BU
    And  I can edit the "China Franchise" BU

