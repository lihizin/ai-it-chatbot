import difflib

# Common questions - dictionary
FAQ: dict[str,str] = {"reset password": "To reset your Microsoft 365 password,go to https://passwordreset.microsoftonline.com and follow the instructions",
                      "vpn connection":"To connect to GlobalProtect VPN, install the app from:'https://morphisec0.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?id=%2FShared%20Documents%2FGlobal%20Protect&viewid=56e026ca%2D10a2%2D4632%2Db398%2D0d296aaf861d' and make sure to use the server address 'mphc,gpcloudservice.com'.",
                      "shared mailbox":"To add or remove a shared mailbox, go to Outlook > File > Account Settings > More Settings > Advanced.",
                      "license renewal":"If you're seeing a license expired message, please fill in this request for a renewal form - 'https://forms.office.com/Pages/ResponsePage.aspx?id=PV2c5tBj5UOWMR6gh8djtBTCBdVkwI5BixKFT4TpTv1UOE5SUUI2TERLSENGMlVIWktNVTY3NkRZRi4u&fswReload=1&fswNavStart=1745495549931'.",
                      "new license":"Fill in the Software Request Application: 'https://forms.office.com/Pages/ResponsePage.aspx?id=PV2c5tBj5UOWMR6gh8djtBTCBdVkwI5BixKFT4TpTv1UOE5SUUI2TERLSENGMlVIWktNVTY3NkRZRi4u'. "

}

# The function is checking if there's a match between the user's input to the dictionary (FAQ)
def get_faq_answer(user_input):
    matches = difflib.get_close_matches(user_input.lower(), FAQ.keys(), n=1, cutoff=0.4)
    if matches:
        return FAQ[matches[0]]
    return None