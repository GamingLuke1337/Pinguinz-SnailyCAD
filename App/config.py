import configparser

# Konfigurationsdatei lesen
config = configparser.ConfigParser()
config.read("config.txt")

# Datenbankoptionen
DATABASE_CONFIG = {
    "host": config.get("database", "host"),
    "port": config.getint("database", "port"),
    "user": config.get("database", "user"),
    "password": config.get("database", "password"),
    "name": config.get("database", "name"),
}

# Serveroptionen
SERVER_CONFIG = {
    "host": config.get("server", "host"),
    "port": config.getint("server", "port"),
    "reload": config.getboolean("server", "reload"),
}
