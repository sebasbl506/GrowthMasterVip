#!/bin/bash

echo "🚀 Iniciando instalación de GrowthMasterVIP..."

# Dependencias
pkg update && pkg upgrade -y
pkg install python git curl unzip tsu termux-api -y
pip install pyTelegramBotAPI pillow qrcode requests

# Clonar de Git
git clone https://github.com/sebasbl506/GrowthMasterVip.git
cd GrowthMasterVip

# Crear estructura
mkdir -p saas_core backups
echo "{}" > saas_core/licencias.json

# Crear archivo de inicio
cat << 'EOF' > iniciar_pro.sh
#!/bin/bash
echo "🚀 Iniciando GROWTH MASTER PRO VIP..."
nohup python control_vip.py &
EOF

chmod +x iniciar_pro.sh

echo "✅ Instalación finalizada correctamente."
