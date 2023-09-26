# coding: utf-8

"""
    A template file for datasets that are about to expire.
"""

from ckan.plugins import toolkit


def message(days):
    groupedByDate = []
    separator = '\n'
    for day, expiring in days.items():
        items = []
        for item in expiring:
            items.append(
                singleItem.format(
                    package_id=item["package_id"],
                    package_title=item["package_title"],
                    valid_till=item["valid_till"],
                    site_url=toolkit.config['ckan.site_url'],
                )
            )
        groupedByDate.append(dayGroup.format(days=day, items=separator.join(items)))
    return messageTemplate.format(content=separator.join(groupedByDate))


subject = "Tietoaineistojesi viimeinen voimassaolopäivä Suomi.fi-avoindatassa lähestyy - You have datasets that are about to expire in Suomi.fi Open Data" # noqa


# TODO: update to use signature template
messageTemplate = """
Hei,
 
Ylläpidät tietoaineistoja Suomi.fi-avoindatassa ja olet merkinnyt niille viimeisen voimassaolopäivän.
 
Alla listatut tietoaineistosi merkitään vanhentuneiksi viimeisen voimassaolopäivän jälkeen. Voit muuttaa tietoaineistojen voimassaoloa
kirjautumalla palveluun, valitsemalla datasetin jonka voimassaolo on umpeutumassa, ja päivittämällä arvon kentässä "Voimassa päättyen".
Lähetämme tämän ilmoituksen kun tietoaineistosi umpeutumiseen on 1 viikko, 5 vuorokautta, ja kun aineistosi umpeutuu 24h kuluttua. 
Jos sinulla on kysyttävää, opastamme sinua tarpeen vaatiessa osoitteessa avoindata@dvv.fi.
 
Ystävällisin terveisin,
Suomi.fi-avoindatan tuki
 
--

Hello,
 
You have uploaded a dataset or datasets in Suomi.fi Open Data and set an expiration date for the data.
 
When your datasets expire, they will be marked as expired. If you want to you extend the validity of your dataset(s), log in the service,
navigate to the expiring dataset, and update the date in the "Valid till" field.
You receive this notification one (1) week, five (5) days and 24 hours before your data set(s) expire
 
Should you have any questions or need help, please get in touch with us at avoindata@dvv.fi.
 
Best regards,
Suomi.fi Open Data support

{content}
---""" # noqa


singleItem = """
Tietoaineisto - Dataset: {package_title} ( {site_url}/data/fi/dataset/{package_id} )
Voimassa päättyen - Valid till: {valid_till}"""

dayGroup = """
---
Expiring in {days} day(s)
---
{items}
"""
