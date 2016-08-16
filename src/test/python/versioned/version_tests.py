import unittest

from versioned.version import Version

class VersionTestCase(unittest.TestCase):
  def setUp(self):
    self.nothing = None

  def tearDown(self):
    self.nothing = None

  def testIsVersionOnNonVersion(self):
    self.assertFalse(Version("FOO").isVersion())
    
  def testIsSnapshotOnSnapshotVersion(self):
    self.assertTrue(Version('1-SNAPSHOT').isSnapshot())

  def testIsSnapshotOnReleaseVersion(self):
    self.assertFalse(Version('1').isSnapshot())

  def testIsVersionWithFullVersionInfixAndSnapshot(self):
    self.assertTrue(Version('1.2.3-RC-4-SNAPSHOT').isVersion())

if __name__ == '__main__':
    unittest.main()
