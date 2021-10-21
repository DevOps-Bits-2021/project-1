usage () {
    echo 'This script deploys the grid'
}

deploy_grid () {
    echo 'Deploying Grid ...'
    docker-compose -f resources/sel_grid_docker_compose.yaml up -d
    echo 'Please wait a few seconds while the grid deploys, It may take time'
}
deploy_grid