from ckanext.reminder.logic import action
import click


def get_commands():
    return [reminder]


@click.group()
def reminder():
    '''Send notification emails of datasets which have a reminder date set
    '''
    pass


@reminder.command()
def send():
    '''Sends emails of all the datasets which have reminder set to current date'''
    action.send_reminders()


@reminder.command()
def notify():
    '''Send notifications'''
    action.send_notifications()


@reminder.command()
def notify_expiry():
    '''Send expiry notifications'''
    action.send_expiry_notifications()


@reminder.command()
def initdb():
    '''Initialize reminder database'''
    import ckan.model as model
    from ckanext.reminder.model import init_tables
    init_tables(model.meta.engine)
