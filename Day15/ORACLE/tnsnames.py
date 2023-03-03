import os

def create_tnsnames_file(dbname, host, port, sid, user, password):
    tns_admin_dir = os.path.join(os.environ['ORACLE_HOME'], 'network', 'admin')
    if not os.path.exists(tns_admin_dir):
        os.makedirs(tns_admin_dir)

    tnsnames_file = os.path.join(tns_admin_dir, 'tnsnames.ora')
    with open(tnsnames_file, 'w') as f:
        f.write(f'{dbname} = \n')
        f.write(f'  (DESCRIPTION = \n')
        f.write(f'    (ADDRESS = (PROTOCOL = TCP)(HOST = {host})(PORT = {port}))\n')
        f.write(f'    (CONNECT_DATA = \n')
        f.write(f'      (SID = {sid}) \n')
        f.write(f'    ) \n')
        f.write(f'  ) \n')

        f.write(f'{dbname}_SERVICE = \n')
        f.write(f'  (DESCRIPTION = \n')
        f.write(f'    (ADDRESS = (PROTOCOL = TCP)(HOST = {host})(PORT = {port}))\n')
        f.write(f'    (CONNECT_DATA = \n')
        f.write(f'      (SERVICE_NAME = {sid}) \n')
        f.write(f'    ) \n')
        f.write(f'  ) \n')

        f.close()

if __name__ == '__main__':
    dbname = 'HRDB'
    host = 'localhost'
    port = '31521'
    sid = 'xe'
    user = 'hr'
    password = 'hr'

    create_tnsnames_file(dbname, host, port, sid, user, password)