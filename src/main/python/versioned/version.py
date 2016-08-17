#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

class VersionBuilder:
  def build(self, version):
    return MvnVersion(version)

class MvnVersion:
  def __init__(self, version):
    self.version_pattern = re.compile('^\d+([\-\.]\w+)*$')
    self.version_split_pattern = re.compile('([\.\-]+)')
    self.int_pattern = re.compile('^\d+$')
    self.version = version

  def isSnapshot(self):
    return self.isVersion() and self.version.endswith('-SNAPSHOT')

  def isVersion(self):
    return self.version_pattern.match(self.version) is not None

  def isRelease(self):
    return self.isVersion() and not self.isSnapshot()

  def removeSnapshot(self):
    return Version(self.version[0:-9]) if self.isSnapshot() else self

  def addSnapshot(self):
    return self if self.isSnapshot() else Version(self.version+'-SNAPSHOT')

  def str(self):
    return self.version

  def nextSnapshot(self):
    return self.nextRelease().addSnapshot()

  def nextRelease(self):
    parts = self.version_split_pattern.split(self.version)
    for index in range(0,len(parts)):
      part = parts[len(parts)-index-1]
      if self.int_pattern.match(part) is not None:
        parts[len(parts)-index-1] = int(part)+1
        break

    return Version("".join([str(part) for part in parts])).removeSnapshot()
