
Feature: Covered in Class includes viewing CIC page
    # Please enter the feature description here
  @skip
  Scenario: Teacher can view course content in CIC page
    Given I am a teacher
    And There is a group with course map
    When I go to CIC page
    Then I can view the course content in CIC page
  @skip
  Scenario Outline: Teacher can add CIC items for CIC page
    Given I am a teacher
    And There is a group with course map
    When I go to CIC page
    And I can add <content> CIC
    Then I can check this CIC <content>
    Examples:
      | content  |
      | All      |
      | Add More |
      | Default  |

  @skip
  Scenario Outline: Teacher can not publish without CIC items checked for CIC page
    Given I am a teacher
    And There is a group with course map
    When I go to CIC page
    And publish the CIC
    Then I will get error alert <content>
    Examples:
    | content |
    | abc     |
  @skip
  Scenario Outline: Teacher can export CIC page with localization
    Given I am a teacher
    When I go to CIC page
    And I publish CIC
    Then I can export the CIC with <language>
    Examples:
      | language |
      | CN       |
      | EN       |
