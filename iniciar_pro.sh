#!/bin/bash
echo "🚀 Iniciando GROWTH MASTER PRO VIP..."
pkill -f control_vip.py
nohup python control_vip.py > logs.txt 2>&1 &
echo "✅ Bot iniciado en segundo plano correctamente."
