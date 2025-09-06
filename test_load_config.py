from ProyectoHoneypot.config import load_config


if __name__ == "__main__":
    cfg = load_config("config.yml")
    print("node_id", cfg["node_id"])
    print("bind_host", cfg["bind_host"])
    print("logging dir:", cfg["logging"]["dir"])
    print("http enabled: ", cfg["services"]["http"]["enabled"],
          "port: ", cfg["services"]["http"]["port"])