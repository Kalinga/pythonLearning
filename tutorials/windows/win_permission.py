import os, sys, re
from shutil import copyfile
import ntsecuritycon as con
import win32security
import win32api
import shutil
import psutil,getpass

#http://pyxr.sourceforge.net/PyXR/c/python24/lib/site-packages/win32/lib/ntsecuritycon.py.html
#0003 DELETE = (65536)
#0004 READ_CONTROL = (131072)
#0005 WRITE_DAC = (262144)
#0006 WRITE_OWNER = (524288)
#0007 SYNCHRONIZE = (1048576)
#0008 STANDARD_RIGHTS_REQUIRED = (983040)
#0009 STANDARD_RIGHTS_READ = (READ_CONTROL)
#0010 STANDARD_RIGHTS_WRITE = (READ_CONTROL)
#0011 STANDARD_RIGHTS_EXECUTE = (READ_CONTROL)
#0012 STANDARD_RIGHTS_ALL = (2031616)
#0013 SPECIFIC_RIGHTS_ALL = (65535)
#0014 ACCESS_SYSTEM_SECURITY = (16777216)
#0015 MAXIMUM_ALLOWED = (33554432)
#0016 GENERIC_READ = (-2147483648)
#0017 GENERIC_WRITE = (1073741824)
#0018 GENERIC_EXECUTE = (536870912)
#0019 GENERIC_ALL = (268435456)
#0020 
#0021 # file security permissions
#0022 FILE_READ_DATA=            ( 1 )
#0023 FILE_LIST_DIRECTORY=       ( 1 )
#0024 FILE_WRITE_DATA=           ( 2 )
#0025 FILE_ADD_FILE=             ( 2 )
#0026 FILE_APPEND_DATA=          ( 4 )
#0027 FILE_ADD_SUBDIRECTORY=     ( 4 )
#0028 FILE_CREATE_PIPE_INSTANCE= ( 4 )
#0029 FILE_READ_EA=              ( 8 )
#0030 FILE_WRITE_EA=             ( 16 )
#0031 FILE_EXECUTE=              ( 32 )
#0032 FILE_TRAVERSE=             ( 32 )
#0033 FILE_DELETE_CHILD=         ( 64 )
#0034 FILE_READ_ATTRIBUTES=      ( 128 )
#0035 FILE_WRITE_ATTRIBUTES=     ( 256 )
#0036 FILE_ALL_ACCESS=           (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 1023)
#0037 FILE_GENERIC_READ=         (STANDARD_RIGHTS_READ | FILE_READ_DATA | FILE_READ_ATTRIBUTES | FILE_READ_EA | SYNCHRONIZE)
#0038 FILE_GENERIC_WRITE=        (STANDARD_RIGHTS_WRITE | FILE_WRITE_DATA | FILE_WRITE_ATTRIBUTES | FILE_WRITE_EA | FILE_APPEND_DATA | SYNCHRONIZE)
#0039 FILE_GENERIC_EXECUTE=      (STANDARD_RIGHTS_EXECUTE | FILE_READ_ATTRIBUTES | FILE_EXECUTE | SYNCHRONIZE)


########Currently NOT used#####
def win32_set_file_access(filename, access_right, allow = True):
	userx, domain, type = win32security.LookupAccountName ("", win32api.GetUserName())
	#print "#GetUserName from win32api:", win32api.GetUserName()
	print "#Gettings details:"
	print "userx", userx
	print "GetSubAuthorityCount", userx.GetSubAuthorityCount()
	print "GetSubAuthority", userx.GetSubAuthority()
	print "GetSidIdentifierAuthority", userx.GetSidIdentifierAuthority()
	print "domain from win32security: ", domain
	print "type", type
	sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()
	ace_count = dacl.GetAceCount()
	print "#ace_count", ace_count
	for i in range(0, ace_count):
		dacl.DeleteAce(0)
	ace_count = dacl.GetAceCount()
	print "#ace_count after deleting all access control entires", ace_count
	
	if allow:
		print "#Allow access", access_right
		dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION, con.OBJECT_INHERIT_ACE|con.CONTAINER_INHERIT_ACE, FILE_ALL_ACCESS, userx)
	else:
		dacl.AddAccessDeniedAceEx(win32security.ACL_REVISION, con.OBJECT_INHERIT_ACE|con.CONTAINER_INHERIT_ACE, FILE_ALL_ACCESS, userx)
		print "#Deny access", access_right
	ace_count = dacl.GetAceCount()
	print "#ace_count after AddAccess*", ace_count
	
	sd.SetSecurityDescriptorDacl(1, dacl, 0)
	win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)

