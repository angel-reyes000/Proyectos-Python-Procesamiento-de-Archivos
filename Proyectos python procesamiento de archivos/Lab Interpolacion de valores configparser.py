import configparser

config = configparser.ConfigParser()

dict1 = {
    "sentry":{"key": "key", "secret": "secret"},
    "github":{"user": "user", "password": "password"}
}

dict2 = {
    "mariadb": {"host": "localhost", "name": "hello", "user": "user", "password":"password"},
    "redis": {"host":"localhoost", "port":6379, "db": 0}
}

for archivo in [dict1, dict2]:
    config.read_dict(archivo)

with open("C:\\Users\\Luis Reyes\\Downloads\\prod_config.ini", "w") as file1:
    config.write(file1)

print("[sentry]")
print("Key = ", config["sentry"]["key"])
print("user = ", config["sentry"]["secret"], "\n")
print("[github]")
print("user = ", config["github"]["user"])
print("password = ", config["github"]["password"])

for q in range(20):
    print("-", end="")
print()

with open("C:\\Users\\Luis Reyes\\Downloads\\dev_config.ini", "w") as file2:
    config.write(file2)

print("[mariadb]")
print("host = ", config["mariadb"]["host"])
print("name = ", config["mariadb"]["name"])
print("user = ", config["mariadb"]["user"])
print("password = ", config["mariadb"]["password"], "\n")
print("[redis]")
print("host = ", config["redis"]["host"])
print("port = ", config["redis"]["port"])
print("db = ", config["redis"]["db"])

config["redis"]["dsn"] = "redis://%(host)s//%(port)s//%(db)s"
print(config.get("redis", "dsn"))

