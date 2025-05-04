import difflib

# Common questions - dictionary
FAQ: dict[str,str] = {"reset password": "To reset your Microsoft 365 password,go to https://passwordreset.microsoftonline.com and follow the instructions",
                      "vpn connection":"To connect to GlobalProtect VPN, install the app from:[Private link]",
                      "shared mailbox":"To add or remove a shared mailbox, go to Outlook > File > Account Settings > More Settings > Advanced.",
                      "license renewal":"If you're seeing a license expired message, please fill in this request for a renewal form - [Private link]",
                      "new license":"Fill in the Software Request Application: [Private link]. "

}

# The function is checking if there's a match between the user's input to the dictionary (FAQ)
def get_faq_answer(user_input):
    matches = difflib.get_close_matches(user_input.lower(), FAQ.keys(), n=1, cutoff=0.4)
    if matches:
        return FAQ[matches[0]]
    return None