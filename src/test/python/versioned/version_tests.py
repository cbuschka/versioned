import unittest

from versioned.version import VersionBuilder

class VersionTestCase(unittest.TestCase):
  def setUp(self):
    self.versionBuilder = VersionBuilder()

  def testIsVersionOnNonVersion(self):
    self.assertFalse(self.versionBuilder.build("FOO").isVersion())
    
  def testIsSnapshotOnSnapshotVersion(self):
    self.assertTrue(self.versionBuilder.build('1-SNAPSHOT').isSnapshot())

  def testIsSnapshotOnReleaseVersion(self):
    self.assertFalse(self.versionBuilder.build('1').isSnapshot())

  def testIsVersionWithFullVersionInfixAndSnapshot(self):
    self.assertTrue(self.versionBuilder.build('1.2.3-RC-4-SNAPSHOT').isVersion())

if __name__ == '__main__':
    unittest.main()
