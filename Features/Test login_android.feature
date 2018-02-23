# Created by sunny at 2018/1/29
@android
Feature: EFPv2 Login functionality validation
  In order to use the features offered by EFPv2
  As a parent
  I want to login to EFPv2 app



  @android
  Scenario Outline: Validate the login functionality through mobile UI
    Given I click login on EFP app login page
    When I input <Username> and <Password> with login android app
    Then I can go to Home page

    Examples: Login
      | Username   | Password     |
      | 777        | 12345        |