class DatabaseConfig:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.db_name = args[0] if args else None
            cls._instance.user = args[1] if len(args) > 1 else None
            cls._instance.password = args[2] if len(args) > 2 else None
        return cls._instance
conf1 = DatabaseConfig("shop_db", "admin", "123")
conf2 = DatabaseConfig("users_db", "root", "000")
print(conf1 is conf2)
print(conf2.db_name)