import os
import datetime
import shutil

sourcedir = os.path.expanduser("~/Desktop/aulas_bit")
backupdir = os.path.expanduser("~/Documents/backups")

def backup_files(sourcedir, backupdir):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = os.path.join(backupdir, f"backup_{current_time}")

    try:
        # Copia a pasta toda para o novo local (sem criar antes)
        shutil.copytree(sourcedir, backup_folder)
        print(f"Parabéns, o backup foi bem-sucedido! Os arquivos foram salvos em: {backup_folder}")
    except Exception as e:
        print(f"Erro ao realizar o backup: {e}")

# Executar
backup_files(sourcedir, backupdir)