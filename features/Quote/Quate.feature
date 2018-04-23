Feature: Admin can login SF system


  Scenario Outline: Admin can quote sale
    Given I am a admin
    When I go to classical model
    Then I can go to home page and <tab> tab
    When I create opp
    And I goto opp and quote
    And I can finish a quote
    And Check and delete quote
    Examples:
      | tab   |
      | Sales |

