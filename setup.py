# -*- coding: utf-8 -*-
"""Setup.

:copyright: (c) 2016, Serge Emond
:license: BSD 3-Clause, http://opensource.org/licenses/BSD-3-Clause

"""

from setuptools import setup


setup_opts = dict(
    name='wow_dungeon_stats',
    version='0.1',
    author=u'Serge Émond',
    author_email='serge@sergeemond.com',
    zip_safe=True,
    packages=['wow_dungeon_stats'],
    description="Obtain and show World of Warcraft dungeon stats",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=[
        'click',
        'oauth2',
    ],
    entry_points="""
    [console_scripts]
    dungeon-stats=wow_dungeon_stats:main
    """,
)

if __name__ == '__main__':
    setup(**setup_opts)
