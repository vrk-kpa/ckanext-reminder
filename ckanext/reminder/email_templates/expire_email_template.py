from pylons import config

"""
    A template file for datasets that are about to expire.
"""


def message(days):
    groupedByDate = []
    separator = '\n'
    for day, expiring in days.iteritems():
        items = []
        for item in expiring:
            item["package_title"] = (item["package_title"].encode('ascii', 'ignore')).decode("utf-8")
            items.append(
                singleItem.format(
                    package_id=item["package_id"],
                    package_title=item["package_title"],
                    valid_till=item["valid_till"],
                    site_url=config['ckan.site_url'],
                )
            )
        groupedByDate.append(dayGroup.format(days=day, items=separator.join(items)))
    return messageTemplate.format(content=separator.join(groupedByDate))


subject = "You have datasets that are about to expire"


messageTemplate = """
You have datasets that are about to expire. When they expire they will be marked as expired.
If you want to you extend the validity by logging in and navigating to the expiring dataset and
updating the "valid till" field.

{content}
---

Best regards

Avoindata.fi support
avoindata@vrk.fi
"""


singleItem = """
Dataset: {package_title} ( {site_url}/data/fi/dataset/{package_id} )
Valid till: {valid_till}"""

dayGroup = """
---
Expiring in {days} day(s)
---
{items}
"""
