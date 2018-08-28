from setuptools import setup

setup(name='backtrader_addons',
      version='0.2.5',
      description='Helpful addons (analyzers, observers, indicators etc) for backtrader',
      url='https://github.com/ab-trader/backtrader_addons',
      author='ab-trader',
      author_email='',
      license='MIT',
      packages=['backtrader_addons'],
	  install_requires=[
		'backtrader',
	  ],
      zip_safe=False)