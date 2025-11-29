import os

command= 'powershell -command "Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory | Format-List"' #RAM INFO
Command= 'powershell -command "Get-Date"' #DATE
command= 'powershell -command "(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime"' #UPTIME
def ram_info(command):
    print(os.system(command))

ram_info('powershell -command "Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory | Format-List"')


def date(command):
    print(os.system("\n=== date ==="))

date('powershell -command "Get-Date"')    

def uptime(command):
    print(os.system(command))
uptime('powershell -command "(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime"')    
