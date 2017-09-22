from mistral_lib import actions
from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class NarutoSay(actions.Action):

    def __init__(self, message) -> None:
        self.message = message if message else 'Dattebayo'

    def run(self, context):
        print(self.message)
        LOG.info('Naruto says: "%s"'.format(self.message))

        return self.message


