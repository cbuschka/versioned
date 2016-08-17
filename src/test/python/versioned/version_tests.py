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
  
  def testNextReleaseOfSnapshotRemovesSnapshot(self):
    self.assertEquals('1.2.3', self.versionBuilder.build('1.2.3-SNAPSHOT').nextRelease().str())
  
  def testNextReleaseOfReleaseIncreasesPatch(self):
    self.assertEquals('1.2.4', self.versionBuilder.build('1.2.3').nextRelease().str())
  
  def testNextSnapshotOfReleaseIncreasesPatchAndAddsSnapshot(self):
    self.assertEquals('1.2.4-SNAPSHOT', self.versionBuilder.build('1.2.3').nextSnapshot().str())
  
  def testNextSnapshotOfSnapshotIncreasesPatchAndKeepsSnapshot(self):
    self.assertEquals('1.2.4-SNAPSHOT', self.versionBuilder.build('1.2.3-SNAPSHOT').nextSnapshot().str())


if __name__ == '__main__':
    unittest.main()
