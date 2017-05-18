#!/usr/bin/env python

from storm_control.test.hal.standardHalTest import halTest


def test_hal_tcp15():

    halTest(config_xml = "none_tcp_config.xml",
            class_name = "TakeMovie7",
            test_module = "storm_control.test.hal.tcp_tests")


if (__name__ == "__main__"):
    test_hal_tcp15()