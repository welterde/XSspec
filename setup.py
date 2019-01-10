from distutils.core import setup

setup(name='XSpec',
      version='0.2',
      packages=['XSpec', 'XSpec.analysis', 'XSpec.io', 'XSpec.utils'],
      package_data={'XSpec': ['etc/*', 'etc/bases/*']},
      scripts=[
          'binaries/starlight',
          'binaries/starlight_mac'
      ]
)
