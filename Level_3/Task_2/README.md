# File Encryption and Decryption

## Overview

This project is a Python command-line application that encrypts and decrypts files using the Fernet symmetric encryption system provided by the `cryptography` library.

It allows users to encrypt a file, decrypt an encrypted file, and exit the application through an interactive menu.

## Features

* Encrypt files using Fernet symmetric encryption.
* Decrypt previously encrypted files.
* Save encrypted and decrypted content to separate files.
* Handle missing files and invalid encryption keys.
* Provide a simple, interactive command-line menu.

## Technologies Used

* Python
* Cryptography library
* Fernet symmetric encryption

## Project Structure

```text
Task_2/
├── main.py
├── message.txt
└── README.md
```

**Note:** The `secret.key` file and generated encrypted and decrypted files are excluded from version control for security.

## Installation

### 1. Install Python

Install Python if it is not already available on your computer.

### 2. Install the required library

Activate the project's virtual environment from the root directory:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependency if necessary:

```powershell
python -m pip install cryptography
```

### 3. Navigate to the application directory

```powershell
cd Level_3\file_encryption
```

## Usage

Run the application from the `file_encryption` directory:

```powershell
python main.py
```

The application displays an interactive menu with four options:

1. **Generate encryption key:** Creates and saves an encryption key if one does not already exist. An existing key is preserved.
2. **Encrypt a file:** Encrypts the specified file and saves the encrypted content in a separate `.encrypted` file.
3. **Decrypt a file:** Decrypts a previously encrypted file and saves the recovered content in a separate `.decrypted` file.
4. **Exit:** Closes the application.

### Example

To encrypt `message.txt`, select option `2` and enter:

```text
message.txt
```

The application creates:

```text
message.txt.encrypted
```

To decrypt that file, select option `3` and enter:

```text
message.txt.encrypted
```

The application creates:

```text
message.txt.decrypted
```

The original file remains unchanged.


## Security Notes

* Keep the encryption key private.
* The same key is required to decrypt a file encrypted with that key.
* Do not upload `secret.key` to GitHub.
* If the key is lost, files encrypted with it may become unrecoverable.
* Store important encryption keys securely and separately from encrypted files.

## Learning Objectives

This project demonstrates practical use of file handling, symmetric encryption, exception handling, functions, and menu-driven programming in Python.