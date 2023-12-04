def check_query(user_command):
    if "open" in user_command:
        return 'Opening'
    elif "close" in user_command:
        return 'Closing'
    else:
        return 'IDFK'
    
