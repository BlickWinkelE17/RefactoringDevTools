import re



def replace_with_strict_case(string, str_to_find, replacement_str):
  return re.sub(str_to_find, replacement_str, string, 1)

def get_refactored(str, settings):
  result = str
  for key in settings.replacements_key_order:
    # Do replacements that make sense
    str_to_find = key
    replacement_str = settings.replacements[key]
    result = re.sub(str_to_find, replacement_str, result)
  return result


def get_refactoring_place(str, str_to_find):
  pattern = re.compile(str_to_find)
  return pattern.findall(str)
