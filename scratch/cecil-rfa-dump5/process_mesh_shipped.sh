NODE_ALPHA_PORT=8081
NODE_BETA_PORT=8082

cleanup_mesh_nodes() {
    print "\n[SHUTDOWN] Terminating background sandbox nodes safely..."
    kill $(jobs -p) 