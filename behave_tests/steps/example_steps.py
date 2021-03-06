from behave import given, when, then
import sys
import os
import StringIO

sys.path.insert(0, os.path.abspath(".."))

from source.SpeedResearcher import *

@given('some speed data')
def step_impl(context):
    context.string_data = "Portland, OR|Miami, FL|4353|12345\n"
    context.string_data += "Portland, OR|Denver, CO|1997|67890\n"
    context.speed_data = SpeedData()

@when('data is read in')
def step_impl(context):
    stream = StringIO.StringIO(context.string_data)
    context.speed_data.read(stream)

@then('there are speed records')
def step_impl(context):
    assert len(context.speed_data.data) > 0

@given('some speed records')
def step_impl(context):
    context.string_data = "Portland, OR|Miami, FL|4353|12345\n"
    context.string_data += "Portland, OR|Denver, CO|1997|67890\n"
    stream = StringIO.StringIO(context.string_data)
    context.speed_data = SpeedData()
    context.speed_data.read(stream)

@when('a record is selected')
def step_impl(context):
    context.record = context.speed_data.find_record("Portland, OR", "Denver, CO")

@then('the record has speed')
def step_impl(context):
    assert context.record.network_speed > 0

@given('a speed computer')
def step_impl(context):
    context.speed_computer = SpeedComputer()

@when('a drive size is set')
def step_impl(context):
    context.speed_computer.drive_size = 1024

@then('the drive size changed')
def step_impl(context):
    assert context.speed_computer.drive_size <> 1

@given('a speed computer and speed data')
def step_impl(context):
    context.string_data = "Portland, OR|Miami, FL|4353|12345\n"
    context.string_data += "Denver, CO|Miami, FL|3322|5\n"
    context.string_data += "Portland, OR|Denver, CO|1997|67890\n"
    stream = StringIO.StringIO(context.string_data)
    context.speed_data = SpeedData()
    context.speed_data.read(stream)
    context.speed_computer = SpeedComputer()

@when('a drive size and cities are set')
def step_impl(context):
    context.speed_computer.drive_size = 1024
    context.speed_computer.ground_speed = 100
    context.speed_computer.speed_datum = context.speed_data.data[0]

@then('the drive speed is calculated')
def step_impl(context):
    assert context.speed_computer.calculate_drive_transport_time() > 0

@then('the speed difference is calculated')
def step_impl(context):
    assert context.speed_computer.calculate_transport_time_difference() > 0

@given('preset ground speeds')
def step_impl(context):
    preset_data = {"Porsche":1,"Bus":2,"Cement Truck":3,"laden swallow":4}
    context.presets = SpeedComputerPresets()
    context.presets.set_ground_speeds(preset_data)

@when('a method of physical transport is selected')
def step_impl(context):
    context.value = context.presets.get_ground_speed("laden swallow")

@then('there is a speed value')
def step_impl(context):
    assert context.value > 0

@given('speed data')
def step_impl(context):
    context.speed_data = SpeedData()

@when('a record is added')
def step_impl(context):
    context.speed_data.add('Denver, CO', 'Miami, FL', 3322, 5)

@then('the number of records increased')
def step_impl(context):
    assert len(context.speed_data.data) > 0

@then('it is streamed out')
def step_impl(context):
    stream = StringIO.StringIO()
    context.speed_data.write(stream)
    assert len(stream.getvalue()) > 0

@when('a drive size and a list of cities are set')
def step_impl(context):
    context.speed_computer.drive_size = 512
    context.speed_computer.ground_speed = 100
    context.route = ['Portland, OR', 'Denver, CO', 'Miami, FL']
    context.speed_computer.data = context.speed_data

@then('the drive speed is calculated from the route')
def step_impl(context):
    assert context.speed_computer.calculate_drive_transport_time_from_route(context.route)

@given('presets')
def step_impl(context):
    context.presets = SpeedComputerPresets()

@when('the start city is set')
def step_impl(context):
    context.presets.start_city = "Wilsonville, OR"

@then('the start city has a value')
def step_impl(context):
    assert len(context.presets.start_city) > 0

@when('a network latency is set')
def step_impl(context):
    context.speed_computer.drive_size = 512
    context.route = ['Portland, OR', 'Denver, CO', 'Miami, FL']
    context.speed_computer.data = context.speed_data
    context.network_latency = 1

@then('the network latency is in the calculation')
def step_impl(context):
    time_without_latency = context.speed_computer.calculate_network_transport_time_from_route(context.route)
    context.speed_computer.network_latency = 1
    time_with_latency = context.speed_computer.calculate_network_transport_time_from_route(context.route)
    assert time_with_latency > time_without_latency

@when('a hard drive speed is set')
def step_impl(context):
    context.speed_computer.drive_size = 512
    context.speed_computer.ground_speed = 100
    context.route = ['Portland, OR', 'Denver, CO', 'Miami, FL']
    context.speed_computer.data = context.speed_data

@then('the hard drive copy time is in the calculation')
def step_impl(context):
    time_without_hard_drive_speed = context.speed_computer.calculate_drive_transport_time_from_route(context.route)
    context.speed_computer.hard_drive_speed = 25
    time_with_hard_drive_speed = context.speed_computer.calculate_drive_transport_time_from_route(context.route)
    assert time_with_hard_drive_speed > time_without_hard_drive_speed