# Auto Backup

Este projeto realiza backups automáticos de uma pasta local, compacta os arquivos e realiza upload para uma pasta específica no Google Drive.

## Funcionalidades

- Criação de backup de uma pasta local
- Compactação dos arquivos em formato ZIP
- Upload do arquivo ZIP para o Google Drive

## Estrutura do Projeto

autoBackup/
├── auto.py
├── .env
├── .gitignore
├── README.md
├── secrets/
│ └── credentials.json
└── backups/

## Requisitos

- Python 3.10 ou superior
- Conta no Google Cloud com projeto configurado
- Tela de consentimento OAuth configurada
- OAuth 2.0 com permissões para `https://www.googleapis.com/auth/drive.file`

## Instalação

1. Clone o repositório:
   
```bash
git clone https://github.com/seu-usuario/auto-backup.git
cd auto-backup
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```


3. Instale as dependências:
   
```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
SOURCE_DIR= [Path de diretorio de backup]
BACKUP_DIR= [Path de diretorio local para backup ]
GOOGLE_CREDENTIALS= [Sua credencial]
DRIVE_FOLDER_ID= [Seu ID]
```

## Configuração

Execute o script:

```bash
python auto.py
```




