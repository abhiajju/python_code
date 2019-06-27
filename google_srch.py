#!/usr/bin/python

import webbrowser as wb

content = raw_input("enter content to be searched in google")
wb.open_new_tab("https://www.google.com/search?q="+content)

