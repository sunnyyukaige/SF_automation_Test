Feature: Admin can login SF system


  Scenario: Admin can goto BU
    Given I am a admin
    Then I can switch-to-lightning module
    When I goto learning module
    Then I can edit contentmap

