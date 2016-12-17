# -*- coding: utf-8 -*-
"""Little World of Warcraft dungeon stats extractor.

:copyright: (c) 2016, Serge Emond
:license: BSD 3-Clause, http://opensource.org/licenses/BSD-3-Clause

"""

from __future__ import absolute_import, print_function

import json
import os.path
import sys

import click

import oauth2 as oauth

USER_HOME = os.path.expanduser('~')
CONFIG_FILE_ORDER = [
    os.path.join(USER_HOME, '.wow-dungeon-stats.json'),
    os.path.join(USER_HOME, 'wow-dungeon-stats.json'),
    'config.json',
]


DUNGEON_NAMES = {
    "Vault of the Wardens", "Neltharion's Lair", "Assault on Violet Hold",
    "Maw of Souls", "Black Rook Hold", "Halls of Valor", "Darkheart Thicket",
    "Eye of Azshara", 'Court of Stars', 'Arcway', 'Return to Karazhan'
}

ACHIEVEMENT_CRITERIAS = [
    dict(criteria=33096, name='Completed Keystone 2+ within time'),
    dict(criteria=33097, name='Completed Keystone 5+ within time'),
    dict(criteria=33098, name='Completed Keystone 10+ within time'),
    dict(criteria=32028, name='Completed Keystone 15+ within time'),
]


def compute_and_print_totals(data):
    """Compute and print dungeon totals."""
    d_stats = [
        z for z in [
            y for y in [
                x for x in data['statistics']['subCategories']
                if x['name'] == 'Dungeons & Raids'
            ][0]['subCategories']
            if y['name'] == 'Legion'
        ][0]['statistics']
    ]
    sums = dict(Normal=0, Heroic=0, Mythic=0)
    total = 0
    for d in d_stats:
        is_d = False
        for pot_name in DUNGEON_NAMES:
            if d['name'].find(pot_name) >= 0:
                is_d = True
                break
        if not is_d:
            continue
        print("%3d %s" % (d['quantity'], d['name']))

        if d['name'].find('Normal') >= 0:
            _type = 'Normal'
        elif d['name'].find('Heroic') >= 0:
            _type = 'Heroic'
        elif d['name'].find('Mythic') >= 0:
            _type = 'Mythic'
        elif d['name'].find('Return to Karazhan') >= 0:
            _type = 'Mythic'
        else:
            raise Exception("Unknown dungeon type, name = " + d['name'])
        sums[_type] += d['quantity']
        total += d['quantity']

    print("\n")
    print(
        "Normal Dungeons: {0[Normal]}\n"
        "Heroic Dungeons: {0[Heroic]}\n"
        "Mythic Dungeons: {0[Mythic]}\n"
        "Total: {1}\n"
        .format(sums, total))


def compute_and_print_keystones(data):
    """Compute and print successful mythic keystones."""
    out = ['']
    for criteria in ACHIEVEMENT_CRITERIAS:
        try:
            index = data['achievements']['criteria'] \
                .index(criteria['criteria'])
            qty = data['achievements']['criteriaQuantity'][index]
        except ValueError:
            qty = 0
        out.append(u'{c[name]!s}: {qty}'.format(c=criteria, qty=qty))

    print(u'\n'.join(out))


def show_dungeons(client, name, realm):
    """Show dungeon totals for a character."""
    resp, content = client.request(
        u"https://us.api.battle.net/wow/character/{realm!s}/{name!s}"
        "?fields=statistics,achievements&locale=en_US"
        "&apikey={client.consumer.key!s}"
        .format(name=name, realm=realm, client=client), 'GET')
    data = json.loads(content)
    compute_and_print_totals(data)
    compute_and_print_keystones(data)


@click.command()
@click.argument('character_name')
@click.option('--realm', help="Character's realm")
@click.option('--config-file', help='Configuration file (json)')
def main(character_name, realm, config_file):
    """Run."""
    config = None
    if config_file:
        try:
            config = json.load(open(config_file, 'rb'))
        except:
            pass
    else:
        for cfg_path in CONFIG_FILE_ORDER:
            if not os.path.exists(cfg_path):
                continue
            try:
                config = json.load(open(cfg_path, 'rb'))
                break
            except Exception:
                pass
    if not config:
        print("Error: Couldn't find configuration file.")
        print("Please create a file 'config.json' with content like this:")
        print("""
{
    "key": "WOW-API-KEY",
    "secret": "WOW-API-SECRET",
    "realm": "Default Realm"
}""")
        sys.exit(1)

    consumer = oauth.Consumer(key=config['key'], secret=config['secret'])
    client = oauth.Client(consumer)

    if not realm:
        realm = config.get('realm', "Kel'Thuzad")

    show_dungeons(client, character_name, realm)


if __name__ == '__main__':
    main()
