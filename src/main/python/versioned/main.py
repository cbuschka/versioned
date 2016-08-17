#!/usr/bin/python
# -*- coding: UTF-8 -*-

from version import VersionBuilder
import sys

if __name__ == '__main__':
  versionBuilder = VersionBuilder()

  if len(sys.argv) == 1:
    print sys.argv[0] + " isVersion|isSnapshot|rmSnapshot|nextVersion|nextSnapshot <value>"
    sys.exit(1)
  elif len(sys.argv) > 1 and sys.argv[1] == 'isVersion':
    print 'true' if versionBuilder.build(sys.argv[2]).isVersion() else 'false'
  elif len(sys.argv) > 1 and sys.argv[1] == 'isSnapshot':
    print 'true' if versionBuilder.build(sys.argv[2]).isSnapshot() else 'false'
  elif len(sys.argv) > 1 and sys.argv[1] == 'removeSnapshot':
    print versionBuilder.build(sys.argv[2]).removeSnapshot().str()
  elif len(sys.argv) > 1 and sys.argv[1] == 'nextRelease':
    print versionBuilder.build(sys.argv[2]).nextRelease().str()
  elif len(sys.argv) > 1 and sys.argv[1] == 'nextSnapshot':
    print versionBuilder.build(sys.argv[2]).nextSnapshot().str()
  else:
    print sys.argv[0] + ": unknown command '{}'".format(sys.argv[1]);
    sys.exit(1)

sys.exit(0)
