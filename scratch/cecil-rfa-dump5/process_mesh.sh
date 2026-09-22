#!/usr/bin/env bash
set -euo pipefail

NODE_ALPHA_PORT=8081
NODE_BETA_PORT=8082

cleanup_mesh_nodes() {
    print "\n[SHUTDOWN] Terminating background sandbox nodes safely..."
    kill $(jobs -p) 2>/dev/null || true
}
trap cleanup_mesh_nodes EXIT

print "=== LAUNCHING LIGHTWEIGHT RFA AGENT PIPELINE OVER APPLE SILICON ==="
touch alpha_cluster.log beta_cluster.log
python3 rfa_neo_core.py > alpha_cluster.log 2>&1 &
ALPHA_PID=$!
print " -> Worker Node Alpha running directly under host Kernel PID: ${ALPHA_PID}"

python3 rfa_neo_core.py > beta_cluster.log 2>&1 &
BETA_PID=$!
print " -> Worker Node Beta running directly under host Kernel PID: ${BETA_PID}"

print "================================================================="
print(" Sandboxes fully operational. Monitor local logs to audit stats.")
print(" Modify rfa_config.json dynamically to view hot-swapping traces.")
print(" Press [CTRL+C] at any time to dismantle active local mesh execution.")
print("=================================================================")

while true; do
    sleep 1
done
