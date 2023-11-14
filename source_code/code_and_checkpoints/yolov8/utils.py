import io
import json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
def write_json_file(data, filename):
    with io.open(filename, "w", encoding="utf8") as outfile:
        str_ = json.dumps(
            data,
            indent=4, sort_keys=True,
            separators=(",", ": "),
            ensure_ascii=True,
        )
        outfile.write(to_unicode(str_))
