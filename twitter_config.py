import re

CONSUMER_KEY    = "5PEuxsbh3rSruUF09pFJOkogl"
CONSUMER_SECRET = "xZYyTo95D6C6vhm37uGWmbAepB1m5f56ritlQL3PWJS8PlvRtx"
ACCESS_TOKEN    = "16561841-fDZWuq2Ciy8uVBSKVi2hhRSsJIeQoIDzuuFmoq1ZN"
ACCESS_SECRET   = "g1KoBYYeP3mctE6ZU68bK5UZnzZblrJA3RjuU85E0dFlT"

hashtag_pattern = re.compile('#[A-Za-z0-9_]+')
at_reference_pattern = re.compile("@[A-Za-z0-9_]+")
RT_regex = re.compile("^RT ")
http_regex = re.compile('https?:\/\/.*[\r\n]*')