#!/usr/bin/env python
# -*- coding: utf-8 -*-
# config file for send_sms.py
# send email via gmail.com

# map port dinstar to Mobile Operator
gw = {0: 'Life',
      1: 'Kyivstar',
      2: 'MTS',
      3: 'MTS',
      }

# move send messages to archive dir
archive = '/var/spool/dwgp/archive/'

# mail configuration
from_addr = 'FROM_ADDR@GMAIL.COM'
to_addrs = 'TO_ADDR@GOOGLE.COM'

# auth username
username = 'user@gmail.com'
password = 'user_password'
server = 'smtp.gmail.com:587'

