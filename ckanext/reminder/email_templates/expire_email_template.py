from pylons import config

"""
    A template file for datasets that are about to expire.
"""


def message(days):
    messageContent = ""
    separator = '\n'
    for day in days:
        items = []
        for item in day:
            # WIP!
            item["package_title"] = (item["package_title"].encode('ascii', 'ignore')).decode("utf-8")
            items.append(
                singleItem.format(
                    package_id=item["package_id"],
                    package_title=item["package_title"],
                    resource_id=item["resource_id"],
                    broken_url=item["broken_url"],
                    site_url=config['ckan.site_url'],
                ).encode('utf-8')
            )
        messageContent += separator.join(items)
    return messageTemplate.format(content=messageContent)


subject = "You have datasets that are about to expire"


messageTemplate = """
You have datasets that are about to expire.
You can update the "valid till" date by logging in and navigating to the expiring dataset.

{content}
---

Best regards

Avoindata.fi support
avoindata@vrk.fi
"""


singleItem = """
Dataset: {package_title} ( {site_url}/data/fi/dataset/{package_id} )
Valid till: {valid_till}
"""

dayGroup = """
Expiring in {days} day(s)
---
{items}
"""
