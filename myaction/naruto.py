from mistral_lib import actions
from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class NarutoSay(actions.Action):
    """This action repeat the famous phrase of Naruto Uzumaki

        :param message: (optional, 'Dattebayo' by default) a phrase for
        Naruto
        """
    def __init__(self, message='Dattebayo'):
        self.message = message

    def run(self, context):
        print(self.message)
        LOG.info('Naruto says: "%s"'.format(self.message))

        return self.message


