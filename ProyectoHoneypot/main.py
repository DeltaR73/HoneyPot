import threading
from ProyectoHoneypot.config import load_config
from ProyectoHoneypot.servers import fake_http_server, fake_ssh_server, fake_fpt_server,fake_sql_server


if __name__ == "__main__":
    cfg = load_config("config.yml")
    host = cfg.get("bind_host", "0.0.0.0")
    services = cfg["services"]
    
    threads = []

    if services["http"]["enabled"]:
        t = threading.Thread(target=fake_http_server, args=(host, services["http"]["port"]))
        threads.append(t)
        t.start()

    if services["ssh"]["enabled"]:
        t = threading.Thread(target=fake_ssh_server, args=(host, services["ssh"]["port"]))
        threads.append(t)
        t.start()

    if services["ftp"]["enabled"]:
        t = threading.Thread(target=fake_fpt_server, args=(host, services["ftp"]["port"]))
        threads.append(t)
        t.start()
       
    if services["ftp"]["enabled"]:
        t = threading.Thread(target=fake_sql_server, args=(host, services["ftp"]["port"]))
        threads.append(t)
        t.start()    

    for t in threads:
        t.join
    
