"""SC2Dictionaries

All imports and local names relevant only to this file are _implied_private.
"""

import functools as _functools
import os as _os

from ._data_utils import (csv_to_dictitems as _csv_to_dictitems,
                          txt_to_iter as _txt_to_iter,
                          csv_to_comastery_dict as _csv_to_comastery_dict,
                          get_file_path
)


_DATADIR = 'SC2Dictionaries'
_joinDATA = _functools.partial(get_file_path, subfolder=_DATADIR)

UnitNameDict = _csv_to_dictitems(_joinDATA('UnitNames.csv'))
UnitAddKillsTo = _csv_to_dictitems(_joinDATA('UnitAddKillsTo.csv'))
CommanderMastery = _csv_to_comastery_dict(_joinDATA('CommanderMastery.csv'))
COMasteryUpgrades = _csv_to_comastery_dict(_joinDATA('COMasteryUpgrades.csv'))

# Set of all units in waves (excluding Medivac)
UnitsInWaves = _txt_to_iter(_joinDATA('UnitsInWaves.txt'))
HFTS_Units = _txt_to_iter(_joinDATA('HFTS_Units.txt'))
TUS_Units = _txt_to_iter(_joinDATA('TUS_Units.txt'))

UnitCompDict = {
'Brooding Corruption':  [{'Zergling'},
                         {'Mutalisk', 'Zergling'},
                         {'Baneling', 'Mutalisk', 'Zergling'},
                         {'Mutalisk', 'Infestor', 'Zergling'},
                         {'Mutalisk', 'Corruptor', 'Infestor', 'Zergling'},
                         {'Mutalisk', 'Infestor', 'Zergling', 'BroodLord'},
                         {'Mutalisk', 'Corruptor', 'Infestor', 'BroodLord'}],
     'Classic Infantry': [{'Marine'},
                          {'Marine', 'Medic'},
                          {'Marine', 'Firebat', 'Medic'},
                          {'Marine', 'SiegeTank', 'Medic'},
                          {'Marine', 'SiegeTank', 'Ghost', 'Medic'},
                          {'Firebat','Marine','Medic','ScienceVessel','SiegeTank'},
                          {'Ghost','Marine','Medic','ScienceVessel','SiegeTank'}],
         'Classic Mech': [{'Vulture'},
                          {'Vulture', 'Goliath'},
                          {'Wraith', 'Vulture', 'Goliath'},
                          {'SiegeTank', 'Wraith', 'Vulture', 'Goliath'},
                          {'SiegeTank', 'Vulture', 'Battlecruiser', 'Goliath'},
                          {'ScienceVessel', 'Battlecruiser', 'Goliath'},
                          {'SiegeTank', 'Battlecruiser', 'ScienceVessel', 'Goliath'}],
     'Devouring Scourge': [{'Zergling'},
                           {'Mutalisk', 'Zergling'},
                           {'Scourge', 'QueenClassic', 'Mutalisk', 'Zergling'},
                           {'Scourge', 'Mutalisk', 'Zergling', 'Guardian'},
                           {'Devourer', 'Mutalisk', 'Guardian'},
                           {'Devourer', 'QueenClassic', 'Mutalisk', 'Guardian'},
                           {'Devourer', 'QueenClassic', 'Guardian', 'Scourge'}],
 'Disruptive Artillery': [{'Adept'},
                          {'Adept', 'Sentry'},
                          {'Adept', 'Immortal'},
                          {'Adept', 'Scout', 'Immortal'},
                          {'Adept', 'Sentry', 'Disruptor', 'Reaver'},
                          {'Adept', 'Disruptor', 'Scout', 'Reaver'},
                          {'Sentry', 'Disruptor', 'Immortal', 'Reaver'}],
 'Dominion Battlegroup': [{'VikingFighter'},
                          {'VikingFighter', 'Banshee'},
                          {'VikingFighter', 'Marine', 'Banshee'},
                          {'VikingFighter', 'Marine', 'Banshee', 'Liberator'},
                          {'VikingFighter', 'Raven', 'Banshee', 'Liberator'},
                          {'Banshee','Battlecruiser','Liberator','Marine','Raven','VikingFighter'},
                          {'Banshee','Battlecruiser','Liberator','Raven','VikingFighter'}],
     'Explosive Threats': [{'Zergling'},
                           {'Baneling', 'Zergling'},
                           {'InfestedAbomination','Mutalisk','Scourge','Viper','Zergling'},
                           {'InfestedAbomination','Mutalisk','Scourge','SwarmHostMP','Zergling'},
                           {'Baneling','InfestedAbomination','Mutalisk','Scourge','Viper','Zergling'},
                           {'Baneling','Mutalisk','Scourge','SwarmHostMP','Viper','Zergling'},
                           {'Baneling','InfestedAbomination','Mutalisk','Scourge','SwarmHostMP','Viper'}],
 'Fleet of the Matriarch': [{'Zealot'},
                            {'Scout', 'Zealot'},
                            {'CorsairMP', 'Scout', 'Zealot'},
                            {'CorsairMP', 'Scout'},
                            {'Scout', 'Carrier'},
                            {'ArbiterMP', 'Scout', 'Carrier'},
                            {'ArbiterMP', 'CorsairMP', 'Scout', 'Carrier'}],
     'Hope of the Khalai': [{'Zealot'},
                            {'Scout', 'Zealot'},
                            {'Stalker', 'Scout'},
                            {'Scout', 'Oracle', 'Zealot'},
                            {'VoidRay', 'Zealot'},
                            {'Oracle', 'Carrier', 'Zealot'},
                            {'VoidRay', 'Oracle', 'Carrier', 'Zealot'}],
     'Invasionary Swarm': [{'Zergling'},
                           {'Zergling', 'Hydralisk'},
                           {'LurkerMP', 'Zergling', 'Hydralisk'},
                           {'LurkerMP', 'Hydralisk'},
                           {'LurkerMP', 'QueenClassic', 'Hydralisk'},
                           {'Ultralisk', 'Zergling', 'Hydralisk'},
                           {'Hydralisk','LurkerMP','QueenClassic','Ultralisk','Zergling'}],
     'Machines of War': [{'Hellion'},
                         {'WarHound', 'Hellion', 'Goliath'},
                         {'HellionTank', 'SiegeTank', 'WarHound', 'Goliath'},
                         {'Goliath','HellionTank','SiegeTank','WarHound','WidowMine'},
                         {'Goliath','ScienceVessel','SiegeTank','WarHound','WidowMine'},
                         {'Goliath','ScienceVessel','Thor','WarHound','WidowMine'},
                         {'Thor', 'SiegeTank', 'ScienceVessel'}],
 'Masters and Machines': [{'Zealot'},
                          {'Stalker', 'Zealot'},
                          {'Stalker', 'HighTemplar', 'Zealot'},
                          {'Stalker', 'HighTemplar', 'Immortal'},
                          {'Stalker', 'Zealot', 'HighTemplar', 'Archon'},
                          {'Stalker', 'Zealot', 'Archon', 'Colossus'},
                          {'Colossus','HighTemplar','Immortal','Stalker','Zealot'}],
         'Raiding Party': [{'Marine', 'Medic'},
                           {'Marine', 'Marauder', 'Medic'},
                           {'Firebat', 'Marauder', 'Medic'},
                           {'Marine', 'Medivac', 'SiegeTank', 'Ghost'},
                           {'Marauder', 'Marine', 'Medivac', 'SiegeTank'},
                           {'Ghost','Marauder','Marine','ScienceVessel','SiegeTank'},
                           {'Battlecruiser','Ghost','Marine','ScienceVessel','SiegeTank'}],
 'Ravaging Infestation': [{'Roach'},
                          {'Roach', 'Zergling'},
                          {'Roach', 'Hydralisk'},
                          {'Ravager', 'LurkerMP', 'Roach', 'Hydralisk'},
                          {'LurkerMP', 'Roach', 'Infestor', 'Hydralisk'},
                          {'Hydralisk','Infestor','Ravager','Roach','Ultralisk'},
                          {'Hydralisk','Infestor','Ravager','Roach','Ultralisk'}],
     'Shadow Disruption': [{'Adept'},
                           {'Adept', 'Stalker'},
                           {'Adept', 'Sentry', 'Stalker'},
                           {'DarkTemplar', 'Stalker', 'Adept', 'Sentry'},
                           {'DarkTemplar', 'Adept', 'Phoenix', 'Sentry'},
                           {'Adept','DarkTemplar','Disruptor','Sentry','Stalker'},
                           {'Adept','DarkTemplar','Disruptor','Phoenix','Sentry'}],
             'Shadow Tech': [{'Reaper'},
                             {'Marauder', 'Reaper'},
                             {'Liberator', 'Marauder', 'Reaper'},
                             {'Cyclone', 'Liberator', 'Marauder', 'Reaper'},
                             {'Marauder', 'Raven', 'Liberator', 'Cyclone'},
                             {'Marauder', 'Raven', 'Cyclone', 'Battlecruiser'},
                             {'Battlecruiser','Cyclone','Liberator','Marauder','Raven'}],
         'Siege of Storms': [{'Adept'},
                             {'Adept', 'Phoenix'},
                             {'Adept', 'Phoenix'},
                             {'Stalker', 'Phoenix', 'Oracle'},
                             {'Adept', 'VoidRay'},
                             {'Adept', 'Oracle', 'Tempest'},
                             {'Adept', 'VoidRay', 'Oracle', 'Tempest'}],
         'Towering Walkers': [{'Zealot'},
                              {'Sentry', 'Zealot'},
                              {'Sentry', 'Immortal'},
                              {'Scout', 'Immortal', 'Zealot'},
                              {'Sentry', 'Scout', 'Zealot', 'Colossus'},
                              {'Scout', 'Zealot', 'Colossus'},
                              {'Sentry', 'Zealot', 'Immortal', 'Colossus'}],
         'Vanguard of Aiur': [{'Zealot'},
                              {'Dragoon', 'Zealot'},
                              {'Dragoon', 'HighTemplar', 'Zealot'},
                              {'Dragoon', 'Reaver'},
                              {'Reaver', 'Archon', 'HighTemplar', 'Zealot'},
                              {'ArbiterMP', 'Dragoon', 'HighTemplar', 'Zealot'},
                              {'ArbiterMP','Archon','Dragoon','HighTemplar','Reaver','Zealot'}]}