def updateACLEntries(filename):
	entries = [{'AccessMode': win32security.DENY_ACCESS,
				'AccessPermissions': 0,
				'Inheritance': win32security.CONTAINER_INHERIT_ACE |
							   win32security.OBJECT_INHERIT_ACE,
				'Trustee': {'TrusteeType': win32security.TRUSTEE_IS_USER,
							'TrusteeForm': win32security.TRUSTEE_IS_NAME,
							'Identifier': ''}}
				]

	entries[0]['AccessPermissions'] = ( con.FILE_ALL_ACCESS )
	entries[0]['Trustee']['Identifier'] = "USAU-VW-W2K16-0\hudson"


	sd = win32security.GetNamedSecurityInfo(filename, win32security.SE_FILE_OBJECT,
			win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()
	dacl.SetEntriesInAcl(entries)
	win32security.SetNamedSecurityInfo(filename, win32security.SE_FILE_OBJECT,
		win32security.DACL_SECURITY_INFORMATION |
		win32security.UNPROTECTED_DACL_SECURITY_INFORMATION,
		None, None, dacl, None)

import csv,subprocess
def get_current_user_processes():
   csv_output = subprocess.check_output(["tasklist","/FI","USERNAME eq {}".format(os.getenv("USERNAME")),"/FO","CSV"]).decode("ascii","ignore")
   cr = csv.reader(csv_output.splitlines())
   next(cr)   # skip title lines
   return {int(row[1]):row[0] for row in cr}
   
#####################################################
	
def get_owner(self):
        r""" Return the name of the owner of this file or directory.

        This follows symbolic links.

        On Windows, this returns a name of the form ur'DOMAIN\User Name'.
        On Windows, a group can own a file or directory.
        """
        if os.name == 'nt':
            if win32security is None:
                raise Exception("path.owner requires win32all to be installed")
            desc = win32security.GetFileSecurity(
                self, win32security.OWNER_SECURITY_INFORMATION)
            sid = desc.GetSecurityDescriptorOwner()
            account, domain, typecode = win32security.LookupAccountSid(None, sid)
            return domain + u'\\' + account
        else:
            if pwd is None:
                raise NotImplementedError("path.owner is not implemented on this platform.")
            st = self.stat()
            return pwd.getpwuid(st.st_uid).pw_name

def user_account_details():
	userx, domain, type = win32security.LookupAccountName ("", win32api.GetUserName())
	print "#GetUserName from win32api:", win32api.GetUserName()
	print "#Gettings details:"
	print "userx", userx

	subAuthorityCount = userx.GetSubAuthorityCount()
	print "ubAuthorityCount", subAuthorityCount

	for i in range (0, subAuthorityCount):
	    authority = userx.GetSubAuthority(i)
	    print "authority", authority

	print "GetSidIdentifierAuthority", userx.GetSidIdentifierAuthority()
	print "domain from win32security: ", domain
	print "type", type
	
	print win32security.LookupAccountSid("", userx)


# code samples found at
# https://stackoverflow.com/questions/27500067/chmod-issue-to-change-file-permission-using-python
# https://stackoverflow.com/questions/26465546/how-to-authorize-deny-write-access-to-a-directory-on-windows-using-python
def win32_get_effective_rights(path):
	print ("*****************Effective Rights for %s*******************")%path
	
	sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_GROUP, 'Identifier': 'System'})
	print "mask for System", mask
	print calculate_plaintext_mask(mask)
	
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_USER, 'Identifier': 'Administrator'})
	print "mask for Administrator", mask
	print calculate_plaintext_mask(mask)
	
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_USER, 'Identifier': 'hudson'})
	print "mask for hudson", mask
	print calculate_plaintext_mask(mask)
	
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_GROUP, 'Identifier': 'Everyone'})
	print "mask for Everyone", mask
	print calculate_plaintext_mask(mask)
	
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_GROUP, 'Identifier': 'Users'})
	print "mask for users", mask
	print calculate_plaintext_mask(mask)

	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_GROUP, 'Identifier': 'kalinga'})
	print "mask for kalinga", mask
	print calculate_plaintext_mask(mask)
	
	mask = dacl.GetEffectiveRightsFromAcl({'TrusteeForm': win32security.TRUSTEE_IS_NAME, 'TrusteeType': win32security.TRUSTEE_IS_GROUP, 'Identifier': 'Administrators'})
	print "mask for Administrators", mask
	print calculate_plaintext_mask(mask)
	print "************************************"


def make_path_non_writable(filename):
	sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()
	ace_count = dacl.GetAceCount()
	print  "ace_count", ace_count  

	for i in range(0, ace_count):
		dacl.DeleteAce(0)
	
	sd.SetSecurityDescriptorDacl(1, dacl, 0)
	win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)

	#rights = FILE_ALL_ACCESS
	rights = con.FILE_ADD_SUBDIRECTORY | con.FILE_ALL_ACCESS
	
	win32_modify_rights(filename, "", "Administrators", rights, False)
	win32_modify_rights(filename, "", "Administrator", rights, False)
	win32_modify_rights(filename, "", "System", rights, False)
	win32_modify_rights(filename, "", "Users", rights, False)
	
	win32_modify_rights(filename, "", "hudson", rights, False)
	win32_modify_rights(filename, "", "kalinga", rights, False)

