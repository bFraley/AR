# Copyright Brett Fraley 2017

import os

# AR settings file, not PY settings.py
class Settings:
    def __init__(self, settings_file):
        self.settings_file = settings_file

# get.utility_methods
class Get:
    def __init__(self):
        self = self

    def py_filename(self, name):
        print(name)
        return name


# System Status Monitoring and Reporting Class Definitions
# Monitors system data and environment information
class SystemReport
    def__init__(self)
        pass



# AR class containing instances of all runtime utility classes defined above
class AR:
    def __init__(self):
        self.get = Get()
        self.settings = Settings()


