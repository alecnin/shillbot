import unittest
import codecs
import os

from workers.basic_worker import BasicUserParseWorker
from mothership.base import MothershipServer
class TestAssignment5(unittest.TestCase):
    def test_worker_connection(self):
            """
            Purpose: Test regular running of worker
            Expectation: startup system, hit the reddit user and parse the data, send to mothership

            :precondition: Mothership server running
            :return:
            """
            server = MothershipServer()
            server.run()
            try:
                worker = BasicUserParseWorker("https://www.reddit.com/user/alecnin")
                worker.send_to_mother()
            # connect to mother, so should not raise exception, should run everything else
            except ConnectionRefusedError:
                self.fail('connection failure')

    def test_worker_originalTarget(self):
        worker = BasicUserParseWorker("https://www.reddit.com/user/alecnin")
        self.assertEqual(worker.original_target, "https://www.reddit.com/user/alecnin")

    def test_worker_ss(self):
         worker = BasicUserParseWorker("https://www.reddit.com/user/thisuserdoesntexistyet")
         self.assertEqual(worker.results, None)
