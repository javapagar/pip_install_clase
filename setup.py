from distutils.core import setup
setup(
  name = 'libraryname',         # How you named your package folder (MyLib)
  packages = ['libraryname'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'ds-dt-e21',                   # Type in your name
  author_email = 'captainvinager@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/javapagar/pip_install_clase',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/javapagar/pip_install_clase/archive/refs/tags/v_04.tar.gz',    # I explain this later on
  keywords = ['Machine Learning', 'Easy', 'Help','Visualization','Clean'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'seaborn',
          'matplotlib',
          'plotly',
          'seaborn',
          'scipy',
          'sklearn'

      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
