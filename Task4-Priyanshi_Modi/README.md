# Task 4 – System Vulnerability Checklist

## 📌 Overview
This project is part of the DecodeLabs Cyber Security Internship (Batch 2026).  
**Task 4** focuses on building a **System Vulnerability Checklist** using a Windows batch script.  
The script automates the collection of critical system security information and saves it into a single `report.txt` file.  
This provides a quick audit of user accounts, firewall, encryption, and patch management.

---

## 🎯 Project Goal
Create a batch script that:
- Lists all **local users** on the system.
- Displays **administrator group members**.
- Shows the **firewall status** for all profiles.
- Reports the **BitLocker encryption status**.
- Lists all **installed Windows updates**.

---

## 🛠️ Skills Applied
- **Windows command line scripting**  
- **System auditing & security checks**  
- **File redirection (`>` and `>>`)**  
- **Automation of vulnerability reporting**  

---

## ⚙️ Requirements
- Windows OS  
- Command Prompt (Run as Administrator)  

---

## 🚀 How to Run
1. Open **Notepad**.  
2. Copy the following script:

   ```bat
   @echo off
   echo Local Users: > report.txt
   net user >> report.txt

   echo Admin Group Members: >> report.txt
   net localgroup administrators >> report.txt

   echo Firewall Status: >> report.txt
   netsh advfirewall show allprofiles >> report.txt

   echo BitLocker Status: >> report.txt
   manage-bde -status >> report.txt

   echo Windows Updates: >> report.txt
   wmic qfe list brief /format:table >> report.txt
