__version__ = '0.1'
__author__  = 'S3phy'

import b3, re
import b3.events
import random
from foaas import fuck
from b3.clients import Client
#--------------------------------------------------------------------------------------------------
class FoaasPlugin(b3.plugin.Plugin):
    _adminPlugin = None

    def startup(self):
      """\
      Initialize plugin settings
      """

   # get the admin plugin so we can register commands
      self._adminPlugin = self.console.getPlugin('admin')
      if not self._adminPlugin:
      # something is wrong, can't start without admin plugin
        self.error('Could not find admin plugin')
        return False
    
    # register our commands (you can ignore this bit)
      if 'commands' in self.config.sections():
        for cmd in self.config.options('commands'):
          level = self.config.get('commands', cmd)
          sp = cmd.split('-')
          alias = None
          if len(sp) == 2:
            cmd, alias = sp

          func = self.getCmd(cmd)
          if func:
            self._adminPlugin.registerCommand(self, cmd, level, func, alias)

      self.debug('Started FOaaS')


    def getCmd(self, cmd):
      cmd = 'cmd_%s' % cmd
      if hasattr(self, cmd):
        func = getattr(self, cmd)
        return func

      return None

    def cmd_foaas(self, data, client, cmd=None):
        """\
        Throw a swear, or add a name to target the swear
        """

        m = self._adminPlugin.parseUserCmd(data)
        if not data:
               self.console.say(fuck.random(from_=client.exactName).text)
        else:
            sclient = self._adminPlugin.findClientPrompt(m[0], client)
            if sclient:
                self.console.say(fuck.random(name=sclient.exactName, from_=client.exactName).text)
