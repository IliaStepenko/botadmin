
class DBConfig:
    DBNAME = "d6m1o6sffr2l8a"
    USER = "sgsonrowlgcoor"
    PASSWORD = "c3ee4c8902762f5b60bdde37717722daad44cc3b43e8731e0553cb21efff1c5e"
    HOST = "ec2-34-242-89-204.eu-west-1.compute.amazonaws.com"

    @classmethod
    def get_ass_db_url(cls):
        return f"postgresql+asyncpg://{cls.USER}:{cls.PASSWORD}@{cls.HOST}:5432/{cls.DBNAME}"

