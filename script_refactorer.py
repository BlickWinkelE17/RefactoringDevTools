#!/usr/bin/env python
import sys
import logging
import pprint

import os
import string_utils


class Settings:
  def __init__(self, target_file, place_of_interest_regexp, replacements_list):
    self.target_file = target_file
    self.place_of_interest_regexp = place_of_interest_regexp
    self.replacements = {}
    self.replacements_key_order = []
    for replacement in replacements_list:
      split = replacement.split('=')
      if len(split) != 2:
        raise ValueError("Bad replacement: " + replacement)
      self.replacements[split[0]] = split[1]
      self.replacements_key_order.append(split[0])


def process_string(string, settings):
  places = string_utils.get_refactoring_place(string, settings.place_of_interest_regexp)
  result = string
  for place in places:
    refactored = string_utils.get_refactored(place, settings)
    result = result.replace(place, refactored)
  return result


def process_file(target_file, settings):
  if os.path.isdir(target_file):
    logging.info("%s is a directory, processing content recursively", target_file)
    files = os.listdir(target_file)
    for file in files:
      process_file(os.path.join(target_file,file), settings)
  else:
    logging.info("Processing %s", target_file)
    try:
      with open(target_file, "r+") as f:
        old = f.read()
        new = process_string(old, settings)
        f.seek(0)
        f.write(new)
        f.truncate()
    except IOError as e:
      logging.error("Error with %s %s", target_file, str(e))



def main():
  if len(sys.argv) <= 2:
    print "Usage: %s place_of_interest_regexp replace1_regexp=replacement1 [replace2_regexp=replacement2 ...] filename/dir" % sys.argv[0]
    sys.exit(1)
  logging.getLogger().setLevel(logging.DEBUG)
  settings = Settings(sys.argv[-1], sys.argv[1], sys.argv[2:-1])
  logging.info("Settings decode:")
  logging.info("Src file: %s", settings.target_file)
  logging.info("place_of_interest_regexp: %s", settings.place_of_interest_regexp)
  logging.info("Replacements: %s", pprint.pformat(settings.replacements))


  process_file(settings.target_file, settings)



if __name__ == "__main__":
  main()