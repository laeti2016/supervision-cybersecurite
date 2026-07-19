# Plateforme de Supervision & Cybersécurité

**Projet PRJ-TEL-2026-001 — FOUSSA Laeticia — IRIS**

## Description

Stack complète de supervision et détection d'intrusion construite avec Docker.  
Combine observabilité (métriques, alertes, dashboards) et sécurité (détection d'intrusion, intégrité des fichiers).

## Technologies utilisées

| Outil | Rôle |
|-------|------|
| Prometheus | Collecte et stockage des métriques |
| Grafana | Dashboards et visualisation |
| Node Exporter | Métriques système |
| Alertmanager | Gestion des alertes |
| Blackbox Exporter | Sondes HTTP/TCP actives |
| fail2ban | Blocage automatique des attaques SSH |
| auditd | Journalisation des événements système |
| AIDE | Contrôle d'intégrité des fichiers |

## Fonctionnalités de sécurité

- Détection d'attaques SSH par force brute
- Supervision des IPs bannies par fail2ban
- Surveillance des modifications de fichiers sensibles (/etc/passwd, /etc/shadow, /etc/sudoers)
- Contrôle d'intégrité du système de fichiers (AIDE)
- Alertes automatiques (8 règles de détection)
- Dashboard Grafana "Security Overview"

## Démarrage rapide

```bash
cd telemetrie-supervision
docker compose up -d
```

## Dashboard

![Security Overview](grafana/dashboards/security-overview.json)

## Auteur

FOUSSA Laeticia — Formation IRIS — 2026
