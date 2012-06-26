"""
Unit tests for the stem.exit_policy.ExitPolicy parsing and class.
"""

import unittest
import stem.exit_policy
import stem.util.system

import test.mocking as mocking

class TestExitPolicy(unittest.TestCase):
  def tearDown(self):
    pass
  
  def test_parsing(self):
    """
    Tests parsing by the ExitPolicy class constructor.
    """
    
    exit_policies = stem.exit_policy.ExitPolicy()
    exit_policies.add("accept *:80")
    exit_policies.add("accept *:443")
    exit_policies.add("reject *:*")
    self.assertEqual(str(exit_policies), "accept *:80, accept *:443, reject *:*")
    
    exit_policies = stem.exit_policy.ExitPolicy()
    
    # check ip address
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept 256.255.255.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept -10.255.255.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept 255.-10.255.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept 255.255.-10.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept -255.255.255.-10:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept a.b.c.d:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept 255.255.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept -255.255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept 255:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept -:80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept :80")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept ...:80")
    
    # check input string
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "foo 255.255.255.255:80")
    
    # check ports
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:0001")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:0")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:-1")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:+1")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:+1-1")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:a")
    self.assertRaises(stem.exit_policy.ExitPolicyError, exit_policies.add, "accept *:70000")
    
  def test_check(self):
    """
    Tests if exiting to this ip is allowed.
    """
    pass
