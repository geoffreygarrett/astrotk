import json
import os

AE4878_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(AE4878_path,'constants.json')) as handle:
    course_constants = json.loads(handle.read())