def make_path_writable(filename):
	rights = con.FILE_ADD_SUBDIRECTORY | con.FILE_ALL_ACCESS
	win32_modify_rights(filename, "", "kalinga", rights, True)
	win32_modify_rights(filename, "", "hudson", rights, True)
		
def win32_modify_rights(filename, group, user, access_right, allow = True):
	sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
	dacl = sd.GetSecurityDescriptorDacl()
	ace_count = dacl.GetAceCount()
	print  "ace_count", ace_count  

	if allow:
		print "#Allow access", access_right
		dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION, con.OBJECT_INHERIT_ACE|con.CONTAINER_INHERIT_ACE, access_right, win32security.LookupAccountName("", user)[0])
	else:
		print "user", user, " PySID:", win32security.LookupAccountName("", user)[0]
		dacl.AddAccessDeniedAceEx(win32security.ACL_REVISION, con.OBJECT_INHERIT_ACE|con.CONTAINER_INHERIT_ACE, access_right, win32security.LookupAccountName("", user)[0])
		print "#Deny access", access_right
	ace_count = dacl.GetAceCount()
	print  "ace_count", ace_count 
	
	sd.SetSecurityDescriptorDacl(1, dacl, 0)
	win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)

  
typical_aces={
    2032127L:"Full Control(All)",
    1179817L:"Read(RX)",
    1180086L:"Add",
    1180095L:"Add&Read",
    1245631L:"Change"
}

binary_aces={
    1:"ACCESS_READ",            #0x00000001
    2:"ACCESS_WRITE",           #0x00000002
    4:"ACCESS_CREATE",          #0x00000004 FILE_ADD_SUBDIRECTORY
    8:"ACCESS_EXEC",            #0x00000008
    16:"ACCESS_DELETE",         #0x00000010
    32:"ACCESS_ATRIB",          #0x00000020
    64:"ACCESS_PERM",           #0x00000040
	128:"FILE_READ_ATTRIBUTES", #0x00034
	256:"FILE_WRITE_ATTRIBUTES",#0x00035
    32768:"ACCESS_GROUP",       #0x00008000
    65536:"DELETE",             #0x00010000
    131072:"READ_CONTROL",      #0x00020000
    262144:"WRITE_DAC",         #0x00040000
    524288:"WRITE_OWNER",       #0x00080000
    1048576:"SYNCHRONIZE",      #0x00100000
    16777216:"ACCESS_SYSTEM_SECURITY",#0x01000000
    33554432:"MAXIMUM_ALLOWED", #0x02000000
    268435456:"GENERIC_ALL",    #0x10000000
    536870912:"GENERIC_EXECUTE",#0x20000000
    1073741824:"GENERIC_WRITE", #0x40000000
    65535:"SPECIFIC_RIGHTS_ALL",#0x0000ffff
    983040:"STANDARD_RIGHTS_REQUIRED",#0x000f0000
    2031616:"STANDARD_RIGHTS_ALL",#0x001f0000
	
    }

def calculate_plaintext_mask(mask):
    a=2147483648L
    #if typical_aces.has_key(mask):
    #    return typical_aces[mask]
    #else:
    result='NONE'
    while a>>1:
        a=a>>1
        masked=mask&a
        if masked:
            print masked
            if binary_aces.has_key(masked):
                result=binary_aces[masked]+':'+result
    return result
	
def main():
  print "Enter main"
  
  user_name = getpass.getuser()
  print "user_name", user_name  

  p = psutil.Process(os.getpid())
  print "pname", p.name()

  print "domain = os.environ['userdomain']"
  domain = os.environ['userdomain']
  print domain
  usr = os.environ['username']
  print "username from env: ",usr
  
  user_account_details()
  
  basePath = r"C:\\tmp\\"
  
  if os.path.exists(basePath):
    print "Trying to remove existing: ", basePath
    print "Owner", get_owner(basePath)
    shutil.rmtree(basePath)
  
  print "Creating: ", basePath
  os.mkdir(basePath)
  
  win32_get_effective_rights(basePath)  

  
  print "make_path_non_writable object:", basePath
  make_path_non_writable(basePath)  
  win32_get_effective_rights(basePath)
  
  backup_dir = os.path.join(basePath,"_backups")
  print "Trying to create a subdirectory using os.mkdir inside: ", basePath
  os.mkdir(backup_dir)
  print ("Contents in %s:")% basePath
  contents = os.listdir(basePath)
  for c in contents:
	print c
  win32_get_effective_rights(backup_dir)
  win32_get_effective_rights(basePath)
  
  open(os.path.join(basePath,"_backups","myFille.txt"), 'w+')
  print ("Contents in %s:")% basePath
  contents = os.listdir(basePath)
  for c in contents:
	print c

  print ("copyfile")
  copyfile("C:\\testFile.txt",  os.path.join(basePath,"_backups"))
  
  contents = os.listdir(basePath)
  print ("Contents in %s:")% basePath
  for c in contents:
	print c
	
  #print "Try to remove: ", basePath
  #shutil.rmtree(basePath)
  
 
main()

