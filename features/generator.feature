Feature: Generator
  As a developer
  I want a tool that will setup behave bdd in my python projects
  So that I can write BDD tests faster.

  Scenario: User enters "behave-generator" command into terminal
    Given I am in an empty directory
    When I type the command "behave-generator"
    Then I should have a features directory
    And I should have a features/steps directory
    And I should have a features/environment.py file

  Scenario: User enters behave-generator with browser command into terminal
    Given I am in an empty directory
    When I type the command "behave-generator --browser=remote"
    Then I should have a features directory
    And I should have a features/steps directory
    And I should have a features/browser.py file
    And I should have a features/environment.py file

  Scenario: User enters behave-generator with unsupported browser
    Given I am in an empty directory
    When I run behave-generator --browser=foo
    Then it throws an exception with message "Invalid Browser Name"
