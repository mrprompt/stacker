from codecs import open as codecs_open
from setuptools import setup, find_packages

# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='stacker',
      version='0.0.1',
      description=u"Image stacker.",
      long_description=long_description,
      classifiers=[],
      keywords='image,stacker',
      author=u"Thiago Paes",
      author_email='mrprompt@gmail.com',
      url='https://github.com/mrprompt/stacker',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'Pillow'
      ],
      extras_require={
          'test': [
              'pytest'
          ],
      },
      entry_points="""
      [console_scripts]
      stacker=stacker.scripts.cli:cli
      """
      )
