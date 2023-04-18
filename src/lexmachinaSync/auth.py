import requests
import configparser
from datetime import datetime
from pathlib import Path


class Auth:
    def __init__(self, config_file_path=None, client_id=None, client_secret=None) -> None:
        self.config_file_path = config_file_path
        self._client_id = client_id
        self._client_secret = client_secret
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def get_token(self):
        config, config_file = self.config_reader()
        with requests.Session() as session:
            token_url = config.get("URLS", "base_url") + config.get("URLS", "token_url")
            if self._client_id is None and self._client_secret is None:
                if config.has_section("TOKEN") and config.get("TOKEN", "ACCESS_TOKEN") != '':
                    now = datetime.utcnow().timestamp()
                else:
                    return self.renew_token(config, config_file, session, token_url)

                if not now - float(config.get("TOKEN", "ISSUED_AT")) >= 3599:
                    return config.get("TOKEN", "ACCESS_TOKEN")
                else:
                    return self.renew_token(config, config_file, session, token_url)
            else:
                with session.post(token_url, headers=self._headers, data={
                    "grant_type": "client_credentials",
                    "client_id": self._client_id,
                    "client_secret": self._client_secret
                }) as response:
                    if response.status_code == 200:
                        access_token = response.json()
                        return access_token['access_token']
                    else:
                        return {"error": response.json()}

    def config_reader(self):
        config = configparser.ConfigParser()
        if not self.config_file_path:
            config_file = Path("./config/config.ini")
        else:
            config_file = Path(self.config_file_path)
        if config_file.is_file():
            config.read(config_file)
        else:
            raise FileNotFoundError("config.ini file not found, please provide path to file")
        return config, config_file

    def renew_token(self, config, config_file, session, token_url):
        with session.post(token_url, headers=self._headers, data={
            "grant_type": "client_credentials",
            "client_id": config.get("CREDENTIALS", "client_id"),
            "client_secret": config.get("CREDENTIALS", "client_secret")
        }) as response:
            if response.status_code == 200:
                access_token = response.json()
                if not config.has_section("TOKEN"):
                    config.add_section("TOKEN")
                config['TOKEN']['ISSUED_AT'] = str(datetime.utcnow().timestamp())
                config['TOKEN']['ACCESS_TOKEN'] = access_token['access_token']
                with open(config_file, "w") as configfile:
                    config.write(configfile)
                return access_token['access_token']
            else:
                return {"error": response.json()}