#!/bin/bash

fecha=$(date +"%Y-%m-%d %H:%M:%S")
git add .
git commit -m "Actualización automática: $fecha"
git push origin main
