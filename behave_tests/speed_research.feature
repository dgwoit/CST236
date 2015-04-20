Feature: Research Speeds

    Scenario:
        Given some speed data
        When data is read in
        Then there are speed records

    Scenario:
        Given some speed records
        When a record is selected
        Then the record has speed

    Scenario:
        Given a speed computer
        When a drive size is set
        Then the drive size changed

    Scenario:
        Given a speed computer and speed data
        When a drive size and cities are set
        Then the drive speed is calculated

    Scenario:
        Given a speed computer and speed data
        When a drive size and cities are set
        Then the speed difference is calculated

     Scenario:
        Given preset ground speeds
        When a method of physical transport is selected
        Then there is a speed value

     Scenario:
        Given speed data
        When a record is added
        Then the number of records increased

    Scenario:
        Given speed data
        When a record is added
        Then it is streamed out