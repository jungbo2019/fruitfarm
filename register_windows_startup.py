import os
import sys

startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
target_bat = r'E:\fruitfarm\autostart_fruitfarm.bat'
shortcut_path = os.path.join(startup_folder, 'FRUIT_FARM_AutoStart.bat')

with open(shortcut_path, 'w', encoding='utf-8') as f:
    f.write(f'@echo off\ncall "{target_bat}"\n')

print(f"Registered Windows Startup task at: {shortcut_path}")
