#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "31/01/2021"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''OSINT tool  for Nigerian Phone numbers'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import random

logo = random.randrange(4)

if logo == 0:
	print("""

███████╗██╗  ██╗██╗████████╗ ██████╗ ██████╗ 
██╔════╝╚██╗██╔╝██║╚══██╔══╝██╔═══██╗██╔══██╗
█████╗   ╚███╔╝ ██║   ██║   ██║   ██║██████╔╝
██╔══╝   ██╔██╗ ██║   ██║   ██║   ██║██╔══██╗
███████╗██╔╝ ██╗██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

Check if an IP address is a Tor exit node
        By L4ser Security Labs
                v1.0.0
""")

elif logo == 1:
	print("""

                                        iiii TTTTTTTTTTTTTTTTTTTTTTT                                  
                                       i::::iT:::::::::::::::::::::T                                  
                                        iiii T:::::::::::::::::::::T                                  
                                             T:::::TT:::::::TT:::::T                                  
    eeeeeeeeeeee  xxxxxxx      xxxxxxxiiiiiiiTTTTTT  T:::::T  TTTTTTooooooooooo   rrrrr   rrrrrrrrr   
  ee::::::::::::ee x:::::x    x:::::x i:::::i        T:::::T      oo:::::::::::oo r::::rrr:::::::::r  
 e::::::eeeee:::::eex:::::x  x:::::x   i::::i        T:::::T     o:::::::::::::::or:::::::::::::::::r 
e::::::e     e:::::e x:::::xx:::::x    i::::i        T:::::T     o:::::ooooo:::::orr::::::rrrrr::::::r
e:::::::eeeee::::::e  x::::::::::x     i::::i        T:::::T     o::::o     o::::o r:::::r     r:::::r
e:::::::::::::::::e    x::::::::x      i::::i        T:::::T     o::::o     o::::o r:::::r     rrrrrrr
e::::::eeeeeeeeeee     x::::::::x      i::::i        T:::::T     o::::o     o::::o r:::::r            
e:::::::e             x::::::::::x     i::::i        T:::::T     o::::o     o::::o r:::::r            
e::::::::e           x:::::xx:::::x   i::::::i     TT:::::::TT   o:::::ooooo:::::o r:::::r            
 e::::::::eeeeeeee  x:::::x  x:::::x  i::::::i     T:::::::::T   o:::::::::::::::o r:::::r            
  ee:::::::::::::e x:::::x    x:::::x i::::::i     T:::::::::T    oo:::::::::::oo  r:::::r            
    eeeeeeeeeeeeeexxxxxxx      xxxxxxxiiiiiiii     TTTTTTTTTTT      ooooooooooo    rrrrrrr            
                                        
                            Check if an IP address is a Tor exit node
                            By L4ser Security Labs
                            v1.0.0
""")

elif logo == 2:
	print("""

 ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌            ▐░▌ ▐░▌       ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌    ▐░▌         ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ 
▐░▌            ▐░▌ ▐░▌       ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌  ▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                            
                Check if an IP address is a Tor exit node
                        By L4ser Security Labs
                                v1.0.0
""")

elif logo == 3:
	print("""

@@@@@@@@  @@@  @@@  @@@  @@@@@@@   @@@@@@   @@@@@@@   
@@@@@@@@  @@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@!  !@@  @@!    @@!    @@!  @@@  @@!  @@@  
!@!       !@!  @!!  !@!    !@!    !@!  @!@  !@!  @!@  
@!!!:!     !@@!@!   !!@    @!!    @!@  !@!  @!@!!@!   
!!!!!:      @!!!    !!!    !!!    !@!  !!!  !!@!@!    
!!:        !: :!!   !!:    !!:    !!:  !!!  !!: :!!   
:!:       :!:  !:!  :!:    :!:    :!:  !:!  :!:  !:!  
:: ::::   ::  :::   ::     ::    ::::: ::  ::   :::  
: :: ::    :   ::   :       :      : :  :    :   : :  

    Check if an IP address is a Tor exit node
    By L4ser Security Labs
    v1.0.0
""")

elif logo == 4:
	print("""

 ___       ___  __   __  
|__  \_/ |  |  /  \ |__) 
|___ / \ |  |  \__/ |  \ 

Check if an IP address is a Tor exit node
By L4ser Security Labs
v1.0.0
""")