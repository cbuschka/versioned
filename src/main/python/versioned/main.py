#!/usr/bin/python
# -*- coding: UTF-8 -*-

from version import VersionBuilder
import sys
from getopt import gnu_getopt

if __name__ == '__main__':
  versionBuilder = VersionBuilder()

  command = ''
  (opts, commandArgs) = gnu_getopt(sys.argv[1:], "f:c:", [])
  for (optName, optValue) in opts:
    if optName == '-f':
      versionBuilder.setFormat(optValue)
    if optName == '-c':
      command = optValue

  if len(commandArgs) > 0 and command == 'isVersion':
    print 'true' if versionBuilder.build(commandArgs[0]).isVersion() else 'false'
  elif len(commandArgs) > 0 and command == 'isRelease':
    print 'true' if versionBuilder.build(commandArgs[0]).isRelease() else 'false'
  elif len(commandArgs) > 0 and command == 'isSnapshot':
    print 'true' if versionBuilder.build(commandArgs[0]).isSnapshot() else 'false'
  elif len(commandArgs) > 0 and command == 'nextRelease':
    print versionBuilder.build(commandArgs[0]).nextRelease().str()
  elif len(commandArgs) > 0 and command == 'nextSnapshot':
    print versionBuilder.build(commandArgs[0]).nextSnapshot().str()
  else:
    print sys.argv[0] + ": unknown command '{}'".format(command);
    sys.exit(1)

sys.exit(0)
