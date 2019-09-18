import os

##############
# CRAIGSLIST #
##############

CL_BASE = 'craigslist.org'
CL_BASE_SEARCH = '/search/sss?query='
CL_BASE_TAIL = 'sort=rel'

CL_CITIES = [
    'atlanta',
    'austin',
    'boston',
    'chicago',
    'dallas',
    'denver',
    'detroit',
    'houston',
    'lasvegas',
    'losangeles',
    'miami',
    'minneapolis',
    'newyork',
    'orangecounty',
    'philadelphia',
    'phoenix',
    'portland',
    'raleigh',
    'sacramento',
    'sandiego',
    'seattle',
    'sfbay',
    'washingtondc'
]


##############
# ALIEXPRESS #
##############

ALI_BASE = 'https://www.aliexpress.com'
ALI_SEARCH = '/wholesale?SearchText='


# https://www.aliexpress.com/wholesale?SearchText=ipad

# https://www.aliexpress.com/wholesale?catId=200216621&initiative_id=AS_20190917170406&SearchText=ipad&switch_new_app=y
# https://www.aliexpress.com/wholesale?ltype=wholesale&d=y&CatId=0&SearchText=ipad&trafficChannel=main&SortType=create_desc&groupsort=1&page=1