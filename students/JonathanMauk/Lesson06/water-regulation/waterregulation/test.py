"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class.
    """

    def test_decider(self):
        """Method for DeciderTests. Should test every decider scenario."""

        di = Decider(100, 0.05)

        scenario1
        scenario2
        scenario3
        scenario4
        scenario5
        scenario6
        scenario7

    # def test_dummy(self):
    #     """
    #     Just some example syntax that you might use
    #     """
    #
    #     pump = Pump('127.0.0.1', 8000)
    #     pump.set_state = MagicMock(return_value=True)
    #
    #     self.fail("Remove this test.")


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class.
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    pass
