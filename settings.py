'''level_map0 = [
'                              ',
'           E                  ',
'                              ',
' XX R  X        X     XX      ',
' XX        R                  ',
' XXXX  R      XX  R      XX   ',
' XXXX       XX                ',
' XX    X  XXXX    XX  XX      ',
'       X  XXXX    XX  XXX   XX',
'P   XXXX  XXXXXX  XX  XXXX  XX',
'XXXXXXXX  XXXXXX  XX  XXXX  XX']'''

level_map0 = [
'                                        ',
'           E                            ',
'                                        ',
' XX R  X        X     XX  R             ',
' XX        R                            ',
' XXXX  R      XX  R      XX          XXX',
' XXXX       XX                 R        ',
' XX    X  XXXX    XX  XX       XX XX    ',
'       X  XXXX    XX  XXX   XX XX XX    ',
'P   XXXX  XXXXXX  XX  XXXX  XX XX XX    ',
'XXXXXXXX  XXXXXX  XX  XXXX  XX XX XX    ']

level_map1 = [
'                              ',
'             E                ',
' P                    R       ',
'XXX           R  X   XXX      ',
' XX                           ',
' XXXX        X           XX   ',
' XXXX      XXX                ',
' XX    X  XXXX    XX   R     X',
'       X  XXXX    XX  XXXX  XX',
'  R  XXX  XXXXX   XX  XXXX  XX',
'XXXXXXXX  XXXXXX  XX  XXXX  XX']

tile_size = 64
screen_width = 1200
screen_height = len(level_map0)*tile_size

#tipo de ecuacion relativo al nivel
number_level0 = 0
number_level1 = 1