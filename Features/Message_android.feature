# Created by sunny at 2018/1/29
@android
Feature: EFPv2 parents can chat in group




  @android
  Scenario Outline: Parents can goto message tab and chat in group
    Given I click login on EFP app login page
    #When I input <Username> and <Password> with login
    And I can go to Message page
    Then I can chat in group
    #Then I logout

    Examples: Login
      | Username   | Password     |
      | 777        | 12345        |