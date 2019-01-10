import os
from setuptools import setup
from setuptools.command.install import install
from distutils import log

class OverrideInstall(install):
    def run(self):
        mode = 0755
        install.run(self) # calling install.run(self) insures that everything that happened previously still happens, so the installation does not break!
        # here we start with doing our overriding and private magic ..
        for filepath in self.get_outputs():
            if os.path.basename(filepath) in ['starlight', 'starlight_mac']:
                log.info("Changing permissions of %s to %s" %
                         (filepath, oct(mode)))
                os.chmod(filepath, mode)


setup(name='XSpec',
      version='0.2',
      packages=['XSpec', 'XSpec.analysis', 'XSpec.io', 'XSpec.utils'],
      package_data={'XSpec': ['etc/*', 'etc/bases/*']},
      cmdclass={'install': OverrideInstall}
)
