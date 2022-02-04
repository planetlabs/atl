from setuptools import setup, find_packages
from setuptools import distutils
import os
import versioneer


def get_version():
    if os.path.exists("PKG-INFO"):
        metadata = distutils.dist.DistributionMetadata("PKG-INFO")
        return metadata.version
    else:
        return versioneer.get_version()


setup(name='datalake',
      url='https://github.com/planetlabs/datalake',
      version=get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='datalake: a metadata-aware archive',
      author='Brian Cavagnolo',
      author_email='brian@planet.com',
      packages=find_packages(exclude=['test']),
      install_requires=[
          'boto>=2.38.0',
          'memoized_property>=1.0.1',
          'simplejson>=3.3.1',
          'pyblake2>=0.9.3; python_version < "3.6.0"',
          'click>=4.1',
          'python-dotenv>=0.1.3',
          'requests>=2.5',
          'six>=1.10.0',
          'python-dateutil>=2.4.2',
          'pytz>=2015.4',
      ],
      extras_require={
          'test': [
              'pytest',
              'moto>=3.0.0',
              'twine',
              'pip',
              'wheel',
              'flake8>=4.0.0',
              'responses',
          ],
          # the queuable feature allows users to offload their datalake pushes
          # to a separate uploader process.
          'queuable': [
              'pyinotify>=0.9.4',
          ],
          'sentry': [
              'raven>=5.0.0',
          ],
      },
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
      entry_points="""
      [console_scripts]
      datalake=datalake.scripts.cli:cli
      """)
