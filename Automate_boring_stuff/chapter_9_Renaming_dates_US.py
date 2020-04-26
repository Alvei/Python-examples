"""chapter_9_Renaming_dates_US.py"""
import shutil, os, re

# Create a regex that matches files with the American date format to European DD-MM-YYYY
date_pattern = re.compile(r"""^(.*?)            # all text before the date
                ((0|1)?d)-                      # one or two digits for the month
                ((0|1|2|3)?\d)-                 # one or two digts for the day
                ((19|20)\d\d)                   # four digits for the year
                (.*?)$                          # all text after the date
                """, re.VERBOSE)

if if __name__ == "__main__":
    pass